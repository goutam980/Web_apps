from flask import Flask
from flask  import request,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask("db_app")
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb/data.sqlite'

#orm
db=SQLAlchemy(app)
print(db)

class ARTH(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column( db.Text )
    age=db.Column( db.Text )
    remarks=db.Column(db.Text)

    def __init__(self,name,age,remarks):
        self.name=name
        self.age=age
        self.remarks=remarks

db.create_all()
#createi
@app.route("/home")
def home():
    a=render_template("home.html")
    return a

@app.route("/db",methods=['GET'])
def db():
    name=request.args.get('x')
    age=request.args.get('y')
    remarks=request.args.get('z')
    a=render_template("db.html",name=name,age=age,remarks=remarks)
    return a
"""
for i in range(2):
    name=input("Enter your name")
    age=input("enter your age")
    age=int(age)
    remarks=input("Enter your remarks")
    ds=ARTH(name,age,remarks)
    db.session.add(ds)
    db.session.commit()

#read
print("Enter your Id here")
id=input("enter here...")
id=int(id)

r2=ARTH.query.get(id)
print(r2.name, r2.age)

"""
