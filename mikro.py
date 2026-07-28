import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

    # Perhitungan Logika Simulasi
    waktu_tanam_padi = 60.0
    waktu_ternak_ayam = 25.0
    waktu_peras_minyak = 15.0
    total_waktu_tanpa_pasar = waktu_tanam_padi + waktu_ternak_ayam + waktu_peras_minyak # 100 Jam

    jam_kerja_pasar = (harga_nasgor_pasar / upah_per_jam) if upah_per_jam > 0 else 999
    total_upah_diterima = jam_kerja_pasar * upah_per_jam

    # Klasifikasi Emosi & "Tingkat Happy"
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
        st.write("- Menyiapkan kayu bakar & alat masak sendiri: **Ekstrem lelah!**")
        st.metric("Total Waktu Kerja Dikorbankan", f"{total_waktu_tanpa_pasar:.1f} Jam")

    with col2:
        st.success("✅ SKENARIO B: Dengan Pasar (Spesialisasi)")
        st.markdown(f"### {mood_emoji} **Kondisi Emosional: {mood_status}**")
        st.progress(energi_persen)
        st.caption(f"🔋 Sisa Energi Hidup: {int(energi_persen * 100)}% — {pesan_emosi}")
        st.write(f"Sebagai seorang **{profesi}** dengan upah **Rp{upah_per_jam:,.0f}/jam**:")
        st.write(f"- Durasi kerja yang dibutuhkan: **{jam_kerja_pasar * 60:.1f} menit**." if jam_kerja_pasar < 1 else f"- Durasi kerja: **{jam_kerja_pasar:.2f} jam**.")
        st.write(f"- Hasil upah yang diperoleh (**Rp{total_upah_diterima:,.0f}**) digunakan membeli makanan di pasar (Rp{harga_nasgor_pasar:,.0f}).")
        st.write("- **Hasil:** Bebas dari keharusan menanam padi & ternak ayam sendiri!")
        st.metric("Total Waktu Kerja Dikorbankan", f"{jam_kerja_pasar * 60:.1f} Menit" if jam_kerja_pasar < 1 else f"{jam_kerja_pasar:.2f} Jam")

    # Grafik Visualisasi Perbandingan
    st.markdown("---")
    st.subheader("📊 Grafik Perbandingan Alokasi Waktu Kerja (Jam)")
    df_chart = pd.DataFrame({
        'Skenario': ['Tanpa Pasar (Autarki)', 'Dengan Pasar (Spesialisasi)'],
        'Waktu Kerja (Jam)': [total_waktu_tanpa_pasar, jam_kerja_pasar]
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

    # KUIS EVALUASI PENGANTAR
    st.markdown("---")
    st.subheader("📝 Kuis Reflektif & Evaluasi Pemahaman (Pengantar)")
    st.caption("Uji pemahaman intuitif Anda mengenai konsep Spesialisasi, Pasar, dan Kesejahteraan.")

    with st.form("kuis_pengantar"):
        st.markdown("**1. Mengapa memproduksi semua barang sendiri (tanpa pasar/autarki) cenderung membuat tingkat kesejahteraan seseorang sangat rendah?**")
        q1 = st.radio(
            "Pilih jawaban yang tepat:",
            [
                "A. Karena waktu dan energi habis hanya untuk memenuhi kebutuhan dasar sederhana.",
                "B. Karena tidak ada orang yang mau memuji hasil produksi sendiri.",
                "C. Karena harga bahan baku di alam selalu lebih mahal daripada di pasar.",
                "D. Karena pemerintah melarang masyarakat memproduksi barang sendiri."
            ],
            index=None, key="pq1"
        )
        st.markdown("---")
        st.markdown("**2. Berdasarkan hasil simulasi di atas, apa fungsi paling mendasar dari keberadaan pasar?**")
        q2 = st.radio(
            "Pilih jawaban yang tepat:",
            [
                "A. Tempat berkumpulnya para pedagang untuk menaikkan harga barang sesuka hati.",
                "B. Mekanisme koordinasi yang memungkinkan manusia melakukan spesialisasi dan bertukar hasil kerja.",
                "C. Satu-satunya tempat bagi pemerintah untuk memungut pajak transaksi.",
                "D. Alat untuk memaksa semua orang memiliki pekerjaan yang sama."
            ],
            index=None, key="pq2"
        )
        st.markdown("---")
        st.markdown("**3. Jika upah/nilai waktu seseorang meningkat, apakah yang terjadi pada efisiensi penggunaan pasar?**")
        q3 = st.radio(
            "Pilih jawaban yang tepat:",
            [
                "A. Pasar menjadi tidak berguna karena uangnya sudah terlalu banyak.",
                "B. Efisiensi pertukaran pasar makin tinggi karena waktu kerjanya untuk membeli suatu barang menjadi makin singkat.",
                "C. Lebih baik ia kembali menanam padi sendiri agar hemat pengeluaran.",
                "D. Kebutuhan barangnya di pasar otomatis berkurang secara drastis."
            ],
            index=None, key="pq3"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        submit_kuis = st.form_submit_button("🎯 Periksa Jawaban Saya")

    if submit_kuis:
        if q1 is None or q2 is None or q3 is None:
            st.warning("⚠️ Harap jawab semua pertanyaan terlebih dahulu!")
        else:
            skor = 0
            if q1.startswith("A"): skor += 100/3
            if q2.startswith("B"): skor += 100/3
            if q3.startswith("B"): skor += 100/3
            
            if skor == 100:
                st.balloons()
                st.success("🎉 **Skor Anda: 100 / 100** — Luar biasa! Pemahaman Anda sangat sempurna!")
            else:
                st.info(f"👍 **Skor Anda: {skor:.0f} / 100** — Tetap semangat dan tinjau kembali pembahasannya!")

# ==========================================
# HALAMAN 2: BAB 1 (PILIHAN KONSUMEN & KETERBATASAN ANGGARAN)
# ==========================================
elif pilihan_modul == "Bab 1: Pilihan Konsumen & Keterbatasan Anggaran":
    st.title("🍜 BAB 1: KEPUTUSAN KONSUMEN & KETERBATASAN ANGGARAN")
    st.caption("Modul Simulasi Sirkulasi Pasar, Anggaran Rp22.500, dan Ekspresi Kepuasan Konsumen")
    st.markdown("---")
    
    st.subheader("🔄 Ilustrasi Arus Melingkar Pasar (Circular Flow of Market)")
    st.write("Pasar mempertemukan 3 elemen utama dalam keputusan ekonomi harianmu:")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric(label="💰 1. UANG (Anggaran/Saldo)", value="Rp 22.500", delta="Keterbatasan Sumber Daya")
    with col_b:
        st.metric(label="🛍️ 2. PASAR (Mekanisme Transaksi)", value="Kantin / App Digital", delta="Pertukaran Efisien")
    with col_c:
        st.metric(label="📦 3. BARANG & JASA", value="Makanan & Internet", delta="Pemenuhan Kebutuhan")
        
    st.markdown("---")

    st.subheader("📊 Simulator Alokasi Anggaran & Ekspresi Kebahagiaan")
    
    st.sidebar.header("⚙️ Parameter Bab 1")
    saldo_mahasiswa = st.sidebar.number_input("Saldo e-Wallet (Rp):", min_value=5000, value=22500, step=1000)
    
    st.write("Atur alokasi pembagian uang sakumu untuk **Makanan** dan **Paket Data**:")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        biaya_makan = st.slider("Pengeluaran untuk Makanan (Rp):", min_value=0, max_value=int(saldo_mahasiswa), value=15000, step=2500)
    with col_input2:
        biaya_data = st.slider("Pengeluaran untuk Paket Data (Rp):", min_value=0, max_value=int(saldo_mahasiswa), value=7500, step=2500)
        
    total_pengeluaran = biaya_makan + biaya_data
    sisa_saldo = saldo_mahasiswa - total_pengeluaran

    if total_pengeluaran > saldo_mahasiswa:
        ekspresi_emoji = "😫"
        status_kepuasan = "Overbudget! Defisit / Saldo Tidak Cukup"
        penjelasan_ekspresi = "Uang sakumu tidak mencukupi kombinasi ini. Kamu harus mengorbankan salah satu barang (Trade-off)!"
        warna_card = st.error
    elif biaya_makan >= 12000 and biaya_data >= 5000:
        ekspresi_emoji = "🥳"
        status_kepuasan = "Sangat Happy & Produktif! (Kombinasi Optimal)"
        penjelasan_ekspresi = "Perut kenyang, tugas kuliah tetap jalan karena koneksi internet aman! Inilah keputusan paling optimal."
        warna_card = st.success
    elif biaya_makan >= 18000 and biaya_data < 5000:
        ekspresi_emoji = "😋"
        status_kepuasan = "Perut Kenyang Tapi Tugas Terhambat!"
        penjelasan_ekspresi = "Makanannya enak dan kenyang, tapi kamu tidak punya kuota untuk submit tugas kuliah jam 12 nanti."
        warna_card = st.warning
    elif biaya_makan < 10000 and biaya_data >= 10000:
        ekspresi_emoji = "📱"
        status_kepuasan = "Internet Kencang Tapi Perut Keroncongan!"
        penjelasan_ekspresi = "Tugas kuliah lancar jaya, tapi perutmu lapar dan konsentrasi belajar jadi terganggu."
        warna_card = st.warning
    else:
        ekspresi_emoji = "😐"
        status_kepuasan = "Kurang Kepuasan (Masih Ada Sisa Saldo)"
        penjelasan_ekspresi = f"Kamu masih menyisakan saldo Rp{sisa_saldo:,.0f}. Kebutuhan dasar belum fully teroptimasi."
        warna_card = st.info

    st.markdown("### **Hasil Efek Keputusan Konsumen:**")
    
    col_exp1, col_exp2 = st.columns([1, 2])
    with col_exp1:
        st.markdown(f"# {ekspresi_emoji}")
        st.markdown(f"**Ekspresi:** {status_kepuasan}")
    with col_exp2:
        warna_card(f"**Analisis Ekonomi:**  \n{penjelasan_ekspresi}")
        st.write(f"- Total Belanja: **Rp {total_pengeluaran:,.0f}**")
        st.write(f"- Sisa Saldo e-Wallet: **Rp {sisa_saldo:,.0f}**")

    st.markdown("---")
    st.write("📊 **Visualisasi Alokasi Anggaran vs Keterbatasan (Budget Constraint):**")
    
    df_bab1 = pd.DataFrame({
        'Kategori': ['Makanan', 'Paket Data', 'Sisa Saldo'],
        'Jumlah (Rp)': [biaya_makan, biaya_data, max(0, sisa_saldo)]
    })
    
    fig_bab1 = px.pie(
        df_bab1, 
        values='Jumlah (Rp)', 
        names='Kategori', 
        hole=0.4,
        color='Kategori',
        color_discrete_map={'Makanan': '#FF9800', 'Paket Data': '#2196F3', 'Sisa Saldo': '#4CAF50'}
    )
    st.plotly_chart(fig_bab1, use_container_width=True)

# ==========================================
# HALAMAN 3: BAB 2 (EKSPRESI MASYARAKAT KONSUMEN & KURVA INDIFERENSI)
# ==========================================
elif pilihan_modul == "Bab 2: Ekspresi Masyarakat Konsumen":
    st.title("📈 BAB 2: EKSPRESI MASYARAKAT KONSUMEN")
    st.caption("Modul Simulasi Model Kebahagiaan, Kurva Indiferensi, dan Marginal Rate of Substitution (MRS)")
    st.markdown("---")
    
    st.subheader("🏬 Dari Ratusan Juta Orang Menjadi Model Sederhana")
    st.write("""
    Bayangkan ada lebih dari **280 juta penduduk Indonesia** yang setiap hari membuat keputusan konsumsi. 
    Ekonom tidak mungkin mewawancarai mereka satu per satu. Karena itu, digunakan **model ekonomi**—seperti belajar naik sepeda di halaman rumah sebelum ke jalan raya. 
    Kita fokus pada satu hal utama: **bagaimana konsumen mengekspresikan pilihan dan kepuasannya (utility)** melalui kombinasi barang dan jasa.
    """)
    
    st.markdown("---")
    st.subheader("🗺️ Kurva Indiferensi: Peta Kebahagiaan Konsumen")
    st.write("Kurva Indiferensi (*Indifference Curve*) menunjukkan berbagai kombinasi dua barang (misal: Makanan dan Paket Data) yang memberikan **tingkat kepuasan yang sama** bagi konsumen.")

    st.sidebar.header("⚙️ Parameter Bab 2")
    tingkat_utility = st.sidebar.slider("Tingkat Kepuasan (Target Utility U):", min_value=10, max_value=30, value=20, step=5)
    
    x_makanan = np.linspace(1, 10, 100)
    y_data_u1 = (tingkat_utility**2) / (x_makanan * 10)
    y_data_u_low = ((tingkat_utility - 5)**2) / (x_makanan * 10)
    y_data_u_high = ((tingkat_utility + 5)**2) / (x_makanan * 10)

    col_grafik, col_penjelasan = st.columns([7, 5])
    
    with col_grafik:
        fig_ic = go.Figure()
        fig_ic.add_trace(go.Scatter(x=x_makanan, y=y_data_u1, mode='lines', name=f'Kepuasan Saat Ini (U = {tingkat_utility})', line=dict(color='#FF9800', width=4)))
        fig_ic.add_trace(go.Scatter(x=x_makanan, y=y_data_u_low, mode='lines', name='Kepuasan Lebih Rendah', line=dict(color='#BDBDBD', width=2, dash='dash')))
        fig_ic.add_trace(go.Scatter(x=x_makanan, y=y_data_u_high, mode='lines', name='Kepuasan Lebih Tinggi 🥳', line=dict(color='#4CAF50', width=2, dash='dash')))
        fig_ic.add_trace(go.Scatter(
            x=[2, 4, 8], 
            y=[(tingkat_utility**2)/(2*10), (tingkat_utility**2)/(4*10), (tingkat_utility**2)/(8*10)],
            mode='markers+text', name='Pilihan Kombinasi (A, B, C)',
            text=['Kombinasi A', 'Kombinasi B', 'Kombinasi C'],
            textposition="top right", marker=dict(size=10, color='#E91E63')
        ))
        fig_ic.update_layout(
            title="Kurva Indiferensi (Pilihan Makanan vs Paket Data)",
            xaxis_title="Makanan / Porsi (X)",
            yaxis_title="Paket Data / GB (Y)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )
        st.plotly_chart(fig_ic, use_container_width=True)

    with col_penjelasan:
        st.info("💡 **Karakteristik Kurva Indiferensi:**")
        st.markdown("""
        1. **Melengkung ke Bawah (Convex):** Menggambarkan **Marginal Rate of Substitution (MRS)**.
        2. **Semakin Tinggi Kurva = Semakin Happy:** Kurva hijau menandakan kepuasan lebih tinggi.
        3. **Kepuasan Sama (Indifferent):** Semua titik sepanjang garis oranye memberikan kepuasan identik.
        """)
        st.metric(label="Tingkat Kepuasan Konsumen Saat Ini", value=f"Indeks Utility: {tingkat_utility}")

# ==========================================
# HALAMAN CADANGAN: BAB 3 SAMPAI BAB 20
# ==========================================
else:
    st.title(f"📦 {pilihan_modul}")
    st.info("Modul ini telah dicadangkan dalam struktur laboratorium dan siap diisi materi simulasi selanjutnya.")
