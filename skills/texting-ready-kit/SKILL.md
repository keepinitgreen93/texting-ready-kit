---
name: texting-ready-kit
description: Fill in A2P-ready Privacy, Terms and opt-in text.
version: 1.0.0
author: Truly Authentic Marketing
license: TAM Private Client License
metadata:
  hermes:
    tags: [a2p, sms, compliance, privacy-policy, terms, product-champ, highlevel]
    related_skills: [brand-voice-builder, premium-client-documents]
---

# Texting Ready Kit

Helps a small business owner write a Privacy Policy, Terms of Service and text opt-in wording that pass A2P 10DLC (business texting) review. Hermes interviews the owner, fills the templates, audits the site, and drafts the pages. The owner approves before anything is published.

This is a starting point, not legal advice. Have an attorney review it for your state and industry. Healthcare and HIPAA businesses must check with counsel first, and Hermes stays out of private health details.

## When to use

- The owner needs a privacy policy and terms before registering for business texting in Product Champ (HighLevel) or another A2P platform.
- A texting campaign was rejected and the policy, terms or opt-in form must be fixed.
- The owner wants an audit of their site and forms against the A2P checklist.

Do not use for: legal advice, regulated or prohibited message categories, or non-US texting rules.

## Files

- `templates/privacy-policy-template.md` and `templates/terms-of-service-template.md`: fill-in templates with [BRACKETED] blanks and an SMS section.
- `templates/opt-in-form-language.md`: checkbox text, confirmation, STOP, HELP and sample messages.
- `references/hermes-prompts.md`: the interview, page-draft and audit prompts.
- `references/presubmit-checklist.md`: the 10 item checklist.
- `references/sources.md`: source links and what could not be confirmed.

## Procedure

1. **Read the owner's Company Brain first.** Pull business facts and tell the owner what you found in three lines. Done when no question repeats something the Brain already answers.
2. **Interview, one question at a time.** Follow Prompt A in `references/hermes-prompts.md`: legal name, DBA, address, phone, business email, website, state, services, text types, frequency, join methods, payments, age limits. Mark unknowns [NEEDS OWNER]. Never invent a fact. Done when every blank has an owner answer or a flag.
3. **Fill both templates.** Copy from `templates/`. Keep the SMS section wording, especially the sentence that mobile information is not shared with third parties or affiliates for marketing or promotional purposes. Never add wording about buying, selling or sharing lists. Done when the name, address, phone, email and website match in both files, and message types and frequency match across Terms, opt-in text and campaign description.
4. **Write the opt-in text.** Use `templates/opt-in-form-language.md`: unchecked, optional, separate checkboxes for marketing and non-marketing, with frequency, rates, STOP, HELP and both links. Default campaign type is Low Volume Mixed unless the owner sends only one kind of text.
5. **Audit.** Run Prompt C from `references/hermes-prompts.md` on the live site and forms. Read-only. Done when each of the 12 items is PASS, FAIL or CAN'T TELL with a quote.
6. **Draft the pages.** Use Prompt B. Create the Privacy and Terms pages as drafts only, add footer links, and show the owner the drafts. Done when the owner has seen a preview.
7. **Get explicit approval before publishing.** Publish only after the owner replies with a clear yes in the chat. Then open each public link with no login and give the owner both URLs.
8. **Run the checklist.** Walk the owner through `references/presubmit-checklist.md`. Submit registration only once the paid plan is active.

## Guardrails

- Never publish, send, delete or change a page, form, text or email without explicit approval from the owner.
- Never ask for or accept passwords, API keys or tokens in chat. Use the platform's own connection.
- Never fabricate laws, fees, rule numbers or approval promises. Say what is not confirmed. Approval is decided by carriers, not by this kit.
- Work only in the owner's own account. Use only the owner's own business details. No other business's names or data.
- Keep plain words at about a seventh grade level. No hype words.

## Pitfalls

- A pre-ticked box, or consent bundled into "I agree to the Terms," is the most common rejection.
- Different business names or addresses across the site, policy, terms and registration cause rejection.
- A policy that says numbers may be shared with partners or affiliates is rejected.
- Free email addresses (Gmail, Yahoo) as the contact are rejected.
- A second form or widget collecting SMS consent on the same page can confuse review.

## Verification

- Both templates have no [BRACKETED] blank left, except items flagged [NEEDS OWNER].
- The disclaimer line is present in every owner-facing document.
- The audit result lists any gaps with exact fixes.
- The owner approved in the chat before any page went live.
