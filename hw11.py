from tracker import get_record
from datetime import datetime
import json

travel_list = [
    get_record("Munnar", "Beautiful hill station", "05-06-2022"),
    get_record("Kochi", "Visited Fort Kochi", "18-11-2023"),
    get_record("Alappuzha", "Enjoyed the houseboat trip", "12-01-2024")
]

for record in travel_list:
    d = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = d.strftime("%B %d, %Y")

json_data = json.dumps(travel_list, indent=4)

print("JSON String:")
print(json_data)

python_data = json.loads(json_data)

print("\nTravel Records:")
for record in python_data:
    print(record)