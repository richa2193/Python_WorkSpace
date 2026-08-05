from flask import Flask, render_template


# app ini
app=Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/single')
def single():
    return render_template('single.html')





# run server
app.run(debug=True)




