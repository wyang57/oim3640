import requests

# Fetch Massachusetts data using your token
response = requests.get(
    'https://oim.108122.xyz/mass',
    headers={'X-Token': 'kalibkalib'},  # your first name x2
)

data = response.json()

# Safety check: ensure the API returned what we expect
if "data" not in data:
    print("Unexpected API format:", data)
    exit()

towns = data["data"]

# Find the smallest town by population
smallest = min(towns, key=lambda t: t["population"])

print("Smallest town in Massachusetts:")
print(f"{smallest['name']} — population {smallest['population']:,}")
