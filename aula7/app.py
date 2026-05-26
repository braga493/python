import calculadora
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",method=['GET','POST'])
def calculadora():
    etapas=calculadora.calcular()
    return render_template("calculadora.html",etapas=etapas)
if __name__ == "__main__":
    app.run(debug=True) 