# Core Pkgs
from utils import load_data 
import streamlit as st 
from vis_function import showMapblue, showMapred
# sub Pkgs
from DataPreprocessing import Ddareungi25, Ddareungi200, Ddareungi0, Top10BikeStation



def main():
    choice = st.sidebar.selectbox("Menu", ["거치율 25% 미만", "거치율 200% 이상", "거치율 0%"])
    
    if choice == "거치율 25% 미만":
        st.title("거치율 25% 미만")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            df = Ddareungi25()
            st.markdown(f"### 거치율이 10% 미만인 곳은 **{len(df)}개** 입니다.")
            showMapblue(df)
        
        with col2:
            df = Ddareungi25()
            st.markdown(f"##### 거치율이 가장 낮은 대여소 Top 10")
            sorted_df = df.sort_values(by='shared').head(10)[['stationName', 'parkingBikeTotCnt', 'shared']]
            st.table(sorted_df.reset_index(drop=True))
        
        st.title("거치율이 가장 낮은 대여소 Top 10")
        df = Ddareungi25().sort_values(by='shared').head(10)
        showMapred(df)
    
    elif choice == "거치율 200% 이상":
        st.title("거치율 200% 이상")
        col1, col2 = st.columns([2, 1])
        with col1:
            df = Ddareungi200()
            st.markdown(f"### 거치율이 200%를 초과한 곳은 **{len(df)}개** 입니다.")
            showMapblue(df)
        
        with col2:
            df = Ddareungi200()
            st.markdown(f"##### 따릉이가 가장 많은 대여소 Top 10")
            sorted_df = df.sort_values(by='parkingBikeTotCnt', ascending=False).head(10)[['stationName', 'parkingBikeTotCnt', 'shared']]
            st.table(sorted_df.reset_index(drop=True))

        st.title("따릉이가 가장 많은 대여소 Top 10")
        df = Ddareungi200().sort_values(by='parkingBikeTotCnt', ascending=False).head(10)
        showMapred(df)

    elif choice == "거치율 0%":
        st.title("거치율 0%")
        col1, col2 = st.columns([2, 1])
        with col1:
            df = Ddareungi0()
            st.markdown(f"### 따릉이가 없는 곳은**{len(df)}개** 입니다.")
            showMapblue(df)
        
        with col2:
            df = Ddareungi0()
            st.markdown(f"##### 거치대가 가장 많은 대여소 Top 10")
            sorted_df = df.sort_values(by='rackTotCnt', ascending=False).head(10)[['stationName', 'rackTotCnt']]
            st.table(sorted_df.reset_index(drop=True))
        
        st.title("따릉이 없는 곳 중 거치대가 가장 많은 대여소 Top 10")
        df = Ddareungi0().sort_values(by='rackTotCnt', ascending=False).head(10)
        showMapred(df)

if __name__ == "__main__":
    main()
