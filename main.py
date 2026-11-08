skor = {
    "E": 0, "I": 0,  
    "S": 0, "N": 0,  
    "T": 0, "F": 0,  
    "J": 0, "P": 0   
}

def hitung_hasil_mbti(skor_akhir):
    hasil = ""
    
    if skor_akhir["E"] >= skor_akhir["I"]:
        hasil += "E"
    else:
        hasil += "I"
        
    if skor_akhir["S"] >= skor_akhir["N"]:
        hasil += "S"
    else:
        hasil += "N"
        
    if skor_akhir["T"] >= skor_akhir["F"]:
        hasil += "T"
    else:
        hasil += "F"
        
    if skor_akhir["J"] >= skor_akhir["P"]:
        hasil += "J"
    else:
        hasil += "P"
        
    return hasil

daftar_pertanyaan = [
    
    {"teks": "1. Apakah kamu merasa lebih berenergi setelah berkumpul dengan banyak orang?", "jika_ya": "E", "jika_tidak": "I"},
    {"teks": "2. Apakah kamu lebih suka menghabiskan waktu luang sendirian untuk mengisi energi?", "jika_ya": "I", "jika_tidak": "E"},
    {"teks": "3. Dalam kerja kelompok, apakah kamu lebih suka langsung berbicara menyampaikan ide?", "jika_ya": "E", "jika_tidak": "I"},
    {"teks": "4. Apakah kamu cenderung berpikir dalam hati terlebih dahulu sebelum mengutarakan pendapat?", "jika_ya": "I", "jika_tidak": "E"},
    
    {"teks": "5. Apakah kamu lebih suka fokus pada fakta yang ada saat ini daripada berimajinasi tentang masa depan (masa yang akan datang)?", "jika_ya": "S", "jika_tidak": "N"},
    {"teks": "6. Apakah kamu sering mencari makna tersembunyi atau pola masa depan dari suatu kejadian?", "jika_ya": "N", "jika_tidak": "S"},
    {"teks": "7. Apakah kamu lebih menyukai petunjuk kerja yang jelas dan pasti daripada yang bersifat umum?", "jika_ya": "S", "jika_tidak": "N"},
    {"teks": "8. Apakah kamu lebih suka mencoba cara-cara baru yang kreatif daripada cara lama yang sudah biasa?", "jika_ya": "N", "jika_tidak": "S"},
 
    {"teks": "9. Saat mengambil keputusan, apakah kamu lebih mengutamakan logika daripada perasaan orang lain?", "jika_ya": "T", "jika_tidak": "F"},
    {"teks": "10. Apakah kamu sering mempertimbangkan perasaan orang lain sebelum menolak permintaan mereka?", "jika_ya": "F", "jika_tidak": "T"},
    {"teks": "11. Apakah kamu lebih menghargai keadilan yang objektif daripada keharmonisan suasana?", "jika_ya": "T", "jika_tidak": "F"},
    {"teks": "12. Apakah kamu lebih mudah diyakinkan oleh argumen yang logis daripada cerita yang menyentuh hati?", "jika_ya": "T", "jika_tidak": "F"},
    
    {"teks": "13. Apakah kamu lebih suka membuat rencana harian yang terjadwal dengan rapi?", "jika_ya": "J", "jika_tidak": "P"},
    {"teks": "14. Apakah kamu merasa lebih nyaman bertindak secara spontan (mendadak) sesuai situasi?", "jika_ya": "P", "jika_tidak": "J"},
    {"teks": "15. Apakah kamu selalu berusaha menyelesaikan tugas sekolah jauh-jauh hari sebelum tenggat waktu?", "jika_ya": "J", "jika_tidak": "P"},
    {"teks": "16. Apakah kamu merasa lebih termotivasi bekerja ketika mendekati batas waktu (deadline)?", "jika_ya": "P", "jika_tidak": "J"}
]

print("--- Welcome to PersonaType App ---")
print("Jawablah pertanyaan berupa kuis di bawah ini dengan mengetik 'Y' untuk YA dan 'T' untuk TIDAK.\n")

for pertanyaan in daftar_pertanyaan:
    print(pertanyaan["teks"])
    jawaban = input("Jawaban kamu (Y/T): ").upper() 
    
    if jawaban == "Y":
        huruf_jika = pertanyaan["jika_ya"]
        skor[huruf_jika] += 1
    elif jawaban == "T":
        huruf_jika = pertanyaan["jika_tidak"]
        skor[huruf_jika] += 1 
    else:
        print("Pilihan tidak valid!.")
    
    print("-" * 30)

hasil_mbti = hitung_hasil_mbti(skor)

print("\n========================================")
print(f"Hasil tipe MBTI kamu adalah: {hasil_mbti}")
print("==========================================")
