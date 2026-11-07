from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("name", "description", "version", "author", "license")
FORBIDDEN = [
    r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/]+[\\/]+Documents[\\/]+tam-aios",
    r"tam-aios[/\\]Company Brain",
    r"Company Brain[/\\]brain[/\\](clients|company|strategy)",
    r"BEGIN (RSA|OPENSSH|EC) PRIVATE KEY",
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"sk-[A-Za-z0-9]{20,}",
]

def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            data[m.group(1)] = m.group(2).strip().strip('"\'')
    return data

errors = []
files = sorted(ROOT.glob("skills/*/SKILL.md")) + sorted(ROOT.glob("packs/**/skills/*/SKILL.md"))
if not files:
    errors.append("No SKILL.md files found")
for path in files:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{path.relative_to(ROOT)}: invalid frontmatter")
        continue
    for key in REQUIRED:
        if not fm.get(key):
            errors.append(f"{path.relative_to(ROOT)}: missing {key}")
    if fm.get("name") and path.parent.name != fm["name"]:
        errors.append(f"{path.relative_to(ROOT)}: folder/name mismatch ({fm['name']})")
    for pattern in FORBIDDEN:
        if re.search(pattern, text, re.I):
            errors.append(f"{path.relative_to(ROOT)}: forbidden pattern {pattern}")
    if not re.search(r"\[REAL PROOF NEEDED\]|Never fabricate|Never invent", text, re.I):
        errors.append(f"{path.relative_to(ROOT)}: missing proof guardrail")
    if "explicit approval" not in text.lower():
        errors.append(f"{path.relative_to(ROOT)}: missing external-action approval gate")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"VALIDATION PASSED: {len(files)} skills")
