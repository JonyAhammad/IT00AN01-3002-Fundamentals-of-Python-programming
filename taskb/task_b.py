from datetime import datetime

def print_reservation_number(reservation: list) -> None:
    # Prints the reservation number
    number = int(reservation[0])
    print(f"Reservation number: {number}")

def print_booker(reservation: list) -> None:
    # Prints the booker name
    booker = reservation[1]
    print(f"Booker: {booker}")

def print_date(reservation: list) -> None:
    # Prints the reservation date in Finnish format
    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_date = date.strftime("%d.%m.%Y")
    print(f"Date: {finnish_date}")

def print_start_time(reservation: list) -> None:
    # "Prints the start time in Finnish format"
    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")

def print_hours(reservation: list) -> None:
    # "Prints number of hours"
    hours = int(reservation[4])
    print(f"Number of hours: {hours}")

def print_hourly_rate(reservation: list) -> None:
    # Prints hourly rate
    rate = float(reservation[5])
    rate_str = f"{rate:.2f}".replace('.', ',')
    print(f"Hourly rate: {rate_str} €")

def print_total_price(reservation: list) -> None:
    # "Prints total price"
    hours = int(reservation[4])
    rate = float(reservation[5])
    total = hours * rate
    total_str = f"{total:.2f}".replace('.', ',')
    print(f"Total price: {total_str} €")

def print_paid(reservation: list) -> None:
    # "Prints paid status"
    paid = reservation[6] == "True"
    print(f"Paid: {'Yes' if paid else 'No'}")

def print_venue(reservation: list) -> None:
    # "Prints venue"
    venue = reservation[7]
    print(f"Venue: {venue}")

def print_phone(reservation: list) -> None:
    # "Prints phone number"
    phone = reservation[8]
    print(f"Phone: {phone}")

def print_email(reservation: list) -> None:
    # "Prints email"
    email = reservation[9]
    print(f"Email: {email}")

def main():
    """Reads reservation data from a file and prints it using functions"""

    filename = "reservations.txt"

    with open(filename, "r", encoding="utf-8") as f:
        reservation = f.read().strip().split('|')

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_rate(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_venue(reservation)
    print_phone(reservation)
    print_email(reservation)

if __name__ == "__main__":
    main()
