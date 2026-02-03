import csv
from datetime import datetime, date
from typing import List, Dict

# Finnish weekdays
WEEKDAYS_FI = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEKDAYS_FI_NAMES = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

def read_data(filename: str) -> List[Dict]:
   
    rows = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for line in reader:
            row = {
                "timestamp": datetime.fromisoformat(line["Time"]),
                "cons_v1": int(line["Consumption phase 1 Wh"]),
                "cons_v2": int(line["Consumption phase 2 Wh"]),
                "cons_v3": int(line["Consumption phase 3 Wh"]),
                "prod_v1": int(line["Production phase 1 Wh"]),
                "prod_v2": int(line["Production phase 2 Wh"]),
                "prod_v3": int(line["Production phase 3 Wh"]),
            }
            rows.append(row)
    return rows

def calculate_daily_totals(rows: List[Dict]) -> Dict[date, Dict[str, float]]:
    

    daily_totals = {}
    for row in rows:
        d = row["timestamp"].date()
        if d not in daily_totals:
            daily_totals[d] = {
                "cons_v1": 0, "cons_v2": 0, "cons_v3": 0,
                "prod_v1": 0, "prod_v2": 0, "prod_v3": 0
            }
        # Add Wh values and convert to kWh later in printing
        daily_totals[d]["cons_v1"] += row["cons_v1"]
        daily_totals[d]["cons_v2"] += row["cons_v2"]
        daily_totals[d]["cons_v3"] += row["cons_v3"]
        daily_totals[d]["prod_v1"] += row["prod_v1"]
        daily_totals[d]["prod_v2"] += row["prod_v2"]
        daily_totals[d]["prod_v3"] += row["prod_v3"]
    return daily_totals

def print_report(daily_totals: Dict[date, Dict[str, float]]) -> None:
    """
    Prints a user-friendly report of daily electricity consumption and production.

    Parameters:
        daily_totals (Dict[date, Dict[str, float]]): Daily totals in Wh
    """
    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print(f"{'Day':<12} {'Date':<12} {'Consumption [kWh]':<30} {'Production [kWh]':<25}")
    print(f"{'':<24} {'v1':>7} {'v2':>7} {'v3':>7} {'v1':>7} {'v2':>7} {'v3':>7}")
    print("-" * 80)

    # Sort by date
    sorted_dates = sorted(daily_totals.keys())
    for d in sorted_dates:
        weekday_index = d.weekday()  
        weekday_name_fi = WEEKDAYS_FI_NAMES[weekday_index]

        totals = daily_totals[d]
        # Convert Wh → kWh 
        cons_v1 = f"{totals['cons_v1']/1000:.2f}".replace(".", ",")
        cons_v2 = f"{totals['cons_v2']/1000:.2f}".replace(".", ",")
        cons_v3 = f"{totals['cons_v3']/1000:.2f}".replace(".", ",")
        prod_v1 = f"{totals['prod_v1']/1000:.2f}".replace(".", ",")
        prod_v2 = f"{totals['prod_v2']/1000:.2f}".replace(".", ",")
        prod_v3 = f"{totals['prod_v3']/1000:.2f}".replace(".", ",")

        print(f"{weekday_name_fi:<12} {d.strftime('%d.%m.%Y'):<12} "
              f"{cons_v1:>7} {cons_v2:>7} {cons_v3:>7} "
              f"{prod_v1:>7} {prod_v2:>7} {prod_v3:>7}")

def main() -> None:
    
    # Main function: reads data, computes daily totals and prints report
    
    filename = "week42.csv"
    rows = read_data(filename)
    daily_totals = calculate_daily_totals(rows)
    print_report(daily_totals)

if __name__ == "__main__":
    main()
