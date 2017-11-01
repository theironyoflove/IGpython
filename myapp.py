from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def GoogleMaps():
    return render_template("index.html")

app.run(debug=True)
