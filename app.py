from flask import Flask, render_template, request, redirect
import json
import os
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.use('Agg')  
from io import BytesIO
import base64

app = Flask(__name__)
DATA_FILE = 'data/records.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    records = load_data()
    balance = sum([r['amount'] if r['type'] == 'income' else -r['amount'] for r in records])
    chart = generate_chart(records)
    return render_template('index.html', balance=balance, records=records, chart=chart)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        record = {
            "type": request.form['type'],
            "amount": float(request.form['amount']),
            "category": request.form['category'],
            "description": request.form['description'],
            "date": request.form['date'] or datetime.today().strftime('%Y-%m-%d')
        }
        records = load_data()
        records.append(record)
        save_data(records)
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    records = load_data()
    if 0 <= index < len(records):
        records.pop(index)
        save_data(records)
    return redirect('/view')    

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    records = load_data()
    if 0 <= index < len(records):
        if request.method == 'POST':
            records[index] = {
                "type": request.form['type'],
                "amount": float(request.form['amount']),
                "category": request.form['category'],
                "description": request.form['description'],
                "date": request.form['date']
            }
            save_data(records)
            return redirect('/view')
        return render_template('edit.html', record=records[index], index=index)
    return redirect('/view')

@app.route('/view')
def view():
    records = load_data()
    filtered = records

    category = request.args.get('category')
    date_from = request.args.get('from')
    date_to = request.args.get('to')

    if category:
        filtered = [r for r in filtered if r['category'] == category]

    if date_from:
        filtered = [r for r in filtered if r['date'] >= date_from]
    if date_to:
        filtered = [r for r in filtered if r['date'] <= date_to]

    search = request.args.get('search', '').strip().lower()
    if search:
        filtered = [r for r in filtered if search in r['description'].lower()]

    filtered = sorted(filtered, key=lambda x: x['date'], reverse=True)

    max_amount = request.args.get('max_amount')
    if max_amount:
        try:
            max_val = float(max_amount)
            filtered = [r for r in filtered if r['amount'] <= max_val]
        except ValueError:
            pass

    categories = list(set(r['category'] for r in records))
    return render_template('view.html', records=filtered, categories=categories,
                           selected_category=category or '',
                           date_from=date_from or '',
                           date_to=date_to or '',
                           max_amount=max_amount or '',
                           search=search)

def generate_chart(records):
    income = {}
    expense = {}

    for r in records:
        cat = r['category']
        amt = r['amount']
        if r['type'] == 'income':
            income[cat] = income.get(cat, 0) + amt
        else:
            expense[cat] = expense.get(cat, 0) + amt

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    def pie(ax, data, title):
        if data:
            ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
            ax.set_title(title)
        else:
            ax.text(0.5, 0.5, 'No data', ha='center')

    pie(axs[0], income, 'Income')
    pie(axs[1], expense, 'Expenses')

    img = BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)
