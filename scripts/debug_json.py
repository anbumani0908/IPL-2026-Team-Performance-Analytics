import json
from pprint import pprint

# Open one sample match file
with open("../raw_json/1527674.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 50)
print("TOP LEVEL KEYS")
print("=" * 50)
print(data.keys())

print("\n" + "=" * 50)
print("MATCH INFO")
print("=" * 50)
pprint(data["info"])

print("\n" + "=" * 50)
print("FIRST INNINGS")
print("=" * 50)

innings = data["innings"]

print("Number of innings:", len(innings))

first_innings = innings[0]

pprint(first_innings.keys())

print("\n" + "=" * 50)
print("FIRST OVER")
print("=" * 50)

first_over = first_innings["overs"][0]

pprint(first_over)

print("\n" + "=" * 50)
print("FIRST DELIVERY")
print("=" * 50)

first_delivery = first_over["deliveries"][0]

pprint(first_delivery)

print("\n" + "=" * 50)
print("DELIVERY KEYS")
print("=" * 50)

print(first_delivery.keys())