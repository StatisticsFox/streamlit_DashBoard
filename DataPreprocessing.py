# Core Pkgs
import pandas as pd 
from utils import load_data 

def Ddareungi25():
    """거치율이 10% 미만인 대여소만 필터링한 데이터프레임을 반환하는 함수"""

    df = load_data()
    filtered_df = df[(df['shared'] <= 10) & (df['shared'] != 0)]
    return filtered_df

def Ddareungi200():
    """거치율이 200% 이상인 대여소만 필터링한 데이터프레임을 반환하는 함수"""

    df = load_data()
    filtered_df = df[df['shared'] >= 200]
    return filtered_df

def Ddareungi0():
    """거치율이 0%인 대여소만 필터링한 데이터프레임을 반환하는 함수"""

    df = load_data()
    filtered_df = df[df['shared'] == 0]
    return filtered_df

def justlatlang():
    """위도, 경도, 대여소명 만 필터링한 데이터프레임을 반환하는 함수"""
    df = load_data()
    filtered_df = df[['stationName','stationLatitude','stationLongitude']]
    return filtered_df

### Idnicators functions    
def Top10BikeStation():
    """따릉이 거치율 25%이하 대여소 중 따릉이 개수가 가장 적은 Top 10을 반환하는 함수"""
    df = load_data()

    df = df[df['shared'] < 25][['stationName','parkingBikeTotCnt']].head(10)
    top10_df = df.sort_values(by='parkingBikeTotCnt', ascending=False).head(10)
    return top10_df
