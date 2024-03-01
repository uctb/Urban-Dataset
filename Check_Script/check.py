import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
import random
# Markdown type table output
import pdb

def json_to_markdown_table(json_data):
    # Ensure the input is a list of dictionaries
    if not isinstance(json_data, list) or not all(isinstance(item, dict) for item in json_data):
        raise ValueError("Input must be a list of dictionaries")

    # Extract column names from the keys of the first dictionary
    columns = list(json_data[0].keys())
    # pdb.set_trace()
    # Create the header row
    header_row = " | ".join(columns)+' |'
    separator_row = "|".join([" --- " for _ in columns])+ '|'

    # Create the rows
    data_rows = []
    for item in json_data:
        row_values = [str(item.get(column, "")) for column in columns]
        data_row ='| ' +" | ".join(row_values)+' |\n'
        data_rows.append(data_row)

    # Combine everything into the Markdown table
    markdown_table = f"| {header_row}\n| {separator_row}\n{''.join(data_rows)}"

    return markdown_table




import os
dataset_dir = '.'
dataset_name = 'flow_luzern.pkl'
dataset_path = os.path.join(dataset_dir,dataset_name)
with open(dataset_path,'rb') as fp:
    dataset = pkl.load(fp)
json_data = [{'TimeFitness':dataset['TimeFitness'],'TimeRange':dataset['TimeRange'][0]+','+dataset['TimeRange'][1],'LengthofTime':dataset['Node']['TrafficNode'].shape[0],'NumofStation':dataset['Node']['TrafficNode'].shape[1]}]
markdown_table = json_to_markdown_table(json_data)
with open("test.md", "w") as f:
    f.write(markdown_table)

# check correctness of temporal information 
node_traffic = dataset['Node']['TrafficNode']
node_traffic_aggre = np.sum(node_traffic,axis=0)
ind_array = np.argsort(node_traffic_aggre)

daily_ts = 24*60//dataset['TimeFitness']

# low traffic station head time series visualization
low_ind = random.choice(list(ind_array[:10]))
low_traffic_station = node_traffic[:7*daily_ts,low_ind]
plt.figure()
plt.plot(low_traffic_station)
plt.title('Low Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

# middle traffic station head time series visualization
middle_ind = random.choice(list(ind_array[ind_array.shape[0]//2-5:ind_array.shape[0]//2+5]))
middle_traffic_station = node_traffic[:7*daily_ts,middle_ind]
plt.figure()
plt.plot(middle_traffic_station)
plt.title('Middle Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

# high traffic station head time series visualization
high_ind = random.choice(list(ind_array[-10:]))
high_traffic_station = node_traffic[:7*daily_ts,high_ind]
plt.figure()
plt.plot(high_traffic_station)
plt.title('High Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

# low traffic station tail time series visualization
low_ind = random.choice(list(ind_array[:10]))
low_traffic_station = node_traffic[-7*daily_ts:,low_ind]
plt.figure()
plt.plot(low_traffic_station)
plt.title('Low Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

# middle traffic station tail time series visualization
middle_ind = random.choice(list(ind_array[ind_array.shape[0]//2-5:ind_array.shape[0]//2+5]))
middle_traffic_station = node_traffic[-7*daily_ts:,middle_ind]
plt.figure()
plt.plot(middle_traffic_station)
plt.title('Middle Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

# high traffic station tail time series visualization
high_ind = random.choice(list(ind_array[-10:]))
high_traffic_station = node_traffic[-7*daily_ts:,high_ind]
plt.figure()
plt.plot(high_traffic_station)
plt.title('High Traffic Station')
plt.xlabel('Time Slots')
plt.ylabel('Traffic Volume')
plt.show()

plt.figure()
plt.plot(node_traffic.sum(axis=1)[:7*daily_ts])
plt.show()
# check correctness of spatial information
import folium
import pdb
middle_ind = ind_array.shape[0]//2
station_info = dataset['Node']['StationInfo']
# pdb.set_trace()
lats = []
lngs = []
for s in station_info:
    lats.append(float(s[2]))
    lngs.append(float(s[3]))
# pdb.set_trace()
c_lat = np.mean(np.array(lats))
c_lng = np.mean(np.array(lngs))
m = folium.Map(location=[c_lat,c_lng],zoom_start=12)
count = 0
for ind in list(ind_array):
    if count<=middle_ind:
        folium.Circle([float(station_info[ind][2]),float(station_info[ind][3])],popup=station_info[ind][-1],color='blue').add_to(m)
    else:
        folium.Circle([float(station_info[ind][2]),float(station_info[ind][3])],popup=station_info[ind][-1],color='red').add_to(m)
    count += 1
m.save('station_info.html')