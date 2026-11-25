# fable-barato

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Seu Fable mais barato](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

O Fable 5.2 êÂ© o modelo mais forte da Anthropic e tambêÂ©m o mais caro: cada token de entrada e de saêÂ­da custa o dobro do Opus. Quem usa o Claude Code pela assinatura gasta o limite do Fable bem mais rêÂ¡pido do que imagina, porque parte do trabalho roda em modelos que vocêÂª nêÂ£o escolheu. A Anthropic publicou um documento explicando onde estêÂ¡ esse gasto e como cortar. Este repositêÂ³rio traz o que o documento diz, o que nêÂ³s medimos na prêÂ¡tica e o **fable-barato**: um kit gratuito que vocêÂª instala em um minuto no Claude Code.

## ê°Å¸ââ Guia de uso

Guia completo (o documento oficial, as mediêÂ§êÂµes e o passo a passo): **https://linnoff88-dev.github.io/

## O que medimos (15/11/2026, Claude Code 2.1.325, pela assinatura, pasta isolada)

| MediêÂ§êÂ£o | Resultado |
|---|---|
| Busca de arquivo numa sessêÂ£o Fable, sem o kit | rodou no **Opus**: US$ 0,05ê¢â¬â0,12 por busca |
| A mesma busca com o `Explore.md` do kit | rodou no **Haiku**: US$ 0,002 por busca, **22êâ a 48êâ mais barata** (por par de rodadas), a mesma resposta nas 12 rodadas |
| Tarefa pequena: Opus sêÂ³ / Fable sêÂ³ / Fable chefiando ajudantes | US$ 0,19 / 0,46 / 0,83, todos com nota mêÂ¡xima |
| Tarefa grande (20 mêÂ³dulos): os mesmos trêÂªs jeitos | US$ 0,42 / 0,62 / 1,01, todos com nota mêÂ¡xima |

Os valores sêÂ£o o "equivalente de API" que o Claude Code informa (na assinatura, viram consumo do limite). Dados brutos em [`medicao/resultados/`](medicao/resultados/). As fontes oficiais, com os trechos, estêÂ£o no guia (seêÂ§êÂ£o "O documento").

## O kit

| Arquivo | O que faz |
|---|---|
| `agentes/Explore.md` | Substitui a busca embutida: sêÂ³ leitura, `model: haiku`, `effort: medium` |
| `agentes/revisor-fable.md` | RevisêÂ£o final no Fable 5.2 (high), sêÂ³ quando vocêÂª pede "revisêÂ£o fable" |
| `regras/QUANDO-DIVIDIR.md` | Bloco para o CLAUDE.md: modelo padrêÂ£o, modelo por tipo de ajudante, quando dividir, briefing de 5 itens |
| `skill/fable-barato/SKILL.md` | `/fable-barato status`, `auditar` e `dividir <tarefa>` |
| `auditar/PROMPT.md` | Auditoria do ambiente sem mudar nada (rodar no Fable a cada modelo novo) |
| `instalar.sh` | Instala, reinstala sem duplicar (com backup) e desfaz |
| `medicao/` | Scripts para refazer as mediêÂ§êÂµes no seu projeto |

## O processo, do inêÂ­cio ao fim

| # | Passo | Comando | Quem |
|---|---|---|---|
| 1 | Baixar o kit | `git clone https://github.com/linnoff88-dev/fable-barato ~/fable-barato` | ê°Å¸Â§Â  vocêÂª |
| 2 | Instalar: para todos os projetos, ou sêÂ³ num projeto | `~/fable-barato/instalar.sh` ou `cd ~/meu-projeto && ~/fable-barato/instalar.sh --projeto` | ê¢Å¡â¢ê¯Â¸Â script |
| 3 | Conferir a busca no Haiku | no Claude Code: peêÂ§a uma busca, rode `/tasks` e `/fable-barato status` | ê°Å¸Â§Â  vocêÂª |
| 4 | Trabalhar no dia a dia | a regra do CLAUDE.md orienta modelo, esforêÂ§o e quando dividir | ê°Å¸Â¤â Claude Code |
| 5 | Decidir se divide uma tarefa grande | `/fable-barato dividir "<tarefa>"` | ê°Å¸Â¤â Claude Code |
| 6 | RevisêÂ£o final de trabalho importante | `revisêÂ£o fable` | ê°Å¸Â¤â Claude Code (Fable) |
| 7 | Auditar a cada modelo novo | `/fable-barato auditar` ê¢â â responder `aplica` | ê°Å¸Â§Â  vocêÂª + ê°Å¸Â¤â |
| 8 | Medir (opcional, Linux) | `cd ~/fable-barato/medicao && PEDIDO="..." ./medir-explore.sh ~/meu-projeto 3 fable medium` | ê¢Å¡â¢ê¯Â¸Â script |
| 9 | Desfazer | `~/fable-barato/instalar.sh --desfazer` (ou `--desfazer --projeto` dentro do projeto) | ê¢Å¡â¢ê¯Â¸Â script |

Testes do kit (nunca tocam o seu `~/.claude`): `bash tests/rodar.sh`.

## NêÂ­vel 2: maestro-roteador

Para escolher modelo e esforêÂ§o por tarefa (inclusive de cada ajudante), use o [maestro-roteador](https://github.com/linnoff88-dev/maestro-roteador), versêÂ£o 1.3 com as regras do Fable 5.2.

## LicenêÂ§a

MIT. GrêÂ¡tis no [ARCKHê AI](https://ARCKHê AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>