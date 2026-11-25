#!/usr/bin/env bash
# medir-3jeitos.sh — a MESMA tarefa em 3 jeitos, pela assinatura, em HOME temporário:
#   fable     = Fable 5.2 medium sozinho (sem subagentes)
#   opus      = Opus 5.5 medium sozinho (sem subagentes)
#   orquestra = Fable 5.2 medium chefiando subagentes mais baratos (Haiku/Sonnet) e revisando no fim
# Cada rodada recebe cópia limpa de projeto/; nota pelo checador oculto (o modelo nêo vê).
# Uso: ./medir-3jeitos.sh <pasta-tarefa com projeto/ pedido.txt oculto/checar.py> [repeticoes] [jeitos]
# Ex.: ./medir-3jeitos.sh tarefas/vinte-modulos 2 fable,opus,orquestra
set -uo pipefail
AQUI=$(cd "$(dirname "$0")" && pwd)
T=$(cd "${1:?pasta da tarefa}" && pwd); REP=${2:-2}; JEITOS=${3:-fable,opus,orquestra}; TETO=${TETO:-1800}
CRED="$HOME/.claude/.credentials.json"; [ -f "$CRED" ] || { echo "sem $CRED" >&2; exit 2; }
unset ANTHROPIC_API_KEY
PEDIDO=$(cat "$T/pedido.txt")
ORQ="Trabalhe como ORQUESTRADOR: planeje, divida as partes independentes e delegue cada parte a um subagente pela ferramenta Agent, escolhendo o modelo pelo trabalho (haiku para ler e resumir, sonnet para corrigir código). Cada subagente recebe um briefing completo: objetivo, resultado esperado, regras, o que nêo fazer e o que fazer se travar. No fim, revise você mesmo o trabalho deles e corrija o que faltar."
SAI="$AQUI/resultados/tres-jeitos-$(basename "$T")-$(date +%Y%m%d-%H%M%S)"; mkdir -p "$SAI"
echo "claude=$(claude --version | head -1) tarefa=$(basename "$T") rep=$REP jeitos=$JEITOS" > "$SAI/config.txt"
for r in $(seq 1 "$REP"); do
  for j in ${JEITOS//,/ }; do
    X=$(mktemp -d "${TMPDIR:-/tmp}/fable-3j-XXXXXX"); mkdir -p "$X/.claude"; ln -s "$CRED" "$X/.claude/.credentials.json"
    cp -r "$T/projeto" "$X/p"
    case $j in
      fable) MOD=fable; P="$PEDIDO Faça você mesmo, sem subagentes."; TOOLS="Read Edit Write Glob Grep Bash(python3:*)"; NEG="Agent Task";;
      opus)  MOD=opus;  P="$PEDIDO Faça você mesmo, sem subagentes."; TOOLS="Read Edit Write Glob Grep Bash(python3:*)"; NEG="Agent Task";;
      orquestra) MOD=fable; P="$PEDIDO $ORQ"; TOOLS="Read Edit Write Glob Grep Bash(python3:*) Agent Task"; NEG="";;
    esac
    id="$j-$r"; echo "→ $id ($(date +%H:%M:%S))"; ini=$(date +%s)
    ( cd "$X/p" && env HOME="$X" PATH="$PATH" timeout "$TETO" claude -p --model "$MOD" --effort medium \
        --strict-mcp-config --disable-slash-commands --no-session-persistence --permission-mode acceptEdits \
        --allowedTools "$TOOLS" ${NEG:+--disallowedTools "$NEG"} --max-turns 200 \
        --output-format stream-json --verbose -- "$P" < /dev/null ) > "$SAI/$id.jsonl" 2> "$SAI/$id.err"
    echo "parede=$(( $(date +%s) - ini ))" > "$SAI/$id.tempo"
    if [ -f "$X/.claude/.credentials.json" ] && [ ! -L "$X/.claude/.credentials.json" ]; then cp -p "$X/.claude/.credentials.json" "$CRED"; fi
    python3 "$T/oculto/checar.py" "$X/p" > "$SAI/$id.checar.txt" 2>&1
    rm -rf "$X"
  done
done
python3 "$AQUI/resumo-3jeitos.py" "$SAI"
