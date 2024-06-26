from app import app
from models import db, Unidade

with app.app_context():
    db.create_all()
    # Preencher com as 10 unidades
    unidades = [
        Unidade(numero='101', proprietario='Proprietário 1', telefone='111111111', email='prop1@exemplo.com'),
        Unidade(numero='102', proprietario='Proprietário 2', telefone='222222222', email='prop2@exemplo.com'),
        # Adicione as outras unidades
    ]
    db.session.bulk_save_objects(unidades)
    db.session.commit()

