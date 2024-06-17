import streamlit as st
from st_pages import show_pages_from_config
from modules.helper import load_dataset

def home_page():
    show_pages_from_config()
    st.html("<img src='/app/static/Bank_Central_Asia.svg.webp' alt='Logo Bank Central Asia' width='200'/>")
    st.title("Prediksi Tunggakan Pinjaman di Bank BCA ✨")
    st.link_button("Goto Predict", "/Prediksi%20dengan%20Machine%20Learning")
    st.divider()
    st.markdown("## Overview")

    # Show Bar Chart
    st.markdown("Chart Jumlah Transaksi per Cabang dan Status kolektibilitas dari 2017-2019")
    df = load_dataset()
    kolektibilitas_counts = df.groupby(["Branch", "kolektibilitas"]).size().unstack()
    st.bar_chart(kolektibilitas_counts)
    st.markdown("""
                Keterangan Kategori Kolektibilitas:
                - 0 atau Kol-1 (LANCAR) = Pembayaran Tepat Waktu
                - 1 atau Kol-2 (DALAM PERHATIAN KHUSUS) = Terlambat 1-90 hari sejak tanggal jatuh tempo
                - 2 atau Kol-3 (KURANG LANCAR) = Terlambat 91-120 hari sejak tanggal jatuh tempo
                - 3 atau Kol-4 (DIRAGUKAN) = Terlambat 121-180 hari sejak tanggal jatuh tempo
                - 4 atau Kol-5 (MACET) = Terlambat lebih dari 180 hari sejak tanggal jatuh tempo
                """
                )

    
