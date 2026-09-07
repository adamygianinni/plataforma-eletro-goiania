# =====================================================================
# PROJETO: Plataforma de Mapeamento de Descarte Eletrônico - Goiânia
# DISCIPLINA: Atividade Extensionista II - CST Análise e Desenvolvimento de Sistemas
# AUTOR: Adamy Gianinni dos Santos | RU: 2600854
# INSTITUIÇÃO: Centro Universitário Internacional UNINTER (Polo Goiânia - GO)
# ANO: 2026
# =====================================================================

import os
import sys
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializacao basica do Flask
app = Flask(__name__)

# Configuracao do SQLite local
# Deixei o caminho relativo padrao na pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pontos_coleta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da tabela do banco de dados
class PontoColeta(db.Model):
    __tablename__ = 'pontos_coleta'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(50), nullable=False) # Sukatech ou Green Eletron
    endereco = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(100), nullable=True)
    contato = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    # Funcao manual para converter os dados para JSON
    def to_dict(self):
        # Formatacao dos dados
        dict_dados = {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'endereco': self.endereco,
            'bairro': self.bairro,
            'horario': self.horario if self.horario else 'Nao informado',
            'contato': self.contato if self.contato else 'Nao informado',
            'latitude': self.latitude,
            'longitude': self.longitude
        }
        return dict_dados

# Funcao auxiliar para popular o banco de dados caso esteja vazio
def popular_dados_iniciais():
    total_registros = PontoColeta.query.count()
    
    if total_registros == 0:
        print("[AVISO] Banco de dados vazio. Inserindo pontos de coleta de Goiania...")
        
        lista_pontos = [
    # --- PROGRAMA SUKATECH / GOVERNO DE GOIÁS ---
    PontoColeta(
        nome="Sede Sukatech - EFG José Luiz Bittencourt",
        categoria="Sukatech",
        endereco="Rua BF-25 esq. c/ Av. JC-15",
        bairro="Jardim Floresta",
        horario="Segunda a Sexta, 08h às 17h",
        contato="(62) 4141-9800",
        latitude=-16.6090,
        longitude=-49.3412
    ),
    PontoColeta(
        nome="Palácio Pedro Ludovico Teixeira (PEV)",
        categoria="Sukatech",
        endereco="Praça Cívica / Rua 82, nº 400",
        bairro="Setor Central",
        horario="08h às 18h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.6818,
        longitude=-49.2559
    ),
    PontoColeta(
        nome="Secretaria de Estado da Educação - SEDUC (PEV)",
        categoria="Sukatech",
        endereco="5ª Avenida, Qd. 71, nº 212",
        bairro="Setor Leste Vila Nova",
        horario="08h às 17h",
        contato="(62) 3269-3134",
        latitude=-16.6715,
        longitude=-49.2415
    ),
    PontoColeta(
        nome="Secretaria de Segurança Pública - SSP (PEV)",
        categoria="Sukatech",
        endereco="Av. Anhanguera, nº 7364",
        bairro="Setor Aeroviário",
        horario="08h às 17h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.6718,
        longitude=-49.2998
    ),
    PontoColeta(
        nome="Secretaria de Estado da Saúde - SES (PEV)",
        categoria="Sukatech",
        endereco="Av. SC 1, nº 299",
        bairro="Parque Santa Cruz",
        horario="08h às 17h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.7198,
        longitude=-49.2312
    ),
    PontoColeta(
        nome="Secretaria de Estado da Economia (PEV)",
        categoria="Sukatech",
        endereco="Av. Vereador José Monteiro, nº 2233",
        bairro="Setor Nova Vila",
        horario="08h às 17h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.6620,
        longitude=-49.2440
    ),
    PontoColeta(
        nome="HUB Goiás (PEV SEAD)",
        categoria="Sukatech",
        endereco="Rua 261, nº 384",
        bairro="Setor Leste Universitário",
        horario="08h às 18h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.6802,
        longitude=-49.2415
    ),
    PontoColeta(
        nome="Goinfra (PEV)",
        categoria="Sukatech",
        endereco="Av. Gov. José Ludovico de Almeida, nº 20",
        bairro="Conjunto Caiçara",
        horario="08h às 17h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.6492,
        longitude=-49.2995
    ),
    PontoColeta(
        nome="SEMAD - Sec. Meio Ambiente (PEV)",
        categoria="Sukatech",
        endereco="Av. José Leandro da Cruz, nº 1578",
        bairro="Parque Amazônia",
        horario="08h às 17h",
        contato="gdct.secti@goias.gov.br",
        latitude=-16.7265,
        longitude=-49.2781
    ),

    # --- REDE GREEN ELETRON ---
    PontoColeta(
        nome="Green Eletron - Casas Bahia Anhanguera",
        categoria="Green Eletron",
        endereco="Av. Anhanguera, nº 4482",
        bairro="Setor Central",
        horario="Horário Comercial",
        contato="contato@greeneletron.org.br",
        latitude=-16.6740,
        longitude=-49.2605
    ),
    PontoColeta(
        nome="Green Eletron - Casas Bahia Centro",
        categoria="Green Eletron",
        endereco="Av. Anhanguera, nº 4603",
        bairro="Setor Central",
        horario="Horário Comercial",
        contato="contato@greeneletron.org.br",
        latitude=-16.6748,
        longitude=-49.2628
    ),
    PontoColeta(
        nome="Green Eletron - Casas Bahia Pio XII",
        categoria="Green Eletron",
        endereco="Av. Pio XII, Qd. 100, nº 829",
        bairro="Vila Aurora Oeste",
        horario="Horário Comercial",
        contato="contato@greeneletron.org.br",
        latitude=-16.6815,
        longitude=-49.3032
    ),
    PontoColeta(
        nome="Green Eletron - Casas Bahia Pedro Ludovico",
        categoria="Green Eletron",
        endereco="Av. Laudelino Gomes, Qd. 210, nº 283",
        bairro="Setor Pedro Ludovico",
        horario="Horário Comercial",
        contato="contato@greeneletron.org.br",
        latitude=-16.7125,
        longitude=-49.2612
    ),
    PontoColeta(
        nome="Green Eletron - Casas Bahia Campinas",
        categoria="Green Eletron",
        endereco="Av. 24 de Outubro, Qd. 46, nº 1504",
        bairro="Setor Campinas",
        horario="Horário Comercial",
        contato="contato@greeneletron.org.br",
        latitude=-16.6688,
        longitude=-49.2905
    ),
    PontoColeta(
        nome="Green Eletron - Shopping Passeio das Águas",
        categoria="Green Eletron",
        endereco="Av. Perimetral Norte, nº 8303",
        bairro="Fazenda Caveiras",
        horario="10h às 22h",
        contato="contato@greeneletron.org.br",
        latitude=-16.6268,
        longitude=-49.2778
    )
]
        
        # Inserindo um a um no banco
        for item in lista_pontos:
            db.session.add(item)
            
        db.session.commit()
        print("[SUCESSO] Dados iniciais cadastrados com sucesso!")
    else:
        print(f"[INFO] O banco ja contem {total_registros} pontos cadastrados.")

# Rota principal - Pagina Web
@app.route('/')
def home():
    # Renderiza a pagina HTML do projeto
    return render_template('index.html')

# Rota da API para retornar os pontos em formato JSON
@app.route('/api/pontos', methods=['GET'])
def get_todos_pontos():
    todos_pontos = PontoColeta.query.all()
    resultado = []
    
    # Loop manual simples para montar a lista
    for p in todos_pontos:
        resultado.append(p.to_dict())
        
    return jsonify(resultado), 200

# Rota para cadastrar um novo ponto sugerido
@app.route('/api/pontos', methods=['POST'])
def post_novo_ponto():
    dados = request.get_json()
    
    # Validacao basica dos campos obrigatorios
    if not dados.get('nome') or not dados.get('endereco') or not dados.get('bairro'):
        return jsonify({'erro': 'Campos obrigatorios nao foram preenchidos'}), 400
    
    # Tratamento simples para coordenadas ficticias na regiao central caso venham vazias
    lat = dados.get('latitude')
    lng = dados.get('longitude')
    
    if not lat:
        lat = -16.6869
    if not lng:
        lng = -49.2648

    novo_registro = PontoColeta(
        nome=dados.get('nome'),
        categoria=dados.get('categoria', 'Ponto Comunitario'),
        endereco=dados.get('endereco'),
        bairro=dados.get('bairro'),
        horario=dados.get('horario', 'A combinar'),
        contato=dados.get('contato', 'Nao informado'),
        latitude=float(lat),
        longitude=float(lng)
    )
    
    try:
        db.session.add(novo_registro)
        db.session.commit()
        print(f"[CADASTRO] Novo ponto inserido: {novo_registro.nome}")
        return jsonify({'status': 'sucesso', 'mensagem': 'Ponto cadastrado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"[ERRO] Falha ao cadastrar: {str(e)}")
        return jsonify({'status': 'erro', 'mensagem': 'Erro interno ao salvar no banco'}), 500

# Execucao do servidor
if __name__ == '__main__':
    print("=" * 60)
    print("Iniciando aplicacao do Projeto Extensionista II - UNINTER")
    print("Aluno: Adamy Gianinni dos Santos | RU: 2600854")
    print("=" * 60)
    
    with app.app_context():
        db.create_all()
        popular_dados_iniciais()
        
    # Rodando em modo de depuracao local
    app.run(debug=True, port=5000)