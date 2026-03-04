from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 🔹 LISTAR INSTITUIÇÕES
def listar_instituicoes():
    from models import Instituicao
    return Instituicao.query.all()

def buscar_instituicao(id):
    from models import Instituicao
    return Instituicao.query.get(id)

def adicionar_instituicao(dados):
    from models import Instituicao
    nova = Instituicao(**dados)
    db.session.add(nova)
    db.session.commit()

def atualizar_instituicao(id, dados):
    from models import Instituicao
    inst = Instituicao.query.get(id)
    if inst:
        for key, value in dados.items():
            setattr(inst, key, value)
        db.session.commit()

def excluir_instituicao(id):
    from models import Instituicao
    inst = Instituicao.query.get(id)
    if inst:
        db.session.delete(inst)
        db.session.commit()

def buscar_instituicoes_por_termo(termo):
    from models import Instituicao
    return Instituicao.query.filter(
        (Instituicao.nome_oficial.ilike(f"%{termo}%")) |
        (Instituicao.email_oficial.ilike(f"%{termo}%"))
    ).all()


# ---------------- PESSOAS ----------------

def listar_pessoas():
    from models import Pessoa
    return Pessoa.query.all()

def adicionar_pessoa(dados):
    from models import Pessoa
    nova = Pessoa(**dados)
    db.session.add(nova)
    db.session.commit()

def buscar_pessoa(id):
    from models import Pessoa
    return Pessoa.query.get(id)

def atualizar_pessoa(id, dados):
    from models import Pessoa
    pessoa = Pessoa.query.get(id)
    if pessoa:
        for key, value in dados.items():
            setattr(pessoa, key, value)
        db.session.commit()

def excluir_pessoa(id):
    from models import Pessoa
    pessoa = Pessoa.query.get(id)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
