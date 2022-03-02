import json

#create infile and outfile to read and write file
infile = open('eq_data_1_day_m1.json', 'r')
#reason for creating outfile to make it avaliable to JSON_PROJECT file from notepad
outfile = open('readable_eq_data.json', 'w')


#take the json file and load load json convets python 
eq_data = json.load(infile)


#to make it more readable format
json.dump(eq_data, outfile, indent=4)

#getting list of earthquick and it will be accessed from feature key 
#ig you give the dictionary key, it returns back the value 
list_of_eqs = eq_data['features']

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    
    mag = eq['properties'] ['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    


#print first 10     
print(mags[:10])
print(lons[:10])
print(lats[:10])
  
  
#plot the data in map  
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = [ Scattergeo(lon= lons, lat = lats)]

my_layout =  Layout(title = "global Earthquack")

#figure is the combination of data and layout
fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'global_earthquicks.htms')
    
    

#print(len(list_of_eqs))