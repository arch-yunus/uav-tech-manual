# 🛠️ Donanım Spesifikasyonları (Hardware Specs)

ARGUS İHA sistemleri, dayanıklılık ve modülerlik üzerine inşa edilmiştir. Donanım seçimleri, yüksek elektromanyetik parazit içeren ortamlarda bile çalışabilecek şekilde optimize edilmiştir.

## 1. Gövde (Airframe)
- **Malzeme**: Karbon Fiber Takviyeli Polimer (CFRP) ve 7075 Alüminyum Alaşım.
- **Konfigürasyon**: X8 (Okto-Quad) - Motor arızası durumunda yedeklilik sağlar.
- **Ağırlık (Boş)**: 2.4 kg
- **MTOW (Maksimum Kalkış Ağırlığı)**: 7.5 kg

## 2. İtki Sistemi (Propulsion)
- **Motorlar**: T-Motor U5 v2.0 (Yüksek verimli BLDC).
- **ESC**: 60A Flame Pro (Hızlı tepki ve termal koruma).
- **Pervaneler**: 15x5.2 Karbon Fiber (Düşük gürültü profili).
- **Batarya**: 6S 22.2V 16000mAh LiPo (High Discharge).

## 3. Aviyonik ve Kontrol (Avionics)
- **Uçuş Kontrolcüsü**: ARGUS-Core (H743 tabanlı, çift işlemci).
- **IMU**: Üçlü yedekli (Triple Redundant) titreşim izolasyonlu sensörler.
- **GNSS**: Ublox F9P (RTK destekli, multi-band).
- **Telemetri**: 868MHz / 2.4GHz AES-256 şifreli LoRa linki.

## 4. Sensör ve Payload
- **EO/IR Kamera**: 4K Optik / 640x512 Termal (Gimbal stabilize).
- **Lidar**: 120m menzilli engel sakınma sensörü.
- **AI İşlemci**: NVIDIA Jetson Orin Nano (Görüntü işleme ve EH kararı için).

---
*Göklerin muhafızı, sağlam temeller üzerine kurulur.*
