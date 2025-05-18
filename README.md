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
- We used the small variant (**3GB**) of the dataset because it was computationally feasible and sufficient for training and evaluation.  
- Images were in **256×256 resolution**, which is suitable for most CNN-based vision models.

---

### Data Filtering Process

#### Language Filtering:

- **What we did**: Filtered entries based on `'language_tag'` starting with `'en'`
- **Why**: 
  - To ensure consistency in training text-based metadata fields.
  - Non-English entries could introduce linguistic variability and noise.
  - Focused on English variants: `en_US`, `en_GB`, `en_CA`, `en_AU`, `en_IN`, `en_SG`, `en_AE`
- **Outcome**: **118,588** English-language entries retained

#### Metadata Structure Analysis:

- **What we did**: Analyzed the metadata JSON files to understand the structure and relevance of different fields.
- **Why**: 
  - To identify fields most relevant to product classification (e.g., `node_name`, `product_type`, etc.)
  - To ensure the data schema was well understood for preprocessing and model input formatting.
- **Focus**: `'node'` fields were particularly important as they contained hierarchical category information crucial for classification.

#### Node-Based Filtering:

- **What we did**: Retained only those entries that contained valid `'node'` information.
- **Why**:
  - Entries without node data lacked proper categorization.
  - For a classification task, having a reliable label or hierarchy is essential.
- **Outcome**: Reduced dataset to **112,600** well-categorized entries

---

### Data Cleaning and Standardization

#### Language Standardization:

- **What we did**: Removed non-English content and stripped language tags.
- **Why**: 
  - Simplified the dataset structure for modeling.
  - Prevented language-specific preprocessing complications.
  - Allowed us to treat text data uniformly.

#### Field Reduction:

- **What we did**: Removed irrelevant fields such as:
  - Other image IDs, item IDs, model numbers, marketplace identifiers  
  - Domain names, 3D model IDs, spin IDs, node IDs  
- **Why**:
  - Reduced memory and computational load.
  - These fields were not useful for visual recognition or classification.
  - Helped in focusing on essential information for training and inference.

#### Record Validation:

- **What we did**: Dropped records with:
  - Missing or null `main_image_id`
  - Missing `node_name`
- **Why**:
  - These fields are critical: an image is necessary for visual recognition, and `node_name` provides the label.
  - Keeping only complete and valid records ensures training integrity.
- **Final Outcome**: **112,119** complete and usable records

---

## Category Analysis

### Hierarchical Category Extraction:

- **What we did**: Parsed `node_name` into multiple levels (category level 1 to 6)
- **Why**:
  - Enabled fine-grained analysis of category depth and structure.
  - Useful for experimenting with different classification granularity (e.g., coarse vs. fine labels).

### Category Distribution:

- **What we did**: Analyzed distribution of top-level categories and filtered low-representation ones.
- **Why**:
  - Some categories were underrepresented and could introduce class imbalance.
  - Focused training on categories with sufficient data improves model generalization.
- **Kept categories**:
  - Categories  
  - Homeware & Furniture  
  - Home & Garden  
  - Products  
  - Departments  

---

## Product Type Analysis

### Product Type Distribution:

- **What we did**: Identified primary product type for each record.
- **Why**:
  - Provided an additional layer of labeling for potential multi-label or fine-grained classification tasks.
  - Helped understand diversity and richness of the dataset.

- **Top product types**:
  - `CELLULAR_PHONE_CASE` – 64,705 entries  
  - `SHOES` – 9,070 entries  
  - `GROCERY` – 4,814 entries  
  - `HOME` – 2,114 entries  
  - `CHAIR` – 1,611 entries  

### Data Balance Analysis:

- **What we did**: Retained only product types with more than **100 entries**.
- **Why**:
  - Extremely imbalanced data (e.g., phone cases dominating) can bias the model.
  - Removing underrepresented types ensured more uniform learning and reduced overfitting to dominant classes.
- **Outcome**: Reduced to **68 product categories** with adequate representation

  The curation process transformed noisy, multilingual, and partially incomplete data into a **clean, English-only dataset** with a **consistent structure**, **valid images**, and **balanced category representation**. This curated dataset provides a strong foundation for training high-quality visual recognition models.

---
