from flask import Flask

app = Flask(__name__)

@app.route('/decorator')

def decorator():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Decorators no Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                background-color: #f4f4f9;
                color: #333;
            }
            h1 {
                color: #007BFF;
            }
            code {
                background-color: #e8e8e8;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <h1>O que são Decorators no Flask?</h1>
        <p>Decorators no Flask são usados para associar rotas (URLs) a funções específicas. Eles permitem que você defina o comportamento de uma rota de forma clara e organizada.</p>
        <h2>Como funciona?</h2>
        <p>Um decorator é aplicado utilizando o símbolo <code>@</code> seguido do nome do decorator. No Flask, o decorator mais comum é <code>@app.route</code>, que mapeia uma URL para uma função.</p>
        <h2>Exemplo:</h2>
        <pre><code>
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo à página inicial!'

if __name__ == '__main__':
    app.run(debug=True)
        </code></pre>
        <p>No exemplo acima, o decorator <code>@app.route</code> associa a URL <code>'/'</code> à função <code>home()</code>. Quando o usuário acessa a URL raiz, a função é executada e retorna a mensagem "Bem-vindo à página inicial!".</p>
        <h2>Vantagens</h2>
        <ul>
            <li>Organização do código.</li>
            <li>Facilidade para definir rotas.</li>
            <li>Clareza na estrutura da aplicação.</li>
        </ul>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)