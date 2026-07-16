# ============================================================
# Candidate Screening Automation
# Author: Suresh Korumilli
# Description: Automated candidate screening script that reads
#              real recruitment data from an ODS/Excel file,
#              screens every candidate against defined criteria,
#              and exports results with Auto_Screen column.
#
# Results: Screened 236 real candidates in under 10 seconds
#
# Concepts used: pandas, DataFrames, functions, loops,
#                if/elif/else, file I/O, data cleaning
#
# How to run:
#   Option 1 — Google Colab (recommended, no install needed)
#     Upload your ODS/Excel file to Colab session storage
#     Run each cell in order
#
#   Option 2 — Local machine
#     pip install pandas odfpy openpyxl
#     python candidate_screening.py
# ============================================================


# ── STEP 1: INSTALL DEPENDENCIES (run once in Colab) ────────
# Uncomment the line below if running in Google Colab
# !pip install odfpy


# ── STEP 2: IMPORT LIBRARIES ────────────────────────────────

import pandas as pd


# ── STEP 3: LOAD YOUR RECRUITMENT DATA ──────────────────────

# For ODS files (LibreOffice format):
df = pd.read_excel(
    "Master Data - 2026.ods",
    sheet_name="Candidate_Master_Data",
    engine="odf"
)

# For XLSX files (Excel format), use this instead:
# df = pd.read_excel(
#     "Recruitment_Tracker.xlsx",
#     sheet_name="Candidate Tracker"
# )

print(f"✅ Data loaded successfully!")
print(f"   Total candidates: {len(df)}")
print(f"   Columns: {df.columns.tolist()}")


# ── STEP 4: CLEAN EXPERIENCE COLUMN ─────────────────────────
# Experience is stored as text like "4.8 Yrs", "5 Yrs"
# We extract just the number so we can use >= comparisons

df["Exp_Clean"] = (
    df["Total Expereince"]
    .str.extract(r'(\d+\.?\d*)')
    .astype(float)
)

print(f"\n✅ Experience column cleaned.")
print(df[["Candidate Name", "Total Expereince", "Exp_Clean"]].head(5))


# ── STEP 5: DEFINE SCREENING FUNCTION ───────────────────────
# Adjust the criteria below to match your active JD

def screen_candidate(exp):
    """
    Screen a candidate based on years of experience.
    Extend this function to add more criteria:
    - notice_period
    - current_ctc
    - location
    - skills

    Args:
        exp (float): Candidate's years of experience

    Returns:
        str: Screening result — Shortlist / Maybe / Reject
    """
    if exp >= 6:
        return "Shortlist"
    elif exp >= 4:
        return "Maybe"
    else:
        return "Reject"


# ── STEP 6: RUN SCREENING ACROSS ALL CANDIDATES ──────────────

shortlist = 0
maybe     = 0
reject    = 0
skipped   = 0

for index, row in df.iterrows():
    exp = row["Exp_Clean"]

    # Skip rows where experience data is missing
    if pd.isna(exp):
        skipped += 1
        continue

    # Call screening function and write result back to DataFrame
    result = screen_candidate(exp)
    df.loc[index, "Auto_Screen"] = result

    # Update counters
    if result == "Shortlist":
        shortlist += 1
    elif result == "Maybe":
        maybe += 1
    else:
        reject += 1


# ── STEP 7: PRINT SUMMARY REPORT ────────────────────────────

total_screened = shortlist + maybe + reject

print("\n" + "=" * 40)
print("   SCREENING COMPLETE")
print("=" * 40)
print(f"   Total Screened    : {total_screened}")
print(f"   ✅ Shortlist       : {shortlist}")
print(f"   🟡 Maybe           : {maybe}")
print(f"   ❌ Reject          : {reject}")
print(f"   ⚠️  Skipped (no data): {skipped}")
print("=" * 40)

# Show first 10 results
print("\nFirst 10 screening results:")
print("-" * 40)
print(df[["Candidate Name", "Total Expereince", "Auto_Screen"]].head(10).to_string(index=False))


# ── STEP 8: EXPORT RESULTS TO EXCEL ─────────────────────────

output_file = "Screened_Candidates.xlsx"
df.to_excel(output_file, index=False)

print(f"\n✅ Results saved to: {output_file}")
print("   Open the file to see the Auto_Screen column for each candidate.")


# ── HOW TO EXTEND THIS SCRIPT ────────────────────────────────
#
# To add more screening criteria, update the screen_candidate
# function and pass more values from each row:
#
# def screen_candidate(exp, notice, ctc, location):
#     if (exp >= 5 and
#         notice <= 30 and
#         ctc <= 20 and
#         location.lower() == "bengaluru"):
#         return "Shortlist"
#     elif exp >= 5 and notice <= 60:
#         return "Maybe"
#     else:
#         return "Reject"
#
# Then call it inside the loop like this:
#
# result = screen_candidate(
#     row["Exp_Clean"],
#     row["Notice Period"],
#     row["Current CTC"],
#     row["Current Location"]
# )
#
# ============================================================
