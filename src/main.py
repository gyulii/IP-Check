
import pandas as pd


from utilities.regx import find_ips, find_port
from utilities.IP import IP

if __name__ == "__main__":
    pass


filename = fr"input\log.txt"
filename_short = fr"input\log_short.txt"


with open(filename_short) as file:
    lines = file.readlines()

IP_list = []

for line in lines:
    line.rstrip()
    ips = find_ips(line)
    ports = find_port(line)

    try:
        IP_list.append(IP(ips[0] , ips[1] , ports[1] , ports[3]))
    except Exception as e:
        print(e)


print(IP_list[0])
print(vars(IP_list[0]))



IP_list_pandas  = pd.DataFrame([vars(element) for element in IP_list])

IP_list_pandas.head(50)




IP_list_pandas.query("destination in ('192.168.10.199' , '172.16.32.242')")

 


IP_list_pandas[['destination']].value_counts()

 

src = IP_list_pandas[['source']]
dst = IP_list_pandas[['destination']]

comb = pd.concat([src , dst])

comb['combined'] = comb['source'].fillna('') + comb['destination'].fillna('')


comb['combined'].value_counts()

comb = comb.drop('source' , axis=1)
comb = comb.drop('destination' , axis=1)





# Filtering

filter_list = ['239.255.255.250' , '172.16.32.242' , 
'172.16.32.242' , '192.168.10.2' , '192.168.10.199']

comb = comb.query("combined !=  @filter_list")

comb.reset_index(drop=True)



IP_list_pandas.query("(source != @filter_list) and (destination != @filter_list)").reset_index(drop=True)





domain_names = {"192.168.10.101": "Google" , "192.168.10.2": "Csomiep"}

IP_list_pandas['Source_Domain'] = IP_list_pandas['source'].map(domain_names).fillna(IP_list_pandas['source'])
IP_list_pandas['Destination_Domain'] = IP_list_pandas['destination'].map(domain_names)
IP_list_pandas = IP_list_pandas[['source' , 'Source_Domain' , 'destination' , 'Destination_Domain']]
IP_list_pandas






# Filtering with regex and create list of class

# Pandas dataframe creation from list

# Querry for data

# Write to output 

