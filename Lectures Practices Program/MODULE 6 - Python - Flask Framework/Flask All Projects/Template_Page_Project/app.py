from flask import Flask, render_template


# app init
app = Flask(__name__)



# make view
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




# run server
app.run(debug=True)