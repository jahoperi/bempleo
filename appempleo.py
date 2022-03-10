# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:48:14 2022

@author: jahop_fz60h0
"""
import json
import streamlit as st
import streamlit.components.v1 as components



#######################################################################################################

import requests  # pip install requests

from streamlit_lottie import st_lottie  # pip install streamlit-lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_hdiNFs.json")

st_lottie(lottie_hello, key = "hello")



#######################################################################################################





st.title('BUSCAMOS EMPLEO')


st.components.v1.iframe("https://onedrive.live.com/embed?resid=3a29599214725288%215671&authkey=%21AEs4fyiZIQ3_0jk&em=2&wdAllowInteractivity=False&AllowTyping=True&ActiveCell='Hoja1'!A2&wdHideHeaders=True&wdInConfigurator=True", width=900, height=600, scrolling=False)