import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from modules.settings import (DATASET)

@st.cache_data
def load_dataset() -> pd.DataFrame:
    df = pd.read_csv(DATASET)

    kota = [
        "01. Jakarta",
        "02. Surabaya",
        "03. Bandung",
        "04. Medan",
        "05. Bekasi",
        "06. Tangerang",
        "07. Depok",
        "08. Semarang",
        "09. Palembang",
        "10. Makassar",
        "11. Bogor",
        "12. Malang",
        "13. Yogyakarta",
        "14. Batam",
        "15. Pekanbaru",
        "16. Denpasar",
        "17. Bandar Lampung",
        "18. Padang"
    ]

    df['Branch'] = df['Branch'].apply(lambda x: kota[x - 1])
    return df

def gap_days(billdate, pdate):
    gap = billdate - pdate
    return [gap.days]

def kolektibilitas(days_late):
    if days_late >= 0:
      return 0
    elif days_late >= -90:
      return 1
    elif days_late >= -120:
      return 2
    elif days_late >= -180:
      return 3
    else:
      return 4

def kategori_status_kolektibilitas(category):
    messages = {
        0: """
            **Status: `0 Lancar`**\n
            Selamat status kolektibilitas lancar.\n
            Tidak ada indikasi masalah yang signifikan dalam kemampuan pembayaran debitur.
            """,
        1: """
            **Status: `1 Dalam Perhatian Khusus`**\n
            Adapun permasalahan sebagai berikut:\n
            - Terdapat beberapa kelemahan yang dapat mempengaruhi kemampuan debitur untuk melunasi kredit.
            - Tunggakan pembayaran pokok dan/atau bunga antara 1-90 hari sejak tanggal jatuh tempo.
            - Kondisi keuangan debitur menunjukkan beberapa masalah yang dapat menjadi lebih serius jika tidak ditangani.
            """,
        2: """
            **Status: `2 Kurang Lancar`**\n
            Adapun permasalahan sebagai berikut:\n
            - Debitur mengalami kesulitan keuangan yang signifikan yang mengganggu kemampuan membayar.
            - Tunggakan pembayaran pokok dan/atau bunga antara 91-120 hari sejak tanggal jatuh tempo.
            - Diperlukan langkah-langkah perbaikan atau restrukturisasi untuk memulihkan pembayaran.            
            """,
        3: """
            **Status: `3 Diragukan`**\n
            Adapun permasalahan sebagai berikut:\n
            - Kemampuan membayar debitur sangat diragukan.
            - Tunggakan pembayaran pokok dan/atau bunga antara 121-180 hari sejak tanggal jatuh tempo.
            - Probabilitas terjadinya kerugian cukup tinggi, dan bank harus mempertimbangkan penyisihan kerugian kredit.
            """,
        4: """
            **Status: `4 Macet `**\n
            Adapun permasalahan sebagai berikut:\n
            - Kredit dianggap tidak tertagih.
            - Tunggakan pembayaran pokok dan/atau bunga lebih dari 181 hari sejak tanggal jatuh tempo.
            - Bank harus mencadangkan kerugian kredit secara penuh untuk menutupi potensi kerugian.
            """
    }
    
    message = messages.get(category, "Kategori tidak dikenali.")
    st.markdown(message)