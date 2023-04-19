from flask import Flask, render_template
from flask_table import Table, Col

app = Flask(__name__)

@app.route('/')
def home():
    data = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'}
    ]
    for d in data:
        d['full_name'] = f"{d['first_name']} {d['last_name']}"
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

