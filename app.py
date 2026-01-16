from flask import Flask, render_template, request, redirect
from database import (
    listar_instituicoes,
    adicionar_instituicao,
    buscar_instituicao,
    buscar_instituicoes_por_termo,
    atualizar_instituicao,
    excluir_instituicao
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
            "pessoa_contato": request.form.get("pessoa_contato")
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
            "pessoa_contato": request.form.get("pessoa_contato")
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


# -----------------------------
# RODAR O SERVIDOR
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
