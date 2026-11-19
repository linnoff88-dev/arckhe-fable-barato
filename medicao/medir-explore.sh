#!/usr/bin/env bash
# medir-explore.sh — mede quanto custa a MESMA busca feita pelo agente Explore numa sessão Fable,
# sem e com o arquivo Explore.md (model: haiku). Roda pela assinatura, num HOME temporário
# (não lê seu CLAUDE.md, hooks, plugins nem MCP; só a credencial é ligada).
#
# Uso: ./medir-explore.sh <pasta-do-projeto-alvo> [repeticoes] [modelo-sessao] [esforco]
# Ex.: ./medir-explore.sh ~/projetos/esforco-medido 2 fable medium
# Saída: resultados/explore-<data>/ (jsonl bruto + resumo.md + resumo.json)
set -uo pipefail
AQUI=$(cd "$(dirname "$0")" && pwd)
ALVO=$(cd "${1:?pasta do projeto alvo}" && pwd); REP=${2:-2}; MOD=${3:-fable}; ESF=${4:-medium}
PEDIDO=${PEDIDO:-"Use the Explore subagent (do not search yourself) to find the file and line where the counter dictionary with the key \"conferencias\" is first initialized. Reply only with path:line."}
CRED="$HOME/.claude/.credentials.json"; [ -f "$CRED" ] || { echo "sem $CRED" >&2; exit 2; }
unset ANTHROPIC_API_KEY
SAI="$AQUI/resultados/explore-$(date +%Y%m%d-%H%M%S)"; mkdir -p "$SAI"
[ -n "${GABARITO:-}" ] && cp "$GABARITO" "$SAI/gabarito.txt"
echo "claude=$(claude --version | head -1) modelo=$MOD esforco=$ESF rep=$REP alvo=$(basename "$ALVO")" > "$SAI/config.txt"
for variante in sem com; do
  for r in $(seq 1 "$REP"); do
    X=$(mktemp -d "${TMPDIR:-/tmp}/fable-barato-XXXXXX"); mkdir -p "$X/.claude"
    ln -s "$CRED" "$X/.claude/.credentials.json"
    # só os arquivos versionados (um repo pode ter centenas de GB de dados fora do git)
    if git -C "$ALVO" rev-parse >/dev/null 2>&1; then mkdir -p "$X/p"; git -C "$ALVO" ls-files -z | rsync -a --from0 --files-from=- "$ALVO/" "$X/p/"
    else rsync -a --max-size=5m --exclude .git --exclude resultados --exclude node_modules "$ALVO/" "$X/p/"; fi
    if [ $variante = com ]; then mkdir -p "$X/.claude/agents"; cp "$AQUI/../agentes/Explore.md" "$X/.claude/agents/"; fi
    id="$variante-$r"; echo "→ $id ($(date +%H:%M:%S))"
    ( cd "$X/p" && env HOME="$X" PATH="$PATH" timeout 600 claude -p --model "$MOD" --effort "$ESF" \
        --strict-mcp-config --disable-slash-commands --no-session-persistence \
        --allowedTools "Read Glob Grep Agent Task" --max-turns 60 \
        --output-format stream-json --verbose -- "$PEDIDO" < /dev/null ) > "$SAI/$id.jsonl" 2> "$SAI/$id.err"
    if [ -f "$X/.claude/.credentials.json" ] && [ ! -L "$X/.claude/.credentials.json" ]; then cp -p "$X/.claude/.credentials.json" "$CRED"; fi
    rm -rf "$X"
  done
done
python3 "$AQUI/resumo-explore.py" "$SAI"
