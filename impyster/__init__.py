from .generator import EmployeeGenerator, CompanyGenerator, DataExporter

# Convenience functions
def generate_employee(**kwargs):
    return EmployeeGenerator().generate_employee(**kwargs)

def generate_employees(count=10, **kwargs):
    return EmployeeGenerator().generate_employees(count, **kwargs)

def generate_company(**kwargs):
    return CompanyGenerator().generate_company(**kwargs)

def generate_department(**kwargs):
    return CompanyGenerator().generate_department(**kwargs)