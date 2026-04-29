# 📡 Modül 5: Elektronik Harp ve Dayanıklı İHA Haberleşmesi

> **Amaç:** RF spektrumunu anlamak, İHA haberleşmesinin zaafiyetlerini tanımak ve bunlara karşı teknik savunma stratejileri geliştirmek.

---

## 5.1 RF Haberleşme Temelleri

### Serbest Uzay Yol Kaybı (Free Space Path Loss)
Sinyal mesafe ilerledikçe yayılır ve zayıflar:
```
FSPL (dB) = 20·log₁₀(d) + 20·log₁₀(f) + 20·log₁₀(4π/c)

d = Mesafe (metre)
f = Frekans (Hz)
c = Işık hızı

Örnek: 2.4GHz, 1km mesafe → ~100 dB yol kaybı
```

### Link Bütçesi (Link Budget)
```
Alınan Güç (dBm) = TX Gücü + TX Anten Kazancı - Yol Kaybı + RX Anten Kazancı
Sistem Çalışması İçin: Alınan Güç > Alıcı Hassasiyeti + Marj
```

---

## 5.2 Haberleşme Protokolleri

| Protokol | Frekans | Menzil | Kullanım |
| :--- | :--- | :--- | :--- |
| **ELRS (ExpressLRS)** | 900MHz / 2.4GHz | 50km+ | Uzun menzil RC kontrol |
| **MAVLink / LTE** | 4G Bant | Teorik sınırsız | Telemetri ve görev planı |
| **LoRa** | 868/915MHz | 15-20km | Düşük bant genişliği telemetri |
| **Starlink / SatCom** | Ka-band | Global | BVLOS operasyonlar |

---

## 5.3 Karıştırma (Jamming) Saldırıları

### Karıştırma Türleri
1. **Geniş Bant Gürültü (Barrage Jamming):** Geniş bir frekans bandını gürültüyle doldurur.
2. **Spot Jamming:** Sadece hedef frekansı karıştırır. Daha verimli ve tespit edilmesi zor.
3. **Sweep Jamming:** Bir frekans bandını tarayarak geçer.

### Karıştırmaya Karşı Savunma Teknikleri
```
1. FHSS (Frequency Hopping Spread Spectrum)
   └─ Sistem saniyede 100+ kez frekans atlar.
   └─ Jammer tüm frekansları aynı anda karıştıramaz.

2. DSSS (Direct Sequence Spread Spectrum)
   └─ Sinyal çok geniş banda yayılır.
   └─ Her bant dilimindeki güç gürültü seviyesine iner.
   └─ Alıcı korelasyon ile orijinal sinyali çıkarır.

3. Yüksek Kazançlı Yönlü Anten
   └─ Kargilleri tek yöne odaklar.
   └─ Jammer açı dışında kalırsa etkisizdir.
```

---

## 5.4 GPS Yanıltma (GNSS Spoofing)

### Spoofing Nedir?
Saldırgan, sahte GPS sinyalleri yayarak İHA'yı yanlış konuma inandırır.

### Tespit Yöntemleri
```
1. IMU Tutarlılık Kontrolü
   └─ GPS koordinatı IMU'dan hesaplanan konumla karşılaştırılır.
   └─ >5m fark → GNSS reddet, Dead Reckoning moduna geç.

2. Uydu Geometrisi Analizi (GDOP)
   └─ Ani GDOP değişimi → Sahte uydu sinyali şüphesi.

3. Sinyal Gücü Analizi
   └─ Gerçek GPS zayıf gelir. Sahte GPS güçlü gelir.
   └─ C/N0 (Taşıyıcı-Gürültü oranı) anormal yüksekliği = Spoofing şüphesi.
```

### Simülatörde EH Testi
Simülatörde "Gürültü Simülasyonu" panelini açarak RSSI değerini düşür. İHA hangi değerde RTH protokolünü başlatıyor?

---

## 5.5 Frekans Atlama (FHSS) Simülasyonu

```python
import random
import time

# Basit FHSS Simülasyonu
freqanslar = [2400, 2425, 2450, 2475, 2500]  # MHz

def fhss_ilet(mesaj):
    for bit in mesaj:
        frekans = random.choice(freqanslar)
        print(f"TX [{frekans}MHz]: {bit}")
        time.sleep(0.001)  # 1ms/kanal

fhss_ilet("SUNGUR_KOMUT_01")
```

---

## 📝 Pratik Alıştırma

1. Simülatörde "Gürültü Simülasyonu"nu artır. Hangi RSSI değerinde bağlantı kopuyor?
2. 900MHz ile 2.4GHz arasında 1km mesafe için link bütçesini hesapla. Hangisi daha iyi?

---

*Sonraki Modül → [Sistem Mimarisi ve Mühendislik Felsefesi](philosophy.md)*
