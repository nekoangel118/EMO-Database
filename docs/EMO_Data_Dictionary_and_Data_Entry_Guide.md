# EMO Data Dictionary and Data Entry Guide 

## Occurrence_record 

ORID: A unique identifier assigned to each occurrence record in EMO.

Accepted Name: Final taxon name assigned after the taxa in the occurrence record. Currently blank; values will be added once the revised taxonomy list is completed.

Superorder：A superorder is a taxonomic rank above order and below class，following the classification reported in the source publication of the occurrence record. 

Order：An order is a taxonomic rank above suborder and below superorder，following the classification reported in the source publication of the occurrence record.
	
Suborder: A suborder is a taxonomic rank above superfamily and below order，following the classification reported in the source publication of the occurrence record.Blank cells indicate that the original publication did not include classification information for this taxonomic rank.
	
Superfamily: A superfamily is a taxonomic rank above family and below suborder，following the classification reported in the source publication of the occurrence record. Blank cells indicate that the original publication did not include classification information for this taxonomic rank.

Family:	 A family is a taxonomic rank above subfamily and below superfamily，following the classification reported in the source publication of the occurrence record. Blank cells indicate that the original publication did not include classification information for this taxonomic rank.

Subfamily: A subfamily is a taxonomic rank above genus and below superfamily，following the classification reported in the source publication of the occurrence record. Blank cells indicate that the original publication did not include classification information for this taxonomic rank.
	
Tribe: A tribe is a taxonomic rank between family and genus，following the classification reported in the source publication of the occurrence record. 
	
Genus: A genus is a taxonomic rank above genus and below superfamily，following the classification reported in the source publication of the occurrence record.
	
Subgenus: A subfamily is a taxonomic rank above genus and below superfamily，following the classification reported in the source publication of the occurrence record.
	
Taxon name: The scientific name assignment to a taxa, following the systematic palaeontology in the source publication of the occurrence record.

Identifier: The person who first described the species with the corresponding taxon name, following the identifier reported in the source publication of the occurrence record.
	
Synonym: The list of the alternative names of the species, showing their historical usage and relationships to the accepted name, following the identifier reported in the source publication of the occurrence record (hence could be incomplete and inaccurate).
	
Image: The position of the image of the species in the source publication of the occurrence record.
	
Type locality and horizon & Stratigraphical range: Biogeographical information of the species (or one piece of its fossils), including its geographical distribution and temporal range.
	
Description: A morphological description of the taxa, following the source publication of the occurrence record.
.	
Diagnosis: Diagnosis distinguishes the taxa from all morphologically similar taxa, following the source publication of the occurrence record.

Remarks: Additional information related to the taxon, following the source publication of the occurrence record.

Ecology: The ecological information of the taxa (including the preferences on water depth, temperature, salinity and nutrient), following the source publication of the occurrence record.
	
Dimensions(L*W*H): The measured data of the taxa, including the length, width and height of the fossil (unit: mm*mm*mm).NA=lack of information. RV/LV=right/left valve; j=juvenile; a=adult; M=male; F=female; Carapace=a complete fossil with both left and right valves; Holotype=a single specimen designated by the original describer of the form (a species or subspecies only); Paratype= other specimens used in the original description other than the holotype. Value and decimal place number follow the source publication of the occurrence record.

Location: The geographical information of the occurrence record, which is a broader scope than sample sites, following the source publication of the occurrence record. It is shared by all occurrence records from the same source publication. 
	
Sample site: Composite sampling information derived from the source publication, encompassing location of sampling sites, station identifiers, and sample or core codes (of the taxon or a single piece of fossils). The level of detail varies among sources; therefore, this field preserves the original notation to maintain data provenance. It can be different for different occurrence records from the same source publication. 
	
Latitude(N>0): The north–south coordinate(s) of the location expressed in decimal degrees (WGS 84 datum) (unit: °). Positive values indicate north latitude; negative values indicate south latitude. 

Longitude(E>0): The east–west coordinate(s) of the location expressed in decimal degrees (WGS 84 datum) (unit: °). Positive values indicate east longitude; negative values indicate west longitude. 
	
Group: A stratigraphical unit above formation, following the stratigraphy reported in the source publication of the occurrence record. 

Formation: A stratigraphical unit above member and below group, following the stratigraphy reported in the source publication of the occurrence record. 
	
Member: A stratigraphical unit below formation, following the stratigraphy reported in the source publication of the occurrence record. 	

Epoch: Epoch is a geochronologic unit. In EMO, all occurrence records are from the Eocene. 

Epoch subdivision: Indicates age of the occurrence record, the Eocene epoch is subdivided into three time intervals, from earliest to the latest: Early (Lower)/Middle/Late (Upper). 
	
Stage:	Stage is the lowest-ranking chronostratigraphic unit. It indicates the geologic time interval of the occurrence record. In EMO, four stages are included:

Min Age (Ma): The lower limit of the sample age of the occurrence record (numerical) (unit: million years ago (Ma)). 
	
Max Age (Ma): The upper limit of the sample age of the occurrence record (numerical) (unit: million years ago (Ma)). 

Depositional Environment: Specific geographic setting in which sediments accumulate, and the fossil assemblage formed; it is the ancient depositional environment reconstructed from sedimentological, stratigraphic, and palaeoecological evidence. Contexts follow the source publication of the occurrence record. 
	
Lithology: The physical characteristics of the sample, usually are the colour, grain size and composition of the sediments, following the source publication of the occurrence record. 
	
Specimen: The number of the fossil of the taxon in the sample, following the source publication of the occurrence record. 
	
Source File: The File name that contributes to the occurrence record. 	

Remarks: Any supplementary related to the occurrence record.	

## Taxonomy_info 

Taxon name: Taxon names include all species and subspecies-level taxon in the Occurrence_record. In the current version, names originally recorded as “sp.” or “spp.” in the source publications are standardized as “sp.”; Taxa marked as “aff.” or “cf.” are marked and provisionally assigned to the corresponding species; After the review, taxon names may be reassigned so that each (sub)species has a corresponding taxon name.

Type: Indicates the revision status of the taxa within the EMO database, i.e. whether the taxa has been manually reviewed, taxonomically revised, and is ready for submission to World Ostracoda Database (WOD); currently left blank.

ORID: Indicates the occurrence records of the taxon. Each taxon may be associated with one or more ORIDs, depending on the number of occurrence records in which it appears.  The ORID enables cross‑linking between Taxonomy_info and Occurrence_record for data retrieval and provenance tracking.

WOD included: Indicates whether the taxon has been included in the WOD; Y=taxa present in WOD, followed by their status (“accepted” or “unaccepted”) and reason. N = taxa absent from WOD; Na = WOD inclusion checking is not applied here, followed by reasons (“spp.” = this group includes multiple taxon). 

AphiaID_of the accepted name\Accepted name: The currently valid AphiaID and taxon name of the taxa as listed in the World Ostracoda Database (WOD). When WOD does not include an accepted name, the value is recorded as “na” (which is rare though, eg. AphiaID: 598963). If the taxa name exists in the World Ostracoda Database (WOD) but is labeled as unaccepted, the fields AphiaID_of the accepted name and Accepted name record the AphiaID and valid name of the corresponding accepted taxon. All associated taxonomic fields (Order, Family, Genus, Species), as well as Identifier and Description, also follow the accepted taxon as defined by WOD. 
	
Order\Family\Genus\Species: Higher‑level taxonomic ranks extracted directly from WOD. These fields follow the classification adopted by WOD at the time of data compilation. 	

Identifier: The formal taxonomic authority adopted by WOD at the time of data compilation, using a uniform format “author, year”.
	
Description: The Original description text provided in WOD. When WOD does not include an original description, the value is recorded as “na”.
	
Remarks: Any supplementary related to the taxa regarding its systematic taxonomy.				

## Reference_list	

File name: A unique name of the source publication using a uniform naming format “author_year_title”, same as the name of its PDF file.
	
Updated in Zotero: Indicates whether the PDF of the source publication has been collected and added to the EMO backup library in Zotero (which stores all reference PDFs). “Date” records when the PDF was added;	

Updated PDF in Drive: Indicates whether the PDF of the source publication has been collected and added to the EMO backup folder in Google Drive (which stores all PDFs alongside the three main data tables). “Date” records when the PDF was added; “to do” indicates that the PDF has not yet been collected; “na_reason” is used when the PDF cannot be obtained, with the reason specified (e.g., “na_hardcopy only”).

Data input: Indicates whether the PDF of the source publication has been collected and added to the EMO backup folder in Google Drive (which stores all PDFs alongside the three main data tables). “Date” records when the PDF was added; “to do” indicates that the PDF has not yet been collected;	

Region: The geographic region of source publication, ranging from broad areas (e.g., countries, basins, oceanic regions) to highly localized sites (e.g., tunnels, mines, counties, islands, or specific geological units).	

Age: The time range of source publication, using tree subdivisions of Eocene (Early, Middle, and Late).
	
Photo input: Indicates whether the image of the source publication was extracted and updated to EMO photogallery (a planned feature that will collect all EMO images; currently under development). Date indicates when the process was completed; todo=process pending; If the process cannot be performed, the entry is recorded as “na_reason”, where the reason specifies why the process is not applicable.	
	
Backward citation searching: Indicates whether the reference list of the source publication was screened to identify additional works related to Eocene marine ostracods that were not yet included in the EMO Database. This process helps ensure that no relevant literature is omitted. Date indicates when the process was completed; todo=process pending; If the process cannot be performed, the entry is recorded as “na_reason”, where the reason specifies why the process is not applicable.	

OccurenceRecord: This publication includes the occurrence record of taxon. Y=yes; Y_partly=only a part of the taxon has this information; N=no. This is the baseline for a reference to be included in the EMO Database.

SystematicPaleontology: This publication includes systematic paleontology information of taxon. Y=yes; Y_partly=only a part of the taxon has this information; N=no. The systematic descriptions of taxa must include a diagnosis, synonymy, stratigraphic and geographic indications, designation of a type or types, depository information, and specification of illustrations.	

Images: This publication includes SEM images of taxon. Y=yes; Y_handwriting=images are handwriting-style illustration or other kinds of photos; N=no.

BodySize: This publication includes body size information of taxon. Y=yes; Y_selected=only a part of the taxon has this information; N=no.
	
Specimen:This publication includes specimen number information of taxon. Y=yes; Y_selected=only a part of the taxons have this information; N=no.
	
Environment: This publication includes depositional environment information of the sample. na=marine; Shallow=water depth <200 m; Deep= water depth>200 m; Shallow and Deep=included both; the entry is recorded as “environment_reason”, where the reason specifies the supporting evidence (in the original publication). 

DatabaseVersion: The earliest version of the database that includes the source publication.											
Remarks: Any supplementary related to the source publication.	

