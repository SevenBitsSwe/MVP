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
        'clickhouse_connect',
        'pyflink.datastream.functions',
        'pyflink.common.types',
        'pyflink.common',
        'pyflink.datastream.formats.json',
        'pyflink.datastream.connectors.kafka',
        'langchain_groq',
        'dotenv',
        'langchain_core.rate_limiters',
        'langchain_core.prompts',
        'pydantic',
        'string',
        'typing',
        'pyflink.common.watermark_strategy',
        'pyflink.datastream',
        'pyflink.datastream.execution_mode'
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
    # parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


def analyze_module_metrics(filepath):
    """Analyzes a Python file and returns metrics about its classes and their methods."""
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=filepath)
    
    metrics = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_metrics = {
                "attributes": len([n for n in node.body if isinstance(n, ast.AnnAssign) or isinstance(n, ast.Assign)]),
                "methods": {}
            }
            
            # Analyze methods within the class
            for method in [n for n in node.body if isinstance(n, ast.FunctionDef)]:
                class_metrics["methods"][method.name] = {
                    "parameters": len(method.args.args),
                    "lines": method.end_lineno - method.lineno + 1
                }
            
            metrics[node.name] = class_metrics
    
    return metrics

def get_class_metrics():
    """Collects metrics for all Python classes in Models and Core directories."""
    class_metrics = {}
    
    # parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for root, dirs, _ in os.walk("."):
        if "Models" in dirs or "Core" in dirs:
            for dirname in ["Models", "Core"]:
                if dirname in dirs:
                    dir_path = os.path.join(root, dirname)
                    for dirpath, _, filenames in os.walk(dir_path):
                        for filename in filenames:
                            if filename.endswith(".py"):
                                filepath = os.path.join(dirpath, filename)
                                metrics = analyze_module_metrics(filepath)
                                if metrics:
                                    for class_name, class_data in metrics.items():
                                        full_name = f"{dirname}.{class_name}"
                                        class_data["fan_in"] = fan_in_dict.get(full_name, 0)
                                        class_data["fan_out"] = fan_out_dict.get(full_name, 0)
                                        class_metrics[full_name] = class_data
    
    return class_metrics

if __name__ == "__main__":
    xml_file = "reports/coverage.xml"
    
    # Get coverage data
    data = write_coverage_report()
    
    # Get fan-in and fan-out metrics
    fan_in_dict, fan_out_dict = write_fan_report()
    
    # Get detailed class metrics
    class_metrics = get_class_metrics()
    
    # Combine all metrics
    final_report = {
        "coverage": {
            "line_coverage": data["line_coverage"],
            "branch_coverage": data["branch_coverage"]
        },
        "class_metrics": class_metrics
    }
    
    # Save to file
    with open("reports/report.json", 'w') as f:
        json.dump(final_report, f, indent=4)