#!/usr/bin/env python3
"""Lê os .jsonl do medir-explore.sh e resume custo por modelo (modelUsage do evento result)."""
import json, sys, pathlib, collections

pasta = pathlib.Path(sys.argv[1])
gab = [l.strip() for l in (pasta/"gabarito.txt").read_text().splitlines() if l.strip()] if (pasta/"gabarito.txt").exists() else []
def nota(resp):
    return f"{sum(g in resp for g in gab)}/{len(gab)}" if gab else "-"
linhas, agg = [], collections.defaultdict(list)
for f in sorted(pasta.glob("*.jsonl")):
    res, agentes = None, []
    for l in f.read_text().splitlines():
        try:
            e = json.loads(l)
        except Exception:
            continue
        if e.get("type") == "result":
            res = e
        if e.get("type") == "assistant":
            for c in e.get("message", {}).get("content", []):
                if c.get("type") == "tool_use" and c.get("name") in ("Agent", "Task"):
                    agentes.append(c.get("input", {}).get("subagent_type", "?"))
    if not res:
        linhas.append((f.stem, "SEM RESULTADO", {}, 0, "", agentes)); continue
    mu = res.get("modelUsage", {})
    por = {m: round(v.get("costUSD", 0), 4) for m, v in mu.items()}
    total = round(res.get("total_cost_usd", sum(por.values())), 4)
    full = res.get("result") or ""
    linhas.append((f.stem, ("ok" if not res.get("is_error") else "erro") + " " + nota(full), por, total, full[:120].replace("\n", " "), agentes))
    agg[f.stem.split("-")[0]].append((total, por))

md = ["| rodada | status | subagentes chamados | custo por modelo (US$) | total (US$) | resposta |", "|---|---|---|---|---|---|"]
for s, st, por, tot, resp, ag in linhas:
    md.append(f"| {s} | {st} | {', '.join(ag) or '-'} | {'; '.join(f'{k}: {v}' for k, v in por.items())} | {tot} | {resp.replace('|', '/')} |")
md.append("")
for v, rs in agg.items():
    md.append(f"- **{v}**: média total US$ {sum(t for t, _ in rs)/len(rs):.4f} em {len(rs)} rodadas")
(pasta / "resumo.md").write_text("\n".join(md) + "\n")
(pasta / "resumo.json").write_text(json.dumps([dict(rodada=s, status=st, por_modelo=p, total=t, resposta=r, subagentes=a) for s, st, p, t, r, a in linhas], indent=1, ensure_ascii=False))
print("\n".join(md))
