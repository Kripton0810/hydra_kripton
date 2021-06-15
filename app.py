from flask import Flask , render_template,request
import jsonify
import MLmodel as model
app = Flask(__name__)

@app.route("/model/")

def hello():
    pm2 = request.args['pm2']
    pm5 = request.args['pm5']
    no = request.args['no']
    no2 = request.args['no2']
    nox = request.args['nox']
    nh3 = request.args['nh3']
    co = request.args['co']
    so2 = request.args['so2']
    o3 = request.args['o3']
    c6 = request.args['c6']
    tol = request.args['tol']
    xy = request.args['xy']
    aqi = request.args['aqi']
    ret = model.fun(pm2, pm5, no, no2, nox, nh3, co, so2, o3, c6, tol, xy, aqi)
    modelrq = {
        "result":str(ret)
    }
    return modelrq
    

if __name__=="__main__":
    app.run(debug=True)

