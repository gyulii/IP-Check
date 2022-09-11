import re

def find_ips(raw_line_data):
    regx = re.compile(r'\d+\.\d+\.\d+\.\d+')
    solution = regx.findall(raw_line_data)
    return solution


def find_port(raw_line_data):
    # Find Port information, () means data is in groups
    # (\:) = have to start with ":" [group 0]
    # (\w+) = tdp, UDP ; [group 1]
    # ,? = optional
    # \s+ = 1 or more space, tab
    # (\D+)? = optional non numeric like "length" [group 2]
    # (\d+) = one or more digit (port number) [group 3]
    global error_log
    regx = re.compile(r'(\:) (\w+),?\s*(\D+)?\s*?(\d+)')
    solution = regx.search(raw_line_data)
    if (solution != None):
        return solution.groups()