from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'letSecretKey=*7strawberry'


@app.route('/')
def counter():
    if 'count' not in session:
        session['count']=0
    session['count']+= 1
    return render_template("counter.html", count=session['count'])

@app.route('/reset')
def resets():
    session.clear()
    return redirect('/')

@app.route('/increase')
def bytwo():
    session['count']+= 1
    return redirect('/')

@app.route('/users', methods=['POST'])
def usersinc():
    session['count']+= int(request.form['number'])-1
    return redirect('/')








if __name__ == "__main__":
    app.run(debug=True)