from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:column>')
@app.route('/<int:row>/<int:column>/<string:colorOne>/')
@app.route('/<int:row>/<int:column>/<string:colorOne>/<string:colorTwo>')
def checkers(row=8,column=8, colorOne="pink", colorTwo="black"):
    return render_template("checker.html", row=row, column=column, colorOne=colorOne, colorTwo=colorTwo)

    
if __name__ == "__main__":
    app.run(debug=True)