from flask import Flask,render_template

app=Flask("tinyt")
@app.route("/tinyt")
def main_app():
    return render_template("arth_main_os.html") 

@app.route("/chat")
def chat_app():
    return render_template("chat.html") 

