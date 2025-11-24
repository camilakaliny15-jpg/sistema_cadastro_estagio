from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("cadastro.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    pessoas = conn.execute("SELECT * FROM pessoas ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", pessoas=pessoas)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO pessoas (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)",
            (nome, email, telefone, endereco)
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()
    pessoa = conn.execute("SELECT * FROM pessoas WHERE id = ?", (id,)).fetchone()

    if pessoa is None:
        conn.close()
        return redirect("/")

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        conn.execute(
            "UPDATE pessoas SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?",
            (nome, email, telefone, endereco, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("edit.html", pessoa=pessoa)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM pessoas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
