# core packages
from utils import load_data 
import streamlit as st
from vis_function import parkingBikeTotCnt_hist, rackTotCnt_pie
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    col1, col2 = st.columns([2, 1])
    with col1:
        parkingBikeTotCnt_hist(load_data())
        
    with col2:
        rackTotCnt_pie(load_data())
    
if __name__ == "__main__":
    main()

