# Unit Converter

A simple web-based unit converter built with Python and Flask.

## Features

- **Length:** Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, Mile
- **Weight:** Milligram, Gram, Kilogram, Ounce, Pound
- **Temperature:** Celsius, Fahrenheit, Kelvin
- Basic input validation and error handling
- Simple web interface

## Technologies

- Python 3
- Flask
- HTML
- JavaScript

## Getting Started

Clone the repository:

```bash
git clone https://github.com/masoud-vosoughi/unit-converter.git
cd unit-converter
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m flask --app app run
```

Open `http://127.0.0.1:5000` in your browser.

## Project Structure

```text
unit-converter/
├── app.py
├── converter.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

## About

Built as a hands-on backend development project to practice Python, Flask, form handling, and unit conversion logic.