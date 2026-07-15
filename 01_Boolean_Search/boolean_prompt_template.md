# 📚 Boolean String Library

A collection of real Boolean search strings built and tested on Naukri
for active tech hiring roles. Each string includes the original version,
a modified version based on results, and the profile count from testing.

---

## How to Use

1. Copy the string for your role
2. Paste directly into Naukri / LinkedIn keyword search
3. If results are under 30 — widen the string (remove conditions)
4. If results are over 500 — tighten the string (add more AND conditions)

---

## Master Prompt Template

Use this prompt with Claude AI to generate Boolean strings for any role:

```
You are an expert IT recruiter. Generate Boolean search strings 
for sourcing candidates on Naukri, LinkedIn, and Google X-Ray.

Role: [JOB TITLE]
Experience: [X-Y YEARS]
Must-have skills: [SKILL 1, SKILL 2, SKILL 3]
Good-to-have skills: [SKILL A, SKILL B]
Location: [CITY]

Generate:
1. Naukri / Indeed Boolean string
2. LinkedIn Boolean string
3. Google X-Ray string (to search Naukri profiles via Google)

After each string explain in 1-2 sentences what it does.
```

---

## Boolean String Library — Real Examples

---

### 1. Senior Data Engineer

**Platform:** Naukri

**Original String** *(20 profiles)*
```
("Senior Data Engineer" OR "Lead Data Engineer" OR "Principal Data Engineer" 
OR "Data Engineering Lead" OR "Analytics Engineer") 
AND (Python) AND (SQL) AND (Spark OR PySpark) 
AND (Azure OR Databricks OR "Azure Data Factory" OR ADF) 
AND ("Data Ingestion" OR ETL OR ELT OR "Data Pipeline*" OR "Data Transformation") 
AND (AI OR GenAI OR LLM OR "Generative AI" OR "Machine Learning") 
AND (POC OR Prototype OR MVP OR "Proof of Concept")
```

**Modified String** *(147 profiles)*
```
("Data Engineer" OR "Senior Data Engineer" OR "Lead Data Engineer" 
OR "Principal Data Engineer") 
AND (SQL OR PL/SQL) AND (Python) 
AND (Spark OR PySpark) 
AND (Azure OR "Azure Data Factory" OR ADF OR Databricks) 
AND ("Data Pipeline*" OR ETL OR ELT OR "Data Ingestion" OR "Data Transformation") 
AND (AI OR GenAI OR "Generative AI" OR LLM OR "Machine Learning")
```

**What changed:** Removed overly specific filters (POC, MVP, GenAI requirement)
and broadened the title group. Result jumped from 20 → 147 profiles.

---

### 2. Data Engineer / Backend DB Developer (PostgreSQL + MDM)

**Platform:** Naukri

**Original String** *(12 profiles)*
```
(PostgreSQL OR "Postgres SQL") 
AND ("Data Engineer" OR "Database Developer" OR "Backend Developer" OR "DB Developer") 
AND (MDM OR "Master Data Management" OR "Data Governance") 
AND ("Data Modeling" OR "Data Modelling") 
AND (CDC OR "Change Data Capture" OR "Event Driven") 
AND (Triggers OR "Stored Procedures") 
AND (Indexing OR Partitioning) 
AND (Redis OR Kubernetes)
```

**Modified String** *(108 profiles)*
```
(PostgreSQL OR Postgres) 
AND ("Data Engineer" OR "Database Developer" OR "Backend Developer") 
AND (MDM OR "Master Data Management" OR "Data Governance") 
AND ("Data Modeling" OR "Data Warehouse") 
AND (CDC OR "Event Driven") 
AND (Triggers OR Procedures OR Indexing OR Partitioning)
```

**What changed:** Simplified aggressively — dropped Redis, Kubernetes,
and redundant terms. Result jumped from 12 → 108 profiles.

---

### 3. Python Backend Developer

**Platform:** Naukri

**Original String** *(10 profiles)*
```
(Python) AND (FastAPI OR Flask) 
AND ("Backend Developer" OR "Backend Engineer" OR "Python Developer" 
OR "Software Engineer") 
AND (Pandas OR "Data Processing") 
AND (Validation OR "Data Validation" OR "Rule Engine") 
AND (SFTP OR FTP) 
AND (Kafka OR RabbitMQ OR Messaging OR "Event Driven") 
AND (PostgreSQL OR Redis)
```

**Modified String** *(31 profiles — recommended)*
```
(Python) 
AND ("Backend Developer" OR "Python Developer" OR "Backend Engineer") 
AND (FastAPI OR Flask OR Django) 
AND (Pandas OR ETL OR Ingestion) 
AND (Validation OR Parsing) 
AND (SFTP OR FTP)
```

**What changed:** Dropped Kafka, RabbitMQ, Redis to widen the pool.
113,736 profiles when too broad — 31 profiles is the sweet spot.

---

### 4. RPA Automation Anywhere Developer

**Platform:** Naukri

**Original String** *(68 profiles)*
```
("Automation Anywhere" OR A360) 
AND (SAP) AND (API OR REST OR SOAP) 
AND ("SQL Server" OR SQL OR Database) 
AND ("Web Automation" OR Selenium OR Browser) 
AND (Python) 
AND ("RPA Developer" OR "Automation Developer")
```

**Modified String** *(198 profiles — recommended)*
```
("Automation Anywhere" OR A360) 
AND (SAP OR ERP) 
AND (API OR REST) 
AND (SQL OR Database) 
AND (Python OR Scripting) 
AND ("RPA" OR "Automation Developer" OR "RPA Developer")
```

**What changed:** Removed Selenium and browser automation filters,
broadened SAP to SAP OR ERP. Result jumped from 68 → 198 profiles.

---

## Key Lessons Learned

| Situation | What to do |
|---|---|
| Under 30 results | Remove one AND condition or broaden OR options |
| Over 500 results | Add one more AND condition with a specific skill |
| Niche roles | Start broad on titles, use skills as the filter |
| Common roles | Start specific on titles, keep skills broad |
| Always | Test both Naukri and LinkedIn — results differ |

---

## Golden Rule of Boolean Search

> Too many AND conditions = too few results.
> Too few AND conditions = too many irrelevant results.
> The sweet spot is **3-4 strong AND filters** with **2-3 OR alternatives** inside each.

---

*Built and tested by Suresh Korumilli — Senior Talent Acquisition Professional*
*Part of the Recruiter Copilot project*
