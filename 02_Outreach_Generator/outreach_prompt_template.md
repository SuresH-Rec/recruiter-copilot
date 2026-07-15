# ✉️ Personalized Outreach Generator

An AI-powered prompt system to generate personalized candidate outreach
messages across LinkedIn InMail, Email, and WhatsApp — built for tech
recruitment targeting niche roles in AI/ML, RPA, Cloud, and Data.

---

## The Problem

Most recruiters send generic messages:
> *"Hi, I came across your profile and have an exciting opportunity.
> Please share your updated resume."*

Candidates — especially senior ones — ignore these. Response rates
hover around 5-10% for generic outreach.

**Personalized outreach that references specific skills, current company,
and career trajectory achieves 25-40% response rates.**

---

## How This Works

```
Paste:  Candidate's LinkedIn/Naukri profile snippet + JD
   ↓
Claude reads both
   ↓
Generates a personalized message that mentions:
  → Their specific skills or current role
  → Why THIS role fits THEM specifically
  → A clear, low-friction call to action
```

---

## Master Prompt Template

```
You are an expert IT recruiter writing personalized candidate 
outreach messages. Your goal is to write a message that feels 
genuinely researched — not templated.

CANDIDATE PROFILE:
[Paste candidate's LinkedIn summary / headline / key skills]

ROLE BEING HIRED FOR:
[Paste JD or summarize key requirements]

RECRUITER NAME: [Your name]
COMPANY: [Hiring company or "a product startup"]
TONE: [Professional & warm / Short & punchy / Conversational]

Generate 3 versions:
1. LinkedIn InMail — max 300 characters message body
2. Email — with subject line and full body
3. WhatsApp — under 200 characters, casual and direct

Rules:
- Open with something specific from their profile
- Mention 1-2 reasons why THIS role fits THEM
- CTA: "Would you be open to a quick 10-min chat?"
- Do NOT use "exciting opportunity" or "dynamic role"
- After messages add: "Why this works" — 2-3 bullet points
```

---

## Real Example — Scrum Master Role

### Candidate Profile Used
```
Bhanuprakash | Scrum Master at Luxoft | 4 years exp
Skills: Scrum, SAFe, Azure DevOps, JIRA, Confluence
Currently managing 2 Agile teams simultaneously
CSM + PSM I certified | Bangalore
```

### JD Summary
```
Scrum Master at AB InBev | Bangalore | 5 days WFO
Must have: SAFe, Azure DevOps, JIRA | 4+ years exp
```

### Generated LinkedIn InMail
**Subject:** SAFe + Azure DevOps experience stood out

**Message:**
Hi Bhanuprakash, managing two Agile teams simultaneously at Luxoft
while holding both CSM and PSM I certifications is exactly the profile
AB InBev is looking for. The role involves SAFe at scale — your current
experience maps directly. Open to a quick 10-min call this week?

— Suresh

---

### Generated Email
**Subject:** Your Scrum Master profile — worth a conversation?

**Body:**

Hi Bhanuprakash,

Your background at Luxoft caught my attention — specifically the
combination of managing two Agile teams simultaneously with hands-on
Azure DevOps experience. That's a rare combination.

AB InBev is looking for a Scrum Master to lead SAFe-aligned delivery
for their technology teams in Bangalore. Your dual-team experience and
certification stack (CSM + PSM I) make you a strong fit for what they
need.

The role is 5 days WFO at their Mahadevpura office — happy to share
more details if you're open to exploring.

Would you be open to a 10-minute call this week? No pressure at all.

Warm regards,
Suresh

---

### Generated WhatsApp
```
Hi Bhanuprakash, saw your Scrum Master profile at Luxoft —
have a SAFe + Azure DevOps role at AB InBev that fits well.
Open to a quick 10-min chat? – Suresh
```

---

## Response Rate Results

| Role | Messages Sent | Responses | Rate |
|---|---|---|---|
| Scrum Master | 3 | 3 | **100%** 🔥 |
| Data Engineer | 3 | 0 | 0% |
| AI Engineer | 3 | 0 | 0% |
| **Total** | **9** | **3** | **33%** |

**Key insight:** 100% response on Scrum Master because it was a
clear skill match. Data Engineer and AI Engineer had partial matches
— personalization helps but fit is the primary driver.

---

## What Makes Outreach Work — Key Rules

| Rule | Why it matters |
|---|---|
| Open with something specific | Shows you actually read their profile |
| Mirror their career language | Resonates immediately |
| Low-friction CTA | "10-min chat" beats "send your resume" |
| Under 150 words for email | Senior candidates skim |
| No "exciting opportunity" | Instantly signals a template |
| One specific reason they fit | Better than listing 5 generic ones |

---

## Platform-Specific Guidelines

**LinkedIn InMail**
- Subject: under 50 characters
- Body: under 300 characters
- Be direct — they can see your profile

**Email**
- Subject: reference their specific skill or company
- Body: 100-150 words maximum
- One ask only — the 10-min call

**WhatsApp**
- Under 200 characters
- Casual tone, first name only
- Single sentence ask

---

*Built by Suresh Korumilli — Senior Talent Acquisition Professional*
*Part of the Recruiter Copilot project*
*Real results: 33% response rate across 9 messages, 3 roles*
