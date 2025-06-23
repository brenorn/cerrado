from flask import Flask, render_template

app = Flask(__name__)


# Rota para a página inicial
@app.route('/')
def home():
    return render_template('website.html')

# Rota para a página do Geoportal
@app.route('/geoportal')
def geoportal():
    return render_template('geoportal.html')

# Rota para a trilha de Gestão Pública
@app.route('/gestao-publica')
def gestao_publica():
    return render_template('gestao-publica.html')

# Rota para a trilha de Desenvolvimento Sustentável
@app.route('/desenvolvimento-sustentavel')
def desenvolvimento_sustentavel():
    return render_template('desenvolvimento-sustentavel.html')

# Rota para a trilha de Análise de Dados
@app.route('/analise-dados')
def analise_dados():
    return render_template('analise-dados.html')

if __name__ == '__main__':
    app.run(debug=True)
