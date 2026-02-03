# Copyright (c) 2026 Jony Ahammad
# License: MIT

from datetime import datetime, date
from typing import List, Dict

WEEKDAYS_FI = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEKDAYS_FI = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

def read_data(filename: str) -> List[Dict]:
    
    # Reads a CSV file 
    
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(";")
            ts = datetime.fromisoformat(parts[0])
            consumption = [float(parts[1]), float(parts[2]), float(parts[3])]
            production = [float(parts[4]), float(parts[5]), float(parts[6])]
            data.append({"timestamp": ts, "consumption": consumption, "production": production})
    return data

def daily_summary(data: List[Dict]) -> List[Dict]:
    
    # Calculates daily totals for consumption and production (in kWh) from the data list.
    
    
    summary = []
    current_day = None
    totals = {"consumption": [0, 0, 0], "production": [0, 0, 0]}

    for row in data:
        day = row["timestamp"].date()
        if current_day is None:
            current_day = day

        if day != current_day:
            summary.append({
                "weekday": WEEKDAYS_FI[current_day.weekday()],
                "date": current_day,
                "consumption": [v / 1000 for v in totals["consumption"]],
                "production": [v / 1000 for v in totals["production"]]
            })
            totals = {"consumption": [0, 0, 0], "production": [0, 0, 0]}
            current_day = day

        for i in range(3):
            totals["consumption"][i] += row["consumption"][i]
            totals["production"][i] += row["production"][i]

    # add last day
    summary.append({
        "weekday": WEEKDAYS_FI[current_day.weekday()],
        "date": current_day,
        "consumption": [v / 1000 for v in totals["consumption"]],
        "production": [v / 1000 for v in totals["production"]]
    })

    return summary

def format_row(day_summary: Dict) -> str:
    """
    Formats a single day summary dictionary as a table row string with Finnish formatting.
    """
    date_str = f"{day_summary['date'].day:02}.{day_summary['date'].month:02}.{day_summary['date'].year}"
    cons_str = "   ".join(f"{v:.2f}".replace(".", ",") for v in day_summary["consumption"])
    prod_str = "   ".join(f"{v:.2f}".replace(".", ",") for v in day_summary["production"])
    return f"{day_summary['weekday']:<10} {date_str}   {cons_str:<10}   {prod_str}"

def write_report(weeks_data: Dict[str, List[Dict]]) -> None:
    """
    Writes the summaries of all weeks to 'summary.txt' in a clear table format.
    """
    with open("summary.txt", "w", encoding="utf-8") as f:
        for week, data in weeks_data.items():
            f.write(f"Week {week} electricity consumption and production (kWh, by phase)\n")
            f.write(f"Day        Date        Consumption [kWh]        Production [kWh]\n")
            f.write(f"           (dd.mm.yyyy)  v1      v2      v3       v1     v2      v3\n")
            f.write("-" * 70 + "\n")
            for day_summary in data:
                f.write(format_row(day_summary) + "\n")
            f.write("\n")

def main() -> None:
    """
    Main function: reads CSV files for weeks 41-43, computes daily summaries, and writes report to summary.txt
    """
    files = {"41": "week41.csv", "42": "week42.csv", "43": "week43.csv"}
    weeks_data = {}
    for week, filename in files.items():
        data = read_data(filename)
        weeks_data[week] = daily_summary(data)
    
    write_report(weeks_data)
    print("Report generated: summary.txt")

if __name__ == "__main__":
    main()
