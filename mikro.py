import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="No Market, No Happy Lab - Bab 1",
    page_icon="⚖️",
    layout="wide"
)

# ==========================================
# SIDEBAR: IDENTITAS PENGEMBANG & KAMPUS
# ==========================================
with st.sidebar:
    # Mengatur layout 2 kolom untuk logo dan foto agar tampil sejajar & estetik
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("logounisbatrans.png", use_column_width=True)
    with col2:
        st.image("yuka.png", use_column_width=True)
    
    # Teks Identitas Pengembang
    st.caption("Dikembangkan oleh **Yuhka Sundaya**  \n*Ekonomi Pembangunan Unisba, 2026*")
    st.divider()

# ==========================================
# HEADER & UTAMA
# ==========================================
st.title("⚖️ NO MARKET, NO HAPPY LAB")
st.caption("Modul 1: Simulator Efisiensi Spesialisasi & Pertukaran Pasar")
st.markdown("---")

# ... (sisa kode simulasi ke bawah tetap sama)

# Deskripsi Pengantar
st.markdown("""
### *Coba bayangkan satu hari saja tanpa pasar...*
Di aplikasi interaktif ini, kamu bisa membandingkan berapa besar waktu dan energi yang harus dikeluarkan jika kamu harus **memproduksi semua kebutuhan sendiri (Skenario Tanpa Pasar)** dibandingkan jika kamu **fokus pada keahlianmu lalu bertransaksi di pasar (Skenario Dengan Pasar)**.
""")

# Sidebar: Input Parameter dari Mahasiswa
st.sidebar.header("⚙️ Parameter Pekerjaan & Pasar")

# Input Pekerjaan Mahasiswa/User
profesi = st.sidebar.selectbox(
    "Pilih Keahlian/Pekerjaanmu saat ini:",
    ["Pengetik Dokumen / Asisten Riset", "Pengembang Web / Programmer", "Desainer Grafis", "Guru / Tutor Les", "Barista"]
)

upah_per_jam = st.sidebar.number_input(
    "Gaji / Nilai Waktumu per Jam (Rp):",
    min_value=10000,
    max_value=500000,
    value=25000,
    step=5000
)

st.sidebar.markdown("---")
st.sidebar.header("🍽️ Target Kebutuhan: Nasi Goreng Telur")
harga_nasgor_pasar = st.sidebar.number_input(
    "Harga 1 Porsi Nasi Goreng di Pasar (Rp):",
    min_value=5000,
    max_value=100000,
    value=15000,
    step=1000
)

# Perhitungan Logika Simulasi
# Skenario 1: Tanpa Pasar (Autarki)
# Mengakumulasi jam kerja yang dibutuhkan untuk menanam padi, ternak ayam, buat minyak, dll.
waktu_tanam_padi = 60.0    # jam (estimasi olah lahan, tanam, panen untuk 1 porsi)
waktu_ternak_ayam = 25.0   # jam (rawat ayam sampai bertelur)
waktu_peras_minyak = 15.0  # jam (kebun sawit/kelapa sampai minyak)
total_waktu_tanpa_pasar = waktu_tanam_padi + waktu_ternak_ayam + waktu_peras_minyak # 100 Jam

# Skenario 2: Dengan Pasar (Spesialisasi)
# Waktu kerja yang dibutuhkan untuk membeli nasi goreng = Harga Nasgor / Upah per jam
waktu_kerja_dengan_pasar = harga_nasgor_pasar / upah_per_jam  # Dalam Jam

# Efisiensi / Penghematan Waktu
penghematan_waktu = total_waktu_tanpa_pasar - waktu_kerja_dengan_pasar
persen_efisiensi = (penghematan_waktu / total_waktu_tanpa_pasar) * 100

# Layout Tampilan Hasil Simulasi
col1, col2 = st.columns(2)

with col1:
    st.error("❌ SKENARIO A: Tanpa Pasar (Semua Bikin Sendiri)")
    st.write(f"Untuk makan **1 porsi Nasi Goreng Telur**, kamu harus:")
    st.write(f"- Menanam padi & panen beras: **{waktu_tanam_padi} jam**")
    st.write(f"- Memelihara ayam sampai bertelur: **{waktu_ternak_ayam} jam**")
    st.write(f"- Memproses kelapa jadi minyak goreng: **{waktu_peras_minyak} jam**")
    st.metric(
        label="Total Waktu Kerja yang Dibutuhkan",
        value=f"{total_waktu_tanpa_pasar:.1f} Jam",
        delta="Lelah Luar Biasa",
        delta_color="inverse"
    )

with col2:
    st.success("✅ SKENARIO B: Dengan Pasar (Spesialisasi & Bertukar)")
    st.write(f"Sebagai seorang **{profesi}** dengan tarif **Rp{upah_per_jam:,}/jam**:")
    st.write(f"- Kamu cukup bekerja selama **{waktu_kerja_dengan_pasar * 60:.1f} menit**.")
    st.write(f"- Hasil pendapatanmu (Rp{harga_nasgor_pasar:,}) kamu belikan Nasi Goreng di pasar.")
    st.write("- Kamu tidak perlu mencangkul sawah atau memelihara ayam!")
    st.metric(
        label="Total Waktu Kerja yang Dibutuhkan",
        value=f"{waktu_kerja_dengan_pasar * 60:.1f} Menit",
        delta=f"Hemat {penghematan_waktu:.1f} Jam ({persen_efisiensi:.1f}%)"
    )

st.markdown("---")

# Visualisasi Grafik Perbandingan Waktu
st.subheader("📊 Grafik Perbandingan Alokasi Waktu Kerja (Jam)")

df_chart = pd.DataFrame({
    'Skenario': ['Tanpa Pasar (Autarki)', 'Dengan Pasar (Spesialisasi)'],
    'Waktu Kerja (Jam)': [total_waktu_tanpa_pasar, waktu_kerja_dengan_pasar],
    'Warna': ['#FF4B4B', '#00C853']
})

fig = px.bar(
    df_chart, 
    x='Skenario', 
    y='Waktu Kerja (Jam)',
    color='Skenario',
    color_discrete_map={'Tanpa Pasar (Autarki)': '#FF4B4B', 'Dengan Pasar (Spesialisasi)': '#00C853'},
    text_auto='.2f',
    title="Berapa Jam Kerja yang Kamu Korbankan Hanya untuk Sepiring Nasi Goreng?"
)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# Kolom Refleksi (Therapeutical Thinking Prompts)
st.markdown("---")
st.subheader("💡 Ruang Refleksi Mahasiswa (Therapeutical Thinking)")

st.info(f"""
**Coba pikirkan hasil simulasi di atas:**
1. Tanpa pasar, kamu menghabiskan **{total_waktu_tanpa_pasar:.0f} jam** hanya untuk urusan makan satu piring nasi goreng. Apakah kamu masih punya waktu untuk belajar, bersosialisasi, atau melakukan hobi yang membuatmu bahagia?
2. Dengan adanya mekanisme pasar dan keahlianmu sebagai **{profesi}**, kamu menyisakan waktu luang sebesar **{penghematan_waktu:.1f} jam**! Apa hal paling bermakna yang akan kamu lakukan dengan sisa waktu tersebut?
3. Mengapa pasar dikatakan sebagai alat penyedia kebahagiaan (*happy*) bagi masyarakat?
""")

refleksi_user = st.text_area("Tuliskan jawaban refleksi atau pendapatmu di sini:", placeholder="Menurut saya, mekanisme pasar membantu saya karena...")

if st.button("Simpan Refleksi Saya"):
    if refleksi_user:
        st.balloons()
        st.success("Refleksi tersimpan! Kamu baru saja memahami esensi utama dari filosofi 'No Market, No Happy'.")
    else:
        st.warning("Tuliskan sedikit pendapatmu dulu sebelum menyimpan ya!")
