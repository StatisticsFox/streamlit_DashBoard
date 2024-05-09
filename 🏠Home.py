# Core Pkgs
from utils import load_data 
import streamlit as st


def main():
    st.balloons()
    image_url = 'https://onedrive.live.com/embed?resid=9DED56BE8CF81C92%21213&authkey=%21AJTYEtR7PedRJJ4&width=868&height=404'
    st.image(image_url, caption='따릉이 데이터 닷컴', use_column_width=True)
    st.markdown("## 대시보드 개요 \n"
        "본 대시보드는 실시간으로 땨릉이 대여소 현황을 알려주는 대시보드입니다.\n"
        "현재 각 대여소에 자전거가 얼마나 거치되어 있는지 등을 나타냅니다.\n"
        "### 데이터 출처 API\n"
        "[서울시 공공자전거 실시간 대여정보](https://data.seoul.go.kr/dataList/OA-15493/A/1/datasetView.do)\n"
        "\n#### 데이터 명세는 아래와 같습니다.\n"
        """| NO | 출력 명           | 자료유형      | DataType | 데이터            | 데이터 설명                                                                            |
|----|-------------------|---------------|----------|-------------------|----------------------------------------------------------------------------------------|
| 1  | rackTotCnt        | 양적/이산형   | Double   | 거치대 개수        | 말 그대로 정거장에 설치된 거치대의 개수를 의미한다.                                     |
| 2  | stationName       | 질적/명목형   | String   | 대여소 이름        | 대여소의 이름을 의미하며 중복 데이터가 존재하지 않는다.                                 |
| 3  | parkingBikeTotCnt | 양적/이산형   | Double   | 자전거 주차 총 건 수 | 현재 거치되어 있는 자전거를 의미한다.                                                  |
| 4  | shared            | 양적/연속형   | float    | 거치율             | 현재 거치대 대비 얼마나 자전거가 거치되어 있는지 비율을 나타낸다. |
| 5  | stationLatitude   | 양적/연속형   | float    | 위도               | 대여소의 위도이다.                                                                     |
| 6  | stationLongitude  | 양적/연속형   | float    | 경도               | 대여소의 경도이다.                                                                     |
| 7  | stationId         | 질적/명목형   | String   | 대여소 ID          | 대여소마다 있는 대여소 고유 ID 이다. 대여소를 식별할 때 사용된다.                       |
""")
    st.markdown("### 데이터 미리보기 \n"
                "데이터의 일부를 미리보기 합니다.")
    df = load_data()
    st.write(df.head(10))    

if __name__ == "__main__":
    main()