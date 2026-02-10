# Copyright (c) 2026 Jony Ahammad
# License: MIT

from datetime import datetime, date
from typing import List, Dict

def read_data(filename: str) -> List[Dict]:
    """Reads the CSV file and returns a list of dictionaries with parsed data."""
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split(";")
            if len(parts) < 4:
                continue  # skip invalid lines
            timestamp, consumption, production, temperature = parts[:4]

            # Clean timestamp (remove milliseconds and timezone)
            ts_clean = timestamp.split(".")[0].split("+")[0]
            dt = datetime.strptime(ts_clean, "%Y-%m-%dT%H:%M:%S")

            data.append({
                "date": dt.date(),
                "consumption": float(consumption.replace(",", ".")),
                "production": float(production.replace(",", ".")),
                "temperature": float(temperature.replace(",", "."))
            })
    return data

def show_main_menu() -> str:
    """Displays the main menu and returns the user's choice."""
    print("\nChoose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit")
    return input("Enter choice (1-4): ").strip()

def create_daily_report(data: List[Dict]) -> List[str]:
    """Builds a daily report for a selected date range."""
    start_str = input("Enter start date (dd.mm.yyyy): ").strip()
    end_str = input("Enter end date (dd.mm.yyyy): ").strip()
    start_date = datetime.strptime(start_str, "%d.%m.%Y").date()
    end_date = datetime.strptime(end_str, "%d.%m.%Y").date()

    filtered = [row for row in data if start_date <= row["date"] <= end_date]
    total_consumption = sum(row["consumption"] for row in filtered)
    total_production = sum(row["production"] for row in filtered)
    avg_temp = sum(row["temperature"] for row in filtered) / len(filtered) if filtered else 0

    # Format numbers
    total_consumption_str = f"{total_consumption:.2f}".replace(".", ",")
    total_production_str = f"{total_production:.2f}".replace(".", ",")
    avg_temp_str = f"{avg_temp:.2f}".replace(".", ",")

    lines = [
        "-----------------------------------------------------",
        f"Report for the period {start_str}–{end_str}",
        f"- Total consumption: {total_consumption_str} kWh",
        f"- Total production: {total_production_str} kWh",
        f"- Average temperature: {avg_temp_str} °C"
    ]
    return lines

def create_monthly_report(data: List[Dict]) -> List[str]:
    """Builds a monthly summary report for a selected month."""
    month = int(input("Enter month number (1–12): ").strip())
    filtered = [row for row in data if row["date"].month == month]
    total_consumption = sum(row["consumption"] for row in filtered)
    total_production = sum(row["production"] for row in filtered)
    avg_temp = sum(row["temperature"] for row in filtered) / len(filtered) if filtered else 0

    month_name = date(2025, month, 1).strftime("%B")

    total_consumption_str = f"{total_consumption:.2f}".replace(".", ",")
    total_production_str = f"{total_production:.2f}".replace(".", ",")
    avg_temp_str = f"{avg_temp:.2f}".replace(".", ",")

    lines = [
        "-----------------------------------------------------",
        f"Report for the month: {month_name}",
        f"- Total consumption: {total_consumption_str} kWh",
        f"- Total production: {total_production_str} kWh",
        f"- Average temperature: {avg_temp_str} °C"
    ]
    return lines

def create_yearly_report(data: List[Dict]) -> List[str]:
    """Builds a full-year summary report."""
    total_consumption = sum(row["consumption"] for row in data)
    total_production = sum(row["production"] for row in data)
    avg_temp = sum(row["temperature"] for row in data) / len(data) if data else 0

    total_consumption_str = f"{total_consumption:.2f}".replace(".", ",")
    total_production_str = f"{total_production:.2f}".replace(".", ",")
    avg_temp_str = f"{avg_temp:.2f}".replace(".", ",")

    lines = [
        
        f"Report for the year: 2025",
        f"- Total consumption: {total_consumption_str} kWh",
        f"- Total production: {total_production_str} kWh",
        f"- Average temperature: {avg_temp_str} °C"
    ]
    return lines

def print_report_to_console(lines: List[str]) -> None:
    """Prints the report lines to the console."""
    for line in lines:
        print(line)

def write_report_to_file(lines: List[str]) -> None:
    """Writes the report lines to report.txt."""
    with open("report.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print("Report written to report.txt")

def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    data = read_data("2025.csv")
    while True:
        choice = show_main_menu()
        if choice == "1":
            report = create_daily_report(data)
        elif choice == "2":
            report = create_monthly_report(data)
        elif choice == "3":
            report = create_yearly_report(data)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        print_report_to_console(report)

        # Second menu
        print("\nWhat would you like to do next?")
        print("1) Write the report to the file report.txt")
        print("2) Create a new report")
        print("3) Exit")
        next_choice = input("Enter choice (1-3): ").strip()
        if next_choice == "1":
            write_report_to_file(report)
        elif next_choice == "2":
            continue
        elif next_choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Returning to main menu.")

if __name__ == "__main__":
    main()
