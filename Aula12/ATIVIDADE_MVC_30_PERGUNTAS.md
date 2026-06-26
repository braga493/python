# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

flask/aula12/models/

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

streamflix.db,aula12

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

ModeloBase,FilmeFavorito,HistoricoBusca,base.py,filme_favorito.py,historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

ModeloBase,id,data_ciracao,data_atualizacao.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

filmes_favoritos, para fazer referencia a tabela no sql a qual a tabela criada em python esta ligada.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

tmdb_id,sim nullable=False e unique=True

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Ele primeiro analiza se o filme não existe por meio do id, e caso ele n existe ele cadastra o filme.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Historico_busca.py, classe:HistoricoBusca metodo:ultimas.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

Inteira, titulo, poster, nota, ano.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

As classes FilmeFavorito,ModeloBase,HistoricoBusca, porque ele seleciona apenas o que será utilizado.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

3,
Filmes_bp = Blueprint("filmes", __name__, url_prefix="/filmes"),
favoritos_bp = Blueprint("favoritos", __name__, url_prefix="/favoritos"),dashboard_bp = Blueprint("dashboard", __name__).


**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

Controllers/filmespopulares,populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

Chama o Service 'TmdbApi' para buscar os filmes, 'FilmeFavorito.listar()' - consulta o Model para saber quais filmes ja estao nos favoritos.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

O controller 'filmes_controller.py',funcao'buscar()'. Usa o model 'HistoricoBusca',54.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

POST,"/adicionar/<int:550>"

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Não vai achar o filme porque o id está vazio.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

Na pasta controllers, 
filmes_bp = Blueprint("filmes", __name__, url_prefix="/filmes"),
favoritos_bp = Blueprint("favoritos", __name__, url_prefix="/favoritos"),
dashboard_bp = Blueprint("dashboard", __name__)



**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

Controller: dashboard_controller.py, função index().
Variáveis enviadas: populares, melhores, total_favoritos, historico, modo_demo.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

É um Service (serviço de API),justificativa: não define rotas nem templates, fornece acesso a dados externos da API TMDB e formata filmes,
quem chama a classe é controllers (dashboard_controller.py e filmes_controller.py) usam TmdbApi para buscar filmes, detalhes e streaming.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

O termo vem de request.args.get("q", ""),é request.args.Quando a requisição é GET se usa request.args , se o formulário for enviado por POST, o controller usa request.form.get("q", "").


---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

flask/aula12/views/templates 

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

flask/aula12/views/templates/layout.html,{% extends "layout.html" %}.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

       StreamFlix:{{ url_for('dashboard.index') }}
       Populares:{{ url_for('filmes.populares') }}
       Melhores: {{ url_for('filmes.melhores') }}
       Buscar:{{ url_for('filmes.buscar') }}
       Favoritos:{{ url_for('favoritos.listar') }}

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

views/templates/filmes/detalhe.html,a variável streaming vem do controller filmes_controller.py, função detalhe(), que chama TmdbApi().streaming(filme_id).

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

É um pedaço reutilizado,ele é incluído por views/templates/filmes/lista.html,usando {% include "filmes/_card.html" %}.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

A view usa a variável favorito passada pelo controller, em detalhe.html, há {% if favorito %}. 

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

flask/Aula12/views/static/css/style.css, o layout.html carrega com <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

{% for fav in favoritos %}, fav.titulo, fav.nota, fav.ano, fav.data_criacao.strftime('%d/%m/%Y')

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Significa que o site está em modo demonstração quando não há chave TMDB configurada, a variável é disponibilizada por app.py.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

View: views/templates/filmes/detalhe.html exibe o botão e o formulário POST para url_for('favoritos.adicionar', tmdb_id=filme.id).

Controller: a rota favoritos.adicionar em controllers/favoritos_controller.py recebe o POST, lê titulo, poster_path, nota, ano e voltar do formulário, e chama FilmeFavorito.adicionar(...).

Model: models/filme_favorito.py realiza FilmeFavorito.adicionar(...), verifica se o filme já existe com buscar_por_tmdb, adiciona o novo favorito à sessão com db.session.add(fav) e salva com db.session.commit().

Redirect: após salvar, o controller redireciona de volta para a página do detalhe usando o valor de voltar ou url_for('favoritos.listar').

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
