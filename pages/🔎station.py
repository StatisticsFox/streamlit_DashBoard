import streamlit as st
import pandas as pd
from utils import load_data_station
from vis_function import showMapred
def search_station(df, search_term):
    """검색어를 사용하여 station을 찾고 해당 정보를 반환하는 함수"""
    station_info = df[df['stationName'].str.contains(search_term)]
    return station_info

# Streamlit 앱 구성
def main():
    st.title('Station 검색기능')
    
    # 검색어 입력 상자
    search_term = st.text_input('검색할 stationName을 입력하세요:')
    
    if search_term:
        # 검색어를 사용하여 station 검색
        station_info = search_station(load_data_station(), search_term)
        station_infosrp = station_info[['stationName','rackTotCnt','parkingBikeTotCnt']]
        if not station_infosrp.empty:
            # 검색 결과 표시
            st.subheader('검색 결과:')
            st.write(station_infosrp)
        else:
            st.write('일치하는 station이 없습니다.')
    
    showMapred(station_info)

if __name__ == '__main__':
    main()
