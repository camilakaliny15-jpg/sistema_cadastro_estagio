from database import db

class Instituicao(db.Model):
    __tablename__ = "instituicoes"

    id = db.Column(db.Integer, primary_key=True)
    nome_oficial = db.Column(db.String, nullable=False)
    nome_fantasia = db.Column(db.String)
    tipo_instituicao = db.Column(db.String)
    status = db.Column(db.String)
    email_oficial = db.Column(db.String)
    telefone_principal = db.Column(db.String)
    telefone_alternativo = db.Column(db.String)
    endereco_completo = db.Column(db.String)
    cep = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    uf = db.Column(db.String)
    site_url = db.Column(db.String)
    pessoa_contato = db.Column(db.String)
    observacao = db.Column(db.String)


class Pessoa(db.Model):
    __tablename__ = "pessoas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    telefone = db.Column(db.String)
    endereco = db.Column(db.String)
    cargo = db.Column(db.String)
    observacao = db.Column(db.String)
    instagram = db.Column(db.String)
