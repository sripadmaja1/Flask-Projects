# step-1 import FLASK
from flask import Flask, request

# step-2 create an object with a parameter __name__
app=Flask(__name__)

# step-3 create an END POINT using route and bind them using functionality
@app.route('/')
def home_page():
    return 'Welcome to the HOME PAGE'

@app.route('/search')
def search_page():
    return 'Welcome to the SEARCH PAGE'

@app.route('/uppercase')
def user_upcase():
    name=request.args.get('name')
    return name.upper()

@app.route('/calculator')
def calculate():
    op=request.args.get('op')
    a=request.args.get('a')
    b=request.args.get('b')
    if op=='add':
        return str(int(a)+int(b))
    elif op=='subtract':
        return str(int(a)-int(b))
    elif op=='multiply':
        return str(int(a)*int(b))
    elif op=='divide':
        return str(int(a)/int(b))
    
    
# step-4 run the application
if __name__=='__main__':
    app.run(debug=True)
