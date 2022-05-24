from flask  import Flask 
from  flask import request,render_template
import subprocess
import datetime


app=Flask("net_app")

@app.route("/home")
def home():
    t=subprocess.getoutput("route -n")
    ab=render_template("home.html" ,t=t)
    return ab



@app.route("/menu")
def menu():

    dlt=request.args.get('x')
    add=request.args.get('y')
    dlt_gtw=subprocess.getoutput("route del -net {}".format(dlt))
    print(add)
    rot_add=subprocess.getoutput("route add -net {} gateway 192.168.43.1  enp0s3".format(add))
    a=render_template("new.html", add=add,dlt=dlt)

    return a


