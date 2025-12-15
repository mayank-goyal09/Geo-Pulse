import streamlit as st
import pandas as pd
import joblib
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Geo-Pulse: US Accident Analytics",
    page_icon="🚨",
    layout="wide"
)

# ========= LOAD DATA =========
@st.cache_data
def load_data():
    df = pd.read_parquet("geo_pulse_sample.parquet")
    return df

@st.cache_resource
def load_model():
    model = joblib.load("geo_pulse_dbscan.joblib")
    return model

df = load_data()
dbscan = load_model()
df = df.rename(columns={"Start_Lat": "lat", "Start_Lng": "lon"})


# ========= THEME =========
CHARCOAL = "#1C1C1C"
CHARCOAL_2 = "#2A2A2A"
BROWN = "#3E2723"
BROWN_DARK = "#2C1810"
BROWN_LIGHT = "#5D4037"
YELLOW = "#FFA000"
YELLOW_DARK = "#FF6F00"
YELLOW_LIGHT = "#FFCA28"

# Token-free basemap (CARTO). Works without Mapbox token and still looks like a real map. [web:46]
CARTO_DARK = "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
CARTO_DARK_NOLABELS = "https://basemaps.cartocdn.com/gl/dark-matter-nolabels-gl-style/style.json"
BASEMAP_STYLE = CARTO_DARK_NOLABELS  # clean + matches your dark theme


st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;600;700;900&family=Inter:wght@400;600;700;800&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

/* App background */
.stApp {{
  background: linear-gradient(135deg, {CHARCOAL} 0%, {BROWN_DARK} 50%, {CHARCOAL} 100%);
}}

.block-container {{ max-width: 1400px; padding-top: 1.3rem; }}
[data-testid="stHeader"] {{ background: transparent; }}

/* All text */
html, body, p, li, span, div, label, small {{ color: {YELLOW} !important; }}
h1, h2, h3, h4 {{ color: {YELLOW_LIGHT} !important; font-weight: 900 !important; text-shadow: 0 2px 8px rgba(255, 160, 0, 0.3); }}

/* HERO */
.hero {{
  position: relative;
  border-radius: 20px;
  padding: 28px 32px;
  background: linear-gradient(135deg, {BROWN_DARK} 0%, {BROWN} 100%);
  border: 3px solid {YELLOW_DARK};
  box-shadow: 0 0 35px rgba(255, 160, 0, 0.4), 0 20px 50px rgba(0,0,0,0.5);
  overflow: hidden;
  margin-bottom: 20px;
}}

@keyframes slide {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(60px); }}
}}

.caution-stripe {{
  position: absolute;
  top: 0;
  left: 0;
  width: 200%;
  height: 8px;
  background: repeating-linear-gradient(
    45deg,
    {YELLOW_DARK},
    {YELLOW_DARK} 20px,
    {CHARCOAL} 20px,
    {CHARCOAL} 40px
  );
  animation: slide 1.5s linear infinite;
}}

.hero-icon {{
  position: absolute;
  right: 25px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 90px;
  opacity: 0.12;
  filter: drop-shadow(0 0 20px {YELLOW});
}}

.hero-title {{
  font-size: 2.5rem;
  font-weight: 900;
  color: {YELLOW_LIGHT} !important;
  margin-bottom: 10px;
}}

.hero-sub {{
  color: {YELLOW} !important;
  font-size: 1.05rem;
  line-height: 1.6;
  opacity: 0.9;
}}

.badges {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 14px;
}}

.badge {{
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 900;
  background: linear-gradient(135deg, {YELLOW_DARK} 0%, {YELLOW} 100%);
  color: {CHARCOAL} !important;
  border: 2px solid {YELLOW_LIGHT};
  box-shadow: 0 4px 12px rgba(255, 160, 0, 0.3);
}}

/* CARDS */
.card {{
  border-radius: 18px;
  background: {CHARCOAL_2};
  border: 2px solid {BROWN_LIGHT};
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  padding: 24px;
  margin-bottom: 18px;
}}

.card-title {{
  font-weight: 900;
  font-size: 1.2rem;
  color: {YELLOW_LIGHT} !important;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
}}

.warning-icon {{
  display: inline-block;
  width: 10px;
  height: 10px;
  background: {YELLOW};
  border-radius: 50%;
  box-shadow: 0 0 15px {YELLOW};
  animation: pulse 1.5s ease-in-out infinite;
}}

@keyframes pulse {{
  0%, 100% {{ opacity: 1; }}
  50% {{ opacity: 0.4; }}
}}

/* Inputs */
.stNumberInput input,
.stSelectbox select,
.stTextInput input,
.stMultiselect {{
  background: {BROWN_DARK} !important;
  border: 2px solid {BROWN_LIGHT} !important;
  border-radius: 10px !important;
  color: {YELLOW_LIGHT} !important;
}}

.stSelectbox div[data-baseweb="select"] > div {{
  background: {BROWN_DARK} !important;
  border: 2px solid {BROWN_LIGHT} !important;
}}

.stSelectbox span {{
  color: {YELLOW_LIGHT} !important;
  font-weight: 800 !important;
}}

/* Buttons */
.stButton > button {{
  border: none;
  border-radius: 12px;
  padding: 0.9rem 1.4rem;
  font-weight: 900;
  font-size: 1rem;
  letter-spacing: 0.05em;
  color: {CHARCOAL} !important;
  background: linear-gradient(135deg, {YELLOW_DARK} 0%, {YELLOW} 50%, {YELLOW_LIGHT} 100%);
  box-shadow: 0 12px 30px rgba(255, 160, 0, 0.4);
}}
</style>
""", unsafe_allow_html=True)


# ========= HERO =========
st.markdown(f"""
<div class="hero">
  <div class="caution-stripe"></div>
  <div class="hero-icon">🚨</div>
  <div class="hero-title">🚨 Geo-Pulse: US Accident Intelligence Hub</div>
  <div class="hero-sub">
    Real-time spatial analytics of 7.7M+ traffic accidents (2016–2023). Powered by DBSCAN clustering + geospatial ML.
  </div>
  <div class="badges">
    <div class="badge">7.7M Records</div>
    <div class="badge">DBSCAN Clustering</div>
    <div class="badge">Haversine Distance</div>
    <div class="badge">By Mayank Goyal</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ========= SIDEBAR =========
with st.sidebar:
    st.markdown("### 🎛️ Control Panel")

    all_states = sorted(df["State"].dropna().unique().tolist())
    selected_states = st.multiselect(
        "🗺️ Filter by State",
        options=all_states,
        default=all_states[:5] if len(all_states) >= 5 else all_states,
    )

    show_noise = st.checkbox("Include noise points (-1)", value=False)

    st.markdown("---")
    st.markdown("### 📊 About")
    st.write("This dashboard analyzes US traffic accidents using spatial clustering to identify high-risk zones.")
    st.caption("⚠️ Data: Kaggle US Accidents Dataset")


# ========= FILTER DATA =========
filtered = df.copy()
if selected_states:
    filtered = filtered[filtered["State"].isin(selected_states)]
if not show_noise:
    filtered = filtered[filtered["cluster"] != -1]


# ========= PYDECK MAP (TOKEN-FREE + WORKING TOOLTIP) =========
def make_pydeck_map(data: pd.DataFrame):
    if data.empty:
        return None

    d = data.dropna(subset=["lat", "lon"]).copy()

    # Ensure tooltip fields exist and are strings (prevents {State}/{cluster} not resolving)
    for col in ["cluster", "State", "City"]:
        if col in d.columns:
            d[col] = d[col].astype(str).fillna("NA")
        else:
            d[col] = "NA"

    # Robust: pass records so picked object always contains these keys
    records = d[["lon", "lat", "cluster", "State", "City"]].to_dict("records")

    view_state = pdk.ViewState(
        latitude=float(d["lat"].mean()),
        longitude=float(d["lon"].mean()),
        zoom=5,
        pitch=50,
        bearing=0,
    )

    # Density layer (no tooltip)
    hex_layer = pdk.Layer(
        "HexagonLayer",
        records,
        get_position="[lon, lat]",
        radius=10000,
        elevation_scale=150,
        elevation_range=[0, 4000],
        extruded=True,
        coverage=0.7,
        pickable=False,
    )

    # Tooltip layer (must be pickable)
    scatter_layer = pdk.Layer(
        "ScatterplotLayer",
        records,
        get_position="[lon, lat]",
        get_radius=3000,
        radius_min_pixels=4,
        get_fill_color=[255, 140, 0, 170],
        pickable=True,
        auto_highlight=True,
    )

    deck = pdk.Deck(
        map_style=BASEMAP_STYLE,  # CARTO token-free basemap
        initial_view_state=view_state,
        layers=[hex_layer, scatter_layer],
        tooltip={
            "html": "<b>Accident</b><br/><b>Cluster:</b> {cluster}<br/><b>State:</b> {State}<br/><b>City:</b> {City}",
            "style": {"backgroundColor": BROWN_DARK, "color": YELLOW, "fontWeight": "bold"},
        },
    )
    return deck


# ========= TABS =========
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔥 Hotspot Analysis", "📈 Trends & Insights", "🧠 Cluster Deep Dive"])


# ========= TAB 1: OVERVIEW =========
with tab1:
    if filtered.empty:
        st.warning("⚠️ No data for selected filters")
    else:
        total = int(filtered.shape[0])
        n_clusters = filtered[filtered["cluster"] != -1]["cluster"].nunique()
        noise_ratio = (filtered["cluster"] == -1).mean()
        avg_severity = filtered["Severity"].mean()

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("🚗 Total Accidents", f"{total:,}")
        m2.metric("🎯 Hotspot Clusters", f"{n_clusters}")
        m3.metric("⚡ Noise Ratio", f"{noise_ratio:.1%}")
        m4.metric("📊 Avg Severity", f"{avg_severity:.2f}")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><span class="warning-icon"></span>3D Accident Density Map</div>', unsafe_allow_html=True)

        map_df = filtered.dropna(subset=["lat", "lon"])
        deck = make_pydeck_map(map_df)
        if deck:
            st.pydeck_chart(deck, use_container_width=True)
        else:
            st.info("No points to plot after filtering.")
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span class="warning-icon"></span>Top 15 States by Accidents</div>', unsafe_allow_html=True)

            state_counts = filtered["State"].value_counts().head(15).reset_index()
            state_counts.columns = ["State", "Accidents"]

            fig_state = px.bar(
                state_counts,
                x="Accidents",
                y="State",
                orientation="h",
                color="Accidents",
                color_continuous_scale=["#FF6F00", "#FFA000", "#FFCA28"],
            )
            fig_state.update_layout(
                paper_bgcolor=CHARCOAL_2,
                plot_bgcolor=CHARCOAL_2,
                font=dict(color=YELLOW),
                showlegend=False,
                height=400,
            )
            st.plotly_chart(fig_state, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span class="warning-icon"></span>Severity Distribution</div>', unsafe_allow_html=True)

            severity_counts = filtered["Severity"].value_counts().sort_index()
            fig_sev = go.Figure(data=[go.Pie(
                labels=[f"Severity {s}" for s in severity_counts.index],
                values=severity_counts.values,
                hole=0.4,
                marker=dict(colors=["#FF6F00", "#FFA000", "#FFCA28", "#FFD54F"]),
            )])
            fig_sev.update_layout(
                paper_bgcolor=CHARCOAL_2,
                plot_bgcolor=CHARCOAL_2,
                font=dict(color=YELLOW),
                height=400,
            )
            st.plotly_chart(fig_sev, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)


# ========= TAB 2: HOTSPOT ANALYSIS =========
with tab2:
    if filtered.empty:
        st.warning("⚠️ No data")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><span class="warning-icon"></span>Top 20 Dangerous Cities</div>', unsafe_allow_html=True)

        top_cities = (
            filtered.groupby(["State", "City"])
            .agg(
                accidents=("cluster", "size"),
                avg_severity=("Severity", "mean"),
                max_severity=("Severity", "max"),
            )
            .reset_index()
            .sort_values("accidents", ascending=False)
            .head(20)
        )

        fig_cities = px.bar(
            top_cities,
            x="accidents",
            y="City",
            orientation="h",
            color="avg_severity",
            color_continuous_scale=["#FFCA28", "#FFA000", "#FF6F00"],
            hover_data=["State", "max_severity"],
        )
        fig_cities.update_layout(
            paper_bgcolor=CHARCOAL_2,
            plot_bgcolor=CHARCOAL_2,
            font=dict(color=YELLOW),
            height=500,
        )
        st.plotly_chart(fig_cities, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><span class="warning-icon"></span>Cluster Size Distribution</div>', unsafe_allow_html=True)

        cluster_sizes = filtered[filtered["cluster"] != -1].groupby("cluster").size().reset_index(name="size")

        fig_cluster = px.histogram(
            cluster_sizes,
            x="size",
            nbins=50,
            color_discrete_sequence=[YELLOW],
        )
        fig_cluster.update_layout(
            paper_bgcolor=CHARCOAL_2,
            plot_bgcolor=CHARCOAL_2,
            font=dict(color=YELLOW),
            xaxis_title="Accidents per Cluster",
            yaxis_title="Number of Clusters",
            height=350,
        )
        st.plotly_chart(fig_cluster, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ========= TAB 3: TRENDS =========
with tab3:
    if filtered.empty or "Start_Time" not in filtered.columns:
        st.warning("⚠️ Time data not available")
    else:
        if pd.api.types.is_string_dtype(filtered["Start_Time"]):
            filtered["Start_Time"] = pd.to_datetime(filtered["Start_Time"], errors="coerce")

        filtered["year"] = filtered["Start_Time"].dt.year
        filtered["month"] = filtered["Start_Time"].dt.month
        filtered["hour"] = filtered["Start_Time"].dt.hour

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span class="warning-icon"></span>Accidents by Year</div>', unsafe_allow_html=True)

            yearly = filtered.groupby("year").size().reset_index(name="accidents")
            fig_year = px.line(
                yearly,
                x="year",
                y="accidents",
                markers=True,
                line_shape="spline",
            )
            fig_year.update_traces(line=dict(color=YELLOW, width=4))
            fig_year.update_layout(
                paper_bgcolor=CHARCOAL_2,
                plot_bgcolor=CHARCOAL_2,
                font=dict(color=YELLOW),
                height=350,
            )
            st.plotly_chart(fig_year, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><span class="warning-icon"></span>Hourly Pattern (Peak Hours)</div>', unsafe_allow_html=True)

            hourly = filtered.groupby("hour").size().reset_index(name="accidents")
            fig_hour = px.bar(
                hourly,
                x="hour",
                y="accidents",
                color="accidents",
                color_continuous_scale=["#FFCA28", "#FFA000", "#FF6F00"],
            )
            fig_hour.update_layout(
                paper_bgcolor=CHARCOAL_2,
                plot_bgcolor=CHARCOAL_2,
                font=dict(color=YELLOW),
                height=350,
            )
            st.plotly_chart(fig_hour, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)


# ========= TAB 4: CLUSTER DEEP DIVE =========
with tab4:
    if filtered.empty:
        st.warning("⚠️ No data")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><span class="warning-icon"></span>Cluster Summary Table</div>', unsafe_allow_html=True)

        cluster_summary = (
            filtered[filtered["cluster"] != -1]
            .groupby("cluster")
            .agg(
                accidents=("cluster", "size"),
                avg_severity=("Severity", "mean"),
                max_severity=("Severity", "max"),
                top_state=("State", lambda x: x.value_counts().idxmax()),
                top_city=("City", lambda x: x.value_counts().idxmax()),
            )
            .sort_values("accidents", ascending=False)
            .head(30)
        )

        st.dataframe(cluster_summary, use_container_width=True, height=400)
        st.markdown("</div>", unsafe_allow_html=True)


# ========= FOOTER =========
st.markdown(f"""
<hr style="margin-top: 2rem; border-color: {BROWN_LIGHT}; border-width: 2px;">
<div style="text-align: center; padding: 1rem 0; color: {YELLOW}; font-size: 0.9rem;">
  © 2025 <span style="font-weight: 900; color: {YELLOW_LIGHT};">Geo-Pulse Analytics</span> · Developed by
  <span style="font-weight: 900;">Mayank Goyal</span><br>
  <a href="https://www.linkedin.com/in/mayank-goyal-4b8756363" target="_blank"
     style="color: {YELLOW_LIGHT}; text-decoration: none; font-weight: 800; margin-right: 16px;">LinkedIn</a>
  <a href="https://github.com/mayank-goyal09" target="_blank"
     style="color: {YELLOW_LIGHT}; text-decoration: none; font-weight: 800;">GitHub</a><br>
  <span style="font-size: 0.75rem; opacity: 0.7;">DBSCAN Spatial Clustering · Haversine Distance · 3D Hex Maps</span>
</div>
""", unsafe_allow_html=True)
