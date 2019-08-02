# Convert Yaml to Json

import yaml
import json

def yaml_to_json(yaml_file, json_file=None):
    # Read Yaml Data from File
    try:
        with open(yaml_file,'r') as y:
            yaml_data = yaml.safe_load(y)
    except FileNotFoundError:
        return 'ERROR! Yaml File not Found.'
    except yaml.scanner.ScannerError:
        return 'ERROR! Yaml file is corrupted.'
    # Convert Yaml to Json
    json_data = json.dumps(yaml_data, indent=4)
    # Write Json Data to File
    if json_file:
        with open(json_file,'w') as j:
            j.write(json_data)
    # Return Json Data
    return json_data

print(yaml_to_json('input.yaml','output.json'))

# Alperen Cubuk