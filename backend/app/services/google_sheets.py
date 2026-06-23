import gspread

from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


credentials = Credentials.from_service_account_file(
    "backend/credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(credentials)

sheet = client.open(
    "Horse Booking"
).worksheet(
    "Bookings"
)

def add_booking_row(booking):
    sheet.append_row(
        [
            booking.id,
            booking.client_name,
            booking.phone,
            booking.gender,
            booking.people_count,
            str(booking.booking_time),
            str(booking.end_time),
            booking.duration,
            booking.status
        ]
    )
def update_booking_status(
    booking_id,
    status
):

    records = sheet.get_all_records()

    for index, row in enumerate(
        records,
        start=2
    ):

        if row["ID"] == booking_id:

            sheet.update_cell(
                index,
                9,
                status
            )

            break