from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def eightByEight():
    return render_template("index.html", number1 = 8)

@app.route('/<x>')
def changeWidth(x):
    integer1 = int(x)
    return render_template("index.html", number1 = integer1)

@app.route('/<x>/<y>')
def changeWidthAndHeight(x, y):
    integer1 = int(x)
    integer2 = int(y)
    return render_template("index.html", number1 = integer1, number2 = integer2)


if __name__=="__main__":
    app.run(debug=True)