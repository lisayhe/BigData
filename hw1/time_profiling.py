import time
#Obtain the time before we open the time:
start_time = time.clock()
fs_file = open('/Users/Lisa/Documents/BigData/Lec1/wrds/fund_summary.csv')
variables_of_interest = ['crsp_portno', 'fund_name', 'mgr_name', 'nav_latest_dt', 'per_com', 'per_pref', 'ticker']
#Read the first line:
single_line =fs_file.readline()

#Go over the header and map each variable name to the column index:
index =0
vti = dict()
variables = single_line.split(",")
for variable in variables:
    variable = variable.strip()
    if variable in variables_of_interest:
        vti[variable]=index
    index+=1

#Create a list of lists:
ll = list()
line_num=1
for line in fs_file:
    vars = line.split(",")
    ll.append([vars[33],vars[35],vars[40],vars[4],vars[17],vars[18],vars[36]])
    line_num+=1
fs_file.close()
#Obtain the time after we are done processing:
end_time = time.clock()
#Compute the running time
print ("Read line by line and storing into list of lists takes "+str(round(end_time - start_time,6))+" seconds")


#Extracting our variables of interest using Pandas:
#Obtain the time before we open the time:
start_time = time.clock()
import pandas as pd
fs_pd = pd.read_csv('/Users/Lisa/Documents/BigData/Lec1/wrds/fund_summary.csv')
fsi_pd = fs_pd[variables_of_interest]
#Obtain the time after we are done processing:
end_time = time.clock()
#Compute the running time
print ("Pandas takes "+str(round(end_time - start_time,6))+" seconds")


