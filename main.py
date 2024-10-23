from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/palestras")
def palestras():
    return render_template("palestras.html")


@app.route("/palestra_loiane")
def palestra_loiane():
    return render_template("palestrante_detalhes_lg.html")


@app.route("/palestra_rodrigo")
def palestra_rodrigo():
    return render_template("palestrante_detalhes_rb.html")


@app.route("/palestra_henrique")
def palestra_henrique():
    return render_template("palestrante_detalhes_hb.html")


@app.route("/palestra_diego")
def palestra_diego():
    return render_template("palestrante_detalhes_df.html")


if __name__ == '__main__':
    app.run(debug=True)
