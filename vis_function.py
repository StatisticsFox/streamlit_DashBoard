# Core Pkgs
import streamlit as st 
from streamlit_folium import st_folium
import folium
import matplotlib.pyplot as plt

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

def parkingBikeTotCnt_hist(df):
    """따릉이 개수 히스토그램을 표시하는 함수"""
    st.markdown("#### 따릉이 개수 히스토그램")
    hist_data = df['parkingBikeTotCnt'].value_counts().sort_index()
    st.bar_chart(hist_data)

def rackTotCnt_pie(df):
    """거치대 개수를 파이차트로 나타내는 함수"""
    st.markdown("#### 거치대 개수 파이차트")
    pie_data = df['rackTotCnt'].value_counts()
    
    # 파이 차트 그리기
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Streamlit에 그래프 추가
    st.pyplot(fig)
