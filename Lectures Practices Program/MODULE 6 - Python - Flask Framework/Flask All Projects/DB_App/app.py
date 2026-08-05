from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

# app ini 
app = Flask(__name__)


# DB Config 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Saves memory/resources


# db object
db=SQLAlchemy(app)


# create Model 
class studinfo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    city=db.Column(db.String(20))


# call the db 
with app.app_context():
    db.create_all()



# make view 
@app.route('/', methods=['GET','POST'])
def index():

    # this check whether request coming from browser is a POST request.
    if request.method=="POST":

        #request.form containes all form data submitted by user.
        name=request.form.get("name")        
        city=request.form.get("city")

        # create new object of the studinfo model
        stdata=studinfo(name=name, city=city)

        # for adding record in db
        db.session.add(stdata)

        # save all pending changes in the session of the db     
        db.session.commit()

    return render_template('index.html')    #display the html page


# create view for showdata
@app.route('/showdata', methods=["GET"])    #To retrieve data
def showdata():
    stdata=studinfo.query.all()     #Retrieve all records from the studinfo
    return render_template()


# app run 
app.run(debug=True)

