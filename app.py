from flask import Flask, render_template, request, redirect
from database import listar_pessoas, adicionar_pessoa, buscar_pessoa, atualizar_pessoa, excluir_pessoa

app = Flask(__name__)

@app.route("/")
def index():
    pessoas = listar_pessoas()
    return render_template("index.html", pessoas=pessoas)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        adicionar_pessoa(nome, email, telefone, endereco)
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    pessoa = buscar_pessoa(id)

    if pessoa is None:
        return redirect("/")

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        telefone = request.form.get("telefone", "").strip()
        endereco = request.form.get("endereco", "").strip()

        atualizar_pessoa(id, nome, email, telefone, endereco)
        return redirect("/")

    return render_template("edit.html", pessoa=pessoa)

@app.route("/delete/<int:id>")
def delete(id):
    excluir_pessoa(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
