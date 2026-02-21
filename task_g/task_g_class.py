# Copyright (c) 2026 Jony Ahammad
# License: MIT

from datetime import datetime
from typing import List


class Reservation:
    """Represents a reservation."""

    def __init__(self, reservation_id, name, email, phone,
                 date, time, duration, price,
                 confirmed, resource, created):

        self.reservation_id = reservation_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.duration = duration
        self.price = price
        self.confirmed = confirmed
        self.resource = resource
        self.created = created

    def is_confirmed(self) -> bool:
        """Returns True if reservation is confirmed."""
        return self.confirmed

    def is_long(self) -> bool:
        """Returns True if reservation lasts 3 hours or more."""
        return self.duration >= 3

    def total_price(self) -> float:
        """Calculates total price of the reservation."""
        return self.duration * self.price


def convert_reservation(data: List[str]) -> Reservation:
    """Converts list data into a Reservation object."""

    return Reservation(
        reservation_id=int(data[0]),
        name=data[1],
        email=data[2],
        phone=data[3],
        date=datetime.strptime(data[4], "%Y-%m-%d").date(),
        time=datetime.strptime(data[5], "%H:%M").time(),
        duration=int(data[6]),
        price=float(data[7]),
        confirmed=data[8].lower() == "true",
        resource=data[9],
        created=datetime.fromisoformat(data[10])
    )


def fetch_reservations(filename: str) -> List[Reservation]:
    """Reads reservations and returns a list of Reservation objects."""
    reservations = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file)

        for line in file:
            parts = line.strip().split("|")
            reservation = convert_reservation(parts)
            reservations.append(reservation)

    return reservations


def print_confirmed(reservations: List[Reservation]) -> None:
    """Prints confirmed reservations."""
    print("\nConfirmed reservations:")

    for reservation in reservations:
        if reservation.is_confirmed():
            print(
                f"- {reservation.name}, {reservation.resource}, "
                f"{reservation.date.strftime('%d.%m.%Y')} at {reservation.time.strftime('%H.%M')}"
            )


def print_long_reservations(reservations: List[Reservation]) -> None:
    """Prints reservations lasting 3 hours or more."""

    print("\nLong reservations (>=3 hours):")

    for reservation in reservations:
        if reservation.is_long():
            print(f"- {reservation.name} ({reservation.duration} hours)")


def calculate_total_revenue(reservations: List[Reservation]) -> None:
    """Calculates total revenue."""

    total = 0

    for reservation in reservations:
        total += reservation.total_price()

    print(f"\nTotal revenue: {total:.2f} €")


def main() -> None:
    """Main function."""

    reservations = fetch_reservations("reservations.txt")

    print_confirmed(reservations)
    print_long_reservations(reservations)
    calculate_total_revenue(reservations)


if __name__ == "__main__":
    main()