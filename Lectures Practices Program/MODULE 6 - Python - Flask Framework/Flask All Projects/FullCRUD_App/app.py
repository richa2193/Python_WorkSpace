from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


# object of app
app=Flask(__name__)

# DB config 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# DB Object
db=SQLAlchemy(app)


#create model 
class studinfo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    city=db.Column(db.String(50))


# create app context
with app.app_context():
    db.create_all()


# create view for index 
@app.route('/', methods=['GET', 'POST'])
def index():

    # check if the form has been submitted using the POST method
    if request.method =="POST":

        # gets the value entered in name field & stores in varible nm
        nm=request.form.get('name')
        em=request.form.get('email')
        ct=request.form.get('city')

        # use dictionary format
        # nm=request.form['name]

        # create new object with entered name, city. email
        stdata=studinfo(name=nm, email=em, city=ct)

        # adds the new project to the db session
        db.session.add(stdata)

        # save the record per. in db
        db.session.commit() 

    return render_template('index.html')


@app.route('/showdata', methods=['GET'])
def showdata():

    # get all data from the db
    stdata=studinfo.query.all()

    return render_template('showdata.html', stdata=stdata)


# view for delete data
@app.route('/deletedata/<int:id>')
def deletedata(id):
    stid=studinfo.query.get(id)

    db.session.delete(stid)
    db.session.commit() 

    return redirect('/showdata')        


# view for update data
@app.route('/updatedata/<int:id>', methods=['GET','POST'])
def updatedata(id):
    stid=studinfo.query.get(id)

    if request.method=='POST':
        stid.name=request.form['name']
        stid.email=request.form['email']
        stid.city=request.form['city']

        db.session.commit()
        print("Record Updated!")
        return redirect('/showdata')

    return render_template('updatedata.html', stid=stid)


# app run 
app.run(debug=True)


