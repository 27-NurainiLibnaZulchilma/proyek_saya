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
