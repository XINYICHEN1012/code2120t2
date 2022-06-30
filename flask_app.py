from flask import Flask
import ghhops_server as hs
import csv
import requests
import os

app = Flask(__name__)
hops = hs.Hops(app)


file_name = 'building-points.csv'
CSV_URL = 'https://data.townofcary.org/api/records/1.0/search/?dataset=building-points&q=&rows=20&sort=-rooms&facet=building_type&facet=building_sub_type&facet=bldgstyle&facet=yearbuilt&facet=storyheight&facet=basement&facet=utilities&refine.building_sub_type=2+Family&refine.building_sub_type=3+Family&refine.building_sub_type=4+Family&refine.building_sub_type=Multi-Family&refine.building_sub_type=Single+Family&refine.building_type=Residential'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

@app.route("/")
def hello_world():
    return "<p>Hello, I am Shandy from UNSW CODE2120 </p>"

@hops.component(
    "/np_addMatrix",
    name= "np_addMatrix",
    description="np_addMatrix",
    inputs=[
        hs.HopsNumber("M1","M1","M1",access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("M2","M2","M2",access=hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("M3","M3","M3")
    ]
)


@app.route("/urlend")
def np_addmatrix(M1,M2):
    import numpy as np
    import json
    matrix1 = np.array(M1).reshape((2,2))
    matrix2 = np.array(M2).reshape((2,2))

    result = np.add(matrix1,matrix2)
    result = result.flatten('F')
    print(result)
    return list(result)


if __name__ == '__main__':
    app.run()
