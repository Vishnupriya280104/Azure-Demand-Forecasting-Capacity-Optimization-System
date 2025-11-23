# Azure Demand Forecasting & Capacity Optimization System

This is a project on AI-driven system using Azure to forecast demand and optimize capacity for efficient supply chain management of Infosys 6.0 internship.

***Architecture of the project:***
![Architecture](https://github.com/user-attachments/assets/7be85a91-cd0b-47dd-ae5c-326cc060cfa4)

***Demo Video:***
https://github.com/user-attachments/assets/6eea2158-29fb-4715-9f94-ec6b47df53d4  

This project implements an end-to-end cloud-based forecasting system designed to predict Azure Compute and Storage demand. The workflow integrates multi-cloud data ingestion, scalable storage, advanced feature engineering, machine learning model training, and Power BI–based visualization to support Azure’s capacity planning and supply chain decision-making.     

<img width="1000" height="342" alt="azure" src="https://github.com/user-attachments/assets/afbbdd90-504f-4193-b094-a3078a6145d0" />   

***1. Data Sources***

The solution brings together data from three major platforms:

Snowflake DB – provides structured enterprise usage and infrastructure data.
Google Cloud Platform (GCP) – supplies external cloud usage signals and demand indicators.
Render API – provides API-level real-time consumption metrics. These diverse sources create a rich dataset combining internal and external demand drivers.  

<img width="1120" height="268" alt="image" src="https://github.com/user-attachments/assets/af9c4fdf-6df3-44df-9beb-2b555a8b2afa" />    


***2. Data Ingestion Layer***

All incoming data is ingested through:

✔ Azure Data Factory (ADF)
+ Automates ingestion workflows
+ Connects securely to Snowflake, GCP, and API endpoints
+ Handles scheduling, pipelines, and logging
  
✔ Azure Data Lake Storage (ADLS)

+ Acts as the centralized raw data storage location
+ Stores data in hierarchical folders for easy integration with Databricks This ensures scalable, fault-tolerant data handling capable of growing with Azure’s infrastructure signals.


<img width="961" height="349" alt="image" src="https://github.com/user-attachments/assets/7e27f470-3a72-47b4-a94d-a820fa5d2102" />  

***3. Data Processing Layer (Azure Databricks)***

Azure Databricks is the core data processing and ML environment in this architecture.

✔ Bronze Layer (Raw Data)

+ Stores unprocessed data exactly as received
+ Maintains full data lineage and fidelity
  
✔ Silver Layer (Clean + Enriched Data)

+ Data cleaning applied
+ Feature engineering performed (lags, moving averages, seasonality, growth, economic indicators, etc.)
+ Time-series alignment and normalization
  
✔ Gold Layer (Model-Ready Data)

+ Final curated dataset
+ Used for machine learning and dashboard consumption
This multi-layered Lakehouse approach ensures clean, high-quality, reliable input for modeling.
<img width="726" height="393" alt="image" src="https://github.com/user-attachments/assets/d8bee825-5636-4950-b0df-29d912337b48" />

***4. Machine Learning Model Training***

The Model Training block uses Databricks ML runtime to build multiple forecasting models:

+ Random Forest
+ XGBoost Regressor
+ Prophet
+ ARIMA (Auto-ARIMA)
+ Each model is trained on engineered features from the Silver/Gold layers.

Model Accuracy- Random Forest: 97.69% (Best), XGBoost: 97.47%, ARIMA: 84.2%, Prophet: 84.19%

Random Forest performed the best due to its ability to learn complex patterns from multiple correlated signals.

The final outputs include:

+ Predicted Compute demand
+ Predicted Storage demand
+ Weekly and monthly trend insights
+ Model performance metrics (MAE, RMSE, SMAPE)
  
***5. Visualization Layer (Power BI)***

The final forecasts and performance metrics are published to Power BI, enabling:

+ Real-time interactive dashboards
+ Demand trend reports
+ Regional and service-level breakdowns
+ Capacity planning insights
+ Model accuracy monitoring  

 <img width="1296" height="733" alt="image" src="https://github.com/user-attachments/assets/afd744db-9ea1-4c24-9987-f6a022c5f638" />

<img width="1307" height="723" alt="image" src="https://github.com/user-attachments/assets/31c88b00-0a9f-4598-bd31-ecc07bc82606" />

<img width="1299" height="725" alt="image" src="https://github.com/user-attachments/assets/e8a9a1e9-8c66-4f7d-b138-13da67420966" />    

The dashboard is visible in this link: 
https://app.powerbi.com/view?r=eyJrIjoiOGYxYTA5NWMtZTg3NC00Nzk4LThjZjMtNDVlMmE2OTc1ZmI2IiwidCI6IjE1YzM0OWUxLTBjNTUtNDYwOS1iMzNhLWM2MjJkOWU2NjRlYSJ9

## Summary

This project delivers an integrated cloud-based forecasting system that ingests multi-cloud data from Snowflake, GCP, and API sources into Azure storage via ADF, processes it through a Databricks Lakehouse (Bronze-Silver-Gold layers), trains multiple ML models to predict Azure Compute & Storage demand, and visualizes the insights in Power BI. Random Forest delivered the best forecast accuracy (97.69%), enabling Azure to optimize capacity planning and reduce infrastructure cost inefficiencies.





