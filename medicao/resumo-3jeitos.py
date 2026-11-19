#!/usr/bin/env python3
"""Resume a pasta do medir-3jeitos.sh: custo por modelo, total, tempo, subagentes, nota do checador oculto."""
import json, sys, pathlib, re, collections

pasta = pathlib.Path(sys.argv[1])
rows, agg = [], collections.defaultdict(list)
for f in sorted(pasta.glob("*.jsonl")):
    res, sub = None, collections.Counter()
    for l in f.read_text().splitlines():
        try:
            e = json.loads(l)
        except Exception:
            continue
        if e.get("type") == "result":
            res = e
        if e.get("type") == "assistant" and not e.get("parent_tool_use_id"):
            for c in e.get("message", {}).get("content", []):
                if c.get("type") == "tool_use" and c.get("name") in ("Agent", "Task"):
                    sub[c.get("input", {}).get("model") or c.get("input", {}).get("subagent_type") or "?"] += 1
    chk = (pasta / f"{f.stem}.checar.txt").read_text() if (pasta / f"{f.stem}.checar.txt").exists() else ""
    m = re.search(r"NOTA (\d+)/(\d+)", chk) or re.search(r"(\d+)\s*/\s*(\d+)", chk)
    nota = f"{m.group(1)}/{m.group(2)}" if m else "?"
    tempo = (pasta / f"{f.stem}.tempo").read_text().strip().split("=")[-1] if (pasta / f"{f.stem}.tempo").exists() else "?"
    por = {k: round(v.get("costUSD", 0), 3) for k, v in (res or {}).get("modelUsage", {}).items()}
    tot = round((res or {}).get("total_cost_usd", 0), 3)
    rows.append(dict(rodada=f.stem, nota=nota, total=tot, por_modelo=por, tempo_s=tempo, subagentes=dict(sub), ok=bool(res) and not res.get("is_error")))
    agg[f.stem.rsplit("-", 1)[0]].append((tot, nota, tempo))

md = ["| rodada | nota | total US$ (equiv. API) | por modelo | tempo (s) | subagentes |", "|---|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['rodada']} | {r['nota']} | {r['total']} | {'; '.join(f'{k.replace('claude-', '')}: {v}' for k, v in r['por_modelo'].items())} | {r['tempo_s']} | {', '.join(f'{k}×{v}' for k, v in r['subagentes'].items()) or '-'} |")
md.append("")
for j, xs in agg.items():
    md.append(f"- **{j}**: custo médio US$ {sum(x[0] for x in xs)/len(xs):.3f} · notas {', '.join(x[1] for x in xs)} · tempos {', '.join(x[2] for x in xs)} s")
(pasta / "resumo.md").write_text("\n".join(md) + "\n")
(pasta / "resumo.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print("\n".join(md))
