import getpass

def autenticar_usuario():
    senha_mestre = getpass.getpass("Digite a senha mestre: ")
    if senha_mestre == "senha_super_secreta":
        print("Acesso concedido!")
        return True
    else:
        print("Acesso negado!")
        return False

# Exemplo de uso
if autenticar_usuario():
    # Acessar gerenciador de senhas
    print("Você pode acessar o gerenciador de senhas.")
else:
    print("Tentativa de acesso negada.")
