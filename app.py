from flask import Flask, render_template, request, redirect, url_for
from models import db, Unidade, Encomenda
from forms import UnidadeForm, EncomendaForm, BaixaEncomendaForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///condominio.db'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unidades')
def listar_unidades():
    unidades = Unidade.query.all()
    return render_template('listar_unidades.html', unidades=unidades)

@app.route('/unidades/alterar', methods=['GET', 'POST'])
def alterar_unidades():
    form = UnidadeForm()
    if request.method == 'POST' and form.validate_on_submit():
        unidade = Unidade.query.filter_by(numero=form.numero.data).first()
        unidade.proprietario = form.proprietario.data
        unidade.telefone = form.telefone.data
        unidade.email = form.email.data
        db.session.commit()
        return redirect(url_for('listar_unidades'))
    unidades = Unidade.query.all()
    return render_template('alterar_unidades.html', unidades=unidades, form=form)

@app.route('/encomendas/registrar', methods=['GET', 'POST'])
def registrar_encomenda():
    form = EncomendaForm()
    if request.method == 'POST' and form.validate_on_submit():
        encomenda = Encomenda(
            unidade=form.unidade.data,
            data_recebimento=form.data_recebimento.data,
            porteiro=form.porteiro.data,
            tipo=form.tipo.data
        )
        db.session.add(encomenda)
        db.session.commit()
        return redirect(url_for('listar_encomendas'))
    return render_template('registrar_encomenda.html', form=form)

@app.route('/encomendas')
def listar_encomendas():
    encomendas = Encomenda.query.filter_by(data_entrega=None).all()
    return render_template('listar_encomendas.html', encomendas=encomendas)

@app.route('/encomendas/baixa', methods=['GET', 'POST'])
def dar_baixa():
    form = BaixaEncomendaForm()
    if request.method == 'POST' and form.validate_on_submit():
        encomenda = Encomenda.query.filter_by(id=form.id.data).first()
        encomenda.data_entrega = form.data_entrega.data
        encomenda.morador = form.morador.data
        encomenda.porteiro_entrega = form.porteiro_entrega.data
        db.session.commit()
        return redirect(url_for('listar_encomendas'))
    encomendas = Encomenda.query.filter_by(data_entrega=None).all()
    return render_template('dar_baixa.html', encomendas=encomendas, form=form)

@app.route('/encomendas/historico')
def historico():
    encomendas = Encomenda.query.filter(Encomenda.data_entrega.isnot(None)).all()
    return render_template('historico.html', encomendas=encomendas)

if __name__ == '__main__':
    app.run(debug=True)
