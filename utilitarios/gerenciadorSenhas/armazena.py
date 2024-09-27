import sqlite3

from utilitarios.gerenciadorSenhas.criptoDecripto import criptografar_senha, descriptografar_senha

# Conectar ao banco de dados
def conectar_bd():
    conexao = sqlite3.connect("gerenciador_senhas.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS senhas
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, servico TEXT, senha BLOB)''')
    conexao.commit()
    return conexao, cursor

# Adicionar uma nova senha criptografada ao banco de dados
def adicionar_senha(servico, senha, chave):
    conexao, cursor = conectar_bd()
    senha_criptografada = criptografar_senha(senha, chave)
    cursor.execute("INSERT INTO senhas (servico, senha) VALUES (?, ?)", (servico, senha_criptografada))
    conexao.commit()
    conexao.close()

# Recuperar e descriptografar senha
def recuperar_senha(servico, chave):
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT senha FROM senhas WHERE servico=?", (servico,))
    resultado = cursor.fetchone()
    if resultado:
        senha_criptografada = resultado[0]
        senha_decriptada = descriptografar_senha(senha_criptografada, chave)
        return senha_decriptada
    else:
        return None

# Exemplo de uso
adicionar_senha("Google", "minha_senha_forte123", chave)
senha_recuperada = recuperar_senha("Google", chave)
print(f"Senha recuperada: {senha_recuperada}")
