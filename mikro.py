import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Laboratorium Ekonomi Mikro - No Market No Happy",
    page_icon="⚖️",
    layout="wide"
)

# ==========================================
# SIDEBAR: IDENTITAS & NAVIGASI BAB
# ==========================================
with st.sidebar:
    # 1. Identitas Pengembang & Kampus
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("logounisba.png", use_container_width=True)
    with col2:
        st.image("yuka.png", use_container_width=True)
    
    st.caption("Dikembangkan oleh **Yuhka Sundaya**  \n*Ekonomi Pembangunan Unisba, 2026*")
    st.divider()

    # 2. Menu Navigasi Modul / Bab (Dicadangkan Sampai Bab 20)
    st.subheader("📚 Pilih Modul Pembelajaran")
    
    daftar_bab = [
        "Pengantar: Filosofi No Market No Happy",
        "Bab 1: Pilihan Konsumen & Keterbatasan Anggaran",
        "Bab 2: Ekspresi Masyarakat Konsumen",
        "Bab 3: Ketika Kebahagiaan Dibatasi Garis Anggaran",
        "Bab 4: Ketika Konsumen Menemukan Pilihan Terbaik",
        "Bab 5: Ketika Pendapatan Berubah",
        "Bab 6: [Cadangan Bab 6]",
        "Bab 7: [Cadangan Bab 7]",
        "Bab 8: [Cadangan Bab 8]",
        "Bab 9: [Cadangan Bab 9]",
        "Bab 10: [Cadangan Bab 10]",
        "Bab 11: [Cadangan Bab 11]",
        "Bab 12: [Cadangan Bab 12]",
        "Bab 13: [Cadangan Bab 13]",
        "Bab 14: [Cadangan Bab 14]",
        "Bab 15: [Cadangan Bab 15]",
        "Bab 16: [Cadangan Bab 16]",
        "Bab 17: [Cadangan Bab 17]",
        "Bab 18: [Cadangan Bab 18]",
        "Bab 19: [Cadangan Bab 19]",
        "Bab 20: [Cadangan Bab 20]",
    ]
    
    pilihan_modul = st.selectbox("Navigasi Bab:", daftar_bab)
    st.divider()

# ==========================================
# HALAMAN 1: PENGANTAR (FILOSOFI NO MARKET NO HAPPY)
# ==========================================
if pilihan_modul == "Pengantar: Filosofi No Market No Happy":
    st.title("⚖️ PENGANTAR: NO MARKET, NO HAPPY LAB")
    st.caption("Modul Simulasi Efisiensi Spesialisasi & Pertukaran Pasar")
    st.markdown("---")
    
    # Input Parameter Khusus Pengantar
    st.sidebar.header("⚙️ Parameter Pengantar")
    profesi = st.sidebar.selectbox(
        "Keahlian/Pekerjaan di Pasar:",
        ["Pengetik Dokumen / Asisten Riset", "Pengembang Web / Programmer", "Desainer Grafis", "Guru / Tutor Les", "Barista"]
    )
    upah_per_jam = st.sidebar.number_input("Upah/Nilai Waktu per Jam (Rp):", min_value=5000, value=25000, step=5000)
    harga_nasgor_pasar = st.sidebar.number_input("Harga 1 Porsi Nasi Goreng (Rp):", min_value=5000, value=15000, step=1000)

    # Perhitungan
    waktu_tanam_padi = 60.0
    waktu_ternak_ayam = 25.0
    waktu_peras_minyak = 15.0
    total_waktu_tanpa_pasar = waktu_tanam_padi + waktu_ternak_ayam + waktu_peras_minyak # 100 Jam

    jam_kerja_pasar = (harga_nasgor_pasar / upah_per_jam) if upah_per_jam > 0 else 999
    total_upah_diterima = jam_kerja_pasar * upah_per_jam

    # Logic Mood
    if jam_kerja_pasar <= 0.5:
        mood_emoji, mood_status, energi_persen = "🥳", "Sangat Happy & Bebas!", 0.95
        pesan_emosi = "Hanya butuh beberapa menit kerja! Sisa hari penuh waktu untuk belajar, bersosialisasi, dan menikmati hidup."
    elif jam_kerja_pasar <= 1.5:
        mood_emoji, mood_status, energi_persen = "😁", "Happy & Sejahtera", 0.85
        pesan_emosi = "Spesialisasi membuat beban kerja sangat efisien."
    elif jam_kerja_pasar <= 4.0:
        mood_emoji, mood_status, energi_persen = "🙂", "Cukup Happy", 0.65
        pesan_emosi = "Harus bekerja beberapa jam, tapi jauh lebih rasional dibanding memproduksi semua kebutuhan sendiri."
    elif jam_kerja_pasar <= 8.0:
        mood_emoji, mood_status, energi_persen = "😐", "Agak Lelah", 0.40
        pesan_emosi = "Nilai upah per jam relatif kecil dibanding harga pasar."
    else:
        mood_emoji, mood_status, energi_persen = "😫", "Sangat Lelah & Tertekan", 0.15
        pesan_emosi = "Daya beli upah terlalu rendah."

    # Tampilan Layar Utama Pengantar
    col1, col2 = st.columns(2)
    with col1:
        st.error("❌ SKENARIO A: Tanpa Pasar (Autarki)")
        st.markdown("### 😫 **Kondisi Emosional: Super Lelah & Burnout**")
        st.progress(0.05)
        st.caption("🔋 Sisa Energi Hidup: 5% (Waktu Habis Hanya untuk Bertahan Hidup)")
        st.write(f"- Menanam padi & panen beras: **{waktu_tanam_padi:.0f} jam**")
        st.write(f"- Memelihara ayam sampai bertelur: **{waktu_ternak_ayam:.0f} jam**")
        st.write(f"- Memproses kelapa jadi minyak: **{waktu_peras_minyak:.0f} jam**")
        st.metric("Total Waktu Kerja Dikorbankan", f"{total_waktu_tanpa_pasar:.1f} Jam")

    with col2:
        st.success("✅ SKENARIO B: Dengan Pasar (Spesialisasi)")
        st.markdown(f"### {mood_emoji} **Kondisi Emosional: {mood_status}**")
        st.progress(energi_persen)
        st.caption(f"🔋 Sisa Energi Hidup: {int(energi_persen * 100)}% — {pesan_emosi}")
        st.write(f"Sebagai seorang **{profesi}** dengan upah **Rp{upah_per_jam:,.0f}/jam**:")
        st.write(f"- Durasi kerja yang dibutuhkan: **{jam_kerja_pasar * 60:.1f} menit**." if jam_kerja_pasar < 1 else f"- Durasi kerja: **{jam_kerja_pasar:.2f} jam**.")
        st.write(f"- Hasil upah (**Rp{total_upah_diterima:,.0f}**) digunakan membeli makanan di pasar (Rp{harga_nasgor_pasar:,.0f}).")
        st.metric("Total Waktu Kerja Dikorbankan", f"{jam_kerja_pasar * 60:.1f} Menit" if jam_kerja_pasar < 1 else f"{jam_kerja_pasar:.2f} Jam")

# ==========================================
# HALAMAN 2: BAB 1 (PILIHAN KONSUMEN & SALDO 22.500)
# ==========================================
elif pilihan_modul == "Bab 1: Pilihan Konsumen & Keterbatasan Anggaran":
    st.title("🍜 BAB 1: KEPUTUSAN KONSUMEN & KETERBATASAN ANGGARAN")
    st.caption("Studi Kasus: Mahasiswa Kelas Pukul 10 Pagi dengan Saldo Rp22.500")
    st.markdown("---")
    
    st.sidebar.header("⚙️ Parameter Bab 1")
    saldo_mahasiswa = st.sidebar.number_input("Saldo e-Wallet / Uang Saku (Rp):", value=22500, step=500)
    
    st.subheader("💡 Simulasi Keputusan Kombinasi Konsumsi")
    st.write(f"Dengan saldo sebesar **Rp{saldo_mahasiswa:,.0f}**, kamu dihadapkan pada pilihan kebutuhan perut vs kebutuhan tugas kuliah:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🍜 **Pilihan 1: Mie Pedas + Paket Data**")
        st.write("- Mie Pedas: Rp15.000")
        st.write("- Paket Data Kategori Kecil: Rp7.500")
        st.write("**Total:** Rp22.500")
        if saldo_mahasiswa >= 22500:
            st.success("✅ **Terjangkau!** (Perut Kenyang + Tugas Kuliah Jalan)")
        else:
            st.error("❌ Saldo Tidak Cukup")
            
    with col2:
        st.info("🍗 **Pilihan 2: Ayam Geprek + Es Teh**")
        st.write("- Ayam Geprek + Nasi: Rp18.000")
        st.write("- Es Teh Manis: Rp4.500")
        st.write("**Total:** Rp22.500")
        if saldo_mahasiswa >= 22500:
            st.success("✅ **Terjangkau!** (Perut Sangat Kenyang, Tugas Buka Wi-Fi Kampus)")
        else:
            st.error("❌ Saldo Tidak Cukup")

    with col3:
        st.warning("☕ **Pilihan 3: Ngopi di Café Modern**")
        st.write("- Kopi Latte: Rp35.000")
        st.write("- Pastry: Rp20.000")
        st.write("**Total:** Rp55.000")
        if saldo_mahasiswa >= 55000:
            st.success("✅ Terjangkau")
        else:
            st.error("❌ **Tidak Terjangkau!** (Mengharuskan Trade-Off / Menunda)")

# ==========================================
# HALAMAN 3: BAB 2 (SIAP DIISI)
# ==========================================
elif pilihan_modul == "Bab 2: Ekspresi Masyarakat Konsumen":
    st.title("📈 BAB 2: EKSPRESI MASYARAKAT KONSUMEN")
    st.caption("Modul Kurva Indiferensi & Konsep Utility")
    st.info("🚧 **Modul Bab 2 siap kita kembangkan!** Silakan input parameter atau konsep teori yang ingin disimulasikan.")

# ==========================================
# HALAMAN CADANGAN: BAB 3 SAMPAI BAB 20
# ==========================================
else:
    st.title(f"📦 {pilihan_modul}")
    st.info(" Modul ini telah dicadangkan dalam struktur laboratorium dan siap diisi materi simulasi selanjutnya.")
