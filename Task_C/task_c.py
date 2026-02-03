from datetime import datetime

HEADERS = [
    "reservationId",
    "name",
    "email",
    "phone",
    "reservationDate",
    "reservationTime",
    "durationHours",
    "price",
    "confirmed",
    "reservedResource",
    "createdAt",
]

def convert_reservation_data(reservation: list) -> list:
    """
    Convert reservation data types
    """
    reservation_id = int(reservation[0])
    name = reservation[1]
    email = reservation[2]
    phone = reservation[3]
    reservation_date = datetime.strptime(reservation[4], "%Y-%m-%d").date()
    reservation_time = datetime.strptime(reservation[5], "%H:%M").time()
    duration_hours = int(reservation[6])
    price = float(reservation[7])
    confirmed = reservation[8] == "True"
    reserved_resource = reservation[9]
    created_at = datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id, name, email, phone,
        reservation_date, reservation_time,
        duration_hours, price,
        confirmed, reserved_resource,
        created_at
    ]

def fetch_reservations(reservation_file: str) -> list:
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.strip().split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations

# PART B FUNCTIONS #

def confirmed_reservations(reservations: list[list]) -> None:
    print("1) Confirmed Reservations")
    for r in reservations:
        if r[8]:  # confirmed == True
            print(f"- {r[1]}, {r[9]}, {r[4].strftime('%d.%m.%Y')} at {r[5].strftime('%H.%M')}")
    print()

def long_reservations(reservations: list[list]) -> None:
    print("2) Long Reservations (≥ 3 h)")
    for r in reservations:
        if r[6] >= 3:  # durationHours >= 3
            print(f"- {r[1]}, {r[4].strftime('%d.%m.%Y')} at {r[5].strftime('%H.%M')}, duration {r[6]} h, {r[9]}")
    print()

def confirmation_statuses(reservations: list[list]) -> None:
    print("3) Reservation Confirmation Status")
    for r in reservations:
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{r[1]} → {status}")
    print()

def confirmation_summary(reservations: list[list]) -> None:
    confirmed_count = sum(r[8] for r in reservations)
    not_confirmed_count = len(reservations) - confirmed_count
    print("4) Confirmation Summary")
    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")
    print()

def total_revenue(reservations: list[list]) -> None:
    revenue = sum(r[7] * r[6] for r in reservations if r[8])  # price * durationHours for confirmed
    amount_str = f"{revenue:.2f}".replace(".", ",")
    print("5) Total Revenue from Confirmed Reservations")
    print(f"Total revenue from confirmed reservations: {amount_str} €")
    print()

#  MAIN  #

def main():
    reservations = fetch_reservations("reservations.txt")

    # PART A: Print all reservations and data types
    print(" | ".join(HEADERS))
    print("-" * 120)
    for reservation in reservations:
        print(" | ".join(str(x) for x in reservation))
        print(" | ".join(type(x).__name__ for x in reservation))
        print("-" * 120)

    # PART B: Print summaries
    confirmed_reservations(reservations)
    long_reservations(reservations)
    confirmation_statuses(reservations)
    confirmation_summary(reservations)
    total_revenue(reservations)

if __name__ == "__main__":
    main()
