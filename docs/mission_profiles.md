# 📋 Modül 4: Görev Profilleri ve Operasyon Planlaması

> **Amaç:** Her görev farklı bir mühendislik problemidir. Bu modül, en yaygın İHA görev tiplerini, her görev için gerekli ekipmanı ve planlama metodolojisini öğretir.

---

## 4.1 Görev Planlaması Temelleri

### Soru Dörtlüsü (Mission Definition Matrix)
Her operasyon öncesi şu 4 soruya cevap verilmeli:

```
1. NE?   → Görev çıktısı nedir? (Harita? Video? Kargo teslimi?)
2. NEREDE? → Operasyon alanı ve hava sahası sınırları?
3. NE ZAMAN? → Hava durumu, gün ışığı, NOTAM kısıtlamaları?
4. NASIL? → Platform, sensör, iletişim ve acil durum planı?
```

---

## 4.2 Görev Profili 1: ISR (Keşif ve Gözetleme)

**Amaç:** Belirli bir alanın fotoğraf veya video ile belgelenmesi.

| Bileşen | Önerilen Seçim | Alternatif |
| :--- | :--- | :--- |
| Platform | Sabit Kanat (uzun menzil) | Hexacopter (hassas hovering) |
| Kamera | Sony A7R (geniş alan) | FLIR Lepton (termal) |
| İletişim | LTE (uzun menzil) | 900MHz Telemetri |
| Uçuş Modu | Waypoint Otopilot | Mission Planner |

**Uçuş Deseni Seçimi:**
```
[Mozaik/Grid Deseni]     [Orbit/Dairesel]     [Corridor Tarama]
    ←→←→←→←→            ────────────           ═══════════
    →←→←→←→←              (merkez)                  ↓
    ←→←→←→←→            ────────────           ═══════════
```

---

## 4.3 Görev Profili 2: Fotogrametri ve 3D Haritalama

**Amaç:** Ortofoto veya 3D nokta bulutu üretmek.

**Kamera Örtüşme (Overlap) Ayarları:**
```
Ön-Arka Örtüşme (Frontlap): 80%  → Daha iyi 3D model, daha fazla fotoğraf
Yan Örtüşme (Sidelap):      70%  → Minimum tavsiye
```

**GCP (Ground Control Point) Kullanımı:**
- GCP'ler, GPS doğruluğunu RTK olmaksızın cm hassasiyete taşır.
- Minimum 4 GCP + 1 doğrulama noktası kullanılır.
- Yazılım: **Agisoft Metashape**, **OpenDroneMap** (açık kaynak).

---

## 4.4 Görev Profili 3: SAR (Arama ve Kurtarma)

**Amaç:** Kayıp şahıs veya araç aramak.

**Kritik Ekipman:**
- **Termal Kamera (FLIR):** Gece ve bitki örtüsü altında vücut ısısı tespiti.
- **Megafon/Hoparlör Payload:** Ses ile iletişim.
- **Real-Time Video Stream:** Yer istasyonuna canlı görüntü.

**Arama Deseni:**
```
[Expanding Square]      [Sector/Radyal]       [Contour/Eş Yükselti]
  ┌─────────────┐           ╱|╲                   Arazi şekline
  │  ┌───────┐  │         ╱  |  ╲                  paralel tarama
  │  │ NOKTA │  │        ╱   |   ╲
  │  └───────┘  │       ╱    |    ╲
  └─────────────┘
```

---

## 4.5 Görev Profili 4: Kargo Teslimatı

**Amaç:** Belirli bir noktaya yük bırakmak.

**Mühendislik Hesaplamaları:**
```python
# Yük kapasitesi hesabı
max_kargo_g = (toplam_itki_g - platform_kalkis_agirligi_g) / guvenlik_katsayisi
# Güvenlik katsayısı = 1.5 önerilir

# Uçuş süresi etkisi (yaklaşık)
# Her 100g ek yük ≈ %3-5 uçuş süresi kaybı
```

---

## 📝 Pratik Alıştırma

1. 500 dönüm (5km²) arazi fotogrametri görevi için grid deseni planla. Kaç fotoğraf çekilir?
2. Simülatörde waypoint görevi tanımla ve telemetri panelinde rotayı izle.

---

*Sonraki Modül → [Elektronik Harp ve Dayanıklı Haberleşme](tactical_ew.md)*
