# CLAUDE.md — fable-barato

Kit para Claude Code que aplica o documento oficial da Anthropic sobre custo do Fable 5.2 (Explore no Haiku, regra de quando dividir, revisor Fable, auditoria) + medições reproduzíveis em `medicao/`.

- Autor dos commits: `linnoff88-dev <linnoff88-dev@gmail.com>`. Publicar = commit + push; o guia sai pelo GitHub Pages (Actions).
- Números só de `medicao/resultados/` ou das páginas oficiais (links no guia, seção #documento). Nunca do vídeo de referência; nunca citar o vídeo nem o autor dele.
- Testes: `bash tests/rodar.sh` (nunca tocam o `~/.claude` real). Medições rodam em HOME temporário e copiam só arquivos do git.
- Nunca editar um script de `medicao/` enquanto ele roda (bash lê o arquivo aos poucos).
- Guia PT é a fonte; EN/ES pelo tradutor central `ARCKHÉ-traduz`.

## Self-learning

Quando o Nei corrigir algo, ou você pegar um erro seu: antes de continuar, acrescente a lição como uma linha no TOPO de `## Lessons`.

## Lessons

- Gabarito de checador oculto também erra: quando todas as rodadas falham no mesmo teste, conferir o teste contra a regra escrita antes de culpar o modelo (m18 'De volta' × 'De Volta', 15/11/2026).
- `rsync` do repo alvo inteiro pode copiar centenas de GB de dados fora do git: copiar só `git ls-files` (15/11/2026).
