# Plataforma Web de Mapeamento para Descarte Eletrônico em Goiânia

Projeto desenvolvido como parte dos requisitos da disciplina **Atividade Extensionista II: Tecnologia Aplicada à Inclusão Digital – Projeto**, do curso de **Tecnologia em Análise e Desenvolvimento de Sistemas** do **Centro Universitário Internacional UNINTER** (Polo Goiânia - GO).

* **Aluno:** Adamy Gianinni dos Santos
* **RU:** 2600854
* **Ano:** 2026

---

## 📌 Sobre o Projeto

A plataforma tem como objetivo centralizar, mapear e dar visibilidade aos Pontos de Entrega Voluntária (PEVs) de lixo eletroeletrônico em Goiânia - GO, conectando o cidadão aos canais oficiais de descarte sustentável e recondicionamento de equipamentos.

O sistema integra dados públicos do **Programa Sukatech** (Secretaria de Ciência, Tecnologia e Inovação de Goiás / EFG José Luiz Bittencourt) e da rede de logística reversa da **Green Eletron**, atuando em convergência com as diretrizes da **Lei Municipal nº 11.049/2023** e com os Objetivos de Desenvolvimento Sustentável da ONU (ODS 4, 9 e 12).

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Flask
* **Banco de Dados:** SQLite (persistência relacional estruturada para simulação local)
* **ORM:** Flask-SQLAlchemy
* **Front-end:** HTML5, CSS3, JavaScript (ES6)
* **Mapas e Geolocalização:** Leaflet.js / OpenStreetMap

---

## ⚙️ Funcionalidades

* **Visualização Georreferenciada:** Mapa interativo com marcadores dos PEVs do Programa Sukatech e da Green Eletron em Goiânia.
* **Busca e Filtragem:** Busca dinâmica por nome do local, bairro ou entidade responsável.
* **Geocodificação Direta via Mapa:** Marcação de novos pontos por meio de clique na interface do mapa.
* **Persistência de Dados:** Registro de novos pontos comunitários em banco relacional local.

---

## 🛠️ Como executar localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.

### Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/adamygianinni/plataforma-eletro-goiania.git](https://github.com/adamygianinni/plataforma-eletro-goiania.git)
   cd plataforma-eletro-goiania
