from flask import Flask



# App Initialization 
app = Flask(__name__)



# view
@app.route('/')
def index():
    return "Hello Flask!!"

@app.route('/about')
def about():
    return "This is About Page!"




# Run Server 
app.run(debug=True)


