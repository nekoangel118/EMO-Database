"""
generate_metadata.py
------------------------------------------------------------
Purpose:
    Automatically generate a NOAA-style metadata .txt file
    (similar to cronin2021-aod2020.txt) from EMO CSV files.

Usage:
    python generate_metadata.py

Output:
    metadata/emo2026-database.txt
------------------------------------------------------------
"""

import pandas as pd
from datetime import date

# === Step 1: Load your CSVs ===
taxonomy = pd.read_csv("data/EMO_Database - Taxonomy_info.csv")
reference = pd.read_csv("data/EMO_Database - reference_list.csv")

# === Step 2: Extract key metadata ===
today = date.today().isoformat()
num_taxa = taxonomy["Taxon name"].nunique()
num_refs = len(reference)
regions = ", ".join(sorted(reference["Region"].dropna().unique()[:8])) + "..."

# === Step 3: Build metadata header ===
header = f"""# Eocene Marine Ostracod Database (EMO)
# ------------------------------------------------------------
# World Data Service for Paleoclimatology, Boulder
# and NOAA Paleoclimatology Program
# Template Version 3.0
# Encoding: UTF-8
# NOTE: Please cite original publication, online resource and date accessed when using this data.
# ------------------------------------------------------------
# Online_Resource: https://github.com/nekoangel118/EMO-Database
# Description: EMO Database (tab-delimited data)
# Data_Type: Paleoceanography
# Dataset_DOI: [to be assigned]
# Parameter_Keywords: Taxonomy, Occurrence, Environment
# ------------------------------------------------------------
# Contribution_Date: {today}
# File_Last_Modified_Date: {today}
# ------------------------------------------------------------
# Title
# Study_Name: Eocene Marine Ostracod Database (EMO)
# ------------------------------------------------------------
# Investigators: Zhang, J.
# ------------------------------------------------------------
# Description
# The EMO database compiles Eocene marine ostracod taxonomy, occurrence records,
# and reference metadata from published literature spanning Early to Late Eocene localities worldwide.
# ------------------------------------------------------------
# Summary
# Total taxa: {num_taxa}
# Total references: {num_refs}
# Geographic coverage: {regions}
# ------------------------------------------------------------
# Data_Table
# (tab-delimited columns from EMO CSVs)
"""

# === Step 4: Combine CSVs into one table (optional) ===
combined = reference[["File name", "Region", "Age", "Environment"]].copy()
combined.columns = ["Reference", "Region", "Age", "Environment"]

# === Step 5: Write output file ===
output_path = "metadata/emo2026-database.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(header)
    combined.to_csv(f, sep="\t", index=False)

print(f"✅ Metadata file generated: {output_path}")

