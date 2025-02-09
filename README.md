# Algoritma Analizi ve Tasarımı Dersi - Ödev 1

## Açıklama
Bu repo, **Algoritma Analizi ve Tasarımı** dersi kapsamında hazırlanan bir ödev içermektedir. Proje, bir bölgedeki mahallelerin belirli kriterlere göre fayda-maliyet analizi yapılarak en uygun mahallenin seçilmesini amaçlamaktadır.

## Kullanılan Yöntem
Bu analiz, **Softmax Fonksiyonu** kullanılarak mahallelere ait kriter puanlarının normalize edilmesi ve ardından **fayda-maliyet oranlarının** hesaplanmasıyla gerçekleştirilmiştir.

## İçerik
Projede aşağıdaki unsurlar yer almaktadır:
- **Mahalleler**: Karakaş, İstasyon, Cumhuriyet
- **Kriterler**: Nüfus Yoğunluğu, Ulaşım Altyapısı, Maliyet Analizi, Çevresel Etki, Sosyal Fayda
- **Fayda ve Maliyet Ağırlıkları**: Her bir kriter için fayda ve maliyet ağırlıkları belirlenmiştir.
- **Hesaplama Fonksiyonları**:
  - `softmax(x)`: Verilen değerlere Softmax işlemi uygular.
  - `hesapla_fayda_maliyet(puanlar)`: Mahallelerin kriter puanlarını kullanarak fayda ve maliyet hesaplar.
- **Çıktılar**: Her mahalle için fayda, maliyet ve fayda-maliyet oranı hesaplanarak en uygun mahalle seçilir.

## Kullanım
Bu kodu çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

### Gereksinimler
Kodun çalışması için **Python 3.x** ve aşağıdaki kütüphaneler gereklidir:
```bash
pip install numpy
```

### Çalıştırma
Aşağıdaki komutu kullanarak kodu çalıştırabilirsiniz:
```bash
python softmax.py
```

Çıktı olarak, her mahalle için fayda-maliyet oranları listelenir ve en yüksek orana sahip mahalle belirlenir.


---

**Geliştirici Notu:** Herhangi bir hata veya öneri için lütfen GitHub Issues sekmesini kullanın.

