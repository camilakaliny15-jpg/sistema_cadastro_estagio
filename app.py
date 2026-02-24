from flask import Flask, render_template, request, redirect, url_for
from database import (
    listar_instituicoes,
    adicionar_instituicao,
    buscar_instituicao,
    buscar_instituicoes_por_termo,
    atualizar_instituicao,
    excluir_instituicao
)
from database import (
    listar_pessoas,
    adicionar_pessoa,
    buscar_pessoa,
    atualizar_pessoa,
    excluir_pessoa
)

app = Flask(__name__)

# -----------------------------
# ROTA PRINCIPAL (INSTITUIÇÕES)
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    termo = request.args.get("q")
    if termo:
        instituicoes = buscar_instituicoes_por_termo(termo)
    else:
        instituicoes = listar_instituicoes()
    return render_template("index.html", instituicoes=instituicoes)

# -----------------------------
# ESCOLHER TIPO DE CADASTRO
# -----------------------------
@app.route("/escolher_cadastro")
def escolher_cadastro():
    return render_template("escolher_cadastro.html")

# -----------------------------
# ROTAS DE INSTITUIÇÃO
# -----------------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        dados = {
            "nome_oficial": request.form.get("nome_oficial"),
            "email_oficial": request.form.get("email_oficial"),
            "telefone_principal": request.form.get("telefone_principal"),
            "site_url": request.form.get("site_url"),
            "endereco_completo": request.form.get("endereco_completo"),
            "status": "Ativo",
            "observacao": request.form.get("observacao"),
        }

        adicionar_instituicao(dados)

        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    instituicao = buscar_instituicao(id)
    if not instituicao:
        return redirect(url_for("index"))

    if request.method == "POST":
        dados = {
            "nome_oficial": request.form.get("nome_oficial"),
            "email_oficial": request.form.get("email_oficial"),
            "telefone_principal": request.form.get("telefone_principal"),
            "site_url": request.form.get("site_url"),
            "endereco_completo": request.form.get("endereco_completo")
        }
        atualizar_instituicao(id, dados)
        return redirect(url_for("index"))
    return render_template("edit.html", instituicao=instituicao)

@app.route("/delete/<int:id>")
def delete(id):
    excluir_instituicao(id)
    return redirect(url_for("index"))

@app.route("/view/<int:id>")
def view(id):
    instituicao = buscar_instituicao(id)
    if not instituicao:
        return redirect(url_for("index"))
    return render_template("view.html", instituicao=instituicao)

# -----------------------------
# ROTAS DE PESSOAS
# -----------------------------
@app.route("/pessoas")
def pessoas():
    query_term = request.args.get("q")
    todas_pessoas = listar_pessoas()
    if query_term:
        pessoas = [
            p for p in todas_pessoas
            if query_term.lower() in p['nome'].lower()
            or query_term.lower() in p['email'].lower()
        ]
    else:
        pessoas = todas_pessoas
    return render_template("pessoas.html", pessoas=pessoas, query_term=query_term)

@app.route("/pessoas/add", methods=["GET", "POST"])
def add_pessoa():
    if request.method == "POST":
        dados = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "telefone": request.form.get("telefone"),
            "instagram": request.form.get("instagram"),
            "cargo": request.form.get("cargo"),
            "observacao": request.form.get("observacao"),
        }
        adicionar_pessoa(dados)
        return redirect(url_for("pessoas"))
    return render_template("add_pessoas.html")

@app.route("/pessoas/<int:id>")
def view_pessoa(id):
    pessoa = buscar_pessoa(id)
    if not pessoa:
        return "Pessoa não encontrada", 404
    return render_template("view_pessoas.html", pessoa=pessoa)

@app.route("/pessoas/edit/<int:id>", methods=["GET", "POST"])
def edit_pessoa(id):
    pessoa = buscar_pessoa(id)
    if not pessoa:
        return "Pessoa não encontrada", 404

    if request.method == "POST":
        dados = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "telefone": request.form.get("telefone"),
            "instagram": request.form.get("instagram"),
            "cargo": request.form.get("cargo"),
            "observacao": request.form.get("observacao"),
        }
        atualizar_pessoa(id, dados)
        return redirect(url_for("pessoas"))
    return render_template("edit_pessoas.html", pessoa=pessoa)

@app.route("/pessoas/delete/<int:id>")
def delete_pessoa(id):
    excluir_pessoa(id)
    return redirect(url_for("pessoas"))

# -----------------------------
# RODAR O SERVIDOR
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
    
