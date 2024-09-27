from cryptography.fernet import Fernet

# Geração de chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

# Carregar chave de criptografia
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar dados
def criptografar_senha(senha, chave):
    f = Fernet(chave)
    senha_encriptada = f.encrypt(senha.encode())
    return senha_encriptada

# Função para descriptografar dados
def descriptografar_senha(senha_encriptada, chave):
    f = Fernet(chave)
    senha_decriptada = f.decrypt(senha_encriptada).decode()
    return senha_decriptada

# Exemplo de uso
gerar_chave()  # Somente execute uma vez para gerar a chave
chave = carregar_chave()

senha = "minha_senha_secreta"
senha_criptografada = criptografar_senha(senha, chave)
print(f"Senha criptografada: {senha_criptografada}")

senha_decriptada = descriptografar_senha(senha_criptografada, chave)
print(f"Senha decriptada: {senha_decriptada}")
