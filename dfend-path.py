import json
import os

# Load JSON data from the file
with open('dfend.json', 'r') as json_file:
    data = json.load(json_file)

# Filter out addresses that are not valid
filtered_addresses = []
for address in data['addresses']:
    if 'path' in address and os.path.exists(address['path']):
        filtered_addresses.append(address)

# Update the data with filtered addresses
data['addresses'] = filtered_addresses

# Save the updated data back to a new file
with open('path.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)