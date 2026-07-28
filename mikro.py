import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="No Market, No Happy - Interactive Lab",
    page_icon="⚖️",
    layout="wide"
)

# ==========================================
# SIDEBAR: NAVIGASI MENU BAB & IDENTITAS
# ==========================================
with st.sidebar:
    # Identitas Pengembang & Kampus
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("logounisbatrans.jpg", use_container_width=True)
    with col2:
        st.image("yuka.png", use_container_width=True)
    
    st.caption("Dikembangkan oleh **Yuhka Sundaya**  \n*Ekonomi Pembangunan Unisba, 2026*")
    st.divider()
    
    # MENU NAVIGASI DASHBOARD
    st.header("📚 Navigasi Modul Buku")
    menu_pilihan = st.radio(
        "Pilih Bab / Modul Belajar:",
        [
            "📖 Pengantar: Filosofi Pasar & Spesialisasi",
            "📖 Bab 1: No Market, No Happy (Keputusan & Anggaran)",
            "📖 Bab 2: Ekspresi Masyarakat Konsumen (Kurva Indiferensi)",
            "📖 Bab 3: Garis Anggaran & Batas Pilihan (Coming Soon)"
        ]
    )
    st.divider()


# ==========================================
# MENU 1: PENGANTAR (FILOSOFI PASAR & SPESIALISASI)
# ==========================================
if menu_pilihan == "📖 Pengantar: Filosofi Pasar & Spesialisasi":
    st.title("⚖️ PENGANTAR: FILOSOFI PASAR & SPESIALISASI")
    st.caption("Simulator Efisiensi Waktu: Autarki (Tanpa Pasar) vs Spesialisasi (Dengan Pasar)")
    st.markdown("---")

    # Input Parameter khusus Pengantar
    st.sidebar.subheader("⚙️ Parameter Modul Pengantar")
    profesi = st.sidebar.selectbox(
        "Pilih Keahlian/Pekerjaan Anda:",
        ["Pengetik / Asisten Riset", "Programmer / Pengembang Web", "Desainer Grafis", "Tutor Les", "Barista"]
    )
    upah_per_jam = st.sidebar.number_input("Tarif Upah per Jam (Rp):", min_value=5000, value=25000, step=5000)
    harga_nasgor_pasar = st.sidebar.number_input("Harga 1 Porsi Nasi Goreng (Rp):", min_value=5000, value=15000, step=1000)

    # Perhitungan
    waktu_tanam_padi = 60.0
    waktu_ternak_ayam = 25.0
    waktu_peras_minyak = 15.0
    total_waktu_tanpa_pasar = 100.0
    
    jam_kerja_pasar = (harga_nasgor_pasar / upah_per_jam) if upah_per_jam > 0 else 999
    total_upah_diterima = jam_kerja_pasar * upah_per_jam

    # Emosi Dinamis
    if jam_kerja_pasar <= 0.5:
        mood_emoji, mood_status, energi_persen, pesan_emosi = "🥳", "Sangat Happy & Bebas!", 0.95, "Sisa waktu penuh kebebasan untuk belajar & menikmati hidup."
    elif jam_kerja_pasar <= 1.5:
        mood_emoji, mood_status, energi_persen, pesan_emosi = "😁", "Happy & Sejahtera", 0.85, "Spesialisasi membuat beban kerja sangat efisien."
    elif jam_kerja_pasar <= 4.0:
        mood_emoji, mood_status, energi_persen, pesan_emosi = "🙂", "Cukup Happy / Lumayan", 0.65, "Jauh lebih rasional dibanding memproduksi semua sendiri."
    else:
        mood_emoji, mood_status, energi_persen, pesan_emosi = "😫", "Sangat Lelah & Tertekan", 0.15, "Daya beli upah terlalu rendah."

    # Tampilan Simulasi Pengantar
    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ SKENARIO A: Tanpa Pasar (Autarki)")
        st.markdown("### 😫 **Kondisi Emosional: Super Lelah & Burnout**")
        st.progress(0.05)
        st.caption("🔋 Sisa Energi Hidup: 5% (Terjebak Kerja Fisik Seharian)")
        st.write("Untuk makan **1 porsi Nasi Goreng**, Anda harus:")
        st.write(f"- Menanam padi & panen beras: **{waktu_tanam_padi:.0f} jam**")
        st.write(f"- Memelihara ayam sampai bertelur: **{waktu_ternak_ayam:.0f} jam**")
        st.write(f"- Memproses kelapa jadi minyak: **{waktu_peras_minyak:.0f} jam**")
        st.metric("Total Waktu Kerja Dikorbankan", f"{total_waktu_tanpa_pasar:.1f} Jam", delta="Tidak Ada Waktu Bersantai", delta_color="inverse")

    with col2:
        st.success("✅ SKENARIO B: Dengan Pasar (Spesialisasi)")
        st.markdown(f"### {mood_emoji} **Kondisi Emosional: {mood_status}**")
        st.progress(energi_persen)
        st.caption(f"🔋 Sisa Energi Hidup: {int(energi_persen * 100)}% — {pesan_emosi}")
        st.write(f"Sebagai seorang **{profesi}** dengan upah **Rp{upah_per_jam:,.0f}/jam**:")
        st.write(f"- Cukup bekerja selama **{jam_kerja_pasar * 60:.1f} menit** ({jam_kerja_pasar:.2f} jam).")
        st.write(f"- Hasil upah (**Rp{total_upah_diterima:,.0f}**) digunakan membeli porsi nasi goreng di pasar.")
        st.metric("Total Waktu Kerja Dikorbankan", f"{jam_kerja_pasar * 60:.1f} Menit" if jam_kerja_pasar < 1 else f"{jam_kerja_pasar:.2f} Jam", delta=f"Hemat {total_waktu_tanpa_pasar - jam_kerja_pasar:.1f} Jam")


# ==========================================
# MENU 2: BAB 1 (NO MARKET, NO HAPPY - KEPUTUSAN & ANGGARAN)
# ==========================================
elif menu_pilihan == "📖 Bab 1: No Market, No Happy (Keputusan & Anggaran)":
    st.title("🍜 BAB 1: NO MARKET, NO HAPPY")
    st.caption("Simulator Keterbatasan Anggaran & Trade-off Mahasiswa di Kelas Jam 10 Pagi")
    st.markdown("---")

    st.markdown("""
    > *"Jam menunjukkan pukul 10 pagi. Kamu sedang duduk di kelas. Dosen menjelaskan materi, tapi perut mulai lapar. Di dompet tersisa saldo **Rp 22.500**. Apa keputusan ekonomimu?"*
    """)

    # Sidebar Parameter Bab 1
    st.sidebar.subheader("⚙️ Parameter Dompet & Pilihan")
    saldo = st.sidebar.number_input("Saldo Dompet / E-Wallet (Rp):", min_value=5000, value=22500, step=2500)[cite: 1]
    
    st.subheader("🛒 Tentukan Kombinasi Pilihan Konsumsi Anda:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        porsi_makanan = st.slider("Jumlah Porsi Makanan (Mie Pedas / Ayam Geprek @ Rp15.000):", 0, 3, 1)[cite: 1]
    with col_b:
        paket_data = st.slider("Paket Data Internet (GB) (@ Rp7.500/GB):", 0, 5, 1)[cite: 1]

    # Hitung Pengeluaran
    total_belanja = (porsi_makanan * 15000) + (paket_data * 7500)
    sisa_saldo = saldo - total_belanja

    # Display Hasil Keputusan
    st.markdown("---")
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Total Saldo", f"Rp {saldo:,.0f}")[cite: 1]
    col_m2.metric("Total Pengeluaran", f"Rp {total_belanja:,.0f}")
    
    if sisa_saldo >= 0:
        col_m3.metric("Sisa Saldo Dompet", f"Rp {sisa_saldo:,.0f}", delta="Anggaran Cukup")
        st.success(f"🎉 **Keputusan Layak (Feasible)!** Anda mendapatkan {porsi_makanan} porsi makanan dan {paket_data} GB paket data. Perut kenyang, tugas kuliah tetap jalan!"[cite: 1])
    else:
        col_m3.metric("Defisit Anggaran", f"Rp {sisa_saldo:,.0f}", delta="Anggaran Tidak Cukup", delta_color="inverse")
        st.error("⚠️ **Keputusan Tidak Layak!** Pilihan Anda melebihi saldo dompet Rp22.500. Silakan kurangi porsi makan atau paket data!"[cite: 1])

    # Kuis Reflektif Bab 1
    st.markdown("---")
    st.subheader("📝 Kuis Reflektif Bab 1")
    with st.form("kuis_bab1"):
        q1 = st.radio(
            "Mengapa saat saldo Rp22.500 Anda tidak memilih ngopi di café modern?",[cite: 1]
            [
                "A. Karena tidak suka kopi.",
                "B. Karena adanya keterbatasan anggaran (budget constraint) yang memaksa adanya trade-off.",[cite: 1]
                "C. Karena café ditutup oleh pemerintah."
            ]
        )
        if st.form_submit_button("Cek Jawaban"):
            if q1.startswith("B"):
                st.success("✅ **Benar!** Keterbatasan anggaran membuat kita harus membuat keputusan prioritas."[cite: 1])
            else:
                st.error("❌ **Kurang tepat.** Jawaban yang benar adalah B (Keterbatasan Anggaran)."[cite: 1])


# ==========================================
# MENU 3: BAB 2 (EKSPRESI MASYARAKAT KONSUMEN)
# ==========================================
elif menu_pilihan == "📖 Bab 2: Ekspresi Masyarakat Konsumen (Kurva Indiferensi)":
    st.title("📈 BAB 2: EKSPRESI MASYARAKAT KONSUMEN")
    st.caption("Modul Simulasi Kurva Indiferensi & Peta Kebahagiaan Konsumen")
    st.markdown("---")
    st.info("🚧 Modul Bab 2 siap dikembangkan! Kita akan membuat kurva melengkung (Indifference Curve) dan garis anggaran interaktif di sini.")

else:
    st.title("🚧 MODUL DALAM PENGEMBANGAN")
    st.write("Modul bab ini akan segera dibuka seiring berjalannya penulisan naskah buku.")
