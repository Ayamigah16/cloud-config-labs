# Cloud Config Labs
A hands-on learning repository focused on configuration-as-code fundamentals using YAML and JSON. This project is designed to help learners and early-career engineers build production-ready configuration patterns  

## Learning Objectives

- By working through this repository, you will learn how to:

- Write well-formed YAML and JSON configuration files

- Understand and apply indentation, mappings, and scalars in YAML

- Validate configuration files before deployment

- Convert YAML configurations to JSON

## Prerequisites

- Python 3 with PyYAML library
- Text editor (VS Code recommended)
- Optional: `yq` for command-line conversion

---

### Installation

#### Install yq (YAML processor)
```bash
sudo snap install yq
```

Verify installation:
```bash
yq --version
```

#### Install PyYAML (Python library)
```bash
pip install pyyaml
```

---

### Validation Tools

- Online: https://yamlvalidator.com
- Online: https://jsonlint.com
- Command line: Use the Python validation command above

---
 
### Repository Structure

```
scripting-and-cloud-fundamentals/
├── README.md              # Lab documentation and instructions
├── app-config.yaml        # YAML configuration file
├── app-config.json        # JSON version of the configuration
└── yaml_to_json.py        # Python conversion script
```

---

### Application Configuration Structure
- ***app-config.yaml***

```yaml
application:
  name: my-web-app
  version: 1.0.0
  environment: production

server:
  host: 0.0.0.0
  port: 8080

database:
  engine: mysql
  host: db.example.com
  port: 3306
  username: admin
  password: mysecurepassword
```

### Usage

#### Validate YAML Syntax
```bash
python3 -c "import yaml; yaml.safe_load(open('app-config.yaml'))"
```

#### Convert YAML to JSON

**Option 1: Using yq**
```bash
yq eval -o=json app-config.yaml > app-config.json
```

**Option 2: Using Python Script**
```bash
python3 yaml_to_json.py <yaml_file>

# Example
python3 yaml_to_json.py app-config.yaml
```

The script will automatically create a JSON file with the same base name (e.g., `app-config.yaml` → `app-config.json`)

**Option 3: Manual Python Command (Advanced)**
```bash
python3 -c "import yaml, json; data = yaml.safe_load(open('app-config.yaml')); print(json.dumps(data, indent=2))" > app-config.json
```

---
### YAML Best Practices

✓ Use consistent spacing (2 or 4 spaces per indentation level)  
✓ Avoid using tabs in YAML files  
✓ Always validate your configuration before deploying  
✓ Use meaningful key names  
✓ Keep configurations organized in logical sections  



### Expected Outcome

A valid YAML configuration file that accurately represents the application's structure and parameters, along with its JSON equivalent for use in different contexts.

### Lab Completion Checklist

- [✔️] Created app-config.yaml with proper indentation
- [✔️] Validated YAML syntax
- [✔️] Converted YAML to JSON format
- [✔️] Created Python conversion script
- [✔️] Documented the lab in README

---
