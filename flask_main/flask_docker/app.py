from flask  import Flask,render_template,request
import subprocess
app=Flask("mycmdapp")


@app.route("/dock",methods=["GET"])
def dock():
    name=request.args.get("x")
    port=request.args.get("y")
    cont=subprocess.getoutput("docker run -it --name {} myimage:v1 ".format(name))

    data1 =render_template("dock.html",mn=cont)
    return data1

@app.route("/home")
def home():
    a=subprocess.getoutput("docker ps -a ")
    print(a)
    dt1=render_template("home.html",mm=a)
    return dt1

app.run(port=5000,debug=True)
