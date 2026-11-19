# Prompt de auditoria do ambiente (rodar no Fable 5.2, uma vez por modelo novo)

Cole na sessão do Claude Code (`/model fable`) a partir da pasta do projeto:

```
Audite meu ambiente do Claude Code SEM MUDAR NADA. Leia:
- ~/.claude/CLAUDE.md e o CLAUDE.md deste projeto
- ~/.claude/agents/ e .claude/agents/ (todos os agentes)
- ~/.claude/skills/ e .claude/skills/ (só o SKILL.md de cada uma)
- ~/.claude/settings.json (model, effortLevel, modelSettings, env)

Para cada item, responda em uma tabela: item | problema | por que custa caro ou erra | correção proposta | certeza (alta/média/baixa).
Procure principalmente:
1. Agente de leitura/busca sem campo `model` (herda o modelo caro da sessão).
2. Ausência de um agente `Explore` com `model: haiku` (a busca embutida roda no modelo da sessão, até Opus).
3. Esforço fixo em xhigh/max sem motivo; agentes sem `effort` em modelo diferente da sessão.
4. Instruções contraditórias, vagas ou escritas para um modelo mais antigo (regras que o modelo atual já segue sozinho, ou que fazem ele trabalhar a mais).
5. Skills que mandam abrir subagentes para tarefas pequenas.
6. Texto duplicado entre CLAUDE.md, skills e agentes (paga tokens em toda sessão).

No fim: lista "posso aplicar já" (só correções de certeza alta) e lista "você decide". Não edite nenhum arquivo até eu responder "aplica".
```

Por que funciona: a Anthropic mediu 14% de economia só por revisar os prompts contra o modelo atual, nas duas trocas de modelo testadas (página "Optimizing for cost and intelligence").
