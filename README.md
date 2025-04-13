# ImPyster 🐍

[![PyPI version](https://img.shields.io/pypi/v/impyster.svg)](https://pypi.org/project/impyster/)
[![Python Versions](https://img.shields.io/pypi/pyversions/impyster.svg)](https://pypi.org/project/impyster/)
[![Downloads](https://static.pepy.tech/badge/impyster)](https://pepy.tech/project/impyster)
[![License](https://img.shields.io/github/license/yourusername/impyster.svg)](https://github.com/yourusername/impyster/blob/main/LICENSE)

**Generate realistic fake corporate data for Python backends**

ImPyster is a powerful, opinionated fake data generator built specifically for Python backend developers. Whether you're prototyping a Flask app, populating your Django test database, or setting up staging environments, ImPyster gives you realistic corporate data in seconds.

## Features ✨

- 🏢 **Corporate-focused**: Employee records, company profiles, departments, and more
- 🧰 **Python-native API**: Simple, intuitive interfaces designed for backend workflows
- 🔄 **Multiple output formats**: Export to JSON, CSV, or Python dictionaries
- 🛠️ **Customizable schemas**: Define your own data structures and relationships
- 💻 **CLI support**: Generate data without writing code

## Installation 📦

```bash
pip install impyster
```

## Quick Start 🚀

### Python API

```python
from impyster import generate_employees, generate_company

# Generate a single company
company = generate_company(industry="tech")
print(company)
# {'name': 'Quantum Systems', 'domain': 'quantumsystems.com', 'founded': '2015-03-12', ...}

# Generate 5 employees for this company
employees = generate_employees(5, company=company['name'])
print(employees[0])
# {'id': 'EMP-00421', 'name': 'Sarah Johnson', 'email': 'sarah.johnson@quantumsystems.com', ...}
```

### Command Line

```bash
# Generate 10 employees and output as JSON
impyster employee 10 --format json > employees.json

# Generate a company profile with tech industry focus
impyster company 1 --industry tech --format json > company.json

# Generate 5 departments with 3-8 employees each
impyster department 5 --employees-min 3 --employees-max 8 --format csv > departments.csv
```

## Data Types 📊

ImPyster can generate various types of corporate data:

### Employees

- Employee IDs (customizable formats)
- Names (diverse and realistic)
- Corporate emails
- Job titles and departments
- Hire dates and employment status
- Salary ranges and employee types

### Companies

- Company names and domains
- Industry classifications
- Founding dates
- Company sizes
- Corporate addresses and contact info

### Departments

- Department names and codes
- Reporting structures
- Budget allocations
- Department heads and team members

## Advanced Usage: Schemas 🏗️

Define custom data structures with schemas:

```python
from impyster import generate_from_schema

# Define a custom schema
schema = {
    "employee": {
        "id": "EMP-{number:5}",
        "name": "{first_name} {last_name}",
        "email": "{first_name}.{last_name}@{company_domain}",
        "department": ["Engineering", "Marketing", "Sales"],
        "hire_date": {"type": "date", "min": "2020-01-01", "max": "2023-12-31"},
        "manager": {"type": "bool", "probability": 0.15}
    }
}

# Generate 10 records based on this schema
data = generate_from_schema(schema, count=10)
```

## Custom Templates 📝

Create templates for specialized formats:

```python
from impyster import generate_from_template

template = """
## Employee Record
- **ID**: {{employee.id}}
- **Name**: {{employee.name}}
- **Department**: {{employee.department}}
- **Contact**: {{employee.email}}
"""

# Generate 5 records using this template
records = generate_from_template(template, count=5, data_type="employee")
```

## CLI Reference 📚

ImPyster's command line interface provides flexible options:

```
Usage: impyster [OPTIONS] DATA_TYPE COUNT

  Generate fake corporate data

Arguments:
  DATA_TYPE  [required] Type of data to generate: employee, company, or department
  COUNT      [required] Number of records to generate

Options:
  --format TEXT           Output format: json or csv  [default: json]
  --pretty                Pretty-print JSON output
  --seed INTEGER          Random seed for reproducible results
  --output PATH           Output file path (defaults to stdout)
  --schema PATH           Path to custom schema file
  --help                  Show this message and exit.
```

## Python API Reference 📖

### Core Functions

- `generate_employee(**kwargs)` - Generate a single employee
- `generate_employees(count=10, **kwargs)` - Generate multiple employees
- `generate_company(**kwargs)` - Generate company profile
- `generate_department(**kwargs)` - Generate department information
- `generate_from_schema(schema, count=1)` - Generate data from custom schema
- `generate_from_template(template, count=1, data_type="employee")` - Generate using custom template

### Exporters

- `export_to_json(data, pretty=False)` - Export data to JSON string
- `export_to_csv(data)` - Export data to CSV string
- `save_to_file(data, format="json", filepath="output.json")` - Save data to file

## Development 🛠️

Contributions are welcome! To set up your development environment:

```bash
git clone https://github.com/yourusername/impyster.git
cd impyster
pip install -e ".[dev]"
pytest
```

## License 📄

MIT

---

Made with ❤️ for Python backend developers. Happy coding!
