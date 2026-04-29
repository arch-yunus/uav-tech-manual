# 🔧 Modül 3: Bakım, Arıza Tespiti ve Onarım

> **Amaç:** Bir İHA'nın en iyi pilotu, bakımını en iyi yapandır. Bu modül, düzenli bakım rutinlerini ve sahada karşılaşılan yaygın arızaları teşhis etmeyi öğretir.

---

## 3.1 Arıza Tespit Ağacı (Troubleshooting Tree)

```
İHA Kalkış Yapmıyor / Kararsız Uçuyor
│
├─── Motor(lar) dönmüyor?
│     ├─── EVET → ESC kalibrasyonu yapıldı mı?
│     │           └─── HAYIR → ESC kalibrasyon protokolünü uygula.
│     │           └─── EVET  → FC-ESC kablo bağlantısını kontrol et.
│     └─── HAYIR → Tüm motorlar mı duruyor?
│           ├─── EVET → Batarya / FC arm durumu kontrol et.
│           └─── HAYIR → Sadece 1-2 motor → O motorun ESC'sini değiştir.
│
├─── Drift / Kararsızlık var mı?
│     ├─── Yatay drift → IMU kalibrasyonu yap + vibrasyon damperleri kontrol et.
│     ├─── Rotasyonel sapma → Pusula (Magnetometre) kalibrasyonu yap.
│     └─── İrtifa değişimi → Barometrik sensörde tıkanma var mı?
│
└─── Telemetri / Bağlantı Sorunu?
      ├─── GCS göremiyor → Telemetri modülü frekans ayarını kontrol et.
      └─── RC bağlantısı yok → RC alıcı bağlama (binding) prosedürünü uygula.
```

---

## 3.2 Motor Sağlık Kontrolü

### Elle Kontrol
- Motor mili sallanıyor mu? → **Rulman ömrü dolmuş.** Değiştir.
- Elle döndürüldüğünde takılıyor mu? → **Mıknatıs veya sarım sorunu.** Değiştir.
- Sıcaklık uçuş sonrası 55°C üstü mi? → **Hava akışı yetersiz.** Montaj pozisyonunu gözden geçir.

### Manyetik Alan Testi
```bash
# PX4/ArduPilot üzerinden motor test:
MAVLink → mavlink_shell → motor_test test -e 4 -t 0.5 -p 15
# Her motoru %15 gaz ile 0.5 saniye test eder
```

---

## 3.3 Batarya Sağlık Protokolü

| Test | Araç | Sağlıklı Değer | Kritik Değer |
| :--- | :--- | :--- | :--- |
| **Statik Gerilim** | Multimetre | 4.15V – 4.20V/hücre | < 4.00V → Şarj et |
| **Hücre Dengesi** | Balancer Şarjcı | Sapma < 0.02V | > 0.05V → Kontrollü deşarj |
| **İç Direnç** | iCharger / Junsi | < 5 mΩ/hücre | > 15 mΩ → Emekli et |
| **Kapasite Testi** | Şarjcı Yazılımı | > %90 nominal kapasite | < %75 → Emekli et |

> ⚠️ İç direnci yükselen batarya, tam gaz anlarda gerilim çökmesine (voltage sag) yol açar. Bu, motor hız farklılıklarına ve kaza riskine neden olur.

---

## 3.4 Vibrasyon Analizi

Yüksek vibrasyon IMU'yu kör eder ve uçuş stabilitesini bozar.

**Ölçüm:** FC loglarında `IMU.AccX`, `IMU.AccY`, `IMU.AccZ` grafiklerini incele.
- Pürüzsüz dalgalanma → Normal
- Yüksek frekanslı gürültü → Pervane dengesi bozuk / motor rulmanı yıpranmış

**Çözüm Adımları:**
1. Her pervaneyi tek tek değiştir → Bozuğu bul.
2. Motor montaj vidalarının torku kontrol et.
3. Vibrasyon damperleri (O-ring veya Gel pad) ekle.

---

## 3.5 Periyodik Bakım Protokolü

```
SUNGUR BAKIM FORMU
==================
Uçuş #: _____  Tarih: _____  Teknisyen: _____

[ ] UÇUŞ ÖNCESİ (Her Uçuş)
  [ ] Pervane görsel kontrol
  [ ] Batarya gerilim ve denge kontrolü
  [ ] FC bağlantı LED'leri teyit

[ ] PERİYODİK (Her 10 Uçuş)
  [ ] Konektör ısı izleri
  [ ] Motor mili oynaklık testi
  [ ] Log dosyaları yedeklendi

[ ] KAPSAMLI SERVİS (Her 25 Uçuş)
  [ ] Tüm vid torku (renk markası ile)
  [ ] Motor iç temizliği (izopropil alkol)
  [ ] IMU ve pusula kalibrasyonu
  [ ] Firmware güncelleme
  [ ] Batarya kapasitesi testi

Not: ___________________________
==================
```

---

## 📝 Pratik Alıştırma

1. Simülatörde "Arıza Simülasyonu Başlat" butonuna bas. Telemetride hangi değerler değişiyor? Ne yapmalısın?
2. Batarya iç direnç ölçümünü araştır. Hangi araçlar kullanılır?

---

*Sonraki Modül → [Görev Profilleri ve Planlama](mission_profiles.md)*
