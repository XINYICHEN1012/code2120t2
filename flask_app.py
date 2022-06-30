from flask import Flask
import ghhops_server as hs


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
    return json.dumps(list(result))


if __name__ == '__main__':
    app.run()
