#!/usr/bin/env bash
# instalar.sh — instala o kit fable-barato no Claude Code.
#   ./instalar.sh            → global (~/.claude): agentes + bloco de regras no ~/.claude/CLAUDE.md + skill
#   ./instalar.sh --projeto  → só neste projeto (./.claude/agents + ./.claude/skills + ./CLAUDE.md)
#   ./instalar.sh --desfazer [--projeto] → tira o bloco de regras, a skill e o revisor; devolve o Explore.md antigo (o CLAUDE.md.bak-fable-barato fica como cópia)
# Idempotente: rodar de novo não duplica. Todo arquivo que já existia ganha backup <arquivo>.bak-fable-barato.
set -euo pipefail
KIT=$(cd "$(dirname "$0")" && pwd)
ALVO="${CLAUDE_HOME_DIR:-$HOME/.claude}"; MD="$ALVO/CLAUDE.md"; DESFAZER=0; PROJ=0
for a in "$@"; do case $a in --projeto) PROJ=1;; --desfazer) DESFAZER=1;; -h|--help) sed -n '2,7p' "$0"; exit 0;; *) echo "opção desconhecida: $a" >&2; exit 2;; esac; done
[ $PROJ = 1 ] && { ALVO="$PWD/.claude"; MD="$PWD/CLAUDE.md"; }
AG="$ALVO/agents"; SK="$ALVO/skills/fable-barato"
INI='<!-- fable-barato:inicio'; FIM='<!-- fable-barato:fim -->'

tira_bloco() { [ -f "$MD" ] && python3 - "$MD" "$INI" "$FIM" <<'E'
import sys, re
p, ini, fim = sys.argv[1:]
t = open(p).read()
t2 = re.sub(r"\n?" + re.escape(ini) + r".*?" + re.escape(fim) + r"\n?", "\n", t, flags=re.S)
if t2 != t: open(p, "w").write(t2.rstrip("\n") + "\n")
E
}

if [ $DESFAZER = 1 ]; then
  for f in Explore.md revisor-fable.md; do
    if [ -f "$AG/$f.bak-fable-barato" ]; then mv "$AG/$f.bak-fable-barato" "$AG/$f"; echo "devolvido: $AG/$f"
    elif [ -f "$AG/$f" ] && grep -q "fable-barato\|^name: \(Explore\|revisor-fable\)" "$AG/$f"; then rm "$AG/$f"; echo "removido: $AG/$f"; fi
  done
  tira_bloco || true; [ -d "$SK" ] && rm -rf "$SK" && echo "removida skill: $SK"
  echo "pronto: kit desfeito"; exit 0
fi

mkdir -p "$AG"
for f in Explore.md revisor-fable.md; do
  if [ -f "$AG/$f" ] && ! cmp -s "$KIT/agentes/$f" "$AG/$f"; then
    [ -f "$AG/$f.bak-fable-barato" ] || cp -p "$AG/$f" "$AG/$f.bak-fable-barato"; echo "backup: $AG/$f.bak-fable-barato"
  fi
  cp "$KIT/agentes/$f" "$AG/$f"; echo "agente: $AG/$f"
done
[ -f "$MD" ] && { [ -f "$MD.bak-fable-barato" ] || cp -p "$MD" "$MD.bak-fable-barato"; }
tira_bloco || true
{ [ -s "$MD" ] && echo; cat "$KIT/regras/QUANDO-DIVIDIR.md"; } >> "$MD"; echo "regras: $MD (bloco fable-barato)"
mkdir -p "$SK"; cp "$KIT/skill/fable-barato/SKILL.md" "$SK/"; cp "$KIT/auditar/PROMPT.md" "$SK/AUDITAR.md"; echo "skill: $SK"
echo "pronto. Abra o Claude Code de novo e confira: peça uma busca e rode /tasks — o Explore tem que aparecer no Haiku."
