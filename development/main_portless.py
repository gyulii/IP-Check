# For using RegX
import re

# To not close cmd automatically
import os

print(f"Program starting...\n")

# Open file and read in lines
filename = 'log.txt' 

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# Class for important information: Source IP , Destination IP, Port name, Port number
class IP_Entry:
    def __init__(self, source, destination, port,portnumber):
        self.source = source
        self.destination = destination
        self.port = port
        self.portnumber = portnumber
    def printself(self):
        print(f"Source: {self.source}, Destination: {self.destination}, Port: {self.port}, PortNumber: {self.portnumber} \n")

# Class for IPs and their occurences
class IP_Occurence:
    def __init__(self, ip_number, occurence_number = 0):
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


print(f"Errors:\n")

# Find Port information, () means data is in groups
# (\:) = have to start with ":" [group 0]
#(\w+) = tdp, UDP ; [group 1]
# ,? = optional 
# \s+ = 1 or more space, tab
# (\D+)? = optional non numeric like "length" [group 2]
# (\d+) = one or more digit (port number) [group 3]
def find_port(raw_line_data , line_number):
    regx = re.compile(r'(\:) (\w+),?\s*(\D+)?\s*?(\d+)')
    solution = regx.search(raw_line_data)
    if(solution == None):
        print(f"Line Error ({line_number + 1}): {raw_line_data}")
    else:
        return solution.groups()

ip_list = []

# Create class list from each line
for index , line in enumerate(lines):
    ips = find_ips(line)
    port = find_port(line , index)
    if(len(ips) >= 2 and port != None):
        ip_list.append(IP_Entry(ips[0] , ips[1] , port[1] , port[3]))


ip_unique_list = []

# Find all unuique IP
for element in ip_list:
    if(element.source not in ip_unique_list):
        ip_unique_list.append(element.source)

for element in ip_list:
    if(element.destination not in ip_unique_list):
        ip_unique_list.append(element.destination)

# Remove not needed IPs

ip_unique_list.remove("79.120.134.178")
ip_unique_list.remove("84.1.119.110")


ip_occurence_list = []

# Init list with Occurence class elements
for element in ip_unique_list:
    ip_occurence_list.append(IP_Occurence(element , 0))


# Count occurences
for occu in ip_occurence_list:
    for entry in ip_list:
        if(occu.ip_number == entry.source):
            occu.occurence_number = occu.occurence_number + 1
        if(occu.ip_number == entry.destination):
            occu.occurence_number = occu.occurence_number + 1


# Sort by occurence number
ip_occurence_list.sort(key=lambda x: x.occurence_number, reverse=True)

final_solution = ""

# Create the solution string
for i in ip_occurence_list:
    final_solution = final_solution + f"IP: {i.ip_number} , Occurence: {i.occurence_number}\n"
    

# Write the solution to file
with open('data.txt', 'w') as f:
    f.writelines(final_solution)

# Keep the messages on the screen

print(f"\nProgram finished running\n")

os.system('pause')