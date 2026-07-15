# 🔍 Resume Screener & Candidate Ranker

An AI-assisted resume screening system that evaluates candidates against
a Job Description and produces structured screening reports with fit
scores, strengths, gaps, and recruiter recommendations.

---

## The Problem

Manual resume screening is:
- **Time-consuming** — 3–5 minutes per profile to read and decide
- **Inconsistent** — stricter at 9am than at 4pm
- **Error-prone** — skills buried on page 2 get missed
- **Unscalable** — 50 resumes = 3+ hours of manual work

**With AI-assisted screening:** same 50 resumes in under 15 minutes,
consistent evaluation criteria, structured output ready to share
with hiring managers.

---

## How This Works

```
Upload resumes (or paste profile snapshots)
         ↓
Claude evaluates each candidate against the JD
         ↓
Output per candidate:
  → Fit Score (out of 10)
  → Top 3 strengths
  → Top 2 gaps / watch-outs
  → Recruiter recommendation
  → First screening question to ask
         ↓
Final ranking + Hiring Manager pitch
```

---

## Master Screening Prompt

```
You are an expert IT recruiter and talent evaluator.
Screen and rank the following candidates against the
job description below.

JD:
[Paste full JD or summarize key requirements]

SCREENING PRIORITIES:
[Must-have skills / Years of experience / Domain fit /
Stability / Location / Career progression]

CANDIDATE 1:
[Paste resume or profile snapshot]

CANDIDATE 2:
[Paste resume or profile snapshot]

For EACH candidate provide:
1. Fit Score: X/10
2. Strengths — 2-3 bullet points matching the JD
3. Gaps / Watch-outs — 1-2 bullet points
4. Recruiter Recommendation:
   ✅ Strong Shortlist
   🟡 Conditional Shortlist (clarify X first)
   ❌ Not a Fit Right Now
5. Suggested first screening question

After all candidates:
- Final Ranking (1st to last) with one-line reason
- Hiring Manager Pitch — 2-3 lines on top candidate

Be honest about gaps. Do not oversell weak candidates.
```

---

## Real Example — Scrum Master Screening

**JD:** Scrum Master | AB InBev | 4+ Years | Bengaluru Mahadevpura |
5 Days WFO | SAFe, Azure DevOps, JIRA, ClickUp | Agile Coaching

**Screening Priorities:** Must-have skills, Years of experience,
Domain fit, Stability

---

### Candidate 1 — Aniruddha V

**Profile Summary:**
Certified Scrum Master | 6 years total exp | Scrum Master at Alshaya
Groups (Aug 2022 – Jan 2024) | Previously Team Lead Operations at
Unisys (Jan 2018 – Feb 2022) | Certifications: CSM, CSPO,
AI-Empowered SAFe Scrum Master, Generative AI | Bengaluru

**Fit Score: 7/10**

**Strengths:**
- Strong certification stack — CSM + CSPO + AI-Empowered SAFe
  Scrum Master + GenAI certifications. The AI certifications are a
  bonus given AB InBev's innovation culture
- Hands-on SAFe experience including PI Planning, system demos, sprint
  ceremonies at Alshaya Groups
- Led teams of 8–15 people with conflict mediation and KPI dashboards

**Gaps / Watch-outs:**
- Actual Scrum Master experience is only ~1.5 years (Aug 2022 – Jan
  2024). Before that: Team Lead Operations at Unisys (non-tech) and
  Technical Support at Dell. The 6 years total is misleading
- No mention of Azure DevOps specifically — JD requires it

**Recruiter Recommendation:** 🟡 Conditional Shortlist
Clarify actual SM tenure and Azure DevOps exposure before presenting
to hiring manager.

**First Screening Question:**
*"Your resume shows Scrum Master experience from Aug 2022 to Jan 2024.
Are you currently in an SM role, and what have you been doing since
January 2024?"*

---

### Candidate 2 — Sweta Dash

**Profile Summary:**
Scrum Master | 5.8 years exp | Scrum Master at Eterno Infotech
(Apr 2021 – Jul 2025) | Banking/FX Deals domain | Skills: SAFe,
JIRA, Confluence, AI Tools (Atlassian Intelligence, Copilot),
Power BI, Agile Metrics, DevOps collaboration | Bengaluru

**Fit Score: 8.5/10**

**Strengths:**
- Nearly 4.5 years as Scrum Master at Eterno Infotech on a
  Banking/FX Deals project — domain depth and tenure are both strong
- Already using AI tools within Agile ceremonies (Atlassian
  Intelligence, Copilot) — direct match for AB InBev's
  innovation-driven culture
- Power BI skills, SAFe exposure, advanced Agile metrics
  (Burndown, Velocity, CFD) — goes beyond basic SM capability

**Gaps / Watch-outs:**
- Started career as QA (Dec 2019 – Mar 2021) — not a gap but
  worth noting that SM journey started in 2021
- Azure DevOps not explicitly mentioned — JIRA is primary tool

**Recruiter Recommendation:** ✅ Strong Shortlist
Best overall fit of the three. Present to hiring manager.

**First Screening Question:**
*"The AB InBev role uses Azure DevOps alongside JIRA — do you have
any hands-on experience with Azure DevOps, even in a limited
capacity?"*

---

### Candidate 3 — Bhanuprakash S

**Profile Summary:**
Scrum Master | 4 years exp | Currently managing 2 Agile teams
simultaneously at Luxoft (1 SAFe + 1 Scrum) | Certifications:
CSM + PSM I + Google Project Management | Tools: Azure DevOps,
JIRA, Confluence | SAFe PI Planning, Scrum of Scrums, ART syncs |
Bengaluru

**Fit Score: 8/10**

**Strengths:**
- Currently managing TWO Agile teams simultaneously — exactly the
  multi-team SM experience AB InBev needs
- Azure DevOps explicitly listed — direct JD match, strongest of
  the three on this point
- SAFe PI Planning, Scrum of Scrums, ART syncs — advanced SAFe
  exposure. Trained 4+ developers in Agile transition

**Gaps / Watch-outs:**
- Total IT experience ~4 years, SM experience ~3 years — slightly
  on the lower end of the 4+ years requirement. Quality is high
  but tenure is a potential concern
- Joined Luxoft recently — worth checking if there is a notice
  period concern or reason for early move

**Recruiter Recommendation:** ✅ Strong Shortlist
Flag to HM as high potential. Strong technical match despite
slightly lower tenure.

**First Screening Question:**
*"You joined Luxoft in October 2025 — that's fairly recent. What's
prompting you to explore new opportunities so soon?"*

---

## Final Ranking

| Rank | Candidate | Score | Reason |
|---|---|---|---|
| 🥇 1st | Sweta Dash | 8.5/10 | Longest pure SM tenure, AI tool adoption, banking domain, solid metrics depth |
| 🥈 2nd | Bhanuprakash S | 8/10 | Azure DevOps match, multi-team SAFe, strong certs — slightly lower tenure |
| 🥉 3rd | Aniruddha V | 7/10 | Good certs but only 1.5 years actual SM exp, employment gap needs clarity |

---

## Hiring Manager Pitch — Top Candidate

> *"Sweta Dash brings 4.5 years of focused Scrum Master experience in
> a Banking domain, which maps well to AB InBev's enterprise environment.
> She is already using AI tools within Agile ceremonies and understands
> advanced Agile metrics. Only point to validate is Azure DevOps
> familiarity — everything else is a strong match."*

---

## Time Saved

| Task | Manual Process | AI-Assisted |
|---|---|---|
| Reading 3 resumes | 15–20 minutes | 2 minutes |
| Comparing against JD | 10–15 minutes | Instant |
| Writing screening notes | 15 minutes | Included in output |
| Preparing HM summary | 10 minutes | Included in output |
| **Total** | **~50 minutes** | **~5 minutes** |

**Time saved per screening batch: ~45 minutes**

---

## Live Screening Workflow — Edge Copilot + Claude

For live Naukri screening without downloading resumes:

```
Step 1: Open candidate profile in Microsoft Edge
Step 2: Select all visible text (Ctrl+A → Ctrl+C)
Step 3: Open Claude or Edge Copilot sidebar
Step 4: Paste this quick screening prompt:

"Screen this candidate against my JD.
JD: [your JD summary]
Candidate: [pasted profile text]

Give me:
1. Fit Score out of 10
2. Top 3 matching skills
3. Top 2 gaps
4. One screening question
5. Verdict: Shortlist / Conditional / Reject"

Step 5: Get instant verdict → Download only shortlisted profiles
```

**Result:** Only download profiles that already have a screening
verdict. Average 30 seconds per profile vs 3–5 minutes manually.

---

## Screening Prompt Variations

| Situation | Prompt adjustment |
|---|---|
| Partial match candidate | Add "focus on skill gaps and what to clarify" |
| Senior / leadership role | Add "assess career trajectory and leadership signals" |
| Niche technical role | Add "weight technical depth over years of experience" |
| Contract / payroll role | Add "assess flexibility and contract role openness signals" |

---

*Built by Suresh Korumilli — Senior Talent Acquisition Professional*
*Real screening: 3 resumes, AB InBev Scrum Master role*
*Time saved: ~45 minutes per screening batch*
*Part of the Recruiter Copilot project*
