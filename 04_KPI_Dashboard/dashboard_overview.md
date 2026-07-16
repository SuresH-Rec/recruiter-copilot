# 📊 KPI Dashboard & Pipeline Tracker

A fully automated recruitment KPI dashboard and pipeline tracker built
using Microsoft Excel and Power BI — designed to track end-to-end
recruitment metrics across multiple clients, recruiters, and requisitions.

---

## The Problem

Most recruiters track candidates in messy Excel sheets with no structure,
no formulas, and no visibility into pipeline health. Hiring managers ask
for updates and recruiters spend hours manually compiling numbers.

**With a structured tracker + live dashboard:**
- Pipeline status visible in one click
- KPIs update automatically as data is entered
- Hiring manager reports generated in seconds not hours

---

## What Was Built

### Part 1 — Excel Pipeline Tracker

A structured multi-sheet Excel workbook with:

**Sheet 1 — Settings**
- Single source of truth for all dropdown values
- Recruiter names, client names, locations managed here
- All dropdowns across the tracker pull from this sheet automatically
- Add a new recruiter once → appears everywhere instantly

**Sheet 2 — Req Master**
- One row per open requirement
- Tracks: Req ID, Client, Position, Primary Skill, Recruiter,
  No. of Positions, Req Status, Target Closure Date
- Req Ageing auto-calculates from Req Received Date
- Ageing stops counting when Req Status = Closed / Hold / Cancelled

**Sheet 3 — Candidate Tracker**
- One row per candidate
- 35 columns covering the full candidate journey:
  Sourced → Screened → L1 Interview → Final Interview →
  Offered → Offer Accepted → Joined
- Color-coded dropdowns for Stage, Source, Screen Status,
  Interview Status, Offer Status, Joined Status
- Req Ageing auto-pulled from Req Master via Req ID (VLOOKUP)
- Conditional formatting — green for select/join, red for reject,
  amber for in-progress

**Formulas Used:**
```
VLOOKUP   — pulls Req Ageing from Req Master into Candidate Tracker
COUNTIFS  — counts candidates matching multiple conditions
IF/IFERROR — handles empty cells and division by zero gracefully
Data Validation — dropdown lists ensuring clean, consistent data entry
```

---

### Part 2 — KPI Dashboard (Excel)

Auto-updating dashboard built on the same Excel file with:

**Pipeline Overview — 10 KPI boxes**
- Total Reqs, Active Reqs, On Hold, Cancelled, Closed
- Total Candidates Sourced
- Screened-Select count
- Final Selects count
- Offers Made, Offer Accepted, Joined

**Key Ratios & Conversion**
- Screen-to-Select %
- L1 Select Rate %
- Final Select Rate %
- Select → Offer %
- Offer Acceptance %
- Offer Decline %
- Offer → Join %
- Overall Closure %

**Source of Hire Table**
- Naukri, LinkedIn, Referral, Vendor, Others
- Count of candidates and selects per source

**Client-wise Pipeline**
- Per client: Total Reqs, Candidates, Selects, Offered, Joined

**Recruiter Performance Scorecard**
- Per recruiter: Sourced, Screened-Select, Final Selects,
  Offered, Joined, Closure %, Offer Acceptance %, Avg Ageing

**Quarterly Trend Table**
- Q1 (Jan–Mar), Q2 (Apr–Jun), Q3 (Jul–Sep), Q4 (Oct–Dec)
- QoQ improvement % calculated automatically

**Req-wise Status Summary**
- Live per-req view pulled from Req Master
- Status color coded: Active (blue), Closed (green),
  Hold (amber), Cancelled (red)

---

### Part 3 — Power BI Dashboard

Connected the Excel tracker to Power BI Desktop for interactive
visual reporting:

**Page 1 — Executive Summary**
- 5 KPI cards: Total Candidates, Final Selects, Offers Made,
  Offer Accepted, Joined
- Clustered bar chart: Client-wise candidate pipeline
  (Select vs Reject breakdown per client)
- Donut chart: Source of Hire mix
- Req Status table: Live open requirements with ageing

**Page 2 — Candidate Master Data**
- Connected to historical data from old recruitment tracker
- Recruiter slicer, Client slicer, Source slicer
- All visuals filter dynamically when slicers are changed

**Slicers Added:**
- Filter by Recruiter
- Filter by Client
- Filter by Source

**Clicking any slicer value instantly filters every visual on the page.**

---

## Real Data — What the Dashboard Tracked

| Metric | Value |
|---|---|
| Total Candidates in tracker | 208 |
| Clients tracked | 9 (AB InBev, Diageo, HCCB, PGS, Tesco, Olam/Mindsprint, Internal, Honey Well, Tata Exlsi) |
| Recruiters tracked | 2 (Suresh K, Samyaka L) |
| Req IDs tracked | 14+ active and closed reqs |
| Sources tracked | Naukri, LinkedIn, Referral, Vendor, Indeed |

---

## Key Design Decisions

**Why separate Req Master and Candidate Tracker sheets?**
One req can have many candidates. Keeping them separate and linking
via Req ID (like a database relationship) means req-level data
(ageing, status) only needs updating in one place.

**Why a Settings sheet for dropdowns?**
Hardcoded dropdowns break when you need to add a new recruiter or
client. A Settings sheet means one update propagates everywhere —
no hunting through sheets to update every dropdown manually.

**Why Power BI in addition to Excel dashboard?**
Excel dashboards require Ctrl+Alt+F9 to refresh and can only be
viewed by one person at a time. Power BI dashboards update
instantly when slicers change and can be shared via a link —
anyone can view without needing Excel.

---

## Tools Used

| Tool | Purpose |
|---|---|
| Microsoft Excel | Data entry, pipeline tracker, formula-based dashboard |
| Power BI Desktop | Interactive visual dashboard with slicers |
| VLOOKUP | Linking Candidate Tracker to Req Master |
| COUNTIFS | Calculating all KPI metrics dynamically |
| Data Validation | Enforcing consistent dropdown values |
| Conditional Formatting | Color-coding pipeline stages |

---

## Files in This Folder

| File | Description |
|---|---|
| `dashboard_overview.md` | This documentation file |

> **Note:** The actual Excel and Power BI files contain real candidate
> data and are kept private. This documentation describes the structure,
> logic, and metrics tracked.

---

*Built by Suresh Korumilli — Senior Talent Acquisition Professional*
*208 real candidates tracked across 9 clients and 14+ requisitions*
*Part of the Recruiter Copilot project*
