from flask import Flask, jsonify, request

#Initialise the app
app = Flask(__name__)

#Define what the app does

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.get("/greet")
def index():
    """
    1- Capture first name & last name
    2- If either is not provided: respond with an error
    3- if first name is not provided and second name is provided:
        respond with "Hello Mr. <second-name>!"
    4- if first name is provided but second name is not provided:
        respond with "Hello, <first-name>!"
    5- if both names are provided: respond with a question,
        "Is your name <first-name> <second-name>" 
    """
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if  fname and lname:
        #if none of the above is true, then both names must be present
        response = {"data" : "Is your name {} {}?".format(fname, lname)}
        
    elif fname and not lname:
        #if first name is present but last name is missing
        response = {"data" : f"Hello, {fname}!"}
    elif not fname and lname:
        response = {"date" : f"Hello, Mr. {lname}!"}
    else:
        #if both first name and last name are missing, return an error
        return jsonify({"status" : "error"})
    
    return jsonify(response)
    
