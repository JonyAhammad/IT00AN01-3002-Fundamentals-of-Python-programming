from datetime import datetime

def main():
    # File name
    filename = "reservations.txt"

    # Read reservation line
    with open(filename, "r", encoding="utf-8") as f:
        reservation = f.read().strip()

    # Split fields
    reservation = reservation.split('|')

    # Convert data types
    reservation_number = int(reservation[0])
    booker = reservation[1]

    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_date = date.strftime("%d.%m.%Y")

    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")

    hours = int(reservation[4])
    hourly_price = float(reservation[5])
    paid = reservation[6] == "True"
    location = reservation[7]
    phone = reservation[8]
    email = reservation[9]

    total_price = hours * hourly_price

    
    hourly_price_str = f"{hourly_price:.2f}".replace('.', ',')
    total_price_str = f"{total_price:.2f}".replace('.', ',')

    # Print output
    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {booker}")
    print(f"Date: {finnish_date}")
    print(f"Start time: {finnish_time}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {hourly_price_str} €")
    print(f"Total price: {total_price_str} €")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()
