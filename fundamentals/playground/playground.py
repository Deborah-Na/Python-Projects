from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/')
@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def play2(num=3,color="teal"):
    return render_template("playground.html", num=num, color=color)



if __name__=="__main__":
    app.run(debug=True)
