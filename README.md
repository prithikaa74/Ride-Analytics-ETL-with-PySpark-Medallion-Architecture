# Ride-Analytics-ETL-with-PySpark-Medallion-Architecture

📌 Project Overview

This project implements an ETL pipeline for ride analytics data using PySpark with the Medallion Architecture (Bronze → Silver → Gold). The pipeline ensures data is cleaned, transformed, and enriched at each layer for analytics and reporting purposes.

🏗 Architecture

Medallion Layers:

Bronze: Raw ingested ride data, minimal transformation.

Silver: Cleansed and standardized data with missing values handled.

Gold: Aggregated and enriched data suitable for analytics dashboards, including metrics like fare, ride duration, and distance.

⚙️ Tech Stack

PySpark – Data processing

Pandas – Initial data exploration (optional)

CSV – Data storage at each medallion layer

📝 Author

Prithikaa R N – Data Engineering & Analytics Enthusiast

Power BI / Excel – Visualization of Gold layer data
