import re

filename = 'log.txt' 
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

class IP_Entry:
    def __init__(self, source, destination, port,portnumber):
        self.source = source
        self.destination = destination
        self.port = port
        self.portnumber = portnumber
    def printself(self):
        print(f"Source: {self.source}, Destination: {self.destination}, Port: {self.port}, PortNumber: {self.portnumber} \n")

class IP_Occurence:
    def __init__(self, ip_number, occurence_number = 0):
        self.ip_number = ip_number
        self.occurence_number = occurence_number
    def printself(self):
        print(f"IP: {self.ip_number}, Occurence: {self.occurence_number} \n")
      
def find_ips(raw_line_data):
    regx = re.compile(r'\d+\.\d+\.\d+\.\d+')
    solution = regx.findall(raw_line_data)
    return solution



def find_port(raw_line_data):
    regx = re.compile(r'(\:) (\w+),?\s(\D+)?\s?(\d+)')
    solution = regx.search(raw_line_data)
    return solution.groups()

ip_list = []

for line in lines:
    ips = find_ips(line)
    port = find_port(line)
    ip_list.append(IP_Entry(ips[0] , ips[1] , port[1] , port[3]))


ip_unique_list = []

for element in ip_list:
    if(element.source not in ip_unique_list):
        ip_unique_list.append(element.source)

for element in ip_list:
    if(element.destination not in ip_unique_list):
        ip_unique_list.append(element.destination)

ip_unique_list.remove("79.120.134.178")
ip_unique_list.remove("84.1.119.110")


ip_occurence_list = []

for element in ip_unique_list:
    ip_occurence_list.append(IP_Occurence(element , 0))



for occu in ip_occurence_list:
    for entry in ip_list:
        if(occu.ip_number == entry.source):
            occu.occurence_number = occu.occurence_number + 1
        if(occu.ip_number == entry.destination):
            occu.occurence_number = occu.occurence_number + 1



ip_occurence_list.sort(key=lambda x: x.occurence_number, reverse=True)

final_solution = ""

for i in ip_occurence_list:
    final_solution = final_solution + f"IP: {i.ip_number} , Occurence: {i.occurence_number}\n"
    
print(final_solution)


with open('data.txt', 'w') as f:
    f.writelines(final_solution)