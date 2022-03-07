#Find me@LinkedIn - https://www.linkedin.com/in/gyan4cybersecurity/

import pandas as pd
import numpy as np
import ipaddress
from tabulate import tabulate

df = pd.read_excel('sample_ip_add_management_list.xlsx') #Replace file with your IP network inventory
dstip = ipaddress.ip_network('10.7.0.45') #Input desired IP address for lookup

def find_nearest(array, value):
    #Function to find closest match
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def lpm_function(dstip, df):
    #Function to perform longest prefix match
    pfx_array = []
    plen_array = []
   
    #Loop through Network column for returning arrays for Subnets/Supernets & Netmask of those
    for pfx in df['Network']:
        if dstip.subnet_of(ipaddress.ip_network(pfx)):
            pfx_array.append(pfx)
            plen_array_item = ipaddress.IPv4Network(pfx)
            plen_array.append(int(plen_array_item.netmask))
    
    #Apply find_nearest function to retun closest match of netmask
    if not (plen_array or pfx_array) == []:
        lpm_plen = find_nearest(plen_array, int(ipaddress.IPv4Address(dstip.netmask)))
        #Loop through returned aray from 1st loop to find LPM
        for lpm in pfx_array:
            if dstip.subnet_of(ipaddress.ip_network(lpm)) and lpm_plen == int(ipaddress.ip_network(lpm).netmask):
                final_lpm_retuned = df.set_index('Network').loc[lpm]
        return pd.DataFrame(final_lpm_retuned)
    else:
        print('No match found for: '+str(dstip))

final_lpm = lpm_function(dstip, df)
print(tabulate(final_lpm, headers='keys', tablefmt='psql'))
