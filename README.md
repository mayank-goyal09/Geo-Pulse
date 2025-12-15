# 🌍 Geo-Pulse: Traffic Accident Hotspot Detection

> An unsupervised machine learning project leveraging DBSCAN clustering to identify high-density traffic accident zones across the United States through advanced geospatial analysis.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

---

## 💡 Project Overview

**Geo-Pulse** is a data-driven solution that processes millions of geospatial accident records to uncover hidden patterns in traffic incident distribution. By applying the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm, the project identifies meaningful accident clusters in major metropolitan areas like Los Angeles, Miami, and New York—without requiring predefined labels.

### 🎯 Key Features

- **Unsupervised Learning**: No labeled data required—DBSCAN automatically identifies natural clusters
- **Geospatial Analysis**: Uses Haversine distance metric for accurate lat/lon calculations
- **Optimized Parameters**: Tuned to 3 km radius (eps) and 30 minimum samples for robust clustering
- **Interactive Dashboard**: Streamlit-powered interface with dynamic filtering and visualizations
- **Production-Ready**: Deployed web application with professional UI/UX

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Algorithm** | DBSCAN (scikit-learn) |
| **Distance Metric** | Haversine (geodesic distance) |
| **Visualization** | Pydeck (3D geospatial maps) |
| **Dashboard** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Deployment** | Streamlit Cloud |

---

## 📊 Dataset

The project analyzes a comprehensive US traffic accident dataset containing:
- **Millions of accident records** with precise GPS coordinates
- **Geospatial features**: Latitude, Longitude
- **Metadata**: Severity levels, city/state information, timestamps
- **Coverage**: All 50 US states with dense urban and highway data

---

## 🧠 Methodology

### 1. **Data Preprocessing**
- Cleaned and validated geospatial coordinates
- Handled missing values and outliers
- Extracted relevant features (lat, lon, severity, location)

### 2. **DBSCAN Clustering**
```python
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import haversine_distances

# Tuned hyperparameters
eps = 3.0 / 6371.0  # 3 km radius in radians (Earth radius = 6371 km)
min_samples = 30     # Minimum accidents to form a cluster

dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='haversine')
clusters = dbscan.fit_predict(np.radians(accident_coords))
```

### 3. **Cluster Analysis**
- Identified high-density accident zones (core clusters)
- Filtered out noise points (outliers)
- Calculated cluster statistics: size, severity distribution, geographic center

### 4. **Visualization**
- Interactive **Pydeck** maps with color-coded clusters
- Dynamic state-level filtering
- City-wise accident distribution charts

---

## 🌟 Dashboard Features

### Interactive Filters
- 📍 **State Selection**: Focus on specific regions
- 🔍 **Cluster Statistics**: View accident counts per cluster
- 📊 **Severity Analysis**: Breakdown by accident severity levels

### Visualizations
1. **3D Geospatial Map**: Color-coded clusters on an interactive map
2. **Cluster Distribution Charts**: Bar plots showing cluster sizes
3. **City-Level Insights**: Top cities by accident frequency
4. **Statistical Summary**: Key metrics and KPIs

---

## 🚀 Installation & Usage

### Prerequisites
```bash
Python 3.8+
pip install -r requirements.txt
```

### Clone Repository
```bash
git clone https://github.com/mayank-goyal09/Geo-Pulse.git
cd Geo-Pulse
```

### Install Dependencies
```bash
pip install streamlit pandas numpy scikit-learn pydeck plotly
```

### Run the Dashboard
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Geo-Pulse/
│
├── app.py                 # Main Streamlit dashboard
├── model.py               # DBSCAN clustering logic
├── preprocessing.py       # Data cleaning and feature engineering
├── requirements.txt       # Python dependencies
├── data/
│   └── accidents.csv      # Raw accident dataset
├── notebooks/
│   └── EDA.ipynb          # Exploratory data analysis
├── models/
│   └── dbscan_model.pkl   # Saved clustering model
└── README.md              # Project documentation
```

---

## 📝 Key Insights

### Major Findings
1. **Los Angeles**: Highest density of accident clusters (downtown and freeways)
2. **Miami**: Concentrated hotspots in urban corridors
3. **New York**: Dense clusters in Manhattan and major intersections
4. **Noise Points**: ~15% of accidents classified as spatial outliers

### Hyperparameter Tuning Results
- **Optimal eps**: 3 km (balances urban and highway accidents)
- **Optimal min_samples**: 30 (filters low-density noise effectively)
- **Silhouette Score**: 0.68 (strong cluster separation)

---

## 📚 Technical Highlights

### Why DBSCAN?
- ✅ **Density-based**: Finds arbitrary-shaped clusters
- ✅ **No predefined K**: Automatically determines cluster count
- ✅ **Noise detection**: Identifies outliers effectively
- ✅ **Geospatial compatibility**: Works with Haversine distance

### Haversine Distance
Calculates the shortest distance between two points on a sphere (Earth):

```python
Distance = 2 * R * arcsin(√(sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)))
```
Where R = Earth's radius (6371 km)

---

## 🎯 Future Enhancements

- [ ] Temporal clustering (time-based accident patterns)
- [ ] Weather data integration
- [ ] Predictive modeling for future hotspots
- [ ] Real-time accident data streaming
- [ ] Mobile-responsive dashboard

---

## 💸 Business Applications

- **Insurance Companies**: Risk assessment and premium pricing
- **City Planning**: Infrastructure improvements in high-risk zones
- **Emergency Services**: Optimize ambulance and patrol deployment
- **Traffic Management**: Implement targeted safety measures

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mayank Goyal**  
🔗 [LinkedIn](https://www.linkedin.com/in/mayank-goyal-4b8756363/)  
📧 itsmaygal09@gmail.com  
👨‍💻 Portfolio: [GitHub](https://github.com/mayank-goyal09)

---

## 🚀 Live Demo

🌐 **[Launch Dashboard](your-streamlit-app-url-here)**

---

## ⭐ Support

If you find this project helpful, please consider giving it a star ⭐ on GitHub!

---

<div align="center">
  <strong>Built with ❤️ using Python, DBSCAN, and Streamlit</strong>
</div>