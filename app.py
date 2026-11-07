from flask import Flask, render_template, request

from converter import convert_length, convert_temperature, convert_weight

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        category = request.form.get("category")
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")
        try:
            str_value = request.form.get("value")
            if str_value is None or str_value.strip() == "":
                raise ValueError("Please enter a value")
            value = float(str_value)
            if category == "length":
                result = convert_length(value, from_unit, to_unit)
            elif category == "weight":
                result = convert_weight(value, from_unit, to_unit)
            elif category == "temperature":
                result = convert_temperature(value, from_unit, to_unit)
            else:
                raise ValueError("the category is unknown")
        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)
