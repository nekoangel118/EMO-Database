"""
Generate three metadata files from EMO CSVs:
- emo2026-reference-list.txt
- emo2026-occurrence-record.txt
- emo2026-taxonomy-list.txt
"""

import pandas as pd
from datetime import date

# === Load CSVs ===
taxonomy = pd.read_csv("data/EMO_Database - Taxonomy_info.csv")
occ = pd.read_csv("data/EMO_Database - occurrence_record.csv")
ref = pd.read_csv("data/EMO_Database - reference_list.csv")

today = date.today().isoformat()

# === Professional non-NOAA metadata header ===
def build_header(description):
    return f"""# EMO Database Metadata
# Maintainer: Jingwen Zhang
# Repository: https://github.com/nekoangel118/EMO-Database
# License: MIT
# Metadata Version: 2026.1
# Encoding: UTF-8
# Description:
#   {description}
# ----------------------------------------------------------------------

"""

# === Output 1: Reference List ===
ref_header = build_header("Reference list extracted from EMO reference_list.csv.")
ref_output = "metadata/emo2026-reference-list.txt"

with open(ref_output, "w", encoding="utf-8") as f:
    f.write(ref_header)
    ref.to_csv(f, sep="\t", index=False)

print(f"Generated: {ref_output}")

# === Output 2: Occurrence Record ===
occ_header = build_header("Occurrence records extracted from EMO occurrence_record.csv.")
occ_output = "metadata/emo2026-occurrence-record.txt"

with open(occ_output, "w", encoding="utf-8") as f:
    f.write(occ_header)
    occ.to_csv(f, sep="\t", index=False)

print(f"Generated: {occ_output}")

# === Output 3: Taxonomy List ===
tax_header = build_header("Taxonomy information extracted from EMO taxonomy_info.csv.")
tax_output = "metadata/emo2026-taxonomy-list.txt"

with open(tax_output, "w", encoding="utf-8") as f:
    f.write(tax_header)
    taxonomy.to_csv(f, sep="\t", index=False)

print(f"Generated: {tax_output}")


