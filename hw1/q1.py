#Lisa He
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
ld = list()
line_num=1
for line in fs_file:
    vars = line.split(",")
    td = dict()
    for var in variables_of_interest:
               td[var]=vars[vti[var]]
    ld.append(td)
    line_num+=1
fs_file.close()
#Obtain the time after we are done processing:
end_time = time.clock()
#Compute the running time
print ("Read line by line and storing into list of dictionaries takes "+str(round(end_time - start_time,6))+" seconds")

#Results:
#Read line by line and storing into list of lists takes 9.343406 seconds
#Read line by line and storing into list of dictionaries takes 11.503206 seconds

#list of lists are faster than list of dictionaries
#because dictionaries take up more space in memory due to the hashing process. We are storing somme key value as well,
#whereas in a list we would be storing an index

