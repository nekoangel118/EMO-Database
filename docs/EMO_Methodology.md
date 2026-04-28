# EMO Database – Methodology

## 1. Data Integration
Describes how EMO integrates data from multiple sources.

### 1.1 Source Acquisition
- Data sources include scientific publications, PDFs, figures, WOD, PBDB, and other curated materials.
- File naming follows a unified convention: `author_year_title`.
- Data entry is managed through Google Sheets, with PDF storage and backup in Zotero and Google Drive.

#### 1.1.1 WOD
- WOD provides a valuable bibliographic record associated with the original description of taxon.  
- Because WOD does not support filtering by geological age, Eocene‑related references cannot be retrieved directly.  
- To identify relevant literature, the “Advanced Search” function was used with targeted title‑restricted keyword combinations such as **“Eocene” AND “Ostracoda”**.

#### 1.1.2 PBDB
1. **Retrieval of Relevant Fossil Occurrences**  
   Query parameters used:
   - Taxon: *Ostracoda*  
   - Time interval: Late Paleocene → Early Oligocene (using overlap rule to capture all Eocene‑intersecting records)  
   - Environment: Marine  

   This ensures inclusion of occurrences with broad or boundary‑crossing age assignments. Retrieved records include coordinates, paleoenvironment, stratigraphy, and lithology.

2. **Extraction of Reference Information Linked to Occurrences**  
   - Each PBDB occurrence links to a literature source via `reference_no`.  
   - All reference numbers were extracted, consolidated, and deduplicated to form a unique bibliography list.

3. **Download of Full Bibliographic Records (RIS Format)**  
   - PBDB’s reference API was used to retrieve complete citation metadata:  
     `https://paleobiodb.org/data1.2/refs/list.ris?id=<ref_id_list>`  
   - The resulting RIS file was imported into EndNote for management and integration with additional sources.

---

### 1.2 Data Extraction
- Manually extract occurrence, taxonomy, and reference information from source publications.

### 1.3 Data Harmonization
- Follow **EMO_Data_Dictionary_and_Data_Entry_Guide.md** for terminology, missing‑value rules, and standardization.

---

## 2. Data Conversion
Describes how EMO data are converted into different output formats.

### 2.1 Machine‑Readable TXT Conversion
**Purpose:** Generate NOAA‑style, human‑readable `.txt` files.  
**Process:**
- Read the three EMO tables.
- Apply formatting and field‑cleaning rules.
- Export outputs to `exports/txt/` using `metadata_generation.py`.
- Automated through GitHub Actions workflow (`main.yml`).

---

### 2.2 PBDB‑Ready Conversion
**Purpose:** Convert EMO data into PBDB submission format.  
**Process:**
- Apply mapping dictionaries to translate EMO fields into PBDB‑standard fields.
- Automatically generate three PBDB‑ready files:
  - `pbdb_occurrence.txt`
  - `pbdb_taxonomy.txt`
  - `pbdb_reference.txt`
- Export outputs to `exports/pbdb/` using `convert_to_pbdb.py`.
- Executed by an independent workflow (`pbdb.yml`).

---

### 2.3 WOD‑Ready Conversion
**Purpose:** Prepare EMO taxonomy for submission to the World Ostracoda Database (WOD).  
**Process:**
- Match taxon names with AphiaID, accepted names, and authorities.
- Format fields according to WOD requirements.
- Export outputs to `exports/wod/`.
- Managed by a separate workflow (`wod.yml`).

---

## 3. Version Control & Automation
- All conversion scripts stored in `scripts/`.
- All automated processes handled by GitHub Actions.
- Each output format has its own workflow.
- All generated files are automatically committed to the repository.

---

## 4. Reproducibility
- All mapping tables, scripts, and workflows are version‑controlled.
- Outputs regenerated consistently through automated workflows.
- All methodology documentation stored in `docs/`.

