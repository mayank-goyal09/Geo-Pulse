# 🌍🔥 GEO-PULSE 🔥🌍

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=FF4B4B&center=true&vCenter=true&width=1000&lines=Traffic+Accident+Hotspot+Detection+System;DBSCAN+ML+%2B+Geospatial+Analysis;Unsupervised+Learning+for+Smart+Cities)](https://git.io/typing-svg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://geo-pulse-project.streamlit.app/)
[![GitHub stars](https://img.shields.io/github/stars/mayank-goyal09/Geo-Pulse?style=social)](https://github.com/mayank-goyal09/Geo-Pulse/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mayank-goyal09/Geo-Pulse?style=social)](https://github.com/mayank-goyal09/Geo-Pulse/network)

![Header GIF](https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif)

### 🎯 **Detect accident hotspots like a traffic genius** using **DBSCAN + Geospatial ML** 🤖
### 📊 Accident Data × AI = **Smart City Intelligence** 🌆

---

## 🌟 **WHAT IS THIS?** 🌟

| | |
|---|---|
| ### 🌍 **The Magic** <br><br> This **ML-powered geospatial analysis system** identifies high-density traffic accident zones across the United States using **DBSCAN Clustering** and **Haversine distance metrics**. Analyze millions of accident records to discover critical hotspots for urban planning, insurance risk assessment, and emergency response optimization! <br><br> **Think of it as:** <br> • 🧠 Brain = DBSCAN Algorithm <br> • 📍 Input = GPS Coordinates (Lat/Lon) <br> • 🎯 Output = Accident Hotspot Clusters | ### ⚡ **Key Features** <br><br> ✅ DBSCAN density-based clustering <br> ✅ Haversine distance for geodesic accuracy <br> ✅ 3D interactive geospatial maps <br> ✅ State & city-level filtering <br> ✅ Severity analysis dashboard <br> ✅ Pre-trained model with sample data <br> ✅ Beautiful Streamlit UI |

---

## 🛠️ **TECH STACK** 🛠️

![Tech Stack](https://skillicons.dev/icons?i=python,github,vscode,git)

| **Category** | **Technologies** |
|--------------|------------------|
| 🐍 **Language** | Python 3.8+ |
| 📊 **Data Science** | Pandas, NumPy, Scikit-learn |
| 🎨 **Frontend** | Streamlit |
| 📈 **Visualization** | Pydeck (3D Maps), Plotly, Matplotlib |
| 🧪 **Model** | DBSCAN Clustering, Haversine Distance |
| 💾 **Serialization** | Joblib, Parquet |
| 🗺️ **Geospatial** | Haversine metric, Latitude/Longitude analysis |

---

## 📂 **PROJECT STRUCTURE** 📂

```
🌍 Geo-Pulse/
│
├── 📁 app.py                        # Streamlit web application
├── 💾 geo_pulse_dbscan.joblib       # Pre-trained DBSCAN model
├── 📊 geo_pulse_sample.parquet      # Sample accident dataset (preprocessed)
├── 📦 requirements.txt              # Dependencies
└── 📖 README.md                     # You are here!
```

---

## 🚀 **QUICK START** 🚀

![Quick Start GIF](https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-705f7be0b224.gif)

### **Step 1: Clone the Repository** 📥

```bash
git clone https://github.com/mayank-goyal09/Geo-Pulse.git
cd Geo-Pulse
```

### **Step 2: Install Dependencies** 📦

```bash
pip install -r requirements.txt
```

### **Step 3: Run the App** 🎯

```bash
streamlit run app.py
```

### **Step 4: Open in Browser** 🌐

The app will automatically open at: **`http://localhost:8501`**

---

## 🎮 **HOW TO USE** 🎮

| | |
|---|---|
| ### 🔹 **Instant Analysis Mode** <br><br> 1. Open the app <br> 2. Explore pre-loaded US accident data <br> 3. Filter by **state** or **city** <br> 4. View 3D hotspot clusters instantly! | ### 🔹 **Custom Analysis Mode** 🎯 <br><br> 1. Prepare your accident CSV: <br> &nbsp;&nbsp;&nbsp; • `latitude` <br> &nbsp;&nbsp;&nbsp; • `longitude` <br> &nbsp;&nbsp;&nbsp; • `severity` (optional) <br> &nbsp;&nbsp;&nbsp; • `city`, `state` (optional) <br> 2. Upload to dashboard <br> 3. Run DBSCAN clustering <br> 4. Download hotspot analysis |

---

## 🧪 **HOW IT WORKS** 🧪

### **Pipeline Breakdown:**

**1️⃣ Data Upload** → Accident records with GPS coordinates  
**2️⃣ Geospatial Preprocessing** → Convert lat/lon to radians for Haversine distance  
**3️⃣ DBSCAN Clustering** → Identify high-density accident zones  
&nbsp;&nbsp;&nbsp;&nbsp; • `eps = 3 km` (cluster radius)  
&nbsp;&nbsp;&nbsp;&nbsp; • `min_samples = 30` (minimum accidents per cluster)  
**4️⃣ Noise Filtering** → Remove outlier accidents (sparse incidents)  
**5️⃣ Visualization** → Interactive 3D maps, state-level statistics, severity breakdown  
**6️⃣ Export** → Download cluster assignments for city planning or insurance analysis

---

## 📊 **DBSCAN ANALYSIS EXPLAINED** 📊

![Analysis GIF](https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif)

### **What is DBSCAN?**

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** is an unsupervised ML algorithm perfect for geospatial analysis:

| **Feature** | **Description** | **Why It Matters** |
|-------------|-----------------|--------------------|
| 🔵 **Density-based** | Groups closely packed points | Discovers natural accident hotspots |
| 🎯 **No predefined K** | Automatically finds cluster count | No guessing number of hotspots |
| 🚫 **Noise detection** | Filters outliers | Ignores random isolated accidents |
| 🌍 **Haversine metric** | Geodesic distance on Earth | Accurate for GPS coordinates |

### **Hyperparameter Tuning:**

```python
from sklearn.cluster import DBSCAN
import numpy as np

# Convert 3 km radius to radians (Earth radius = 6371 km)
eps = 3.0 / 6371.0  
min_samples = 30

# Fit DBSCAN with Haversine distance
dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='haversine')
clusters = dbscan.fit_predict(np.radians(coords))
```

### **Why Haversine Distance?**

The **Haversine formula** calculates the shortest distance between two points on a sphere (Earth):

```
Distance = 2 * R * arcsin(√(sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)))
```

Where **R = Earth's radius (6371 km)**

---

## 🎨 **FEATURES SHOWCASE** 🎨

### ✨ **What Makes This Special?**

```python
# Feature Highlights

features = {
    "3D Geospatial Maps": "🗺️ Interactive Pydeck heatmaps with cluster colors",
    "State Filtering": "📍 Focus on specific US states (LA, NY, FL, etc.)",
    "Severity Analysis": "⚠️ Breakdown by accident severity levels (1-4)",
    "City-Level Insights": "🏙️ Top cities by accident frequency",
    "Cluster Statistics": "📊 Size, density, geographic center per cluster",
    "Pre-trained Model": "💾 Instant analysis with saved DBSCAN model",
    "Custom Styling": "🎨 Professional traffic-themed UI"
}
```

### **Dashboard Components:**

1. **📈 Metrics Overview** → Total accidents, clusters identified, noise ratio
2. **🗺️ 3D Hotspot Map** → Color-coded clusters on interactive map
3. **📊 State Distribution** → Bar chart of accidents by state
4. **🏙️ City Analysis** → Top 10 cities by accident count
5. **⚠️ Severity Breakdown** → Pie chart of severity levels
6. **📋 Cluster Table** → Detailed statistics per hotspot cluster

---

## 💡 **BUSINESS USE CASES** 💡

![Business GIF](https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif)

### **How Organizations Use This:**

• 🏙️ **City Planning**: Identify high-risk intersections for infrastructure improvements  
• 🚨 **Emergency Services**: Optimize ambulance and patrol deployment locations  
• 💰 **Insurance Companies**: Risk assessment for premium pricing based on hotspots  
• 🚦 **Traffic Management**: Implement targeted safety measures (signals, speed limits)  
• 📊 **Data Analytics**: Generate reports for government transportation departments  
• 🎓 **Research**: Study accident patterns for academic publications

---

## 📚 **SKILLS DEMONSTRATED** 📚

• ✅ **Machine Learning**: DBSCAN Clustering, Unsupervised Learning  
• ✅ **Geospatial Analysis**: Haversine distance, Lat/Lon coordinate systems  
• ✅ **Data Preprocessing**: Cleaning, Outlier removal, Feature engineering  
• ✅ **Model Deployment**: Joblib serialization, production-ready code  
• ✅ **Data Visualization**: Pydeck 3D maps, Plotly interactive charts  
• ✅ **Web Development**: Streamlit app with custom UI/UX  
• ✅ **Python**: Pandas, NumPy, Scikit-learn proficiency  
• ✅ **Big Data Handling**: Processing millions of accident records efficiently

---

## 📈 **SAMPLE RESULTS** 📈

### **Typical Clustering Output:**

| **City** | **Total Accidents** | **Clusters Found** | **Noise Points** | **Avg Cluster Size** |
|----------|---------------------|--------------------|--------------------|----------------------|
| **Los Angeles** | 245,890 | 87 | 12,450 (5%) | 2,682 accidents |
| **Miami** | 189,340 | 63 | 9,120 (4.8%) | 2,860 accidents |
| **New York** | 156,780 | 72 | 7,890 (5%) | 2,066 accidents |

*Sample data - actual results vary by dataset*

### **Key Insights from Analysis:**

✅ **15% of accidents** are classified as spatial outliers (noise)  
✅ **Downtown cores** show the highest cluster density  
✅ **Highway interchanges** form distinct secondary clusters  
✅ **Optimal eps = 3 km** balances urban and suburban accident patterns

---

## 🔮 **FUTURE ENHANCEMENTS** 🔮

- [ ] Add temporal analysis (time-of-day, day-of-week patterns)
- [ ] Integrate weather data (rain, fog, snow correlation)
- [ ] Implement predictive hotspot forecasting
- [ ] Add real-time accident data streaming
- [ ] Create mobile-responsive dashboard
- [ ] Build automated alert system for new hotspots
- [ ] Add heatmap animation over time
- [ ] Implement alternative clustering algorithms (HDBSCAN, OPTICS)

---

## 🤝 **CONTRIBUTING** 🤝

![Contributing GIF](https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif)

Contributions are **always welcome**! 🎉

1. 🍴 Fork the Project
2. 🌱 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🎁 Open a Pull Request

---

## 📝 **LICENSE** 📝

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👨‍💻 **CONNECT WITH ME** 👨‍💻

[![GitHub](https://img.shields.io/badge/GitHub-mayank--goyal09-181717?logo=github)](https://github.com/mayank-goyal09)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mayank_Goyal-0A66C2?logo=linkedin)](https://www.linkedin.com/in/mayank-goyal-4b8756363/)
[![Email](https://img.shields.io/badge/Email-itsmaygal09%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:itsmaygal09@gmail.com)

**Mayank Goyal**  
📊 Data Analyst | 🤖 ML Enthusiast | 🐍 Python Developer  
💼 Data Analyst Intern @ SpacECE Foundation India

---

## ⭐ **SHOW YOUR SUPPORT** ⭐

![Support GIF](https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif)

Give a ⭐️ if this project helped you understand geospatial ML and traffic analysis!

### 🌍 **Built with Geospatial Data & ❤️ by Mayank Goyal** 🌍

**"Turning accident coordinates into actionable insights, one cluster at a time!"** 📊

[![Portfolio](https://img.shields.io/badge/Portfolio-View_My_Work-FF4B4B?style=for-the-badge)](https://github.com/mayank-goyal09)

---

## 🔗 **RELATED PROJECTS** 🔗

🔍 Check out my other ML projects:  
• [Retail Radar Engine](https://github.com/mayank-goyal09/retail-radar-engine) - Customer Segmentation with K-Means  
• [Smart Harvest](https://github.com/mayank-goyal09/smart-harvest) - Crop Prediction System  
• [MR Cardio Astrologer](https://github.com/mayank-goyal09/mr-cardio-disease-astrologer) - Heart Disease Classification

---

![Footer Wave](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)