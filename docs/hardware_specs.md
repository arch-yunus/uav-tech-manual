# 🛠️ Modül 1: İHA Donanım Bileşenleri ve Seçim Kriterleri

> **Amaç:** Bu modül, bir İHA'yı meydana getiren her bileşeni tanıtır, nasıl çalıştığını açıklar ve hangi durumlarda hangi bileşenin seçilmesi gerektiğini öğretir.

---

## 1.1 Çerçeve (Frame) Seçimi

Çerçeve, tüm bileşenlerin monte edildiği fiziksel iskelet ve güç dağıtım yollarının taşıyıcısıdır.

| Parametre | Önemi | Tipik Değerler |
| :--- | :--- | :--- |
| **Dingil Açıklığı (Wheelbase)** | Motor merkezleri arası mesafe (mm). Büyük çerçeve = daha stabil, daha ağır. | 250mm (Yarış) / 450mm (Görev) / 800mm+ (Taşıma) |
| **Materyal** | Karbon Fiber: Hafif ve sert. Naylon+GF: Ucuz ve dayanıklı. | Racing: CF; Cargo: Alüminyum |
| **Motor Kol Sayısı** | Quadcopter (4): Basit. Hexacopter (6): 1 motor arızasında bile uçar. | 4, 6, 8 |

**Teorik Not:** Hexacopter ve Octocopter'lar, motor arızası durumunda "Motor Mixing" algoritması sayesinde geri kalan motorlarla yük dengesini yeniden dağıtabilir. Bu, kritik görevler için tercih sebebidir.

---

## 1.2 Motor Seçimi: KV Değeri ve İtki

### KV Nedir?
KV, bir motorun volt başına dakikada kaç devir döndüğünü gösterir.
```
Devir (RPM) = KV × Gerilim (V)
Örnek: 2300KV × 11.1V (3S) = 25,530 RPM
```

| KV Aralığı | Kullanım | Pervane | Karakteristik |
| :--- | :--- | :--- | :--- |
| **900–1200 KV** | Büyük yük taşıyan platformlar | 12–18 inç | Düşük devir, yüksek tork, verimli |
| **1300–2000 KV** | Genel amaçlı görev İHA'ları | 7–10 inç | Denge noktası |
| **2300–3000 KV** | Yarış ve çevik manevralar | 5 inç | Yüksek devir, düşük tork |

### İtki Hesaplama (Thrust Estimation)
```
Temel Kural: Toplam itki ≥ 2 × Kalkış Ağırlığı (Hover Efficiency)
Örnek: 1.5kg TOM → Minimum 3kg toplam itki gerekir
Motor başına ihtiyaç (Quad): 3000g / 4 = 750g/motor
```

---

## 1.3 ESC (Electronic Speed Controller) Seçimi

ESC, uçuş bilgisayarının PWM/DSHOT komutlarını motora iletilen 3 fazlı AC akıma dönüştürür.

### Kritik Parametreler
- **Sürekli Akım Kapasitesi (A):** Motor zirve akımının en az %20 üstünde seçilmeli.
- **Protokol Desteği:** DSHOT600/DSHOT1200 → PWM/Oneshot'tan çok daha güvenilir dijital iletişim sağlar.
- **BLHeli_32 vs. AM32:** İkisi de 32-bit ESC firmware'i. AM32 açık kaynaklıdır.

---

## 1.4 Batarya: LiPo Anatomisi

```
Kapasite: 5000mAh → Teorik olarak 5 Amper akım çekerken 1 saat
C-Rating:  50C    → Anlık 50 × 5A = 250 Amper verebilir
Hücre:     4S     → 4 × 3.7V = 14.8V (Nominal), 4 × 4.2V = 16.8V (Tam Şarj)
```

> ⚠️ **Güvenlik Notu:** LiPo pilleri 3.4V/hücre altına asla düşürme. Aşırı deşarj gaz salınımına ve yangına yol açabilir.

### Batarya Kapasitesi ve Uçuş Süresi
```python
# Tahmini Uçuş Süresi Formülü
# Bkz: scripts/flight_calculator.py

uçus_suresi_dk = (kapasite_mah * 0.8) / (ortalama_akim_a * 1000) * 60
```

---

## 1.5 Uçuş Kontrolcüsü (FC) ve Aviyonik

### Sensör Füzyonu Zinciri
```
IMU (Jiroskop + İvmeölçer)  ─┐
Barometrik Basınç Sensörü   ─├──► EKF (Extended Kalman Filter) ──► Uçuş Durumu
GNSS (GPS/Galileo/GLONASS)  ─┤                                    (Konum, Hız, İrtifa)
Magnetometre                ─┘
```

| Sensör | Fonksiyon | Hata Kaynakları |
| :--- | :--- | :--- |
| **IMU** | Açısal hız ve ivme ölçümü | Termal sürüklenme (thermal drift), vibrasyon |
| **Barometrik Sensör** | Göreli irtifa ölçümü | Hava sıcaklığı, rüzgar basıncı |
| **GNSS** | Mutlak konum | Çok yollu yayılma (multipath), iyonosferik bozulma |
| **Magnetometre** | Pusula yönü | Motor manyetik alanı, demir yapılar |

---

## 📝 Pratik Alıştırma

1. Ağırlığı 800g olan bir quadcopter için motor seçin. Hangi KV aralığı ve pervane boyutu uygun?
2. `uav-mission-control` simülatöründe batarya %80'den %40'a düştüğünde telemetride ne değişiyor?

---

*Sonraki Modül → [Uçuş Operasyonları ve SOP](flight_ops.md)*
