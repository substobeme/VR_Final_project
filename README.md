# VR Final Project

## Table of Contents

- [Project Overview](#project-overview)  
- [Components and Evaluation](#components-and-evaluation)  
- [Data Curation](#data-curation)  
  - [Dataset Description](#dataset-description)  
  - [Data Filtering Process](#data-filtering-process)  
  - [Data Cleaning and Standardization](#data-cleaning-and-standardization)  
  - [Category Analysis](#category-analysis)  
  - [Product Type Analysis](#product-type-analysis)  
- [Baseline Evaluation](#baseline-evaluation)  
 

---

## Project Overview

This project focuses on working with the **Amazon Berkeley Objects (ABO) Dataset** to implement machine learning models for visual recognition tasks. The project involves several key components including:

- Data curation  
- Baseline model evaluation  
- Fine-tuning using **LoRA (Low-Rank Adaptation)**  
- Evaluation metrics  
- Inference scripting  
- Performance testing on hidden datasets  

---



## Data Curation

### Dataset Description

The **Amazon Berkeley Objects (ABO) Dataset** includes:

- **147,702** product listings with multilingual metadata  
- **398,212** unique catalog images  
- Used the small variant (**3GB**) with:
  - Metadata in CSV format  
  - Images resized to 256×256 resolution  

---

### Data Filtering Process

#### Language Filtering:

- Filtered entries based on `'language_tag'` starting with `'en'`
- Found multiple English variants: `en_US`, `en_GB`, `en_CA`, `en_AU`, `en_IN`, `en_SG`, `en_AE`
- Result: **118,588** English-language entries retained

#### Metadata Structure Analysis:

- Inspected structure of JSON metadata files  
- Focused on key fields and `'node'` fields (hierarchical categories)

#### Node-Based Filtering:

- Further filtered for entries containing valid `node` information  
- Resulted in **112,600** entries  
- Ensured proper categorization for all retained products

---

### Data Cleaning and Standardization

#### Language Standardization:

- Removed all non-English content  
- Stripped language tags after filtering  

#### Field Reduction:

- Removed unnecessary fields including:
  - Other image IDs, item IDs, model numbers, marketplace identifiers  
  - Domain names, 3D model IDs, spin IDs, node IDs  
- Resulted in a simplified, reduced-size dataset

#### Record Validation:

- Ensured:
  - All records have valid `node_name`  
  - Non-null `main_image_id`  
- Final curated dataset: **112,119** complete records  

---

## Category Analysis

### Hierarchical Category Extraction:

- Split `node_name` into **category levels 1 to 6**  
- Created a tree-based product hierarchy  

### Category Distribution:

- Frequency analysis of top-level categories  
- Kept only those with more than **100 entries**  
- Top categories:
  - Categories  
  - Homeware & Furniture  
  - Home & Garden  
  - Products  
  - Departments  

---

## Product Type Analysis

### Product Type Distribution:

- Extracted primary product types  
- Found **496 unique product types**  
- Top product types:
  - `CELLULAR_PHONE_CASE` – 64,705 entries  
  - `SHOES` – 9,070 entries  
  - `GROCERY` – 4,814 entries  
  - `HOME` – 2,114 entries  
  - `CHAIR` – 1,611 entries  

### Data Balance Analysis:

- Found **CELLULAR_PHONE_CASE** heavily overrepresented  
- Filtered to keep only types with more than **100 entries**  
- Resulted in **68 product categories**

---






