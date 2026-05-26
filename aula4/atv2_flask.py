from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def curriculo():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo - Lucas Braga</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                background-color: #f4f4f9;
                color: #333;
            }
            h1, h2 {
                color: #007BFF;
            }
            .section {
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Currículo</h1>
        <div class="section">
            <h2>Lucas Braga</h2>
            <p><strong>Idade:</strong> 17 anos</p>
            <p><strong>Data de Nascimento:</strong> 10/03/2009</p>
        </div>
        <div class="section">
            <h2>Educação</h2>
            <p>Ensino Médio em andamento.</p>
        </div>
        <div class="section">
            <h2>Habilidades</h2>
            <ul>
                <li>Programação em Python</li>
                <li>Desenvolvimento Web com Flask</li>
                <li>HTML e CSS</li>
            </ul>
        </div>
        <div class="section">
            <h2>Contato</h2>
            <p>Email: lucas.braga@example.com</p>
            <p>Telefone: (11) 99999-9999</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)