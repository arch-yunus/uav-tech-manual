# 🛠️ Donanım Spesifikasyonları ve Bileşen Topolojisi

SUNGUR platformunun fiziksel katmanı, maksimum dayanıklılık ve minimum ağırlık prensibiyle tasarlanmıştır.

## 1. Sistem Mimarisi (Topoloji)

```mermaid
graph TD
    A[SUNGUR Taktik Çekirdek] --> B[Aviyonik Paketi]
    A --> C[İtki Modülü]
    A --> D[EH Dayanıklılık Kalkanı]
    
    subgraph "Duyular ve Zekâ (Senses & Brain)"
    B --> B1[EH-Dayanıklı IMU Kümesi]
    B --> B2[AI Görü Edge Motoru]
    B --> B3[Magnetometre & Baro Shield]
    end
    
    subgraph "Güç ve Hareket (Power & Motion)"
    C --> C1[Yüksek Verimli BLDC Sürücü]
    C --> C2[Akıllı Batarya Yönetim Sistemi]
    C --> C3[Aktüatör Yedekleme Sistemi]
    end
    
    subgraph "Kalkan ve Bağlantı (Shield & Link)"
    D --> D1[Sinyal Aldatma Birimi (SDU)]
    D --> D2[Frekans Atlamalı Link]
    D --> D3[Şifreleme Katmanı AES-256]
    end
```

## 2. İtki Sistemi

- **Motorlar:** 4x 2806.5 1300KV Yüksek Verimli BLDC.
- **ESC'ler:** 60A 4-in-1 BLHeli_32 (DSHOT1200 desteği).
- **Pervaneler:** 7 inç Karbon Fiber Takviyeli.

## 3. Aviyonik ve Hesaplama

- **Uçuş Kontrolcüsü (FC):** STM32H743 (Pixhawk Cube Orange+ dengi).
- **Görev Bilgisayarı (CC):** NVIDIA Orin Nano (8GB) - Uçta YZ için.
- **Sensörler:** 
    - Bosch BMI088 IMU
    - Sensirion SDP3x Diferansiyel Basınç Sensörü (Hava Hızı)
    - U-Blox F9P Yüksek Hassasiyetli GNSS (RTK Uyumlu).

## 4. Güç Dağıtımı

- **Batarya:** 6S 4500mAh 100C LiPo / Li-Ion Hibrit.
- **BMS:** Hücre bazlı izleme ve akım şöntü içeren SUNGUR Akıllı BMS.

---
**Egemen Mimari | Donanım Standartları**
