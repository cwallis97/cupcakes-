from flask import Flask, render_template, url_for, redirect
from cupcakes import Cupcake, Regular, Mini, Large

app = Flask(__name__)


cupcakes_data = [
    Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate"),
    Mini("Oreo", 0.99, "Chocolate", "Cookies and Cream"),
    Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese"),
    Regular("Triple Chocolate", 2.99, "Chocolate", "Chocolate", "Chocolate"),
    Regular("Strawberry", 2.99, "Strawberry", "Vanilla")
]

orders_data = []

@app.route("/")
def home():
    order_total = round(sum([float(c.price) for c in orders_data]), 2)
    return render_template("index.html", cupcakes=cupcakes_data, items_num=len(orders_data), order_total=order_total)

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes=cupcakes_data)

@app.route("/add_cupcake/<name>")
def add_cupcake(name):
   
    cupcake = next((c for c in cupcakes_data if c.name == name), None)

    if cupcake:
        orders_data.append(cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route("/individual_cupcake/<name>")
def individual_cupcake(name):
    
    cupcake = next((c for c in cupcakes_data if c.name == name), None)

    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route("/order")
def order():
    cupcake_set = set((c.name, c.price, orders_data.count(c)) for c in orders_data)
    order_total = round(sum(float(x[1]) for x in cupcake_set), 2)

    return render_template("order.html", cupcakes=cupcake_set, items_num=len(orders_data), order_total=order_total)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")
