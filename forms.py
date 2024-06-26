from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UnidadeForm(FlaskForm):
    numero = StringField('Número da Unidade', validators=[DataRequired()])
    proprietario = StringField('Proprietário', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class EncomendaForm(FlaskForm):
    unidade = StringField('Unidade', validators=[DataRequired()])
    data_recebimento = DateField('Data de Recebimento', validators=[DataRequired()])
    porteiro = StringField('Porteiro', validators=[DataRequired()])
    tipo = SelectField('Tipo de Encomenda', choices=[('carta', 'Carta'), ('envelope', 'Envelope'), ('caixa', 'Caixa')], validators=[DataRequired()])
    submit = SubmitField('Registrar')

class BaixaEncomendaForm(FlaskForm):
    id = StringField('ID da Encomenda', validators=[DataRequired()])
    data_entrega = DateField('Data de Entrega', validators=[DataRequired()])
    morador = StringField('Morador', validators=[DataRequired()])
    porteiro_entrega = StringField('Porteiro que Entregou', validators=[DataRequired()])
    submit = SubmitField('Dar Baixa')
