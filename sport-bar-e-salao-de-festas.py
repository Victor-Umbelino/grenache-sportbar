import streamlit as st
import pandas as pd
import os
import tempfile
from datetime import datetime
def imagem_ao_fundo():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://delman.com.br/admin/wp-content/uploads/2020/12/IMG_0956-Copia-1024x683.jpg");
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
imagem_ao_fundo()
st.title("Reserva do Sport Bar e do Salão de Festas")
