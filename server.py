from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="John Doe")

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def create_user():
    return render_template('dojos.html')

@app.route('/spiders', methods=['POST'])
def pass_data():
    print request.form
    name= request.form['name']
    email= request.form['email']
    return redirect('/')

app.run(debug=True)