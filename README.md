# fable-barato

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Seu Fable mais barato](guia/assets/banner.jpg)](https://inematds.github.io/fable-barato/guia/)

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

O Fable 5.2 Ã© o modelo mais forte da Anthropic e tambÃ©m o mais caro: cada token de entrada e de saÃ­da custa o dobro do Opus. Quem usa o Claude Code pela assinatura gasta o limite do Fable bem mais rÃ¡pido do que imagina, porque parte do trabalho roda em modelos que vocÃª nÃ£o escolheu. A Anthropic publicou um documento explicando onde estÃ¡ esse gasto e como cortar. Este repositÃ³rio traz o que o documento diz, o que nÃ³s medimos na prÃ¡tica e o **fable-barato**: um kit gratuito que vocÃª instala em um minuto no Claude Code.

## ðŸ“– Guia de uso

Guia completo (o documento oficial, as mediÃ§Ãµes e o passo a passo): **https://inematds.github.io/fable-barato/guia/**

## O que medimos (15/11/2026, Claude Code 2.1.325, pela assinatura, pasta isolada)

| MediÃ§Ã£o | Resultado |
|---|---|
| Busca de arquivo numa sessÃ£o Fable, sem o kit | rodou no **Opus**: US$ 0,05â€“0,12 por busca |
| A mesma busca com o `Explore.md` do kit | rodou no **Haiku**: US$ 0,002 por busca, **22Ã— a 48Ã— mais barata** (por par de rodadas), a mesma resposta nas 12 rodadas |
| Tarefa pequena: Opus sÃ³ / Fable sÃ³ / Fable chefiando ajudantes | US$ 0,19 / 0,46 / 0,83, todos com nota mÃ¡xima |
| Tarefa grande (20 mÃ³dulos): os mesmos trÃªs jeitos | US$ 0,42 / 0,62 / 1,01, todos com nota mÃ¡xima |

Os valores sÃ£o o "equivalente de API" que o Claude Code informa (na assinatura, viram consumo do limite). Dados brutos em [`medicao/resultados/`](medicao/resultados/). As fontes oficiais, com os trechos, estÃ£o no guia (seÃ§Ã£o "O documento").

## O kit

| Arquivo | O que faz |
|---|---|
| `agentes/Explore.md` | Substitui a busca embutida: sÃ³ leitura, `model: haiku`, `effort: medium` |
| `agentes/revisor-fable.md` | RevisÃ£o final no Fable 5.2 (high), sÃ³ quando vocÃª pede "revisÃ£o fable" |
| `regras/QUANDO-DIVIDIR.md` | Bloco para o CLAUDE.md: modelo padrÃ£o, modelo por tipo de ajudante, quando dividir, briefing de 5 itens |
| `skill/fable-barato/SKILL.md` | `/fable-barato status`, `auditar` e `dividir <tarefa>` |
| `auditar/PROMPT.md` | Auditoria do ambiente sem mudar nada (rodar no Fable a cada modelo novo) |
| `instalar.sh` | Instala, reinstala sem duplicar (com backup) e desfaz |
| `medicao/` | Scripts para refazer as mediÃ§Ãµes no seu projeto |

## O processo, do inÃ­cio ao fim

| # | Passo | Comando | Quem |
|---|---|---|---|
| 1 | Baixar o kit | `git clone https://github.com/inematds/fable-barato ~/fable-barato` | ðŸ§  vocÃª |
| 2 | Instalar: para todos os projetos, ou sÃ³ num projeto | `~/fable-barato/instalar.sh` ou `cd ~/meu-projeto && ~/fable-barato/instalar.sh --projeto` | âš™ï¸ script |
| 3 | Conferir a busca no Haiku | no Claude Code: peÃ§a uma busca, rode `/tasks` e `/fable-barato status` | ðŸ§  vocÃª |
| 4 | Trabalhar no dia a dia | a regra do CLAUDE.md orienta modelo, esforÃ§o e quando dividir | ðŸ¤– Claude Code |
| 5 | Decidir se divide uma tarefa grande | `/fable-barato dividir "<tarefa>"` | ðŸ¤– Claude Code |
| 6 | RevisÃ£o final de trabalho importante | `revisÃ£o fable` | ðŸ¤– Claude Code (Fable) |
| 7 | Auditar a cada modelo novo | `/fable-barato auditar` â†’ responder `aplica` | ðŸ§  vocÃª + ðŸ¤– |
| 8 | Medir (opcional, Linux) | `cd ~/fable-barato/medicao && PEDIDO="..." ./medir-explore.sh ~/meu-projeto 3 fable medium` | âš™ï¸ script |
| 9 | Desfazer | `~/fable-barato/instalar.sh --desfazer` (ou `--desfazer --projeto` dentro do projeto) | âš™ï¸ script |

Testes do kit (nunca tocam o seu `~/.claude`): `bash tests/rodar.sh`.

## NÃ­vel 2: maestro-roteador

Para escolher modelo e esforÃ§o por tarefa (inclusive de cada ajudante), use o [maestro-roteador](https://github.com/inematds/maestro-roteador), versÃ£o 1.3 com as regras do Fable 5.2.

## LicenÃ§a

MIT. GrÃ¡tis no [INEMA.CLUB](https://inema.club).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>