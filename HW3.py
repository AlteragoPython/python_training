import os
import re
def validate_line(line):
    elements = line.split()
    if len(elements) != 5:
        return False, 'validate_line'
    else:
        return True, ''

def validate_date(line):
    elements = line.split()
    date = elements[-1]
    return re.match(r'^\d{4}-\d{2}-\d{2}$', date) is not None

def check_data(filepath, validators):
    report_file = "report.txt"
    with open(filepath) as file, open(report_file, "w") as report:
        for line in file:
            line = line.strip()
            failed_validators = [v.__name__ for v in validators if not v(line)]
            if failed_validators:
                reason = failed_validators[0]
                report.write(f"{line} {reason}\n")
    return os.path.abspath(report_file)



