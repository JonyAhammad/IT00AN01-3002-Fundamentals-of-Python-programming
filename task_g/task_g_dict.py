# Copyright (c) 2026 Jony Ahammad
# License: MIT

from datetime import datetime
from typing import List, Dict


def convert_reservation(data: List[str]) -> Dict:
    """Converts reservation list data into a dictionary."""
    return {
        "id": int(data[0]),
        "name": data[1],
        "email": data[2],
        "phone": data[3],
        "date": datetime.strptime(data[4], "%Y-%m-%d").date(),
        "time": datetime.strptime(data[5], "%H:%M").time(),
        "duration": int(data[6]),
        "price": float(data[7]),
        "confirmed": data[8].lower() == "true",
        "resource": data[9],
        "created": datetime.fromisoformat(data[10])
    }


def fetch_reservations(filename: str) -> List[Dict]:
    """Reads reservations from a file and returns them as dictionaries."""
    reservations = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # skip header

        for line in file:
            parts = line.strip().split("|")
            reservation = convert_reservation(parts)
            reservations.append(reservation)

    return reservations


def print_confirmed(reservations: List[Dict]) -> None:
    """Prints confirmed reservations."""
    print("\nConfirmed reservations:")
    for reservation in reservations:
        if reservation["confirmed"]:
            print(
                f"- {reservation['name']}, {reservation['resource']}, "
                f"{reservation['date'].strftime('%d.%m.%Y')} at {reservation['time'].strftime('%H.%M')}"
            )


def print_long_reservations(reservations: List[Dict]) -> None:
    """Prints reservations lasting 3 hours or more."""
    print("\nLong reservations (>=3 hours):")
    for reservation in reservations:
        if reservation["duration"] >= 3:
            print(f"- {reservation['name']} ({reservation['duration']} hours)")


def calculate_total_revenue(reservations: List[Dict]) -> None:
    """Calculates and prints total revenue."""
    total = 0
    for reservation in reservations:
        total += reservation["duration"] * reservation["price"]

    print(f"\nTotal revenue: {total:.2f} €")


def main() -> None:
    """Main program."""
    reservations = fetch_reservations("reservations.txt")

    print_confirmed(reservations)
    print_long_reservations(reservations)
    calculate_total_revenue(reservations)


if __name__ == "__main__":
    main()