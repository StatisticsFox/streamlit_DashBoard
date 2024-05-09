# Core Pkgs
import streamlit as st 
from streamlit_folium import st_folium
import folium

def create_popup_html(row):
    """마커 클릭 시 나타나는 팝업 HTML 생성 함수"""
    
    return f"""
    <div style="font-family: Arial; font-size: 14px;">
        <strong>{row['stationName']}</strong><br>
        현재 자전거: <strong>{row['parkingBikeTotCnt']}대</strong><br>
        거치대 개수: <strong>{row['rackTotCnt']}</strong>
    </div>
    """

def showMapblue(df):
    """데이터 프레임 내의 모든 대여소의 위치를 표시하는 함수"""
    latitude = 37.5665
    longitude = 126.9780
    map = folium.Map(location=[latitude, longitude], zoom_start=11, control_scale=True)
    for idx, row in df.iterrows():
        popup_html = create_popup_html(row)
        folium.Marker(
            location=[row['stationLatitude'], row['stationLongitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row['stationName']
        ).add_to(map)
    # Streamlit에서 지도를 표시
    st_folium(map, width=1000, height=600)


def showMapred(df):
    latitude = 37.5665
    longitude = 126.9780
    map = folium.Map(location=[latitude, longitude], zoom_start=11, control_scale=True)
    for idx, row in df.iterrows():
        popup_html = create_popup_html(row)
        folium.Marker(
            location=[row['stationLatitude'], row['stationLongitude']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row['stationName'],
            icon=folium.Icon(color='red')
        ).add_to(map)
    # Streamlit에서 지도를 표시
    st_folium(map, width=1000, height=600)

def rackTotCnt_hist(df):
    """거치대 개수 히스토그램을 표시하는 함수"""
    st.markdown("## 거치대 개수 히스토그램")
    st.bar_chart(df['rackTotCnt'].value_counts())