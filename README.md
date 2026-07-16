# 🤖 Recruiter Copilot

An AI-assisted recruitment workflow built by a Senior Talent Acquisition
professional with 7+ years in tech hiring. This copilot automates the
most time-consuming parts of the recruitment process — from sourcing to
screening to reporting — using Claude AI, Python, Excel, and Power BI.

---

## The Problem

Recruiters spend the majority of their time on manual, repetitive tasks:

- Writing Boolean search strings from scratch for every role
- Drafting individual outreach messages for each candidate
- Reading and comparing resumes manually against JDs
- Updating trackers and compiling reports for hiring managers

This copilot addresses all four — reducing hours of manual work to
minutes of AI-assisted effort.

---

## The 5-Step Workflow

```
JD / Role Input
      ↓
Step 1 → Boolean Search String Generation
      ↓
Step 2 → Personalized Candidate Outreach
      ↓
Step 3 → Resume Screening & Ranking
      ↓
Step 4 → Pipeline Tracking & KPI Dashboard
      ↓
Step 5 → Automated Candidate Screening (Python)
```

---

## Repository Structure

```
recruiter-copilot/
│
├── 01_Boolean_Search/
│   └── boolean_prompt_template.md
│
├── 02_Outreach_Generator/
│   └── outreach_prompt_template.md
│
├── 03_Resume_Screener/
│   └── resume_screener.md
│
├── 04_KPI_Dashboard/
│   └── dashboard_overview.md
│
└── 05_Screening_Automation/
    └── candidate_screening.py
```

---

## Step 1 — Boolean Search String Generator

📁 `01_Boolean_Search/boolean_prompt_template.md`

### Purpose
Generates optimized Boolean search strings for Naukri, LinkedIn, and
Google X-Ray from a simple role description — in under 30 seconds.
Replaces 15–20 minutes of manual Boolean string writing per role.

### How It Works
1. Open Claude AI
2. Copy the master prompt template from the file
3. Fill in: Role, Experience, Must-have skills, Good-to-have skills,
   Location
4. Paste into Claude → get 3 ready-to-use strings instantly
5. Copy the Naukri string → paste into Naukri keyword search

### How to Modify
- **Add more skills** — extend the OR group inside any AND condition
- **Widen results** — remove one AND condition block entirely
- **Tighten results** — add one more AND condition with a specific skill
- **Change platform** — the file includes platform-specific instructions
  for Naukri, LinkedIn, and Google X-Ray separately
- **Add new roles** — save the generated string in your Boolean Library
  with the profile count for future reuse

### What's in the File
- Master prompt template with fill-in-the-blank format
- 4 real tested Boolean strings across different tech roles
- Before and after versions showing how to tune strings
- Profile count results from Naukri testing
- Golden rules for Boolean search logic

---

## Step 2 — Personalized Outreach Generator

📁 `02_Outreach_Generator/outreach_prompt_template.md`

### Purpose
Generates personalized candidate outreach messages across LinkedIn
InMail, Email, and WhatsApp — tailored to each candidate's specific
profile, company, and skills. Replaces generic copy-paste messages
that candidates ignore.

### How It Works
1. Open the candidate's profile on Naukri or LinkedIn
2. Copy their headline, current company, and key skills
3. Open Claude AI and paste the master prompt template
4. Fill in: Candidate snapshot, JD summary, Recruiter name,
   Tone preference
5. Claude generates 3 versions — Email, LinkedIn InMail, WhatsApp
6. Review, personalise further if needed, send

### How to Modify
- **Change tone** — swap between Professional, Exploratory, Direct,
  or Conversational based on seniority and context
- **Partial match candidates** — add instruction: "Ask one specific
  question about their gap skill rather than pitching the full role"
- **Contract roles** — add payroll and conversion details to the
  prompt context so Claude includes them naturally
- **Bulk outreach** — run the same prompt for multiple candidates by
  swapping the candidate snapshot each time
- **Different platforms** — specify only Email or only WhatsApp if
  you don't need all three formats

### What's in the File
- Master prompt template with tone and platform options
- Platform-specific character limits and guidelines
- Rules that consistently improve response rates
- Tone variation guide — when to use which approach

---

## Step 3 — Resume Screener & Ranker

📁 `03_Resume_Screener/resume_screener.md`

### Purpose
Evaluates multiple resumes against a JD simultaneously — producing
fit scores, strengths, gaps, recruiter recommendations, and a final
ranked shortlist. Replaces manual resume reading and comparison which
takes 3–5 minutes per profile.

### How It Works
1. Copy the screening prompt template from the file
2. Paste your JD at the top
3. Add candidate profiles — paste each resume or profile snapshot
   as Candidate 1, Candidate 2 etc.
4. Send to Claude → receive structured screening report for each
5. Use the final ranking and HM pitch directly in your hiring
   manager update

### How to Modify
- **Change screening priorities** — add or remove from the
  SCREENING PRIORITIES section: Must-have skills / Experience /
  Domain fit / Stability / Location / Career progression
- **More candidates** — add Candidate 3, 4, 5 in the same format.
  Works well for up to 5 candidates per run
- **Stricter or looser criteria** — specify in the prompt:
  "Weight technical depth over years of experience" or
  "Flag any candidate with more than 2 job changes in 3 years"
- **Different output format** — ask Claude to output as a table
  for easy copy-paste into an email to the hiring manager
- **Live Naukri screening** — use the Edge Copilot workflow:
  copy profile text from Naukri, paste into Claude with JD,
  get instant verdict before downloading the resume

### What's in the File
- Master screening prompt with all parameters
- Fit score criteria and recommendation categories
- Edge Copilot live screening workflow for Naukri
- Quick screening prompt for 30-second per-profile verdicts
- Prompt variations for different role types

---

## Step 4 — KPI Dashboard & Pipeline Tracker

📁 `04_KPI_Dashboard/dashboard_overview.md`

### Purpose
A structured Excel pipeline tracker and Power BI dashboard that
tracks every candidate from sourced to joined — across multiple
clients, recruiters, and requisitions. Replaces messy ad-hoc
spreadsheets with a live, auto-updating system.

### How It Works

**Excel Tracker (data entry):**
1. Add new recruiters and clients in the Settings sheet
2. Add each new requisition in Req Master with Req ID and status
3. Add each candidate in Candidate Tracker using the same Req ID
4. Use dropdowns for Stage, Source, Screen Status, Offer Status
5. Req Ageing calculates automatically and stops when req is closed

**Power BI Dashboard (reporting):**
1. Open Power BI Desktop
2. Connect to the Excel tracker file via Get Data → Excel
3. Refresh data after each update session
4. Use slicers to filter by Recruiter, Client, or Quarter
5. Share the dashboard link with hiring managers

### How to Modify

**Excel Tracker:**
- **Add a new recruiter** — type their name in Settings sheet →
  appears in all dropdowns automatically
- **Add a new client** — same process in Settings sheet
- **Add new dropdown values** — update the Settings sheet or
  the Data Validation formula for that column
- **Add new KPI** — add a COUNTIFS formula in the KPI Dashboard
  sheet referencing the relevant column

**Power BI Dashboard:**
- **Add a new visual** — select visual type, drag fields from
  the Data panel, apply filters as needed
- **Add a new slicer** — drag any column to a Slicer visual,
  format as Dropdown for clean appearance
- **Add a new page** — click + at the bottom, build page for
  a specific audience (e.g. Recruiter Performance page)
- **Change date grouping** — click date field → change from
  Day to Month or Quarter in the field settings

### What's in the File
- Full description of all 3 Excel sheets and their purpose
- All KPI metrics tracked with formulas explained
- Power BI pages and slicers documented
- Key design decisions and why each choice was made

---

## Step 5 — Screening Automation (Python + Pandas)

📁 `05_Screening_Automation/candidate_screening.py`

### Purpose
A Python script that reads a real recruitment tracker file, screens
every candidate automatically against defined criteria, writes the
result into an Auto_Screen column, and exports the screened file —
all in under 10 seconds regardless of how many candidates are in
the file.

### How It Works
1. Upload your ODS or Excel tracker file to Google Colab
2. Run the script cell by cell
3. The script cleans the experience column (removes "Yrs" text)
4. Loops through every candidate row automatically
5. Calls the screening function for each candidate
6. Writes Shortlist / Maybe / Reject into Auto_Screen column
7. Exports a new Excel file with all results
8. Prints a summary report with counts

### How to Modify

**Change screening criteria:**
```python
def screen_candidate(exp):
    if exp >= 6:        # change this threshold
        return "Shortlist"
    elif exp >= 4:      # change this threshold
        return "Maybe"
    else:
        return "Reject"
```

**Add more conditions (notice period, CTC, location):**
```python
def screen_candidate(exp, notice, ctc):
    if exp >= 5 and notice <= 30 and ctc <= 20:
        return "Shortlist"
    elif exp >= 5 and notice <= 60:
        return "Maybe"
    else:
        return "Reject"

# Then update the loop call:
result = screen_candidate(
    row["Exp_Clean"],
    row["Notice Period"],
    row["Current CTC"]
)
```

**Change the column name for experience:**
```python
# Replace "Total Expereince" with your actual column header
df["Exp_Clean"] = df["Your Column Name"].str.extract(...)
```

**Change output file name:**
```python
df.to_excel("Your_Output_Name.xlsx", index=False)
```

**Add more screening buckets:**
```python
def screen_candidate(exp):
    if exp >= 8:
        return "Senior — Priority"
    elif exp >= 5:
        return "Shortlist"
    elif exp >= 3:
        return "Junior — Consider"
    else:
        return "Reject"
```

### Requirements
```
Python 3.x
pandas
odfpy     (for ODS files)
openpyxl  (for XLSX output)

Install: pip install pandas odfpy openpyxl
```

### Recommended Environment
Google Colab — free, browser-based, no installation needed.
pandas and openpyxl are pre-installed. Only odfpy needs installing.

---

## Results

| Step | Time Before | Time After | Improvement |
|---|---|---|---|
| Boolean string per role | 15–20 mins | 30 seconds | **97% faster** |
| Outreach per candidate | 5–10 mins | 1 minute | **85% faster** |
| Screening 3 resumes | 50 mins | 5 mins | **90% faster** |
| Pipeline report for HM | 1–2 hours | Instant | **Real-time** |
| Screening 236 candidates | 3–4 hours | 10 seconds | **99% faster** |

---

## Tools Used

| Tool | Purpose |
|---|---|
| Claude AI | Boolean generation, outreach, resume screening |
| Python + Pandas | Automated candidate screening at scale |
| Microsoft Excel | Pipeline tracker, formula-based KPI dashboard |
| Power BI Desktop | Interactive visual dashboard with slicers |
| Google Colab | Running Python scripts without local installation |
| Microsoft Edge Copilot | Live Naukri profile screening without downloading |
| Power Automate | Workflow automation for outreach triggers |

---

## About the Author

**Suresh Korumilli** — Senior Talent Acquisition Professional with
7+ years of experience in full-cycle tech recruitment across GCC,
product companies, MNCs, and startups. Expertise in AI/ML, RPA,
GenAI, Cloud, Data, and Full-Stack hiring.

This copilot was built as part of a self-directed upskilling journey
combining recruitment domain knowledge with Python, Power BI, and
AI-assisted tooling.

🔗 [LinkedIn](https://www.linkedin.com/in/sureshvenkataramana/)
💻 [GitHub](https://github.com/SuresH-Rec)

---

*Built with Claude AI · Python · Excel · Power BI*
*Real data · Real results · Real recruitment*
