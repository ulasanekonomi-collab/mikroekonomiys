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
# HALAMAN 4: BAB 3 (GARIS ANGGARAN / BUDGET LINE)
# ==========================================
elif pilihan_modul == "Bab 3: Ketika Kebahagiaan Dibatasi Garis Anggaran":
    st.title("💳 BAB 3: KETIKA KEBAHAGIAAN DIBATASI GARIS ANGGARAN")
    st.caption("Modul Simulasi Batas Anggaran (Budget Line), Intersep, dan Area Pilihan Konsumen")
    st.markdown("---")
    
    st.subheader("💰 Uang Membatasi Pilihan Konsumen")
    st.write("""
    Meskipun konsumen menginginkan kepuasan setinggi-tingginya, dalam kehidupan nyata pilihan kita selalu dibatasi oleh **jumlah uang yang dimiliki ($M$)** dan **harga barang di pasar ($P_x$ & $P_y$)**.
    Persamaan matematis Garis Anggaran (*Budget Line*) dituliskan sebagai:
    $$M = P_x \\cdot X + P_y \\cdot Y$$
    """)
    
    # 📐 PANDUAN CARA MENGGAMBAR GARIS ANGGARAN
    st.subheader("📐 Cara Praktis Menggambar Garis Anggaran")
    st.write("Untuk menggambar Garis Anggaran pada bidang Kartesius, mahasiswa cukup mengikuti 3 langkah sederhana berikut:")
    
    col_step1, col_step2, col_step3 = st.columns(3)
    
    with col_step1:
        st.markdown("### 1️⃣ Cari Intersep Y")
        st.info("""
        **Maksimal Paket Data (Y)**
        $$Y_{\\text{max}} = \\frac{M}{P_y}$$
        $$\\frac{20.000}{10.000} = 2 \\text{ unit}$$
        
        📍 **Titik 1: (0, 2)**
        *(Seluruh uang untuk Data)*
        """)

    with col_step2:
        st.markdown("### 2️⃣ Cari Intersep X")
        st.info("""
        **Maksimal Makanan (X)**
        $$X_{\\text{max}} = \\frac{M}{P_x}$$
        $$\\frac{20.000}{5.000} = 4 \\text{ porsi}$$
        
        📍 **Titik 2: (4, 0)**
        *(Seluruh uang untuk Makanan)*
        """)

    with col_step3:
        st.markdown("### 3️⃣ Tarik Garis Lurus")
        st.success("""
        **Hubungkan Titik 1 & 2**
        
        Garis miring lurus yang terbentuk adalah **Garis Anggaran**. 
        
        📐 **Kemiringan (Slope):**
        $$-\\frac{P_x}{P_y} = -\\frac{5.000}{10.000} = -0.5$$
        """)
    st.markdown("---")

  # ... [Sisa parameter sidebar & grafik Plotly tetap sama] ...
    
    # 📐 PANDUAN CARA MENGGAMBAR GARIS ANGGARAN
    st.subheader("📐 Cara Praktis Menggambar Garis Anggaran")
    st.write("Untuk menggambar Garis Anggaran pada bidang Kartesius, mahasiswa cukup mengikuti 3 langkah sederhana berikut:")
    
    col_step1, col_step2, col_step3 = st.columns(3)
    
    with col_step1:
        st.markdown("### 1️⃣ Cari Intersep Y")
        st.info("""
        **Maksimal Paket Data (Y)**
        $$Y_{\\text{max}} = \\frac{M}{P_y}$$
        $$\\frac{20.000}{10.000} = 2 \\text{ unit}$$
        
        📍 **Titik 1: (0, 2)**
        *(Seluruh uang untuk Data)*
        """)

    with col_step2:
        st.markdown("### 2️⃣ Cari Intersep X")
        st.info("""
        **Maksimal Makanan (X)**
        $$X_{\\text{max}} = \\frac{M}{P_x}$$
        $$\\frac{20.000}{5.000} = 4 \\text{ porsi}$$
        
        📍 **Titik 2: (4, 0)**
        *(Seluruh uang untuk Makanan)*
        """)

    with col_step3:
        st.markdown("### 3️⃣ Tarik Garis Lurus")
        st.success("""
        **Hubungkan Titik 1 & 2**
        
        Garis miring lurus yang terbentuk adalah **Garis Anggaran**. 
        
        📐 **Kemiringan (Slope):**
        $$-\\frac{P_x}{P_y} = -\\frac{5.000}{10.000} = -0.5$$
        """)
    st.markdown("---")


    st.sidebar.header("⚙️ Parameter Bab 3")
    m_anggaran = st.sidebar.number_input("Pendapatan / Saldo M (Rp):", min_value=5000, value=20000, step=2500)
    px_makanan = st.sidebar.number_input("Harga Makanan Px (Rp/porsi):", min_value=1000, value=5000, step=1000)
    py_data = st.sidebar.number_input("Harga Paket Data Py (Rp/paket):", min_value=1000, value=10000, step=1000)

    # HITUNG INTERSEP MAKSIMAL SECARA EKSPLISIT (FLOAT)
    max_x = float(m_anggaran / px_makanan) if px_makanan > 0 else 0.0  # (20.000 / 5.000 = 4.0)
    max_y = float(m_anggaran / py_data) if py_data > 0 else 0.0        # (20.000 / 10.000 = 2.0)

    st.markdown("---")
    st.subheader("📊 Simulator Garis Anggaran Interaktif")
    
    col_inputs, col_status = st.columns([1, 1])
    
    with col_inputs:
        st.write("**Coba Masukkan Kombinasi Barang yang Ingin Dibeli:**")
        pilihan_x = st.slider("Jumlah Makanan (X):", min_value=0.0, max_value=float(max_x * 1.5), value=2.0, step=0.5)
        pilihan_y = st.slider("Jumlah Paket Data (Y):", min_value=0.0, max_value=float(max_y * 1.5), value=1.0, step=0.5)
        
        total_biaya = (pilihan_x * px_makanan) + (pilihan_y * py_data)
        selisih = m_anggaran - total_biaya

    with col_status:
        st.write("**Analisis Posisi Pilihan Konsumen:**")
        if total_biaya == m_anggaran:
            st.success("🟢 **TEPAT PADA GARIS ANGGARAN (On Budget Line)**")
            st.write(f"Total Belanja: **Rp {total_biaya:,.0f}** | Sisa Uang: **Rp 0**  \nSeluruh anggaran habis secara optimal untuk konsumsi.")
        elif total_biaya < m_anggaran:
            st.info("🟡 **DI BAWAH GARIS ANGGARAN (Under Budget)**")
            st.write(f"Total Belanja: **Rp {total_biaya:,.0f}** | Sisa Saldo: **Rp {selisih:,.0f}**  \nKombinasi ini bisa dibeli, tetapi uangmu belum dimanfaatkan sepenuhnya.")
        else:
            st.error("🔴 **DI ATAS GARIS ANGGARAN (Unattainable / Impossible)**")
            st.write(f"Total Belanja: **Rp {total_biaya:,.0f}** | Kurang Saldo: **Rp {abs(selisih):,.0f}**  \nKombinasi ini terlalu mahal! Ini hanya menjadi 'angan-angan'.")

    # GRAFIK GARIS ANGGARAN PRESISI
    # Membuat 100 titik kontinu dari X=0 sampai X=max_x
    # ------------------------------------------
    # GRAFIK PLOTLY DENGAN GARIS PROYEKSI (DROP LINES)
    # ------------------------------------------
    x_line = np.linspace(0, max_x, 100)
    y_line = (m_anggaran - (px_makanan * x_line)) / py_data

    fig_bl = go.Figure()

    # 1. Garis Anggaran Biru
    fig_bl.add_trace(go.Scatter(
        x=x_line, 
        y=y_line, 
        mode='lines', 
        name='Garis Anggaran (Budget Line)',
        line=dict(color='#2196F3', width=4)
    ))

    # Penentuan Warna Titik Pilihan
    if total_biaya == m_anggaran:
        warna_titik = '#4CAF50' # Hijau
        label_posisi = "Tepat di Garis Anggaran"
    elif total_biaya < m_anggaran:
        warna_titik = '#FFC107' # Kuning
        label_posisi = "Di Bawah Garis (Sisa Saldo)"
    else:
        warna_titik = '#F44336' # Merah
        label_posisi = "Di Atas Garis (Terlalu Mahal)"

    # 2. GARIS PROYEKSI KE SUMBU X (Ke Bawah)
    fig_bl.add_trace(go.Scatter(
        x=[pilihan_x, pilihan_x],
        y=[0, pilihan_y],
        mode='lines',
        showlegend=False,
        line=dict(color='gray', width=1.5, dash='dash')
    ))

    # 3. GARIS PROYEKSI KE SUMBU Y (Ke Kiri)
    fig_bl.add_trace(go.Scatter(
        x=[0, pilihan_x],
        y=[pilihan_y, pilihan_y],
        mode='lines',
        showlegend=False,
        line=dict(color='gray', width=1.5, dash='dash')
    ))

    # 4. Titik Plotting Konsumen
    fig_bl.add_trace(go.Scatter(
        x=[pilihan_x], 
        y=[pilihan_y], 
        mode='markers+text', 
        name='Pilihan Kamu',
        text=[f' Pilihan ({pilihan_x} Makanan, {pilihan_y} Paket Data)'],
        textposition="top right", 
        marker=dict(size=14, color=warna_titik, line=dict(width=2, color='black'))
    ))

    fig_bl.update_layout(
        title=f"Garis Anggaran Konsumen (Pendapatan M = Rp {m_anggaran:,.0f})",
        xaxis_title="Makanan / Porsi (Sumbu Horizontal X)",
        yaxis_title="Paket Data / Unit (Sumbu Vertikal Y)",
        xaxis=dict(range=[-0.2, max(max_x * 1.2, 5)]),
        yaxis=dict(range=[-0.2, max(max_y * 1.2, 3)]),
        template="plotly_white"
    )

    st.plotly_chart(fig_bl, use_container_width=True)

    # KUIS BAB 3
    st.markdown("---")
    st.subheader("📝 Kuis Reflektif & Evaluasi Pemahaman (Bab 3)")
    with st.form("kuis_bab3"):
        st.markdown("**1. Jika seorang mahasiswa memiliki uang Rp20.000, harga makanan Rp5.000/porsi, dan harga paket data Rp10.000/paket, berapakah jumlah paket data MAKSIMAL yang bisa dibeli jika ia tidak membeli makanan sama sekali?**")
        q1_b3 = st.radio(
            "Pilih jawaban yang tepat:",
            [
                "A. 4 paket data",
                "B. 2 paket data",
                "C. 1 paket data",
                "D. 0 paket data"
            ],
            index=None, key="b3q1"
        )
        st.markdown("---")
        st.markdown("**2. Apa makna ekonomi jika titik kombinasi pilihan konsumen berada DI BAWAH garis anggaran?**")
        q2_b3 = st.radio(
            "Pilih jawaban yang tepat:",
            [
                "A. Uang konsumen tidak cukup untuk membeli kombinasi tersebut.",
                "B. Kombinasi tersebut dapat dibeli, tetapi masih ada sisa uang yang belum dimanfaatkan untuk menambah kepuasan.",
                "C. Konsumen berada pada tingkat kepuasan tertinggi yang paling efisien.",
                "D. Harga barang di pasar mendadak naik drastis."
            ],
            index=None, key="b3q2"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        submit_b3 = st.form_submit_button("🎯 Periksa Jawaban Bab 3")

    if submit_b3:
        if q1_b3 is None or q2_b3 is None:
            st.warning("⚠️ Harap jawab semua pertanyaan terlebih dahulu!")
        else:
            skor_b3 = 0
            if q1_b3.startswith("B"): skor_b3 += 50
            if q2_b3.startswith("B"): skor_b3 += 50
            
            if skor_b3 == 100:
                st.balloons()
                st.success(f"🎉 **Skor Anda: {skor_b3} / 100** — Sempurna! Anda memahami fungsi Garis Anggaran dan keterbatasan sumber daya!")
            else:
                st.info(f"👍 **Skor Anda: {skor_b3} / 100** — Coba tinjau kembali simulasi di atas.")
# ==========================================
# HALAMAN 5: BAB 4 (PILIHAN OPTIMAL KONSUMEN)
# ==========================================
elif pilihan_modul == "Bab 4: Ketika Konsumen Menemukan Pilihan Terbaik":
  st.title("🎯 BAB 4: KETIKA KONSUMEN MENEMUKAN PILIHAN TERBAIK")
  st.caption(
      "Modul Simulasi Keseimbangan Konsumen (Persinggungan IC & Budget Line,"
      " MRS = Px/Py)"
  )
  st.markdown("---")

  # ------------------------------------------
  # 1. PENGANTAR KONSEPTUAL & PENURUNAN RUMUS
  # ------------------------------------------
  st.subheader("💡 Menggabungkan Keinginan (IC) dan Kemampuan (BL)")
  st.write("""
    Pilihan optimal konsumen terjadi ketika **Kurva Indiferensi (keinginan)** bersinggungan secara presisi dengan **Garis Anggaran (kemampuan)**. 
    Kondisi matematis keseimbangan dicapai pada saat:
    $$MRS_{xy} = \\frac{MU_x}{MU_y} = \\frac{P_x}{P_y}$$
    """)

  # Expander Penjelasan Matematis & Sifat Kurva
  with st.expander("📐 Lihat Penurunan Matematis Fungsi Utilitas $U = XY$"):
    st.latex(r"""
        \begin{aligned}
        \text{Fungsi Utilitas:} \quad & U(X,Y) = X \cdot Y \\
        \text{Bentuk Kurva Indiferensi:} \quad & Y = \frac{U}{X} \quad \implies \frac{d^2Y}{dX^2} = \frac{2U}{X^3} > 0 \quad (\text{Konveks/Cembung}) \\
        \text{Fungsi Lagrange:} \quad & \mathcal{L} = XY + \lambda (M - P_x X - P_y Y) \\
        \text{FOC (\lambda):} \quad & \frac{\partial \mathcal{L}}{\partial X} = Y - \lambda P_x = 0 \implies \lambda = \frac{Y}{P_x} \\
        & \frac{\partial \mathcal{L}}{\partial Y} = X - \lambda P_y = 0 \implies \lambda = \frac{X}{P_y} \\
        \text{Syarat Equilibrium:} \quad & \frac{Y}{P_x} = \frac{X}{P_y} \implies P_x X = P_y Y \\
        \text{Solusi Optimal:} \quad & X^* = \frac{M}{2 P_x} \quad \text{dan} \quad Y^* = \frac{M}{2 P_y}
        \end{aligned}
        """)
    st.info(
        "💡 **Sifat Penting:** Fungsi utilitas ini menunjukkan bahwa konsumen"
        " yang rasional selalu mengalokasikan tepat **50% anggarannya** untuk"
        " Makanan ($P_x X^*$) dan **50% sisanya** untuk Paket Data ($P_y Y^*$).Card"
        " indikator di bawah secara otomatis menghitung nilai $X^*$ dan $Y^*$"
        " ini."
    )

  # ... [Sisa parameter sidebar & grafik Plotly tetap sama] ...

  # ------------------------------------------
  # 1. PENGANTAR KONSEPTUAL
  # ------------------------------------------
  st.subheader("💡 Menggabungkan Keinginan (IC) dan Kemampuan (BL)")
  st.write("""
    Pilihan optimal konsumen terjadi ketika **Kurva Indiferensi (keinginan)** bersinggungan secara presisi dengan **Garis Anggaran (kemampuan)**. 
    Syarat matematis keseimbangan konsumen adalah:
    $$MRS_{xy} = \\frac{P_x}{P_y}$$
    """)

  # ------------------------------------------
  # 2. PARAMETER INPUT
  # ------------------------------------------
  st.sidebar.header("⚙️ Parameter Bab 4")
  m_anggaran = st.sidebar.number_input(
      "Pendapatan M (Rp):", min_value=5000, value=20000, step=2500
  )
  px_makanan = st.sidebar.number_input(
      "Harga Makanan Px (Rp):", min_value=1000, value=5000, step=1000
  )
  py_data = st.sidebar.number_input(
      "Harga Paket Data Py (Rp):", min_value=1000, value=10000, step=1000
  )

  # Hitung Intersep & Titik Optimal
  max_x = m_anggaran / px_makanan  # 20.000 / 5.000 = 4
  max_y = m_anggaran / py_data  # 20.000 / 10.000 = 2

  # Titik Optimal Tangency (Cobb-Douglas alpha=0.5, beta=0.5)
  opt_x = max_x / 2  # 2.0
  opt_y = max_y / 2  # 1.0
  u_optimal = np.sqrt(opt_x * opt_y)  # Utility level

  st.markdown("---")
  st.subheader("📊 Grafik Keseimbangan Konsumen (Titik Singgung Optimal)")

  col_info1, col_info2, col_info3 = st.columns(3)
  with col_info1:
    st.metric(
        "Kombinasi Optimal Makanan (X)",
        f"{opt_x:.1f} Porsi",
        f"Rp {opt_x * px_makanan:,.0f}",
    )
  with col_info2:
    st.metric(
        "Kombinasi Optimal Data (Y)",
        f"{opt_y:.1f} Unit",
        f"Rp {opt_y * py_data:,.0f}",
    )
  with col_info3:
    st.metric(
        "Kondisi MRS vs Rasio Harga",
        f"{px_makanan/py_data:.2f}",
        "MRS = Px / Py (Optimal)",
    )

  # ------------------------------------------
  # 3. GRAFIK PLOTLY PERSINGBUNGAN IC DAN BL
  # ------------------------------------------
  x_vals = np.linspace(0.1, max_x * 1.2, 100)

  # Budget Line: Y = (M - Px*X) / Py
  y_bl = (m_anggaran - (px_makanan * x_vals)) / py_data

  # IC Optimal (U_optimal): Y = (U_optimal^2) / X
  y_ic_opt = (u_optimal**2) / x_vals

  # IC Sub-optimal (U_rendah) & IC Non-terjangkau (U_tinggi)
  y_ic_low = ((u_optimal * 0.7) ** 2) / x_vals
  y_ic_high = ((u_optimal * 1.3) ** 2) / x_vals

  fig_opt = go.Figure()

  # Garis Anggaran (Budget Line)
  fig_opt.add_trace(
      go.Scatter(
          x=x_vals,
          y=y_bl,
          mode="lines",
          name="Garis Anggaran (BL)",
          line=dict(color="#2196F3", width=3),
      )
  )

  # IC Rendah (Di bawah)
  fig_opt.add_trace(
      go.Scatter(
          x=x_vals,
          y=y_ic_low,
          mode="lines",
          name="IC-1 (Sub-Optimal)",
          line=dict(color="#BDBDBD", width=2, dash="dash"),
      )
  )

  # IC Optimal (Bersinggungan)
  fig_opt.add_trace(
      go.Scatter(
          x=x_vals,
          y=y_ic_opt,
          mode="lines",
          name="IC-2 (Optimal / Bersinggungan)",
          line=dict(color="#4CAF50", width=4),
      )
  )

  # IC Tinggi (Tidak terjangkau)
  fig_opt.add_trace(
      go.Scatter(
          x=x_vals,
          y=y_ic_high,
          mode="lines",
          name="IC-3 (Angan-angan / Unattainable)",
          line=dict(color="#E91E63", width=2, dash="dash"),
      )
  )

  # Titik Singgung Optimal
  fig_opt.add_trace(
      go.Scatter(
          x=[opt_x],
          y=[opt_y],
          mode="markers+text",
          name="Titik Optimal (Equilibrium)",
          text=[f" Optimal ({opt_x:.1f}, {opt_y:.1f})"],
          textposition="top right",
          marker=dict(
              size=14, color="#FF9800", line=dict(width=2, color="black")
          ),
      )
  )

  # Garis Proyeksi Putus-putus
  fig_opt.add_trace(
      go.Scatter(
          x=[opt_x, opt_x],
          y=[0, opt_y],
          mode="lines",
          showlegend=False,
          line=dict(color="gray", width=1.5, dash="dot"),
      )
  )
  fig_opt.add_trace(
      go.Scatter(
          x=[0, opt_x],
          y=[opt_y, opt_y],
          mode="lines",
          showlegend=False,
          line=dict(color="gray", width=1.5, dash="dot"),
      )
  )

  fig_opt.update_layout(
      title=(
          "Keseimbangan Konsumen: Persinggungan Kurva Indiferensi dan Garis"
          " Anggaran"
      ),
      xaxis_title="Makanan / Porsi (X)",
      yaxis_title="Paket Data / Unit (Y)",
      xaxis=dict(range=[0, max_x * 1.25]),
      yaxis=dict(range=[0, max_y * 1.25]),
      template="plotly_white",
  )

# ------------------------------------------
    # PILAR PEDAGOGIS DINAMIS: PROSES FOC & PROPOSISI EKONOMI
    # ------------------------------------------
    st.markdown("---")
    st.subheader("🎓 Eksplorasi Pedagogis: Menggali Logika FOC secara Dinamis")
    st.write(
        "Mari kita bedah bagaimana ekonom menggunakan *First-Order Conditions*"
        " (FOC) untuk menemukan informasi logis di balik pilihan optimal ini:"
    )

    # Menghitung nilai matematis riil secara dinamis berdasarkan input sidebar
    mu_x_opt = opt_y  # dU/dX = Y
    mu_y_opt = opt_x  # dU/dY = X
    equi_x = mu_x_opt / px_makanan
    equi_y = mu_y_opt / py_data
    lambda_val = equi_x  # Marginal Utility of Money

    tab_step1, tab_step2, tab_step3 = st.tabs([
        "1️⃣ Formulasi Lagrange",
        "2️⃣ Turunan Pertama (FOC)",
        "3️⃣ Proposisi Ekonomi Logis",
    ])

    with tab_step1:
      st.markdown("#### **Langkah 1: Membentuk Fungsi Lagrange**")
      st.write(
          "Konsumen memaksimumkan $U(X,Y) = X \\cdot Y$ dengan batas anggaran"
          f" $\\text{{Rp}}{m_anggaran:,.0f} = \\text{{Rp}}{px_makanan:,.0f}X +"
          f" \\text{{Rp}}{py_data:,.0f}Y$."
      )
      st.latex(
          r"\mathcal{L}(X, Y, \lambda) = (X \cdot Y) + \lambda ("
          + str(m_anggaran)
          + r" - "
          + str(px_makanan)
          + r"X - "
          + str(py_data)
          + r"Y)"
      )
      st.info(
          "💡 **Makna Pedagogis:** $\\lambda$ (Pengali Lagrange) mewakili 'harga"
          " bayangan' atau **tambahan kepuasan untuk setiap tambahan satu"
          " rupiah anggaran**."
      )

    with tab_step2:
      st.markdown(
          "#### **Langkah 2: Mencari Keseimbangan via Turunan Pertama"
          " (FOC)**"
      )
      st.write(
          "Agar fungsi mencapai titik maksimum, turunan parsial pertama terhadap"
          " $X$, $Y$, dan $\\lambda$ disamakan dengan $0$:"
      )

      col_foc1, col_foc2 = st.columns(2)
      with col_foc1:
        st.latex(
            r"\frac{\partial \mathcal{L}}{\partial X} = Y - \lambda P_x = 0"
            r" \implies MU_x = \lambda P_x"
        )
        st.caption(
            f"Pada titik optimal: $MU_x = {mu_x_opt:.2f}$ util dari porsi"
            f" ke-{opt_x:.1f} Makanan."
        )

      with col_foc2:
        st.latex(
            r"\frac{\partial \mathcal{L}}{\partial Y} = X - \lambda P_y = 0"
            r" \implies MU_y = \lambda P_y"
        )
        st.caption(
            f"Pada titik optimal: $MU_y = {mu_y_opt:.2f}$ util dari unit"
            f" ke-{opt_y:.1f} Data."
        )

    with tab_step3:
      st.markdown(
          "#### **Langkah 3: Menggali Proposisi Ekonomi (Informasi Logis)**"
      )
      st.write(
          "Dengan membagi kedua kondisi FOC di atas, ekonom memperoleh"
          " **dua proposisi utama**:"
      )

      st.success(
          "**📌 Proposisi 1: Rasio Penukaran Subjektif = Rasio Harga Pasar ($MRS"
          " = P_x / P_y$)**\n\n"
          f"$$MRS = \\frac{{MU_x}}{{MU_y}} = \\frac{{{mu_x_opt:.2f}}}{{{mu_y_opt:.2f}}} = {mu_x_opt/mu_y_opt:.2f}$$\n\n"
          f"$$\\text{{Rasio Harga}} = \\frac{{P_x}}{{P_y}} = \\frac{{{px_makanan}}}{{{py_data}}} = {px_makanan/py_data:.2f}$$\n\n"
          "*Tingkat kesediaan konsumen menukar Makanan dengan Data tepat sama"
          " dengan rasio harga relatif kedua barang di pasar.*"
      )

      st.warning(
          "**📌 Proposisi 2: Prinsip Equi-Marginal Utility per Rupiah"
          " ($\lambda$)**\n\n"
          f"$$\\frac{{MU_x}}{{P_x}} = \\frac{{{mu_x_opt:.2f}}}{{{px_makanan}}} = {equi_x:.6f} \\text{{ util/rupiah}}$$\n\n"
          f"$$\\frac{{MU_y}}{{P_y}} = \\frac{{{mu_y_opt:.2f}}}{{{py_data}}} = {equi_y:.6f} \\text{{ util/rupiah}}$$\n\n"
          "*Rupiah terakhir yang dibelanjakan untuk Makanan memberikan"
          " tambahan kepuasan yang **persis sama** dengan rupiah terakhir"
          f" yang dibelanjakan untuk Paket Data (sebesar $\\lambda ="
          f" {lambda_val:.6f}$ util/rupiah).*"
      )

    # ------------------------------------------
    # 4. KUIS EVALUASI BAB 4
    # ------------------------------------------
    st.markdown("---")
    st.subheader("📝 Kuis Reflektif & Evaluasi Pemahaman (Bab 4)")

  # ------------------------------------------
  # 4. KUIS EVALUASI BAB 4
  # ------------------------------------------
  st.markdown("---")
  st.subheader("📝 Kuis Reflektif & Evaluasi Pemahaman (Bab 4)")

  with st.form("kuis_bab4"):
    st.markdown(
        "**1. Apakah syarat matematis utama terjadinya kondisi pilihan optimal"
        " konsumen (keseimbangan konsumen)?**"
    )
    q1_b4 = st.radio(
        "Pilih jawaban yang tepat:",
        [
            "A. MRS = Px / Py (Kemiringan Kurva Indiferensi sama dengan kemiringan Garis Anggaran).",
            "B. Px = Py (Harga barang X harus sama dengan harga barang Y).",
            "C. Pendapatan konsumen harus bernilai nol.",
            "D. Konsumen membeli lebih banyak barang Y daripada barang X.",
        ],
        index=None,
        key="b4q1",
    )

    st.markdown("---")
    st.markdown(
        "**2. Mengapa titik persinggungan antara Kurva Indiferensi dan Garis"
        " Anggaran disebut sebagai pilihan paling optimal?**"
    )
    q2_b4 = st.radio(
        "Pilih jawaban yang tepat:",
        [
            "A. Karena pada titik itu harga barang menjadi paling murah.",
            (
                "B. Karena konsumen memperoleh tingkat kepuasan tertinggi"
                " yang masih dapat dicapai dengan seluruh anggaran yang"
                " dimilikinya."
            ),
            "C. Karena konsumen tidak perlu membayar barang yang dibelinya.",
            "D. Karena titik tersebut berada di luar batas anggaran.",
        ],
        index=None,
        key="b4q2",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_b4 = st.form_submit_button("🎯 Periksa Jawaban Bab 4")

  if submit_b4:
    if q1_b4 is None or q2_b4 is None:
      st.warning("⚠️ Harap jawab semua pertanyaan terlebih dahulu!")
    else:
      skor_b4 = 0
      if q1_b4.startswith("A"):
        skor_b4 += 50
      if q2_b4.startswith("A") or q2_b4.startswith("B"):
        if q2_b4.startswith("B"):
          skor_b4 += 50

      if skor_b4 == 100:
        st.balloons()
        st.success(
            f"🎉 **Skor Anda: {skor_b4} / 100** — Luar biasa! Anda telah"
            " menguasai konsep Keseimbangan Konsumen dan Pilihan Optimal!"
        )
      else:
        st.info(f"👍 **Skor Anda: {skor_b4} / 100** — Coba tinjau kembali grafik persinggungan di atas.")
