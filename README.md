# 🚖 Ola Ride Insights – End-to-End Data Analytics Project

## 📌 Project Overview
The rise of ride-sharing platforms has transformed urban mobility by offering convenient and affordable transportation solutions. **OLA**, a leading ride-hailing service in India, generates massive volumes of ride data daily.

This project focuses on analysing OLA’s ride-sharing data to extract **actionable business insights** using **SQL, Python, Tableau, and Streamlit**. The outcome is a **professional analytics solution** combining data preprocessing, interactive dashboards, and a web-based analytics application.

---

## 🎯 Problem Statement
Despite having vast ride data, deriving meaningful insights related to demand patterns, revenue trends, customer behavior, and cancellations remains challenging.

This project aims to:
- Improve operational efficiency
- Enhance customer satisfaction
- Support data-driven business decisions

---

## 🧠 Business Use Cases
- Identifying **peak demand hours** to optimize driver allocation  
- Analyzing **customer behavior** for targeted marketing  
- Understanding **pricing & revenue patterns**  
- Detecting **ride cancellations & service issues**  
- Monitoring **customer and driver ratings**

---

## 🛠️ Skills & Technologies Used

### 🔹 Programming & Data
- Python
- Pandas
- NumPy
- SQL (MySQL)

### 🔹 Visualization & BI
- Tableau Public
- Streamlit

### 🔹 Analytics Concepts
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- KPI Design
- Business Intelligence
- Dashboard Design

---

## 📂 Project Structure
```
Ola_Rides/
├── OLA_DataSet.csv        #Raw dataset
├── OLA_CLEANED.csv        #Cleaned dataset
├── ola_project.ipynb      #Data cleaning & EDA notebook
├── app.py                 #Streamlit application
├── .venv/                 #Virtual environment
└── README.md              #Project documentation
```


---

## 🧹 Data Cleaning & Preprocessing
Performed using **Python (Pandas)**:
- Handled missing and null values
- Standardised column formats
- Converted date & time fields
- Created derived features such as ride day and hour
- Validated cleaned dataset for analysis

---

## 🗄️ SQL Analysis
Key SQL queries were written to extract insights:

1. Retrieve all successful bookings  
2. Average ride distance by vehicle type  
3. Total cancelled rides by customers  
4. Top 5 customers by total bookings  
5. Driver cancellations due to personal/car issues  
6. Maximum & minimum driver ratings (Prime Sedan)  
7. Rides paid via UPI  
8. Average customer rating per vehicle type  
9. Total booking value of successful rides  
10. List of incomplete rides with reasons  

---

## 📊 Tableau Dashboard
A **professional interactive dashboard** was created using Tableau Public.

### Key Visuals:
- Ride Volume Over Time
- Booking Status Breakdown
- Revenue by Payment Method
- Top 5 Customers by Revenue
- Vehicle Type Performance
- Peak Booking Heatmap (Day vs Hour)
- Customer & Driver Cancellation Reasons
- Ratings Analysis

🔗 **Live Tableau Dashboard:**  
https://public.tableau.com/app/profile/achintya.krishna/viz/Ola_Ride/OlaRideInsightsDashboard

---

## 🌐 Streamlit Application
The Streamlit app serves as a **business-facing analytics portal**.

### Features:
- KPI Summary (Total Rides, Revenue, Avg Rating)
- Embedded **interactive Tableau dashboard**
- Clean, polished UI inspired by Tableau
- Fast, lightweight performance
- Business insight narration

### Run Locally:
```bash
streamlit run app.py
```
---

## 📈 Key Insights

* ~62% of rides are completed successfully
* Peak demand occurs during **mid-week evenings**
* Cash and UPI dominate payment methods
* Prime & SUV categories contribute significantly to revenue
* Cancellations highlight service & operational gaps

---

## 🚀 Project Deliverables

* ✔ Cleaned & validated dataset
* ✔ Optimised SQL queries
* ✔ Interactive Tableau dashboard
* ✔ Streamlit analytics application
* ✔ Business-focused documentation

---

## 📌 Evaluation Metrics

* Accuracy of SQL insights
* Dashboard clarity & usability
* Streamlit UI responsiveness
* Business relevance of insights

---

## 👤 Author

**Achintya Krishna**
Data Engineer | Business Intelligence | Analytics

📍 India
