# ✈️ Uçuş Operasyonları (Flight Operations)

Uçuş disiplini, operasyonel başarının yarısıdır. ARGUS sistemleri için belirlenen standart operasyon prosedürleri (SOP) aşağıdadır.

## 1. Uçuş Öncesi Kontroller (Pre-Flight)
- [ ] **Görsel Muayene**: Pervanelerde çatlak, gövdede gevşek vida kontrolü.
- [ ] **Güç Bağlantısı**: Batarya voltajı (Hücre başı 4.1V+).
- [ ] **Sinyal Testi**: RC ve Telemetri linklerinin RSSI değerleri.
- [ ] **GNSS Fix**: Minimum 12 uydu ve HDOP < 1.0.
- [ ] **Failsafe**: 'Return to Home' (RTH) irtifası ve konumu doğrulaması.

## 2. Kalkış ve Seyir (Take-off & Cruise)
- **Kalkış**: Arm sonrası motor devirlerinin stabil olduğundan emin olun.
- **İrtifa**: Operasyonel irtifaya kademeli geçiş.
- **Hız**: Maksimum verimlilik için 12-15 m/s seyir hızı.

## 3. Görev İcrası (Mission)
- **Otonomi**: Waypoint takibi esnasında telemetri verilerini anlık izleyin.
- **EH İzleme**: Spektrum analizörü üzerinden parazit seviyelerini kontrol edin.
- **Acil Durum**: Beklenmedik durumlarda manuel kontrol (Loiter/AltHold) moduna geçiş.

## 4. İniş ve Operasyon Sonrası (Landing & Post-Flight)
- **İniş**: İniş alanının güvenliğini doğrulayın.
- **Log Analizi**: Uçuş kayıtlarını (SD Card) analiz için Mission Control'e aktarın.
- **Soğuma**: Motor ve ESC sıcaklıklarını kontrol edin.

---
*Hata kabul etmeyen gökyüzü, kusursuz hazırlık ister.*
