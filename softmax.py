import math
import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

# Mahalleler ve kriterleri
mahalleler = ['Karakaş', 'İstasyon', 'Cumhuriyet']
kriterler = ['Nüfus Yoğunluğu', 'Ulaşım Altyapısı', 'Maliyet Analizi', 'Çevresel Etki', 'Sosyal Fayda']

# Her mahalle için kriter puanları (1-10 arası)
veriler = [
    [8, 5, 7, 6, 9],  # Karakaş
    [7, 7, 6, 7, 8],  # İstasyon
    [9, 5, 8, 6, 7]   # Cumhuriyet
]

# Kriterlerin maliyet ve faydaya ağırlıkları
fayda_agirliklari = [0.3, 0.2, -0.1, 0.1, 0.2]
maliyet_agirliklari = [0.0, -0.1, 0.5, 0.1, 0.0]

def hesapla_fayda_maliyet(puanlar):
    fayda = 0
    maliyet = 0
    softmax_puanlar = softmax(puanlar)
    for i in range(len(puanlar)):
        fayda += softmax_puanlar[i] * fayda_agirliklari[i]
        maliyet += softmax_puanlar[i] * maliyet_agirliklari[i]
    return fayda, maliyet

# Her bir mahalle için fayda ve maliyetin hesaplanması
fayda_sonuclari = []
maliyet_sonuclari = []
fayda_maliyet_oranlari = []

for puanlar in veriler:
    fayda, maliyet = hesapla_fayda_maliyet(puanlar)
    fayda_sonuclari.append(fayda)
    maliyet_sonuclari.append(maliyet)
    fayda_maliyet_oranlari.append(fayda / maliyet)

# Sonuçları yazdırma
print("Fayda-Maliyet Analizi:")
for i in range(len(mahalleler)):
    print(f"{mahalleler[i]}:")
    print(f"  Fayda: {fayda_sonuclari[i]:.2f}")
    print(f"  Maliyet: {maliyet_sonuclari[i]:.2f}")
    print(f"  Fayda-Maliyet Oranı: {fayda_maliyet_oranlari[i]:.2f}")
    print()

max_index = fayda_maliyet_oranlari.index(max(fayda_maliyet_oranlari))
print(f"En yüksek Fayda-Maliyet oranına sahip mahalle: {mahalleler[max_index]} ({fayda_maliyet_oranlari[max_index]:.2f})")
