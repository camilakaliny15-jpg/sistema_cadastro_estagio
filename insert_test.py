import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

registros = [
    ("Maria Silva", "88 9XXXX-XXXX", "maria@example.com", "Rua A, 123, JP"),
    ("João Souza", "88 9YYYY-YYYY", "joao@example.com", "Av. B, 456, JP"),
]

cursor.executemany('INSERT INTO pessoas (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)', registros)

conn.commit()
conn.close()
print("Inseridos registros de teste.")
