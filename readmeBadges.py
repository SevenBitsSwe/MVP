import os.path
import re
import json

def get_pylintScore(file_path = ".github/reports/pylint_report.txt"):
    # Verifica che il file esista
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Pylint output file not found at {file_path}")

    # Legge il contenuto del file
    with open(file_path, "r", encoding="utf8") as f:
        content = f.read()
        
    # Opzionalmente stampa il contenuto per debug

    # Estrae il punteggio usando una regex
    pattern = r"(?<=rated at )(\d+(?:\.\d+)?)"
    match = re.search(pattern, content)
    
    # Verifica che il pattern sia stato trovato
    if not match:
        raise ValueError(f"Unable to find Pylint score in the file {file_path}")
    
    # Restituisce il punteggio come float
    return float(match.group(1))

def get_lineCoverageScore(file_path = ".github/reports/report.json"):
    # Verify file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Coverage report file not found at {file_path}")

    # Read JSON content
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)
        
    # Extract line coverage percentage from the new format
    coverage = data.get("coverage", {}).get("line_coverage")
    if coverage is None:
        raise ValueError("Line coverage data not found in the JSON report")
        
    return round(float(coverage), 2)

def get_branchCoverageScore(file_path = ".github/reports/report.json"):
        # Verify file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Coverage report file not found at {file_path}")

        # Read JSON content
        with open(file_path, "r", encoding="utf8") as f:
            data = json.load(f)
            
        # Extract branch coverage percentage
        coverage = data.get("coverage", {}).get("line_coverage")
        if coverage is None:
            raise ValueError("Coverage data not found in the JSON report")
            
        return round(float(coverage), 2)

def get_color(score):
    if score > 9:
        return 'brightgreen'
    if score > 8:
        return 'green'
    if score > 7.5:
        return 'yellowgreen'
    if score > 6.6:
        return 'yellow'
    if score > 5.0:
        return 'orange'
    if score >= 0.00:
        return 'red'
    return 'bloodred'

README_PATH = "README.md"
NUMERIC_SCORE = get_pylintScore()
BADGE_TEXT = 'PyLint'
BADGE_COLOR = get_color(float(NUMERIC_SCORE))

if not os.path.isfile(README_PATH):
    raise FileNotFoundError(f"README.md path is wrong, no file can be located at {README_PATH}")

with open(README_PATH, "r", encoding="utf8") as f:
    content = f.read()

### Write pylint result
query = f"{BADGE_TEXT}-{NUMERIC_SCORE}-{BADGE_COLOR}?logo=python&logoColor=white"
badge_url = f"https://img.shields.io/badge/{query}"

patt = r"(?<=!\[pylint]\()(.*?)(?=\))"
if re.search(patt, content) is None:
    raise ValueError("Pylint badge not found! Be sure to put an empty one which acts as a placeholder "
                     "if this is your first run. Check README.md for examples!")

result = re.sub(patt, badge_url, content)

### Write line-coverage result
COVERAGE_SCORE = get_lineCoverageScore()
coverage_query = f"coverage-{COVERAGE_SCORE}%25-{get_color(COVERAGE_SCORE/10)}?logo=python&logoColor=white"
coverage_badge_url = f"https://img.shields.io/badge/{coverage_query}"

# Update coverage badge
coverage_patt = r"(?<=!\[Line coverage]\()(.*?)(?=\))"
if re.search(coverage_patt, content) is None:
    raise ValueError("Coverage badge not found! Be sure to put an empty one which acts as a placeholder")

result = re.sub(coverage_patt, coverage_badge_url, result)
with open(README_PATH, "w", encoding="utf8") as f:
    f.write(result)

### Write branch-coverage result
COVERAGE_SCORE = get_branchCoverageScore()
coverage_query = f"coverage-{COVERAGE_SCORE}%25-{get_color(COVERAGE_SCORE/10)}?logo=python&logoColor=white"
coverage_badge_url = f"https://img.shields.io/badge/{coverage_query}"

# Update coverage badge
coverage_patt = r"(?<=!\[Branch coverage]\()(.*?)(?=\))"
if re.search(coverage_patt, content) is None:
    raise ValueError("Coverage badge not found! Be sure to put an empty one which acts as a placeholder")

result = re.sub(coverage_patt, coverage_badge_url, result)
with open(README_PATH, "w", encoding="utf8") as f:
    f.write(result)