import json, os, sys, collections

path = sys.argv[1]
try:
    with open(path) as fh:
        data = json.load(fh)
except (OSError, json.JSONDecodeError):
    print("## Vale report\n\nVale produced no parsable output.")
    raise SystemExit(0)

ORDER = {"error": 0, "warning": 1, "suggestion": 2}
ICON = {"error": "🔴", "warning": "🟡", "suggestion": "🔵"}

counts = collections.Counter()
for alerts in data.values():
    for a in alerts:
        counts[a["Severity"]] += 1
total = sum(counts.values())

out = ["## Vale report", ""]
if not total:
    out.append("No issues found.")
    print("\n".join(out))
    raise SystemExit(0)

out.append(
    "**{} issues** across **{} files** — {}".format(
        total,
        len(data),
        ", ".join(
            "{} {} {}".format(ICON.get(s, ""), counts[s], s)
            for s in sorted(counts, key=lambda x: ORDER.get(x, 9))
        ),
    )
)
out += ["", "| File | Errors | Warnings | Suggestions |", "|---|---:|---:|---:|"]
for f in sorted(data, key=lambda f: -len(data[f])):
    c = collections.Counter(a["Severity"] for a in data[f])
    out.append(
        "| `{}` | {} | {} | {} |".format(
            f, c["error"], c["warning"], c["suggestion"]
        )
    )

out.append("")
for f in sorted(data):
    alerts = sorted(
        data[f], key=lambda a: (ORDER.get(a["Severity"], 9), a["Line"])
    )
    out += [
        "<details><summary><b>{}</b> — {} issues</summary>".format(f, len(alerts)),
        "",
        "| Line | Severity | Rule | Message |",
        "|---:|---|---|---|",
    ]
    for a in alerts:
        msg = a["Message"].replace("|", "\\|")
        out.append(
            "| {} | {} {} | `{}` | {} |".format(
                a["Line"], ICON.get(a["Severity"], ""), a["Severity"],
                a["Check"], msg,
            )
        )
    out += ["", "</details>", ""]

print("\n".join(out))
