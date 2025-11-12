from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    products = []
    
    # Read from JSON
    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
        except FileNotFoundError:
            return render_template('product_display.html', error="File not found")
    
    # Read from CSV
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    products.append({
                        'id': int(row['id']),
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    })
        except FileNotFoundError:
            return render_template('product_display.html', error="File not found")
    
    # Filter by id if provided
    if product_id:
        product_id = int(product_id)
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
