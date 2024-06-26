from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Unidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(4), unique=True, nullable=False)
    proprietario = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Encomenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unidade = db.Column(db.String(4), db.ForeignKey('unidade.numero'), nullable=False)
    data_recebimento = db.Column(db.Date, nullable=False)
    porteiro = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data_entrega = db.Column(db.Date, nullable=True)
    morador = db.Column(db.String(100), nullable=True)
    porteiro_entrega = db.Column(db.String(100), nullable=True)

