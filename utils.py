# -*- coding:utf-8 -*-

# Core Pkgs
import streamlit as st
import pandas as pd


def load_data():
    """데이터를 불러오는 함수"""

    data = pd.read_csv('data/seoul_bike_stations.csv')

    return data