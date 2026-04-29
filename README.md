![UAV Teknik Şema](assets/tech_manual_schematic.png)

# 🦅 SUNGUR Teknik Kılavuz: SUNGUR Sistem Referansı `v3.0-SUNGUR`

[![Donanım Standartı](https://img.shields.io/badge/Standart-MIL--STD--810G-orange?style=for-the-badge&logo=bosch)](https://github.com/arch-yunus/uav-tech-manual)
[![Dökümantasyon](https://img.shields.io/badge/Durum-Tam--Dökümante-success?style=for-the-badge&logo=readme)](https://github.com/arch-yunus/uav-tech-manual)
[![Bakım](https://img.shields.io/badge/Periyot-25s--Servis-yellow?style=for-the-badge&logo=ifixit)](https://github.com/arch-yunus/uav-tech-manual)

> **"Göklerin derinliğinde, teknoloji ve ruhun muazzam raksı."**

**SUNGUR Teknik Deposu**'na hoş geldiniz—SUNGUR İHA ekosistemi için donanım spesifikasyonları, bakım protokolleri ve taktik operasyonel standartların kesin kaynağı. Bu sadece bir kılavuz değil; gökyüzündeki hakimiyetin stratejik temelidir.

---

## 🛰️ Stratejik Vizyon ve LCHI Felsefesi

**SUNGUR Platformu**, **Düşük-Maliyet Yüksek-Etki (LCHI)** doktrini altında mühendislik edilmiştir. Bu felsefe, sadece ekonomik bir tercih değil, asimetrik harp ortamlarında sürdürülebilirlik ve hızlı ölçeklenebilirlik için teknik bir zorunluluktur.

### 🛡️ Siber-Asabiyet (Cyber-Solidarity)
Sistemin her katmanı, teknik disiplin ve ruhsal odaklanmanın bir birleşimidir. En yoğun Elektronik Harp (EH) ortamlarında dahi sistemin operasyonel bütünlüğünü koruması, bu "dirençli asabiyet" kültürü ile sağlanır.

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

Sistemin donanım mimarisi, hata toleransı yüksek ve modüler bir yapı üzerine kuruludur. Her birim, bağımsız bir "Fail-Safe" mekanizmasına sahiptir.

```mermaid
graph TD
    A[SUNGUR Taktik Çekirdek] --> B[Aviyonik Paketi]
    A --> C[İtki Modülü]
    A --> D[EH Dayanıklılık Kalkanı]
    
    subgraph "Senses & Brain"
    B --> B1[EH-Dayanıklı IMU Kümesi]
    B --> B2[AI Görü Edge Motoru]
    B --> B3[Magnetometre & Baro Shield]
    end
    
    subgraph "Power & Motion"
    C --> C1[Yüksek Verimli BLDC Sürücü]
    C --> C2[Akıllı Batarya Yönetim Sistemi]
    C --> C3[Aktüatör Yedekleme Sistemi]
    end
    
    subgraph "Shield & Link"
    D --> D1[Sinyal Aldatma Birimi (SDU)]
    D --> D2[Frekans Atlamalı Link]
    D --> D3[Encryption Layer AES-256]
    end
```

---

## 📐 Kritik Sistem Parametreleri ve Toleranslar

Maksimum operasyonel verimlilik için aşağıdaki nominal ve limit değerler esas alınmalıdır. Bu değerlerin dışındaki operasyonlar sistem bütünlüğünü tehlikeye atar.

### Performans Matrisi
- **Maksimum İrtifa:** 500m (Nominal) / 2500m (Limit AGL)
- **Seyir Hızı:** 15 m/s (Nominal) / 28 m/s (Limit Dash)
- **Operasyonel Menzil:** 5km (Nominal) / 12km (Limit C2 Link)
- **Rüzgar Dayanımı:** 20 km/s (Nominal) / 35 km/s (Limit Gust)

### Güç ve Enerji
- **Sistem Voltajı:** 22.2V (Nominal 6S) / 25.2V (Max Charge)
- **Kritik Voltaj:** 3.4V (Hücre başı acil iniş eşiği)

---

## 🔧 Bakım Periyotları ve Servis Protokolü

LCHI doktrini uyarınca, sistemin ömrünü uzatmak için periyodik bakım zorunludur.

| Periyot | Kontrol Noktası | Eylem |
| :--- | :--- | :--- |
| **Her Uçuş Öncesi** | Pervane & Motor | Çatlak ve gevşeklik kontrolü, elle tork testi. |
| **10 Saat Uçuş** | Konektör & Kablo | XT60 ve sinyal kablolarında korozyon/ısınma izi. |
| **25 Saat Uçuş** | Full Sistem Servis | Rulman yağlaması, gövde stres analizi, yazılım güncelleme. |
| **50 Saat Uçuş** | Batarya Sağlığı | İç direnç (mΩ) ölçümü ve kapasite testi. |

---

## 🚨 Güvenlik ve Acil Durum (Failsafe) Refleksleri

Sistem, insan hatasını veya dış saldırıları minimize etmek için şu otomatik reflekslere sahiptir:

1.  **Bağlantı Kaybı (Link Loss)**: 3 saniye süreyle sinyal alınamazsa otonom RTH (Eve Dönüş) başlar.
2.  **GPS Aldatmacası (Spoofing)**: GNSS verisi ile IMU verisi arasında >5m sapma saptandığında, sistem "Dead Reckoning" moduna geçer.
3.  **EH Tehdit Algılama**: Spektrumda anormal gürültü artışı olduğunda, frekans atlama hızı (hop rate) otomatik olarak artırılır.

---

## 📂 Depo Mimarisi

```bash
uav-tech-manual/
├── docs/               # Teknik Spesifikasyonlar ve Protokoller
│   ├── hardware_specs.md   # Donanım bileşen detayları
│   ├── flight_ops.md       # Uçuş operasyon standartları
│   ├── maintenance.md      # Bakım ve onarım kılavuzu
│   ├── mission_profiles.md # Görev odaklı senaryolar
│   ├── tactical_ew.md      # Elektronik Harp stratejileri
│   └── philosophy.md       # Siber-Asabiyet doktrini
├── assets/             # Şemalar ve Teknik Görseller
└── README.md           # Ana Giriş Kapısı
```

---

## 🚀 Hızlı Operasyonel Dağıtım

1.  **Güç Kontrolü**: Hücre dengesini doğrulayın (hücre başı min 3.7V).
2.  **IMU Kalibrasyonu**: Birincil IMU kümesinde sıfır sapma olduğundan emin olun.
3.  **EH Kalkanı**: OMEGA-tier aldatma modüllerini **SUNGUR Mission Control** üzerinden aktif edin.
4.  **Senkronizasyon**: Gerçek zamanlı telemetri doğrulaması için Taktik HUD ile bağlantı kurun.

---

---

## 🌌 Gelecek Vizyonu: Omni-Domain Egemenliği

SUNGUR ekosistemi, sadece gökyüzüyle sınırlı kalmayacak. **SUNGUR-OMNI** projesi ile denizlerin derinliğinden uzayın sessizliğine kadar her ortamda var olabilen, karada otonom hareket kabiliyetine sahip "Omni-Domain" platformlar üzerine çalışıyoruz.

> *"Sınırları teknoloji belirlemez, irade belirler."*

---

**arch-yunus tarafından ⚔️ ile geliştirilmiştir.**
