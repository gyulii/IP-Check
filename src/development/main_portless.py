# For using RegX
import re

# To not close cmd automatically
import os
from traceback import print_tb


if __name__ == "__main__":
    pass

print(f"Program starting...\n")


error_log = ""

# Open file and read in lines
filename = 'log.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# Class for important information: Source IP , Destination IP, Port name, Port number
class IP_Entry:
    def __init__(self, source, destination, port, portnumber):
        self.source = source
        self.destination = destination
        self.port = port
        self.portnumber = portnumber

    def printself(self):
        print(
            f"Source: {self.source}, Destination: {self.destination}, Port: {self.port}, PortNumber: {self.portnumber} \n")

# Class for IPs and their occurences


class IP_Occurence:
    def __init__(self, ip_number, occurence_number=0):
        self.ip_number = ip_number
        self.occurence_number = occurence_number

    def printself(self):
        print(f"IP: {self.ip_number}, Occurence: {self.occurence_number} \n")

# Find the ip, \d+ = 1 or more digit.
# Find all returns a list.


def find_ips(raw_line_data):
    regx = re.compile(r'\d+\.\d+\.\d+\.\d+')
    solution = regx.findall(raw_line_data)
    return solution


# print(f"Errors:\n")
error_log = error_log + f"Errors:\n"


def find_port(raw_line_data, line_number):
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
    if (solution == None):
       # print(f"Line Error ({line_number + 1}): {raw_line_data}")
        error_log = error_log + \
            f"Line Error ({line_number + 1}): {raw_line_data}\n"
    else:
        return solution.groups()


ip_list = []

filtered_ip_list = ip_list

filtered_log = ""

exc = []

try:
    with open('settings/config.ini') as file:
        conf = file.readlines()
        conf = [line.rstrip() for line in conf]
        regx = re.compile(r'\d+\.\d+\.\d+\.\d+')
        for line in conf:
            if (regx.search(line) != None):
                exc.append(regx.search(line).group()
                           )
except:
    print("Error no config.ini was found\n")
    print("The program will now exit\n")
    os.system('pause')
    exit()


try:
    with open('settings/filter.ini') as file:
        row = file.readlines()
        row = [line.rstrip() for line in row]
except:
    print("Error no filter.ini was found\n")


# Create class list from each line
for index, line in enumerate(lines):
    ips = find_ips(line)
    port = find_port(line, index)
    if (len(ips) >= 2 and port != None):
        if ((ips[0] not in exc) and ips[1] not in exc):
            ip_list.append(IP_Entry(ips[0], ips[1], port[1], port[3]))
        # Create filtered list based on filter.ini >> row
        for filt in row:
            # Match to filter ok ?
            if (filt == ips[0] or filt == ips[1]):
                # Exclude if found in config.ini
                if ((ips[0] not in exc) and ips[1] not in exc):
                    filtered_log = filtered_log + f"{line}\n"


with open('log_filtered.txt', 'w') as f:
    f.writelines(filtered_log)


ip_unique_list = []

ip_unique_source_list = []

ip_unique_destination_list = []

# Find all unique source

for element in ip_list:
    if (element.source not in ip_unique_source_list):
        ip_unique_source_list.append(element.source)
# Find all unique destinaton

for element in ip_list:
    if (element.destination not in ip_unique_destination_list):
        ip_unique_destination_list.append(element.destination)


# Find all unique ip
for element in ip_list:
    if (element.source not in ip_unique_list):
        ip_unique_list.append(element.source)

for element in ip_list:
    if (element.destination not in ip_unique_list):
        ip_unique_list.append(element.destination)


# Remove not needed IPs


for index, line in enumerate(exc):
    try:
        ip_unique_list.remove(f"{line}")
    except:
        #print(f"{line} was not found in the list")
        error_log = error_log + f"\n {line} was not found in the list"

for index, line in enumerate(exc):
    try:
        ip_unique_source_list.remove(f"{line}")
    except:
        pass


for index, line in enumerate(exc):
    try:
        ip_unique_destination_list.remove(f"{line}")
    except:
        pass


ip_occurence_list = []

ip_occurence_list_before_mark = []

ip_occurence_list_after_mark = []


# Init list with Occurence class elements
for element in ip_unique_list:
    ip_occurence_list.append(IP_Occurence(element, 0))

# Init list with Occurence class elements before
for element in ip_unique_source_list:
    ip_occurence_list_before_mark.append(IP_Occurence(element, 0))


# Init list with Occurence class elements after
for element in ip_unique_destination_list:
    ip_occurence_list_after_mark.append(IP_Occurence(element, 0))


# Count occurences
for occu in ip_occurence_list:
    for entry in ip_list:
        if (occu.ip_number == entry.source):
            occu.occurence_number = occu.occurence_number + 1
        if (occu.ip_number == entry.destination):
            occu.occurence_number = occu.occurence_number + 1

 # Count before
for occu in ip_occurence_list_before_mark:
    for entry in ip_list:
        if (occu.ip_number == entry.source):
            occu.occurence_number = occu.occurence_number + 1
# Count after
for occu in ip_occurence_list_after_mark:
    for entry in ip_list:
        if (occu.ip_number == entry.destination):
            occu.occurence_number = occu.occurence_number + 1

# Sort by occurence number
ip_occurence_list.sort(key=lambda x: x.occurence_number, reverse=True)

ip_occurence_list_before_mark.sort(
    key=lambda x: x.occurence_number, reverse=True)

ip_occurence_list_after_mark.sort(
    key=lambda x: x.occurence_number, reverse=True)

final_solution = ""

final_solution_before_mark = ""

final_solution_after_mark = ""

# Create the solution string

for i in ip_occurence_list:
    final_solution = final_solution + \
        f"IP: {i.ip_number} , Occurence: {i.occurence_number}\n"

for i in ip_occurence_list_before_mark:
    final_solution_before_mark = final_solution_before_mark + \
        f"IP: {i.ip_number} , Occurence: {i.occurence_number}\n"

for i in ip_occurence_list_after_mark:
    final_solution_after_mark = final_solution_after_mark + \
        f"IP: {i.ip_number} , Occurence: {i.occurence_number}\n"

# Write the solution to file
with open('data.txt', 'w') as f:
    f.writelines(final_solution)


with open('data_source.txt', 'w') as f:
    f.writelines(final_solution_before_mark)

with open('data_destination.txt', 'w') as f:
    f.writelines(final_solution_after_mark)

with open('error_log.txt', 'w') as f:
    f.writelines(error_log)
# Keep the messages on the screen

print(f"\nProgram finished running\n")

os.system('pause')
