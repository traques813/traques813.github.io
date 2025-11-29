
import pandas as pd
from fuzzywuzzy import process

# ---------------------------
# Load raw data + headers
# ---------------------------
mn = pd.read_csv("mn.csv")
headers = pd.read_csv("mn_headers.csv")

# ---------------------------
# Basic checks
# ---------------------------
print("Rows:", len(mn))
print("Columns:", len(mn.columns))

# Remove index column if present
if "Unnamed: 0" in mn.columns:
    mn = mn.drop(columns=["Unnamed: 0"])

# ---------------------------
# Step 1 — Build header map
# ---------------------------
raw_cols = list(mn.columns)
header_map = dict(zip(headers["Name"], headers["Label"]))

matched = []
unmatched = []

for c in raw_cols:
    if c in header_map:
        matched.append(c)
    else:
        unmatched.append(c)

print("Matched headers:", len(matched))
print("Unmatched headers:", len(unmatched))

# ---------------------------
# Step 2 — Rename headers where possible
# ---------------------------
new_names = []
for c in raw_cols:
    if c in header_map:
        new_names.append(header_map[c])
    else:
        new_names.append(c)

mn.columns = new_names

# ---------------------------
# Step 3 — Light cleaning
# ---------------------------
mn = mn.replace(["NA", "N/A", " ", "NaN"], pd.NA)

# Remove full-empty columns
mn = mn.dropna(axis=1, how="all")

# Remove duplicate rows
duplicates = mn.duplicated().sum()
mn = mn.drop_duplicates()

print("Duplicate rows removed:", duplicates)

# ---------------------------
# Step 4 — NA and type summaries
# ---------------------------
na_summary = mn.isna().sum()
type_summary = mn.dtypes

print("Missing values summary:")
print(na_summary.head())

print("Data type summary:")
print(type_summary.value_counts())

# ---------------------------
# Step 5 — Fuzzy matching (string similarity)
# Demonstrates matching inconsistent or unknown labels
# ---------------------------
# Only run fuzzy matching on a small sample to keep it simple
sample_unmatched = unmatched[:5]

fuzzy_matches = []
for raw in sample_unmatched:
    match = process.extractOne(raw, list(headers["Name"]))
    fuzzy_matches.append({"raw": raw, "closest_match": match[0], "score": match[1]})

fuzzy_df = pd.DataFrame(fuzzy_matches)
fuzzy_df.to_csv("fuzzy_matches.csv", index=False)

# ---------------------------
# Step 6 — Save outputs
# ---------------------------
mn.to_csv("clean_mn.csv", index=False)

pd.DataFrame({"raw": matched, "label": [header_map[c] for c in matched]}).to_csv(
    "matched_headers.csv", index=False
)

pd.DataFrame({"raw": unmatched}).to_csv("unmatched_headers.csv", index=False)

print("Cleaning complete. Files saved:")
print(" - clean_mn.csv")
print(" - matched_headers.csv")
print(" - unmatched_headers.csv")
print(" - fuzzy_matches.csv")