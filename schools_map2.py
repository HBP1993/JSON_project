"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.

Map 2) Percent of total enrollment that are Black or African American over 10%

"""

import json
import csv

#create infile to read the json file
infile = open('univ.json', 'r')

#take the json file and load load json convets python
univ_data = json.load(infile)

#create infile to read the cvs file
cvs_file = open('ValueLabels.csv', 'r')
read_cvs = csv.reader(cvs_file, delimiter = ',')

next(read_cvs) 

#Universities with Total Enrollment of Black or African American Over 10%
enroll_BAA, lons, lats, hover_texts, enrolls  = [], [], [], [], []

divisions = ["Atlantic Coast Conference", "Big Twelve Conference", "Big Ten Conference", "Pacific-12 Conference", "Southeastern Conference"]
division_dict = {}


for line in read_cvs:
    if line[2] in divisions:
        division_dict[line[2]] = line[1]


for univ in univ_data:
    if str(univ["NCAA"]["NAIA conference number football (IC2020)"]) in division_dict.values():
        if univ["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
            lon = univ["Longitude location of institution (HD2020)"]
            lons.append(lon)
            lat = univ["Latitude location of institution (HD2020)"]
            lats.append(lat)
            enroll_rate_BAA = univ["Percent of total enrollment that are Black or African American (DRVEF2020)"]
            enroll_BAA.append(enroll_rate_BAA)
            inst_name = univ["instnm"]
            hover_text = inst_name + ',' + str(enroll_rate_BAA) +'%'
            hover_texts.append(hover_text)
            enroll = univ["Total  enrollment (DRVEF2020)"]
            enrolls.append(enroll)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[0.0005*enroll for enroll in enrolls],
        'color':enrolls,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Number of enrolls'}
    },
    }]

my_layout = Layout(title='Universities with Total Enrollment of Black or African American Over 10%')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='Total_Enrollment_of_Black_or_African_American.html')
