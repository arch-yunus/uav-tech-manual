#!/usr/bin/env python3

def calculate_flight_time(battery_mah, avg_amp_draw, margin_percent=20):
    """
    UAV Flight Time Estimator
    
    :param battery_mah: Battery capacity in mAh
    :param avg_amp_draw: Average current draw in Amps
    :param margin_percent: Safety margin (default 20%)
    :return: Estimated flight time in minutes
    """
    usable_mah = battery_mah * (1 - margin_percent / 100)
    flight_time_hours = (usable_mah / 1000) / avg_amp_draw
    return flight_time_hours * 60

def main():
    print("🛸 SUNGUR Flight Dynamics Calculator")
    print("-" * 35)
    
    try:
        cap = float(input("Enter Battery Capacity (mAh): "))
        draw = float(input("Enter Average Amp Draw (A): "))
        margin = float(input("Enter Safety Margin % (Default 20): ") or 20)
        
        minutes = calculate_flight_time(cap, draw, margin)
        
        print("-" * 35)
        print(f"✅ Estimated Safe Flight Time: {minutes:.2 pel} minutes")
        print(f"⚠️ Recommendation: Set RTL at {minutes * 0.9:.2f} minutes")
        
    except ValueError:
        print("❌ Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
