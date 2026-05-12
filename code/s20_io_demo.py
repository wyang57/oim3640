import csv

# Read CSV (each row becomes a dict)
with open('students.csv') as f:
    for row in csv.DictReader(f):
        print(f"{row['name']}: {row['grade']}")

# Write CSV
data = [{'name': 'Alice', 'grade': 95},
        {'name': 'Bob', 'grade': 87}]
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'grade'])
    writer.writeheader()
    writer.writerows(data)

def display_portfolio():
    """Display all the stocks in the portfolio table."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor=db.cursor()
        for row in db.execute("SELECT * FROM portfolio"):
            print(row)


def display_expensive_stocks(threshold_price):
    """Display all the stocks in the portfolio table with price above threshold_price."""
    with sqlite3.connect("data/stocks.db") as db:
        cursor=db.cursor()
        results=cursor.execute("SELECT * FROM portfolio WHERE price > ?", (threshold_price,))
        for row in results:
            print(row)

def main():
    create_portfolio_table()
    stocks=[("AAPL", 150.0), ("GOOG", 2800.0), ("TSLA", 700.0)]
    insert_stocks(stocks)
    print("All stocks:")


