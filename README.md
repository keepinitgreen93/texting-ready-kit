# Texting Ready Kit

A Hermes skill and printable kit that helps small business owners write a Privacy Policy, Terms of Service and text opt-in wording that pass A2P 10DLC (business texting) review. Built for Product Champ (HighLevel) businesses.

This kit is a starting point, not legal advice. Have an attorney review it for your state and industry.

## What is inside

```text
skills/texting-ready-kit/
  SKILL.md                 What the skill does and the steps Hermes follows
  templates/               Privacy Policy, Terms of Service, opt-in checkbox language
  references/              Hermes prompts, 10 item checklist, sources
kit/                       Texting-Ready-Kit.pdf and Word (.docx) copies
scripts/validate_skill.py  Local checker for SKILL.md files
```

## Install in Hermes

You need access to this private repository (a GitHub invite from TAM) and the GitHub CLI signed in.

Option 1, tap the repo:

```bash
hermes skills tap add keepinitgreen93/texting-ready-kit
hermes skills install texting-ready-kit
```

Option 2, copy the folder:

1. Download or clone this repo: `gh repo clone keepinitgreen93/texting-ready-kit`
2. Copy `skills/texting-ready-kit` into your Hermes skills folder (run `hermes skills list` to see where skills live).
3. Start a new Hermes session, then check that `texting-ready-kit` shows in `hermes skills list`.

## Use it

Tell Hermes: "Use the texting-ready-kit skill. Interview me and fill in my Privacy Policy and Terms." Hermes asks one question at a time, reads your Company Brain, and fills the templates. It drafts your pages in Product Champ, and nothing goes live until you say yes.

## Check the skill

```bash
python scripts/validate_skill.py
```

## Rules

- Keep this repository private.
- No client names, credentials or machine paths belong in this repo.
- Submit your texting registration only once your paid plan is active.
