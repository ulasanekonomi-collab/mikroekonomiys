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
        st.image("logounisba.png", use_column_width=True)
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

# ==========================================
# HITUNG LOGIKA EMOSI DINAMIS (BERDASARKAN PENGANTAR)
# ==========================================
# Jam kerja yang dibutuhkan untuk membeli 1 porsi makanan di pasar
jam_kerja_pasar = (harga_nasgor_pasar / upah_per_jam) if upah_per_jam > 0 else 999

# Total pendapatan upah dari durasi kerja tersebut
total_upah_diterima = jam_kerja_pasar * upah_per_jam

# Klasifikasi Emosi & "Tingkat Happy" (Menyesuaikan Filosofi Pengantar)
if jam_kerja_pasar <= 0.5: # < 30 menit kerja
    mood_emoji = "🥳"
    mood_status = "Sangat Happy & Bebas!"
    energi_persen = 0.95
    pesan_emosi = "Hanya butuh beberapa menit kerja! Sisa hari penuh waktu untuk belajar, bersosialisasi, dan menikmati hidup."
elif jam_kerja_pasar <= 1.5: # 30 menit - 1.5 jam kerja
    mood_emoji = "😁"
    mood_status = "Happy & Sejahtera"
    energi_persen = 0.85
    pesan_emosi = "Spesialisasi membuat beban kerja sangat efisien. Kebutuhan dasar terpenuhi dengan mudah."
elif jam_kerja_pasar <= 4.0: # 1.5 - 4 jam kerja
    mood_emoji = "🙂"
    mood_status = "Cukup Happy / Lumayan"
    energi_persen = 0.65
    pesan_emosi = "Harus bekerja beberapa jam, tapi jauh lebih rasional dibanding memproduksi semua kebutuhan sendiri."
elif jam_kerja_pasar <= 8.0: # 4 - 8 jam kerja
    mood_emoji = "😐"
    mood_status = "Agak Lelah (Daya Beli Rendah)"
    energi_persen = 0.40
    pesan_emosi = "Nilai upah per jam relatif kecil dibanding harga pasar. Waktu untuk menikmati hidup mulai tergerus."
else: # Bekerja > 8 jam hanya untuk 1 porsi makan
    mood_emoji = "😫"
    mood_status = "Sangat Lelah & Tertekan"
    energi_persen = 0.15
    pesan_emosi = "Keterbatasan daya beli membuat pertukaran pasar terasa berat, mendekati beban kerja autarki."


# ==========================================
# LAYOUT TAMPILAN SIMULASI (SESUAI NARASI PENGANTAR)
# ==========================================
col1, col2 = st.columns(2)

with col1:
    st.error("❌ SKENARIO A: Tanpa Pasar (Autarki)")
    
    # Visualisasi Lelah Ekstrem (Hidup Tanpa Pasar)
    st.markdown("### 😫 **Kondisi Emosional: Super Lelah & Burnout**")
    st.progress(0.05)
    st.caption("🔋 Sisa Energi Hidup: 5% (Waktu Habis Hanya untuk Bertahan Hidup)")
    
    st.markdown("**Bayangkan 1 hari tanpa pasar. Untuk makan 1 porsi Nasi Goreng, Anda harus:**")
    st.write(f"- Menanam padi & panen beras: **{waktu_tanam_padi:.0f} jam**")
    st.write(f"- Memelihara ayam sampai bertelur: **{waktu_ternak_ayam:.0f} jam**")
    st.write(f"- Memproses kelapa jadi minyak: **{waktu_peras_minyak:.0f} jam**")
    st.write("- Menyiapkan kayu bakar & alat masak sendiri: **Ekstrem lelah!**")
    
    st.metric(
        label="Total Waktu Kerja yang Dikorbankan",
        value=f"{total_waktu_tanpa_pasar:.1f} Jam",
        delta="Tidak Ada Waktu Menikmati Hidup",
        delta_color="inverse"
    )

with col2:
    st.success("✅ SKENARIO B: Dengan Pasar (Spesialisasi)")
    
    # Visualisasi Dinamis "Tingkat Happy"
    st.markdown(f"### {mood_emoji} **Kondisi Emosional: {mood_status}**")
    st.progress(energi_persen)
    st.caption(f"🔋 Sisa Energi Hidup: {int(energi_persen * 100)}% — {pesan_emosi}")
    
    st.markdown(f"**Dalam sistem terspesialisasi sebagai seorang {profesi}:**")
    st.write(f"- Tarif upah kerja Anda: **Rp{upah_per_jam:,.0f} / jam**.")
    
    if jam_kerja_pasar < 1:
        st.write(f"- Durasi kerja yang dibutuhkan: **{jam_kerja_pasar * 60:.1f} menit**.")
    else:
        st.write(f"- Durasi kerja yang dibutuhkan: **{jam_kerja_pasar:.2f} jam**.")
        
    st.write(f"- Hasil upah yang diperoleh digunakan untuk membeli makanan di pasar (Rp{harga_nasgor_pasar:,.0f}).")
    st.write("- **Hasil:** Bebas dari keharusan menanam padi & ternak ayam sendiri!")
    
    st.metric(
        label="Total Waktu Kerja yang Dikorbankan",
        value=f"{jam_kerja_pasar * 60:.1f} Menit" if jam_kerja_pasar < 1 else f"{jam_kerja_pasar:.2f} Jam",
        delta=f"Hemat {total_waktu_tanpa_pasar - jam_kerja_pasar:.1f} Jam"
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

# ==========================================
# EVALUASI & KUIS REFLEKTIF INTERAKTIF
# ==========================================
st.markdown("---")
st.subheader("📝 Kuis Reflektif & Evaluasi Pemahaman")
st.caption("Uji pemahaman intuitif Anda mengenai konsep Spesialisasi, Pasar, dan Kesejahteraan.")

# Inisialisasi Form Kuis
with st.form("kuis_bab1"):
    
    # Soal 1
    st.markdown("**1. Mengapa memproduksi semua barang sendiri (tanpa pasar/autarki) cenderung membuat tingkat kesejahteraan (kebahagiaan) seseorang sangat rendah?**")
    q1 = st.radio(
        "Pilih jawaban yang paling tepat:",
        [
            "A. Karena waktu dan energi habis hanya untuk memenuhi kebutuhan dasar sederhana.",
            "B. Karena tidak ada orang yang mau memuji hasil produksi sendiri.",
            "C. Karena harga bahan baku di alam selalu lebih mahal daripada di pasar.",
            "D. Karena pemerintah melarang masyarakat memproduksi barang sendiri."
        ],
        index=None,
        key="q1"
    )
    
    st.markdown("---")
    
    # Soal 2
    st.markdown("**2. Berdasarkan hasil simulasi di atas, apa fungsi paling mendasar dari keberadaan pasar bagi kehidupan masyarakat modern?**")
    q2 = st.radio(
        "Pilih jawaban yang paling tepat:",
        [
            "A. Tempat berkumpulnya para pedagang untuk menaikkan harga barang sesuka hati.",
            "B. Mekanisme koordinasi yang memungkinkan manusia melakukan spesialisasi dan bertukar hasil kerja.",
            "C. Satu-satunya tempat bagi pemerintah untuk memungut pajak transaksi.",
            "D. Alat untuk memaksa semua orang memiliki pekerjaan yang sama."
        ],
        index=None,
        key="q2"
    )
    
    st.markdown("---")

    # Soal 3
    st.markdown("**3. Jika upah/nilai waktu seseorang meningkat, apakah yang terjadi pada efisiensi penggunaan pasar dalam memenuhi kebutuhan hidupnya?**")
    q3 = st.radio(
        "Pilih jawaban yang paling tepat:",
        [
            "A. Pasar menjadi tidak berguna karena uangnya sudah terlalu banyak.",
            "B. Efisiensi pertukaran pasar makin tinggi karena waktu kerjanya untuk membeli suatu barang menjadi makin singkat.",
            "C. Lebih baik ia kembali menanam padi sendiri agar hemat pengeluaran.",
            "D. Kebutuhan barangnya di pasar otomatis berkurang secara drastis."
        ],
        index=None,
        key="q3"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit_kuis = st.form_submit_button("🎯 Periksa Jawaban Saya")

# Logika Penilaian & Pembahasan
if submit_kuis:
    if q1 is None or q2 is None or q3 is None:
        st.warning("⚠️ Harap jawab semua pertanyaan terlebih dahulu sebelum memeriksa skor!")
    else:
        skor = 0
        
        # Cek Soal 1 (Jawaban Benar: A)
        ans1_correct = q1.startswith("A")
        if ans1_correct: skor += 100/3
        
        # Cek Soal 2 (Jawaban Benar: B)
        ans2_correct = q2.startswith("B")
        if ans2_correct: skor += 100/3
        
        # Cek Soal 3 (Jawaban Benar: B)
        ans3_correct = q3.startswith("B")
        if ans3_correct: skor += 100/3
        
        # Tampilan Skor
        st.markdown("---")
        st.subheader("📊 Hasil Evaluasi Anda")
        
        if skor == 100:
            st.balloons()
            st.success(f"🎉 **Skor Anda: 100 / 100** — Luar biasa! Anda telah memahami filosofi utama 'No Market, No Happy' dengan sangat sempurna!")
        elif skor >= 60:
            st.info(f"👍 **Skor Anda: {skor:.0f} / 100** — Bagus! Pemahaman Anda tentang fungsi pasar sudah cukup matang.")
        else:
            st.error(f"💡 **Skor Anda: {skor:.0f} / 100** — Tetap semangat! Coba cermati kembali grafik simulasi di atas dan baca ulang pembahasannya.")
            
        # Detail Pembahasan
        with st.expander("🔍 **Lihat Pembahasan Kuis**", expanded=True):
            st.write("**Pembahasan Soal 1:**")
            if ans1_correct:
                st.markdown("✅ **Benar!** Tanpa pasar, waktu 100+ jam habis hanya untuk sepiring makanan dasar. Tidak ada sisa waktu untuk mengembangkan potensi diri atau menikmati hidup.")
            else:
                st.markdown("❌ **Kurang Tepat.** Jawaban benar adalah **A**. Keterbatasan waktu dan keahlian manusia membuat sistem tanpa pasar (*autarki*) sangat tidak efisien.")
                
            st.write("**Pembahasan Soal 2:**")
            if ans2_correct:
                st.markdown("✅ **Benar!** Pasar adalah institusi sosial tempat mempertemukan hasil spesialisasi kerja jutaan manusia agar saling melengkapi.")
            else:
                st.markdown("❌ **Kurang Tepat.** Jawaban benar adalah **B**. Pasar berfungsi sebagai alat koordinasi pertukaran hasil kerja secara masif.")
                
            st.write("**Pembahasan Soal 3:**")
            if ans3_correct:
                st.markdown("✅ **Benar!** Makin tinggi produktivitas/upah Anda per jam, makin singkat waktu kerja yang Anda butuhkan untuk membeli barang di pasar. Sisa waktu Anda untuk menikmati kebahagiaan (*happy*) makin melimpah.")
            else:
                st.markdown("❌ **Kurang Tepat.** Jawaban benar adalah **B**. Kenaikan produktivitas meningkatkan nilai daya beli waktu Anda terhadap barang pasar.")
