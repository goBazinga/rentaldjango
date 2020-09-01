from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def cart():
    cnxn = sqlite3.connect('database.db')
    cnxn.row_factory = sqlite3.Row
    cur = cnxn.cursor()
    cur.execute ('SELECT * FROM Dim_Item')
    item = cur.fetchall()
    #item = [description[0] for description in cur.description]

    print(item)


    return render_template("login.html", item=item);


if __name__ == "__main__":
    app.run()