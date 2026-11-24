# fable-barato

[![Tu Fable más barato](guia/assets/banner-es.jpg)](https://linnoff88-dev.github.io/

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Fable 5.2 es el modelo más potente de Anthropic y también el más caro: cada token de entrada y de salida cuesta el doble que en Opus. Quienes usan Claude Code con la suscripción consumen el límite de Fable mucho más rápido de lo que imaginan, porque parte del trabajo se ejecuta con modelos que no eligieron. Anthropic publicó un documento que explica dónde se produce ese gasto y cómo reducirlo. Este repositorio presenta lo que dice el documento, lo que medimos en la práctica y **fable-barato**: un kit gratuito que instalas en un minuto en Claude Code.

## 📖 Guía de uso

Guía completa (el documento oficial, las mediciones y el paso a paso): **https://linnoff88-dev.github.io/

## Lo que medimos (15/11/2026, Claude Code 2.1.325, con la suscripción, en una carpeta aislada)

| Medición | Resultado |
|---|---|
| Búsqueda de archivo en una sesión de Fable, sin el kit | se ejecutó en **Opus**: US$ 0,05–0,12 por búsqueda |
| La misma búsqueda con `Explore.md` del kit | se ejecutó en **Haiku**: US$ 0,002 por búsqueda, **22× a 48× más barata** (por par de rondas), la misma respuesta en las 12 rondas |
| Tarea pequeña: solo Opus / solo Fable / Fable dirigiendo asistentes | US$ 0,19 / 0,46 / 0,83, todos con la puntuación máxima |
| Tarea grande (20 módulos): las mismas tres formas | US$ 0,42 / 0,62 / 1,01, todos con la puntuación máxima |

Los valores son el «equivalente de API» que informa Claude Code (con la suscripción, se convierten en consumo del límite). Datos sin procesar en [`medicao/resultados/`](medicao/resultados/). Las fuentes oficiales, con sus fragmentos, están en la guía (sección «El documento»).

## El kit

| Archivo | Qué hace |
|---|---|
| `agentes/Explore.md` | Reemplaza la búsqueda integrada: solo lectura, `model: haiku`, `effort: medium` |
| `agentes/revisor-fable.md` | Revisión final con Fable 5.2 (high), solo cuando pides «revisión fable» |
| `regras/QUANDO-DIVIDIR.md` | Bloque para el CLAUDE.md: modelo predeterminado, modelo por tipo de asistente, cuándo dividir, resumen de 5 puntos |
| `skill/fable-barato/SKILL.md` | `/fable-barato status`, `auditar` y `dividir <tarefa>` |
| `auditar/PROMPT.md` | Auditoría del entorno sin cambiar nada (ejecutar en Fable con cada modelo nuevo) |
| `instalar.sh` | Instala, reinstala sin duplicar (con copia de seguridad) y deshace |
| `medicao/` | Scripts para repetir las mediciones en tu proyecto |

## El proceso, de principio a fin

| # | Paso | Comando | Quién |
|---|---|---|---|
| 1 | Descargar el kit | `git clone https://github.com/linnoff88-dev/fable-barato ~/fable-barato` | 🧠 tú |
| 2 | Instalar: para todos los proyectos o solo en uno | `~/fable-barato/instalar.sh` o `cd ~/meu-projeto && ~/fable-barato/instalar.sh --projeto` | ⚙️ script |
| 3 | Comprobar la búsqueda en Haiku | En Claude Code: pide una búsqueda, ejecuta `/tasks` y `/fable-barato status` | 🧠 tú |
| 4 | Trabajar en el día a día | La regla del CLAUDE.md orienta sobre el modelo, el esfuerzo y cuándo dividir | 🤖 Claude Code |
| 5 | Decidir si dividir una tarea grande | `/fable-barato dividir "<tarefa>"` | 🤖 Claude Code |
| 6 | Revisión final de un trabajo importante | `revisión fable` | 🤖 Claude Code (Fable) |
| 7 | Auditar con cada modelo nuevo | `/fable-barato auditar` → responder `aplica` | 🧠 tú + 🤖 |
| 8 | Medir (opcional, Linux) | `cd ~/fable-barato/medicao && PEDIDO="..." ./medir-explore.sh ~/meu-projeto 3 fable medium` | ⚙️ script |
| 9 | Deshacer | `~/fable-barato/instalar.sh --desfazer` (o `--desfazer --projeto` dentro del proyecto) | ⚙️ script |

Pruebas del kit (nunca tocan tu `~/.claude`): `bash tests/rodar.sh`.

## Nivel 2: maestro-roteador

Para elegir el modelo y el esfuerzo por tarea (incluidos los de cada asistente), usa [maestro-roteador](https://github.com/linnoff88-dev/maestro-roteador), versión 1.3 con las reglas de Fable 5.2.

## Licencia

MIT. Gratis en [ARCKHÉ AI](https://ARCKHÉ AI).
