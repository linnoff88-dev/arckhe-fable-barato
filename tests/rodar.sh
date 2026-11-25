#!/usr/bin/env bash
# Testes do kit (nunca tocam o seu ~/.claude: tudo em pasta temporária).
set -uo pipefail
KIT=$(cd "$(dirname "$0")/.." && pwd); F=0; ok(){ echo "ok   $1"; }; ko(){ echo "FALHA $1"; F=$((F+1)); }
fm(){ awk '/^---$/{n++; next} n==1' "$1"; }

for a in "$KIT"/agentes/*.md; do
  b=$(basename "$a")
  fm "$a" | grep -q '^name: ' && fm "$a" | grep -q '^description: ' && ok "$b: name+description" || ko "$b: frontmatter"
  fm "$a" | grep -qE '^model: (haiku|sonnet|opus|fable|claude-[a-z0-9-]+)$' && ok "$b: model fixo" || ko "$b: sem model fixo"
  fm "$a" | grep -qE '^effort: (low|medium|high|xhigh|max)$' && ok "$b: effort fixo" || ko "$b: sem effort"
  fm "$a" | grep -qE '^tools:.*\b(Edit|Write|Bash)\b' && ko "$b: agente de leitura com ferramenta de escrita" || ok "$b: só leitura"
done
fm "$KIT/agentes/Explore.md" | grep -q '^name: Explore$' && fm "$KIT/agentes/Explore.md" | grep -q '^model: haiku$' && ok "Explore no haiku" || ko "Explore no haiku"
fm "$KIT/skill/fable-barato/SKILL.md" | grep -q '^name: fable-barato$' && ok "skill: name" || ko "skill: name"
grep -q 'fable-barato:inicio' "$KIT/regras/QUANDO-DIVIDIR.md" && grep -q 'fable-barato:fim' "$KIT/regras/QUANDO-DIVIDIR.md" && ok "regras: marcadores" || ko "regras: marcadores"
if command -v claude >/dev/null; then V=$(mktemp -d); mkdir -p "$V/.claude/agents"; cp "$KIT"/agentes/*.md "$V/.claude/agents/"
  (cd "$V" && claude plugin validate .claude/agents 2>&1) | grep -q 'Validation passed' && ok "claude plugin validate" || ko "claude plugin validate"; rm -rf "$V"
else echo "aviso: claude ausente, validate pulado"; fi

# instalar.sh em HOME falso
H=$(mktemp -d); mkdir -p "$H/agents"; printf 'minhas regras\n' > "$H/CLAUDE.md"; printf -- '---\nname: Explore\ndescription: meu\n---\nmeu\n' > "$H/agents/Explore.md"
CLAUDE_HOME_DIR=$H bash "$KIT/instalar.sh" >/dev/null && CLAUDE_HOME_DIR=$H bash "$KIT/instalar.sh" >/dev/null
[ "$(grep -c 'fable-barato:inicio' "$H/CLAUDE.md")" = 1 ] && ok "instalar 2×: bloco uma vez só" || ko "instalar duplicou bloco"
grep -q 'minhas regras' "$H/CLAUDE.md" && ok "instalar: preserva CLAUDE.md" || ko "instalar apagou CLAUDE.md"
grep -q '^description: meu' "$H/agents/Explore.md.bak-fable-barato" && ok "instalar: backup do Explore antigo" || ko "sem backup do Explore"
cmp -s "$KIT/agentes/Explore.md" "$H/agents/Explore.md" && ok "instalar: Explore novo no lugar" || ko "Explore nêo instalado"
[ -f "$H/skills/fable-barato/SKILL.md" ] && [ -f "$H/skills/fable-barato/AUDITAR.md" ] && ok "instalar: skill + AUDITAR" || ko "skill nêo instalada"
CLAUDE_HOME_DIR=$H bash "$KIT/instalar.sh" --desfazer >/dev/null
grep -q 'fable-barato' "$H/CLAUDE.md" && ko "desfazer deixou o bloco" || ok "desfazer: tira o bloco"
grep -q '^description: meu' "$H/agents/Explore.md" && ok "desfazer: devolve Explore antigo" || ko "desfazer nêo devolveu"
[ -f "$H/agents/revisor-fable.md" ] && ko "desfazer deixou revisor" || ok "desfazer: tira revisor"
P=$(mktemp -d); (cd "$P" && bash "$KIT/instalar.sh" --projeto >/dev/null)
[ -f "$P/.claude/skills/fable-barato/SKILL.md" ] && [ -f "$P/.claude/agents/Explore.md" ] && grep -q fable-barato "$P/CLAUDE.md" && ok "instalar --projeto: skill + agentes + regras" || ko "instalar --projeto incompleto"
(cd "$P" && bash "$KIT/instalar.sh" --desfazer --projeto >/dev/null); [ -d "$P/.claude/skills/fable-barato" ] && ko "desfazer --projeto deixou skill" || ok "desfazer --projeto"
rm -rf "$H" "$P"
echo "falhas: $F"; exit $F
