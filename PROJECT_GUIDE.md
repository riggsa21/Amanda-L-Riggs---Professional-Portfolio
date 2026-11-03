# Project Guide

[Back to the portfolio](README.md)

PDFs, images, and text files usually open in your browser. PowerPoint presentations, Python scripts, and CSV files may download or prompt you to save them, depending on your browser settings.

This guide explains the purpose and scope of the selected work. It separates academic projects, independent demonstrations, and GeoSite Intel report samples. Contributions described below refer to the work presented; source data, software, and references retain their original attribution.

## Applied Research and Property Screening

### Fairview Property Intelligence

**Context:** GeoSite Intel screening report, September 2026; Washington Park, Beaufort County, North Carolina.

**Question:** How can environmental, terrain, drainage, and soil information be organized into an understandable property-screening assessment?

**Work represented:** Synthesis of mapped constraints and a usable-area scenario, presented through a seven-page property intelligence report. The cover summarizes a modeled candidate area and distinguishes it from mapped planning constraints.

**Deliverable and value:** A structured report that connects spatial evidence to questions for further site investigation. It demonstrates analytical organization and communication for decision support.

**Limits:** Screening-level GIS analysis; a modeled candidate area does not establish permitted or buildable land.

[View fairview report (PDF)](Fairview_Property_Intelligence_Report.pdf)

### Mills Road Property Screening

**Context:** GeoSite Intel demonstration, August 2026; Pitt County, North Carolina.

**Question:** Which mapped site conditions deserve further verification before property decisions?

**Work represented:** A subject-parcel and one-mile context review using imagery, parcel information, terrain, drainage, wetlands, flood mapping, soils, and access context. An executive summary translates the findings into follow-up priorities.

**Deliverable and value:** A 13-page demonstration report with mapped evidence and explicit distinctions between observations and unverified interpretations.

**Limits:** The report does not confirm contamination, legal access, wetland boundaries, engineering suitability, or buildability. It is labeled as a demonstration rather than a completed professional determination.

[View mills Road report (PDF)](Mills_Road_Property_Screening_Report.pdf)

### Owen Sound Site Selection

**Context:** Independent demonstration, October 2026; Owen Sound, Ontario.

**Question:** How can parcel records, planning designations, boundary checks, and constraint overlays support a transparent residential-screening workflow?

**Work represented:** An audit of source parcels, separate handling of boundary-crossing records, a documented overlay scenario, and a candidate-table excerpt. The report traces the layers used and the meaning of each deduction.

**Deliverable and value:** A five-page proposal sample showing how to make screening logic and outstanding questions visible to a reviewer.

**Limits:** Scenario acreage is not confirmed developable acreage. No record is cleared for the intended housing form or planning pathway; source geometry, servicing, access, and applicable policies require further checking.

[View owen Sound demonstration (PDF)](Owen_Sound_Site_Selection_Demonstration.pdf)

## Python and Business Data Automation

**Context:** Independent illustrative example using 48 fictional order records; no real customer data.

**Question:** How can a small business-data workflow identify problematic records and produce usable outputs while preserving its input?

**Work represented:** A Python script checks order IDs, dates, amounts, status values, and customer names; routes invalid rows for review; and totals accepted amounts by customer. It uses `csv`, `pathlib`, `datetime`, and `collections` from the standard library.

**Deliverables:** [Download Python script (.py)](process_demo_orders.py), [Download sample input (CSV)](sample_orders.csv), [Download accepted records (CSV)](clean_orders.csv), [Download exceptions (CSV)](review_required.csv), and [Download customer totals (CSV)](customer_summary.csv).

**Limits:** This is a compact demonstration of validation and reporting logic. It does not implement a production accounting system or comprehensive financial validation.

[View run instructions (text)](Order_Validation_README.txt)

## Geoprocessing Automation and Presentations

**Context:** Independent academic project, GEOG-6400, East Carolina University, April 2024.

**Question:** How can repeated feature and raster preparation be consolidated for research workflows?

**Contribution:** Designed and documented a batch preprocessing script tool to clip and mask data to a study boundary, apply coordinate-system transformations, and organize outputs in a default geodatabase. The report describes development challenges and the rationale for its parameters.

**Methods and tools:** ArcGIS Pro, Python, and ArcPy geoprocessing tools; preparation for InVEST-related research.

**Deliverables and value:** A technical report and presentations that explain both the workflow and the problem it addresses.

- [View automation report (PDF)](Geoprocessing_Batch_Automation_Report.pdf)
- [Download batch automation presentation (PowerPoint)](Geoprocessing_Batch_Automation_Presentation.pptx)
- [Download preprocessing tool presentation (PowerPoint)](Data_Preprocessing_Tool_Presentation.pptx)

**Limits:** Reproduction requires the relevant ArcGIS environment and input data. The report documents the workflow; this selection does not include a standalone executable tool package.

## Thesis Research and Environmental Communication

**Context:** Academic research materials; East Carolina University, 2025.

**Focus:** Communicating study geography and modeled environmental information in Pitt County and Greens Mill Run, North Carolina.

**Work represented:** A regional study-area map and selected nutrient-delivery and stormwater-retention outputs. The maps connect broader land-cover context with more focused environmental analysis.

**Deliverables:** [View study area (image)](Thesis_Pitt_County_Study_Area.jpg), [View greens Mill Run nutrient-delivery detail (image)](Thesis_Greens_Mill_Run_Nutrient_Delivery.jpg), and [View stormwater-retention volume (image)](Thesis_Stormwater_Retention_Volume.jpg).

**Limits:** These are selected visual outputs, not the complete thesis, model inputs, or validation record. Quantitative interpretation requires the supporting research context.

## Savannah Land-Cover Classification and Change

**Context:** Academic remote-sensing project, East Carolina University, April 2025.

**Question:** How can imagery from 1999 and 2025 be classified and compared to explore landscape change around Savannah, Georgia?

**Contribution:** Prepared and interpreted training samples and spectral profiles, performed supervised classification, assessed classification accuracy, and communicated land-cover transitions in a written report and maps.

**Methods:** Landsat imagery, spectral interpretation, supervised classification, accuracy assessment, and change detection.

**Deliverables:** [View analysis report (PDF)](Savannah_Land_Cover_Analysis_Report.pdf), [View 1999 classification (image)](Savannah_1999_Classification.jpg), [View 2025 classification (image)](Savannah_2025_Classification.jpg), and [View change map (image)](Savannah_Land_Cover_Change_1999_2025.jpg).

**Limits:** Comparisons depend on classification accuracy, training choices, class definitions, and differences between the imagery dates and sensors. Mapped transitions should be read alongside the report's assessment.

## Hydrologic Terrain Processing

**Context:** Academic project supporting thesis-related hydrologic analysis, East Carolina University, October 2024.

**Question:** How can an urban sub-watershed DEM be prepared for hydrologic and nutrient-delivery modeling?

**Contribution:** Documented a terrain-processing workflow for Greens Mill Run using hydro-flattening, conditioning, and drainage enforcement techniques in ArcGIS Pro. The report connects processing decisions to intended use in the InVEST Nutrient Delivery Ratio model.

**Deliverables:** [View methods report (PDF)](Hydrologic_DEM_Processing_Report.pdf) and [View selected result map (image)](Hydrologic_DEM_Processing_Map.jpg).

**Limits:** DEM processing and modeled flow require interpretation against source resolution, infrastructure representation, and validation evidence. These outputs are research materials rather than an engineering certification.

## Buncombe Flood-Risk Analysis

**Context:** Academic project, GEOG-6460, East Carolina University, October 2024.

**Question:** How can an automated terrain-analysis workflow support a flood-risk mapping exercise?

**Contribution:** Developed and documented a Python workflow in ArcGIS Pro using ArcPy and NumPy, with terrain and hydrologic processing applied to Buncombe County, North Carolina.

**Deliverables:** [View analysis and scripting report (PDF)](Buncombe_Flood_Risk_Analysis_Report.pdf) and [View final map (image)](Buncombe_Flood_Risk_Map.jpg).

**Limits:** This is an academic modeling exercise. Its output is not an official flood-hazard determination or a substitute for a calibrated hydraulic study.

## Cartography and LiDAR

**Context:** Selected cartographic work samples; the LiDAR sheet identifies an East Carolina University Remote Sensing II project, April 2025.

**Focus:** Clear geographic presentation across coastal mapping and three-dimensional building visualization.

**Work represented:** Two coastal maps and a LiDAR building-extraction visualization. These samples demonstrate layout, geographic context, and the presentation of spatial information in different formats.

- [View cape Lookout map (PDF)](Cape_Lookout_Map.pdf)
- [View harkers Island map (image)](Harkers_Island_Map.jpg)
- [View 3D buildings from LiDAR (PDF)](Extracting_3D_Buildings_from_LiDAR.pdf)

**Limits:** The individual sheets are visual work samples. Full processing histories and input datasets are not included; source credits remain on the materials.
