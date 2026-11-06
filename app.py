from flask import Flask, render_template, request

from converter import convert_length

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")
        try:
            str_value = request.form.get("value")
            value = float(str_value)
            result = convert_length(value, from_unit, to_unit)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)
