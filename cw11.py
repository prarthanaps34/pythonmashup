from tripdata import get_trip_details
from datetime import datetime
import json

trips = [
    get_trip_details(),
    {
        "city": "London",
        "date": "20-06-2023",
        "comment": "Explored Big Ben and the London Eye."
    },
    {
        "city": "Dubai",
        "date": "10-08-2023",
        "comment": "Enjoyed the beautiful city and desert safari."
    }
]

for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)