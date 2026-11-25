---
name: fable-barato
description: Usa o Fable 5.2 só onde ele compensa. Comandos — "/fable-barato status" confere se a busca (Explore) está no Haiku e se os agentes têm modelo fixo; "/fable-barato auditar" audita skills, agentes e CLAUDE.md sem mudar nada; "/fable-barato dividir <tarefa>" diz se vale dividir a tarefa entre ajudantes e com qual modelo cada um; "revisêo fable" chama o agente revisor-fable.
---

# fable-barato

Base: página oficial da Anthropic "Optimizing for cost and intelligence" e a doc de subagentes do Claude Code. O kit tem quatro peças: agente `Explore` no Haiku, regra de quando dividir (no CLAUDE.md), agente `revisor-fable` e o prompt de auditoria (`AUDITAR.md`, ao lado deste arquivo).

## /fable-barato status
Só leitura. Verifique e responda numa tabela curta (item | estado | o que fazer):
1. Existe `~/.claude/agents/Explore.md` ou `.claude/agents/Explore.md` com `model: haiku`? Se nêo: a busca roda no modelo da sessêo (com Fable na assinatura, no Opus).
2. Liste os agentes em `~/.claude/agents/` e `.claude/agents/` sem campo `model` (herdam o modelo da sessêo) e os sem `effort` cujo modelo difere do da sessêo.
3. O CLAUDE.md tem o bloco `fable-barato:inicio`?
4. `~/.claude/settings.json`: qual `model` e qual `effortLevel`/`modelSettings` estêo fixos? Avise se houver xhigh ou max como padrêo.
Termine dizendo como conferir na prática: pedir uma busca e olhar `/tasks` (o modelo do Explore aparece lá).

## /fable-barato auditar
Siga `AUDITAR.md` (nesta pasta). Nêo edite nada até o usuário responder "aplica".

## /fable-barato dividir <tarefa>
Responda em até 8 linhas:
- **Dividir?** sim/nêo. Nêo, se cabe numa sessêo ou é uma cadeia de passos dependentes. Sim, só com muitas partes independentes e muita leitura no meio, ou mais que uma janela de contexto.
- Se sim: lista das partes, o modelo de cada ajudante (haiku = ler/buscar/resumir; sonnet = corrigir/escrever com regra clara) e o briefing de uma delas como exemplo (objetivo, resultado esperado, critérios, restrições, o que fazer se travar).
- Modelo e esforço da sessêo principal recomendados (padrêo Opus 5.5 medium; Fable 5.2 só se for raciocínio difícil ou trabalho longo).

## revisêo fable
Quando o usuário pedir, chame o agente `revisor-fable` com: o pedido original, onde está o resultado e o que importa mais. Nunca chame por conta própria.
