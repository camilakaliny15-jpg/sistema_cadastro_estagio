import sqlite3

# Conecta ao banco (se não existir, cria)
conn = sqlite3.connect('cadastro.db')

# Cria cursor
cursor = conn.cursor()

# Cria tabela pessoas
cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    endereco TEXT
)
''')

conn.commit()
conn.close()

print("Banco de dados 'cadastro.db' e tabela 'pessoas' criados com sucesso!")
