![UAV Teknik Şema](assets/tech_manual_schematic.png)

# 🦅 UAV Teknik Kılavuz: ARGUS Sistem Referansı `v3.0-Egemen`

[![Donanım Standartı](https://img.shields.io/badge/Standart-MIL--STD--810G-orange?style=for-the-badge&logo=bosch)](https://github.com/arch-yunus/uav-tech-manual)
[![Dökümantasyon](https://img.shields.io/badge/Durum-Tam--Dökümante-success?style=for-the-badge&logo=readme)](https://github.com/arch-yunus/uav-tech-manual)
[![Bakım](https://img.shields.io/badge/Periyot-25s--Servis-yellow?style=for-the-badge&logo=ifixit)](https://github.com/arch-yunus/uav-tech-manual)

> **"Göklerin derinliğinde, teknoloji ve ruhun muazzam raksı."**

**ARGUS Teknik Deposu**'na hoş geldiniz—ARGUS İHA ekosistemi için donanım spesifikasyonları, bakım protokolleri ve taktik operasyonel standartların kesin kaynağı. Bu sadece bir kılavuz değil; gökyüzündeki hakimiyetin stratejik temelidir.

---

## 🛰️ Stratejik Vizyon ve LCHI Felsefesi

**ARGUS Platformu**, **Düşük-Maliyet Yüksek-Etki (LCHI)** doktrini altında mühendislik edilmiştir. Modüler dayanıklılığa öncelik veriyoruz; en yoğun Elektronik Harp (EH) ortamlarında bile sistemin operasyonel bütünlüğünü teknik disiplin ve ruhsal odaklanma (*Siber-Asabiyet*) ile korumasını sağlıyoruz.

### 📜 Operasyonel Ana Modüller

| Modül | Teknik Odak | Operasyonel Durum |
| :--- | :--- | :--- |
| 🛠️ [Donanım Özellikleri](docs/hardware_specs.md) | İtki, Aviyonik ve Gövde Bütünlüğü | 🟢 Operasyonel |
| ✈️ [Uçuş Operasyonları](docs/flight_ops.md) | Uçuş Öncesi, Esnası ve Sonrası SOP'lar | 🟢 Operasyonel |
| 📋 [Görev Profilleri](docs/mission_profiles.md) | ISR, EH Aldatmacası ve Lojistik Görevler | 🟢 Operasyonel |
| 🔧 [Bakım ve Onarım](docs/maintenance.md) | Periyodik Servis ve Saha Onarım Rehberi | 🟢 Operasyonel |
| 📡 [Taktik EH](docs/tactical_ew.md) | Karıştırma Önleme ve Dayanıklı Navigasyon | 🟢 Operasyonel |
| ⚔️ [Felsefe](docs/philosophy.md) | Makinenin Ruhu ve Disiplin | 🟢 Operasyonel |

---

## 🛠️ Sistem Özeti (Mantıksal Topoloji)

```mermaid
graph TD
    A[ARGUS Taktik Çekirdek] --> B[Aviyonik Paketi]
    A --> C[İtki Modülü]
    A --> D[EH Dayanıklılık Kalkanı]
    
    B --> B1[EH-Dayanıklı IMU Kümesi]
    B --> B2[AI Görü Edge Motoru]
    
    C --> C1[Yüksek Verimli BLDC Sürücü]
    C --> C2[Akıllı Batarya Yönetim Sistemi]
    
    D --> D1[Sinyal Aldatma Birimi (SDU)]
    D --> D2[Frekans Atlamalı Link]
```

---

## 📂 Depo Mimarisi

```bash
uav-tech-manual/
├── docs/               # Teknik Spesifikasyonlar ve Protokoller
│   ├── hardware_specs.md
│   ├── flight_ops.md
│   ├── maintenance.md
│   ├── mission_profiles.md
│   ├── tactical_ew.md
│   └── philosophy.md
├── assets/             # Şemalar ve Teknik Görseller
└── README.md           # Ana Giriş Kapısı
```

---

## 🚀 Hızlı Operasyonel Dağıtım

1.  **Güç Kontrolü**: Hücre dengesini doğrulayın (hücre başı min 3.7V).
2.  **IMU Kalibrasyonu**: Birincil IMU kümesinde sıfır sapma olduğundan emin olun.
3.  **EH Kalkanı**: OMEGA-tier aldatma modüllerini **ARGUS Mission Control** üzerinden aktif edin.
4.  **Senkronizasyon**: Gerçek zamanlı telemetri doğrulaması için Taktik HUD ile bağlantı kurun.

---

**arch-yunus tarafından ⚔️ ile geliştirilmiştir.**
