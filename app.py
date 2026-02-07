from flask import Flask, render_template, request, redirect
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
# ROTA PRINCIPAL COM BUSCA
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    termo = request.args.get("q")  # pega o valor do campo de busca
    if termo:
        instituicoes = buscar_instituicoes_por_termo(termo)
    else:
        instituicoes = listar_instituicoes()
    return render_template("index.html", instituicoes=instituicoes)


# -----------------------------
# ADICIONAR INSTITUIÇÃO
# -----------------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        dados = {
            "cnpj": request.form.get("cnpj"),
            "nome_oficial": request.form.get("nome_oficial"),
            "nome_fantasia": request.form.get("nome_fantasia"),
            "tipo_instituicao": request.form.get("tipo_instituicao"),
            "status": request.form.get("status"),
            "email_oficial": request.form.get("email_oficial"),
            "telefone_principal": request.form.get("telefone_principal"),
            "telefone_alternativo": request.form.get("telefone_alternativo"),
            "endereco_completo": request.form.get("endereco_completo"),
            "cep": request.form.get("cep"),
            "cidade": request.form.get("cidade"),
            "estado": request.form.get("estado"),
            "uf": request.form.get("uf"),
            "site_url": request.form.get("site_url"),
            "pessoa_contato": request.form.get("pessoa_contato"),
            "observacao": request.form.get("observacao"),
        }
        adicionar_instituicao(dados)
        return redirect("/")
    return render_template("add.html")


# -----------------------------
# EDITAR INSTITUIÇÃO
# -----------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    instituicao = buscar_instituicao(id)
    if not instituicao:
        return redirect("/")

    if request.method == "POST":
        dados = {
            "cnpj": request.form.get("cnpj"),
            "nome_oficial": request.form.get("nome_oficial"),
            "nome_fantasia": request.form.get("nome_fantasia"),
            "tipo_instituicao": request.form.get("tipo_instituicao"),
            "status": request.form.get("status"),
            "email_oficial": request.form.get("email_oficial"),
            "telefone_principal": request.form.get("telefone_principal"),
            "telefone_alternativo": request.form.get("telefone_alternativo"),
            "endereco_completo": request.form.get("endereco_completo"),
            "cep": request.form.get("cep"),
            "cidade": request.form.get("cidade"),
            "estado": request.form.get("estado"),
            "uf": request.form.get("uf"),
            "site_url": request.form.get("site_url"),
            "pessoa_contato": request.form.get("pessoa_contato"),
            "observacao": request.form.get("observacao"),
        }
        atualizar_instituicao(id, dados)
        return redirect("/")

    return render_template("edit.html", instituicao=instituicao)


# -----------------------------
# DELETAR INSTITUIÇÃO
# -----------------------------
@app.route("/delete/<int:id>")
def delete(id):
    excluir_instituicao(id)
    return redirect("/")
#-----------------------
# VER DETALHES
#-----------------------
@app.route("/view/<int:id>")
def view(id):
    instituicao = buscar_instituicao(id)

    if not instituicao:
        return redirect("/")

    return render_template("view.html", instituicao=instituicao)

#- - - -  ROTAS DE PESSOAS- - - - -  -  #
#----------------------------
#       buscar/listar pessoas
#----------------------------
@app.route("/pessoas")
def pessoas():
    query_term = request.args.get("q")
    todas_pessoas = listar_pessoas()

    if query_term:
        pessoas = [
            p for p in todas_pessoas
            if query_term.lower() in p['nome'].lower()
            or query_term.lower() in p['email'].lower()
            or query_term.lower() in p['telefone'].lower()
        ]
    else:
        pessoas = todas_pessoas

    return render_template("pessoas.html", pessoas=pessoas, query_term=query_term)
#------------------------------
#          adicionar pessoas
#------------------------------
@app.route("/pessoas/add", methods=["GET", "POST"])
def add_pessoa():
    if request.method == "POST":
        dados = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "telefone": request.form.get("telefone"),
            "endereco": request.form.get("endereco"),
            "instagram": request.form.get("instagram"),
            "facebook": request.form.get("facebook"),
            "cargo": request.form.get("cargo"),
            "observacao": request.form.get("observacao"),
        }

        adicionar_pessoa(dados)
        return redirect("/pessoas")

    return render_template("add_pessoas.html")
#------------------------------
#          ver detalhes
#------------------------------
@app.route("/pessoas/<int:id>")
def view_pessoa(id):
    pessoa = buscar_pessoa(id)

    if not pessoa:
        return "Pessoa não encontrada", 404

    return render_template("view_pessoas.html", pessoa=pessoa)
#------------------------------
#          editar pessoas
#------------------------------
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
            "endereco": request.form.get("endereco"),
            "instagram": request.form.get("instagram"),
            "facebook": request.form.get("facebook"),
            "cargo": request.form.get("cargo"),
            "observacao": request.form.get("observacao"),
        }

        atualizar_pessoa(id, dados)
        return redirect(f"/pessoas/{id}")

    return render_template("edit_pessoas.html", pessoa=pessoa)
#------------------------------
#          deletar pessoas
#------------------------------
@app.route("/pessoas/delete/<int:id>")
def delete_pessoa(id):
    excluir_pessoa(id)
    return redirect("/pessoas")

# -----------------------------
# RODAR O SERVIDOR
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
