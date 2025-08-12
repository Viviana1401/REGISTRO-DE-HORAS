# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 14:22:50 2025

@author: Vivi Rodriguez
"""

import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- CONFIGURACIÓN GOOGLE SHEETS ---
scope = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/drive"]

import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_info, scope)
client = gspread.authorize(credentials)

# Abre la hoja de cálculo
sheet = client.open("registro_horas").sheet1

# --- INTERFAZ ---
st.set_page_config(page_title="Registro de Horas", page_icon="⏱", layout="centered")
st.title("📋 Registro de Horas de Prácticas")

# Datos de entrada
nombre = st.text_input("👤 Nombre")
fecha = st.date_input("📅 Fecha", datetime.today())
horas = st.number_input("⏳ Horas trabajadas", min_value=0.0, step=0.5)
comentarios = st.text_area("📝 Comentarios", "")

if st.button("💾 Guardar registro"):
    if nombre and horas > 0:
        sheet.append_row([nombre, str(fecha), horas, comentarios])
        st.success("✅ Registro guardado correctamente.")
    else:
        st.warning("⚠️ Ingresa un nombre y horas válidas.")

# Mostrar datos registrados
st.subheader("📊 Registros existentes")
data = pd.DataFrame(sheet.get_all_records())
if not data.empty:
    st.dataframe(data)
else:
    st.info("No hay registros todavía.")





