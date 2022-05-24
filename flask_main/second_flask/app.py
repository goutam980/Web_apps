from flask  import Flask,render_template,request
import subprocess
app=Flask("mycmdapp")

@app.route("/search",methods=["GET"])
def search():
    name=request.args.get("x")
    
    data1 =render_template("page.html",mn=name)
    return data1
    
@app.route("/aws",methods=["GET"])
def aws():

    n1=request.args.get("x")
    return render_template("aws.html")

@app.route("/menu",methods=["GET"])
def menu():
    n1=request.args.get("x")
    return subprocess.getoutput(n1)
    
@app.route("/home")
def home():
    page=render_template("arth_main_os.html")
    return page
@app.route("/ansi")
def ansi():
    page=render_template("ansible.html")
    return  page 



app.run(port="1212", debug=True)

