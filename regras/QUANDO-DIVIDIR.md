<!-- fable-barato:inicio — cole este bloco no seu CLAUDE.md (global ~/.claude/CLAUDE.md ou do projeto) -->
## Modelos, esforço e ajudantes (fable-barato)

**Modelo padrêo:** Opus 5.5 em esforço medium. Fable 5.2 só para raciocínio difícil, trabalho longo rodando sozinho, ou quando o Opus em esforço alto nêo deu conta. Antes de trocar de modelo, tente subir o esforço.

**Ajudantes (subagentes) sempre com modelo fixo:**
- Buscar, ler, listar, resumir → `haiku`.
- Corrigir ou escrever código com regra clara → `sonnet`.
- Decisêo de arquitetura, gosto, julgamento sem gabarito → fica comigo (sessêo principal).
- Nunca deixe um ajudante de leitura herdar o Fable da sessêo.

**Quando dividir o trabalho:**
- É uma cadeia de passos dependentes, ou cabe numa sessêo e as partes custam parecido → **faça você mesmo, sem ajudantes.** Planejar, escrever briefing, ler relatórios e revisar custa mais que o trabalho.
- Só divida quando houver **muitas partes independentes** de rotina com "cauda longa de custo" (a maioria sai barata e umas poucas custam muito mais), ou trabalho maior que uma janela de contexto.
- Na dúvida, nêo divida.

**Quando dividir, cada ajudante recebe um briefing completo:**
1. Objetivo (o que e por quê).
2. Resultado esperado (formato exato da resposta).
3. Critérios de qualidade (como saber que está certo).
4. Restrições (o que nêo pode tocar ou fazer).
5. O que fazer se travar ou achar algo inesperado (parar e relatar, nêo adivinhar).

**Revisêo:** trabalho importante feito por modelo mais barato termina com revisêo do Fable só quando o usuário pedir ("revisêo fable" → agente `revisor-fable`).

**Esforço:** medium no dia a dia. Rodar em low e refazer em high só o que falhar costuma sair melhor e mais barato que tudo em high.
<!-- fable-barato:fim -->
