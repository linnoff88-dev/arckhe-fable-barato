# fable-barato

[![Your cheaper Fable](guia/assets/banner-en.jpg)](https://linnoff88-dev.github.io/

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

Fable 5.2 is Anthropic’s strongest model and also its most expensive: each input and output token costs twice as much as Opus. People who use Claude Code through a subscription spend their Fable limit much faster than they realize, because some of the work runs on models they didn’t choose. Anthropic published a document explaining where that spending comes from and how to reduce it. This repository covers what the document says, what we measured in practice, and **fable-barato**: a free kit you can install in one minute in Claude Code.

## 📖 User guide

Complete guide (the official document, the measurements, and the step-by-step instructions): **https://linnoff88-dev.github.io/

## What we measured (11/15/2026, Claude Code 2.1.325, subscription, isolated folder)

| Measurement | Result |
|---|---|
| File search in a Fable session, without the kit | ran on **Opus**: US$ 0.05–0.12 per search |
| The same search with the kit’s `Explore.md` | ran on **Haiku**: US$ 0.002 per search, **22× to 48× cheaper** (per pair of runs), the same answer in all 12 runs |
| Small task: Opus only / Fable only / Fable leading helpers | US$ 0.19 / 0.46 / 0.83, all with top marks |
| Large task (20 modules): the same three approaches | US$ 0.42 / 0.62 / 1.01, all with top marks |

The values are the “API equivalent” reported by Claude Code (on a subscription, they count toward your usage limit). Raw data in [`medicao/resultados/`](medicao/resultados/). Official sources, with excerpts, are in the guide (“The document” section).

## The kit

| File | What it does |
|---|---|
| `agentes/Explore.md` | Replaces built-in search: read-only, `model: haiku`, `effort: medium` |
| `agentes/revisor-fable.md` | Final review in Fable 5.2 (high), only when you ask for “Fable review” |
| `regras/QUANDO-DIVIDIR.md` | Block for `CLAUDE.md`: default model, model by helper type, when to split tasks, 5-item brief |
| `skill/fable-barato/SKILL.md` | `/fable-barato status`, `auditar`, and `dividir <tarefa>` |
| `auditar/PROMPT.md` | Environment audit that changes nothing (run in Fable whenever a new model is released) |
| `instalar.sh` | Installs, reinstalls without duplicating (with backup), and undoes |
| `medicao/` | Scripts to repeat the measurements in your project |

## The process, start to finish

| # | Step | Command | Who |
|---|---|---|---|
| 1 | Download the kit | `git clone https://github.com/linnoff88-dev/fable-barato ~/fable-barato` | 🧠 you |
| 2 | Install: for all projects, or just one project | `~/fable-barato/instalar.sh` or `cd ~/my-project && ~/fable-barato/instalar.sh --projeto` | ⚙️ script |
| 3 | Check the search on Haiku | In Claude Code: ask for a search, run `/tasks` and `/fable-barato status` | 🧠 you |
| 4 | Work day to day | The `CLAUDE.md` rule guides model and effort selection, and when to split tasks | 🤖 Claude Code |
| 5 | Decide whether to split a large task | `/fable-barato dividir "<tarefa>"` | 🤖 Claude Code |
| 6 | Final review of important work | `Fable review` | 🤖 Claude Code (Fable) |
| 7 | Audit whenever a new model is released | `/fable-barato auditar` → reply `aplica` | 🧠 you + 🤖 |
| 8 | Measure (optional, Linux) | `cd ~/fable-barato/medicao && PEDIDO="..." ./medir-explore.sh ~/my-project 3 fable medium` | ⚙️ script |
| 9 | Undo | `~/fable-barato/instalar.sh --desfazer` (or `--desfazer --projeto` inside the project) | ⚙️ script |

Kit tests (never touch your `~/.claude`): `bash tests/rodar.sh`.

## Level 2: maestro-roteador

To choose a model and effort for each task (including each helper), use [maestro-roteador](https://github.com/linnoff88-dev/maestro-roteador), version 1.3 with the Fable 5.2 rules.

## License

MIT. Free on [ARCKHÉ AI](https://ARCKHÉ AI).
