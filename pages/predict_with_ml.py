import pandas as pd
import streamlit as st
from modules.helper import (load_dataset, 
                            gap_days, 
                            kategori_status_kolektibilitas,
                            kolektibilitas,
                            )

st.title('Prediksi Status Kolektibilitas')
with st.form("form_predict"):
            col1,col2 = st.columns(2)
            billdate = col1.date_input("Masukkan Tanggal Jatuh Tempo (Billdate)")
            pdate = col2.date_input("Masukkan Tanggal Pembayaran (Pdate)")
            
            submitted = st.form_submit_button("Predict", use_container_width=True, type="primary")
            if submitted:
                gap_days_late = gap_days(billdate, pdate)[0]
                category_kolektabilitas = kolektibilitas(gap_days_late)
                st.markdown("## Hasil Prediksi:")
                kategori_status_kolektibilitas(category_kolektabilitas)

                st.divider()
                st.markdown(f"### Chart History Setiap Cabang untuk kategori {category_kolektabilitas}")
                df = load_dataset()
                df_kolektibilitas_1 = df[df['kolektibilitas'] == category_kolektabilitas]
                branch_kolektibilitas_1 = df_kolektibilitas_1['Branch'].value_counts().sort_index()
                st.bar_chart(branch_kolektibilitas_1)
                st.balloons()
