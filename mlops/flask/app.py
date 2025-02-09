from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.
'''

#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to MLOps course, this is an amazing course"

@app.route("/index")
def index():
    return "Welcome to index page"

if __name__=="__main__":
    app.run(debug=True) #debug=true helps to run the server automatically wihout restarting it