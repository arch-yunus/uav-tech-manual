# 🛠️ Hardware Specifications & Component Topology

ARGUS platformunun fiziksel katmanı, maksimum dayanıklılık ve minimum ağırlık prensibiyle tasarlanmıştır.

## 1. Propulsion System (İtki Sistemi)

- **Motors:** 4x 2806.5 1300KV High-Efficiency BLDC.
- **ESCs:** 60A 4-in-1 BLHeli_32 (DSHOT1200 support).
- **Propellers:** 7-inch Carbon Fiber Reinforced.

## 2. Avionics & Computation (Aviyonik & İşlem Gücü)

- **Flight Controller (FC):** STM32H743 (Pixhawk Cube Orange+ equivalent).
- **Companion Computer (CC):** NVIDIA Orin Nano (8GB) for Edge AI.
- **Sensors:** 
    - Bosch BMI088 IMU
    - Sensirion SDP3x Differential Pressure Sensor (Airspeed)
    - U-Blox F9P High-Precision GNSS (RTK Ready).

## 3. Power Distribution (Güç Dağıtımı)

- **Battery:** 6S 4500mAh 100C LiPo / Li-Ion Hybrid.
- **BMS:** Sovereign Smart BMS with per-cell monitoring and current shunt.

---
**Sovereign Architecture | Hardware Standards**
