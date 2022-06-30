from nturl2path import url2pathname
from flask import Flask
import ghhops_server as hs
import requests
import os

app = Flask(__name__)
hops = hs.Hops(app)



@app.route("/")
def hello_world():
    return "<p>Hello, I am Shandy from UNSW CODE2120 </p>"


@hops.component(
    "/np_addMatrix",
    name= "np_addMatrix",
    description="np_addMatrix",
    inputs=[
        hs.HopsNumber("M1","M1","M1", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("M2","M2","M2", access=hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("M3","M3","M3")
    ]
)
@app.route("/urlend")
def np_addMatrix(M1,M2):
    import numpy as np
    import json
    matrix1 = np.array(M1).reshape((3,1))
    matrix2 = np.array(M2).reshape((3,1))
    result = np.add(matrix1,matrix2)
    result = result.flatten('F')
    print(result)
    return list(result)
    

##clean dictionary
#@app.route('/')
#def buildinginfor_basement():
    #url = 'https://data.townofcary.org/api/records/1.0/search/?dataset=building-points&q=&rows=20&sort=-rooms&facet=building_type&facet=building_sub_type&facet=bldgstyle&facet=yearbuilt&facet=storyheight&facet=basement&facet=utilities&refine.building_sub_type=2+Family&refine.building_sub_type=3+Family&refine.building_sub_type=4+Family&refine.building_sub_type=Multi-Family&refine.building_sub_type=Single+Family&refine.building_type=Residential'
    #r = requests.get(url)
    #for option in r.json()["building-points","building_sub_type","basement"]:
      #print(option)


#find distance (vectror)between points
#@hops.component(
    "/np_vector",
    name= "np_vector",
    description="np_vector",
    inputs=[
        hs.HopsNumber("M1","M1","M1", access=hs.HopsParamAccess.LIST),
        hs.HopsNumber("M2","M2","M2", access=hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("M3","M3","M3")
    ]
#)
#@app.route("/urlend")
#def np_addMatrix(M1,M2):
   #import numpy as np
   #vector1 = np.array(M1)
   #vector2 = np.array(M2)
   #subtraction = vector2 - vector1
   #print("Vector       : " + str(subtraction))

#scale the point_(maybe could use for zone in geo)
#@hops.component(
    #"/np_scale",
    #name= "np_scale",
    #description="np_scale",
    #inputs=[
       # hs.HopsNumber("v1","v1","v1", access=hs.HopsParamAccess.LIST),
       # hs.HopsNumber("s2","s2","s2", access=hs.HopsParamAccess.LIST),
   # ],
    #outputs=[
       # hs.HopsNumber("k3","k3","k3")
    #]
#)
#@app.route("/urlend")
#def np_addMatrix(v1,s2):
   #import numpy as np
   #vector1 = np.array(v1)
   #scale2 = np.array(s2)
   #scalar_mul = vector * scalar
   #print("Scalar Multiplication : " + str(scalar_mul)))
if __name__ == '__main__':
    app.run()

