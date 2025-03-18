import json
import os
import ast
from collections import defaultdict
from datetime import datetime
import xml.etree.ElementTree as ET

def write_coverage_report():
    """Salva i dati di copertura in un file JSON."""
    
    line_rate, branch_rate = extract_models_coverage(xml_file)
    #condition_rate = calculate_condition_coverage(xml_file)
    
    data = {
        "line_coverage": round(line_rate * 100, 2),
        "branch_coverage": round(branch_rate * 100, 2),
        #"condition_coverage": round(condition_rate, 2)
    }
    
    return data


def extract_models_coverage(xml_file):
    """Estrae i dati di copertura relativi ai modelli."""
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Retrive line and branch coverage
    line_rate = float(root.get('line-rate'))
    branch_rate = float(root.get('branch-rate'))
    return line_rate, branch_rate


# LETTERALMENTE IL BRANCH COVERAGE E' LA STESSA ROBA
# def calculate_condition_coverage(xml_file):
#     """Calculates the average condition coverage from the XML report."""
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
    
#     total_conditions = 0
#     covered_conditions = 0
    
#     # Find all lines with condition-coverage attribute
#     for line in root.findall('.//line[@condition-coverage]'):
#         coverage_text = line.get('condition-coverage')
#         # Extract numbers from format like "50% (1/2)"
#         nums = coverage_text.split('(')[1].strip(')').split('/')
#         covered, total = map(int, nums)
        
#         covered_conditions += covered
#         total_conditions += total
    
#     if total_conditions == 0:
#         return 0
    
#     return (covered_conditions / total_conditions) * 100

def analyze_file(filepath):
    """Analizza un file Python e restituisce i moduli chiamati."""
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=filepath)
        
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                calls.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            calls.add(node.module)
    
    return calls

def analyze_project(root_dir):
    """Analizza ricorsivamente tutti i file Python in una directory."""
    dependencies = defaultdict(set)
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                module_name = os.path.splitext(filename)[0]
                called_modules = analyze_file(filepath)
                
                for called_module in called_modules:
                    dependencies[module_name].add(called_module)
                    
    return dependencies

def calculate_fan_in_out(dependencies):
    """Calcola fan-in e fan-out."""
    # Library modules to exclude
    excluded_modules = {
        'threading', 
        'abc', 
        'os', 
        'sys', 
        'json', 
        'collections', 
        'time', 
        'datetime', 
        'random', 
        'pathlib', 
        'dataclasses',   
        'multiprocessing.pool',
        'functools',
        'uuid',
        'osmnx',
        'confluent_kafka',
        'geopy.distance',
        'clickhouse_connect'
    }
    fan_in = defaultdict(int)
    fan_out = defaultdict(int)
    
    for module_name, calls in dependencies.items():
        filtered_calls = {call for call in calls if call not in excluded_modules}
        fan_out[module_name] = len(filtered_calls)
        for call in filtered_calls:
            fan_in[call] += 1
    
    return fan_in, fan_out

# Esegui l'analisi
def write_fan_report():
    # Find all Models directories recursively
    models_dirs = []
    for root, dirs, _ in os.walk("."):
        if "Models" in dirs:
            models_dirs.append(os.path.join(root, "Models"))
        if "Core" in dirs:
            models_dirs.append(os.path.join(root, "Core"))

    # Initialize combined metrics
    all_dependencies = defaultdict(set)
    combined_fan_in = defaultdict(int)
    combined_fan_out = defaultdict(int)

    # Process each Models directory
    for models_dir in models_dirs:
        dependencies = analyze_project(models_dir)
        fan_in, fan_out = calculate_fan_in_out(dependencies)
        
        # Merge dependencies and metrics
        for module, deps in dependencies.items():
            all_dependencies[module].update(deps)
        for module, count in fan_in.items():
            combined_fan_in[module] += count
        for module, count in fan_out.items():
            combined_fan_out[module] += count

    # Save results to report
    return dict(combined_fan_in), dict(combined_fan_out)


if __name__ == "__main__":

    xml_file = "reports/coverage.xml"

    data = write_coverage_report()

    fan_in_dict, fan_out_dict = write_fan_report()

    data["fan_in"] = fan_in_dict
    data["fan_out"] = fan_out_dict

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    with open(f"reports/report_{timestamp}.json", 'w') as f:
        json.dump(data, f, indent=4)