#!/usr/bin/env python3
"""
YAML to JSON Converter
Converts any YAML file to JSON format
"""

import yaml
import json
import sys
import os

def convert_yaml_to_json(yaml_file):
    """
    Convert a YAML file to JSON format
    
    Args:
        yaml_file: Path to input YAML file
    """
    try:
        # Generate JSON filename from YAML filename
        json_file = os.path.splitext(yaml_file)[0] + '.json'
        
        # Read YAML file
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        
        # Write to JSON file
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✓ Successfully converted {yaml_file} to {json_file}")
        
        # Display the JSON output
        print("\nJSON Output:")
        print(json.dumps(data, indent=2))
        
    except FileNotFoundError:
        print(f"Error: {yaml_file} not found!")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 yaml_to_json.py <yaml_file>")
        print("Example: python3 yaml_to_json.py app-config.yaml")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    convert_yaml_to_json(yaml_file)
