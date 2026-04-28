# EMO to PBDB data conversion script
# Author: Jingwen Zhang
# Purpose: Convert EMO data tables into PBDB-ready format for automated submission.

import pandas as pd
from pathlib import Path

# === Define paths ===
data_dir = Path("data")
output_dir = Path("exports/pbdb")
output_dir.mkdir(parents=True, exist_ok=True)

# === Load EMO data ===
occurrence = pd.read_csv(data_dir / "EMO_Database - occurrence_record.csv")
taxonomy = pd.read_csv(data_dir / "EMO_Database - taxonomy_info.csv")
reference = pd.read_csv(data_dir / "EMO_Database - reference_list.csv")

# === Mapping dictionaries ===
pbdb_occurrence_mapping = {
    "ORID": "occurrence_no",
    "Accepted Name": "taxon_name",
    "Taxon name": "identified_name",
    "Identifier": "author_name",
    "Synonym": "synonym_name",
    "Ecology": "environment",
    "Latitude(N>0)": "lat",
    "Longitude(E>0)": "lng",
    "Formation": "formation",
    "Member": "member",
    "Epoch": "early_interval",
    "Epoch subdivision": "interval_name",
    "Stage": "stage_name",
    "Min Age (Ma)": "max_ma",
    "Max Age (Ma)": "min_ma",
    "Depositional Environment": "environment",
    "Lithology": "lithology",
    "Specimen": "abundance",
    "Source File": "reference_no",
    "Remarks": "comments",
}

pbdb_taxonomy_mapping = {
    "Taxon name": "taxon_name",
    "Type": "status",
    "ORID": "occurrence_no",
    "WOD included": "accepted_status",
    "AphiaID_of the accepted name": "external_id",
    "Accepted name": "accepted_name",
    "Order": "order_name",
    "Family": "family_name",
    "Genus": "genus_name",
    "Species": "species_name",
    "Identifier": "authority",
    "Description": "original_description",
    "Remarks": "comments",
}

pbdb_reference_mapping = {
    "File name": "title",
    "Updated in Zotero": "data_source",
    "Updated PDF in Drive": "data_source",
    "Data input": "data_source",
    "Region": "geographic_extent",
    "Age": "interval_name",
    "Photo input": "illustrations",
    "Backward citation searching": "comments",
    "OccurenceRecord": "contains_occurrences",
    "SystematicPaleontology": "contains_taxa",
    "Images": "illustrations",
    "BodySize": "contains_measurements",
    "Specimen": "contains_specimens",
    "Environment": "environment",
    "DatabaseVersion": "database_version",
    "Remarks": "comments",
}

# === Function to rename columns ===
def map_columns(df, mapping):
    return df.rename(columns={k: v for k, v in mapping.items() if k in df.columns})

# === Apply mappings ===
occurrence_pbdb = map_columns(occurrence, pbdb_occurrence_mapping)
taxonomy_pbdb = map_columns(taxonomy, pbdb_taxonomy_mapping)
reference_pbdb = map_columns(reference, pbdb_reference_mapping)

# === Export to PBDB-ready .txt files ===
occurrence_pbdb.to_csv(output_dir / "pbdb_occurrence.txt", sep="\t", index=False)
taxonomy_pbdb.to_csv(output_dir / "pbdb_taxonomy.txt", sep="\t", index=False)
reference_pbdb.to_csv(output_dir / "pbdb_reference.txt", sep="\t", index=False)

print("✅ PBDB-ready files generated in exports/pbdb/")
