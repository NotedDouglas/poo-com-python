import sqlite3

# Conecta ao banco ou cria se não existir
conn = sqlite3.connect('animal.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando a tabela (sem aspas erradas e com sintaxe correta)
cursor.execute('''CREATE TABLE IF NOT EXISTS dog (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               weight REAL,
               height REAL,
               breed TEXT
               )''')

# Dados para inserir na tabela
pets_data = [
    ('Luke', 9, 45, 0.80, 'Pastor Alemão'),
    ('Buddy', 2, 7.2, 0.3, 'Golden Retriever'),
    ('Whiskers', 1, 1.2, 0.15, 'Siamese'),
    ('Max', 4, 5.0, 0.4, 'Labrador')
]

# Inserindo os dados na tabela (corrigido INSERT INTO e VALUES)
for pet in pets_data:
    cursor.execute('INSERT INTO dog (name, '
                   'age, '
                   'weight, '
                   'height, '
                   'breed) VALUES (?, ?, ?, ?, ?)',
                   pet)

# Commit das alterações
conn.commit()
conn.close()

print("Registros inseridos com sucesso")
