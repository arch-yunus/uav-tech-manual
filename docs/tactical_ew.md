# 📡 Taktik Elektronik Harp ve Dayanıklı Seyrüsefer

SUNGUR sistemleri, GPS-denied (GPS'in engellendiği) ve yüksek radyo paraziti bulunan çatışma sahalarında hayatta kalmak üzere optimize edilmiştir.

## 1. Karıştırma Önleme Stratejileri

### A. Frekans Atlama
- **Protokol:** OMEGA-Link v3.0
- **Hız:** 1000 hop/s (Sinyal gürültüsüne göre dinamik artış).
- **Spektrum:** 2.4GHz - 5.8GHz dinamik geçiş.

### B. GNSS Yanıltma Tespiti (Anti-Spoofing) ve Dead Reckoning
- **Algoritma:** EKF tabanlı IMU/GNSS Tutarlılık Kontrolü.
- **Müdahale:** Sapma 5 metreyi aşarsa GNSS verisi reddedilir ve sistem "Dead Reckoning" (Hesaplı Seyir) moduna geçer.
- **Navigasyon:** VIO (Visual Inertial Odometry) ve V-SLAM verileriyle otonom uçuş sürdürülür.

## 2. OMEGA-tier Sinyal Dayanıklılığı

| Tehdit | Karşı Tedbir | Etki Seviyesi |
| :--- | :--- | :--- |
| Geniş Bant Gürültüsü | Adaptif Filtreleme | 🟢 Yüksek |
| GPS Yanıltma (Spoofing) | V-SLAM ve IMU Füzyonu | 🟢 Yüksek |
| Haberleşme Karıştırma | Otonom RTH (LCHI Protokolü) | 🟢 Yüksek |

## 3. Güvenlik ve Şifreleme
- **Veri Hattı:** Tüm C2 hattı AES-256 donanımsal şifreleme ile korunur.
- **Sinyal Aldatma (SDU):** Düşman radarlarını yanıltmak için sahte sinyal klonlama.

---
**Egemen Mimari | EH Standartları**
