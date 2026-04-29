# 📡 Taktik Elektronik Harp ve Dayanıklı Seyrüsefer

ARGUS sistemleri, GPS-denied (GPS'in engellendiği) ve yüksek radyo paraziti bulunan çatışma sahalarında hayatta kalmak üzere optimize edilmiştir.

## 1. Karıştırma Önleme Stratejileri

### A. Frekans Atlama
- **Protokol:** OMEGA-Link v2.0
- **Hız:** 1000 hop/s
- **Spektrum:** 2.4GHz - 5.8GHz dinamik geçiş.

### B. GNSS Yanıltma Tespiti (Anti-Spoofing)
- **Algoritma:** EKF-based IMU/GNSS Consistency Check.
- **Müdahale:** Sapma 5 metreyi aşarsa GNSS verisi reddedilir ve VIO (Visual Inertial Odometry) moduna geçilir.

## 2. Siber-Asabiyet (Signal Resilience)

| Tehdit | Karşı Tedbir | Etki Seviyesi |
| :--- | :--- | :--- |
| Wideband Noise | Adaptive Filtering | 🟢 High |
| GPS Spoofing | V-SLAM & IMU Fusion | 🟢 High |
| C2 Link Jamming | Autonomous RTH (LCHI Protocol) | 🟢 Medium |

---
**Sovereign Architecture | EW Standards**
