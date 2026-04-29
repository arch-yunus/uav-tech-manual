# ✈️ Modül 2: Uçuş Operasyonları ve Standart Prosedürler (SOP)

> **Amaç:** Güvenli ve verimli bir uçuş operasyonu, havada başlamaz — hazırlık masasında başlar. Bu modül, profesyonel bir operatörün her uçuşta takip etmesi gereken prosedürleri öğretir.

---

## 2.1 Uçuş Risk Analizi (FRAT — Flight Risk Assessment Tool)

Her operasyon öncesi **PAVE** kontrol listesi yapılır:

| Harf | Kategori | Sorular |
| :--- | :--- | :--- |
| **P** | **Pilot** | Yorgun muyum? Son 8 saatte alkol aldım mı? Bu görevi yapmış mıyım? |
| **A** | **Aircraft** | Batarya tam şarjlı mı? Pervaneler sağlam mı? Firmware güncel mi? |
| **V** | **enVironment** | Rüzgar <10m/s mi? Yağmur var mı? Görüş mesafesi yeterli mi? |
| **E** | **External Pressures** | "Şimdi uçmam lazım" baskısı var mı? Baskıya rağmen uçmak yasak. |

---

## 2.2 Uçuş Öncesi Kontrol Listesi (Pre-Flight Checklist)

```
PRE-FLIGHT CHECKLIST v2.0 — SUNGUR AKADEMI
==========================================

[ ] DONANIM
  [ ] Gövde çatlak/kırık kontrolü (görsel)
  [ ] Tüm vidaların torku kontrol edildi
  [ ] Pervaneler: çatlak yok, dengeli monte
  [ ] Motor: elle döndürüldüğünde pürüzsüz
  [ ] Konektörler: ısınma ve karartma yok

[ ] ENERJI
  [ ] Batarya gerilimi > 4.0V/hücre (tam şarj)
  [ ] Hücre dengesi sapması < 0.05V
  [ ] LiPo şişme yok (göbek testi)

[ ] YAZILIM
  [ ] FC parametreleri son sürümde
  [ ] IMU kalibrasyonu tarih içinde
  [ ] RTH noktası güncel konuma ayarlandı
  [ ] Geofence sınırları aktif

[ ] HAVA DURUMU
  [ ] Rüzgar < platformun limiti (m/s)
  [ ] NOTAM sorgulandı (ne zaman?)
  [ ] Yasal uçuş saatleri teyit edildi
==========================================
```

---

## 2.3 İHA Kalkış Sekansı (Arming Procedure)

```
1. Motor Arming (Silah Güvenliği Açma)
   └── FC → Arm komutu → ESC'ler motoru düşük hızda döndürür
   └── GÖSTERGEler: LED'ler yeşil, motorlar alçak tonda uğultu

2. Pre-Arm Kontrolleri
   └── Kalibrasyon durumu: OK
   └── GPS Fix: En az 8 uydu (HDOP < 2.0)
   └── Batarya: Nominal

3. Kalkış (Takeoff)
   └── Throttle yavaşça %50'ye
   └── 1-2m'de Hover — stabilite teyidi
   └── Kalkış kabul edilirse göreve devam
```

---

## 2.4 Uçuş Sırası: Telemetri Okuma

Bir operatörün takip etmesi gereken kritik telemetri değerleri:

```
[SUNGUR Telemetri Paneli]
IRTİFA:  125.4 m  ← AGL (Arazi üstü), GPS irtifasıyla karıştırma
HIZ:     14.2 m/s ← Horizontal ground speed
BATARYA: 73%      ← Bu %30'a düşmeden RTH tetiklenmeli
RSSI:    -68 dBm  ← -85 dBm altı = kritik link zayıflığı
PITCH:   +2.4°    ← Öne eğim (pozitif = öne)
ROLL:    -1.1°    ← Sağ eğim (negatif = sol)
```

---

## 2.5 Uçuş Sonrası Protokol (Post-Flight)

1. **İniş:** Gaz kolu sıfırla, motor durana kadar bekle, ardından Disarm.
2. **Batarya:** Hemen şarj etme. 30 dakika soğuma. Sonra iç direnci ölç.
3. **Log Kaydetme:** Blackbox/log dosyalarını bilgisayara yedekle.
4. **Arıza Kaydı:** En küçük anomaliyi bakım formuna kaydet.

---

## 📝 Pratik Alıştırma

1. Simülatörde RSSI değerini izle. Hangi değerde telemetri hata veriyor?
2. Kalkıştan önce GPS fix gelmezse ne yaparsın? En az 3 seçenek yaz.

---

*Sonraki Modül → [Bakım, Arıza ve Onarım](maintenance.md)*
