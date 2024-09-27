import nmap

# Mapeamento de serviços comuns e suas vulnerabilidades
VULNERABILIDADES_CONHECIDAS = {
    "ftp": "FTP é inseguro e transmite dados em texto claro. Use SFTP.",
    "ssh": "Verifique se a autenticação com chave pública está habilitada.",
    "telnet": "Telnet é inseguro e deve ser substituído por SSH.",
    "http": "Considere usar HTTPS para proteger a comunicação.",
    "https": "Verifique se o certificado SSL é válido e atualizado.",
    "mysql": "Certifique-se de que a autenticação por senha está forte e que o acesso remoto está restrito.",
    "smtp": "Verifique a configuração de autenticação do SMTP para evitar vulnerabilidades.",
    "dns": "Certifique-se de que o servidor DNS está configurado corretamente para evitar ataques de spoofing."
}

def relatorio_vulnerabilidades(servico):
    """ Retorna a vulnerabilidade conhecida associada a um serviço """
    return VULNERABILIDADES_CONHECIDAS.get(servico.lower(), "Nenhuma vulnerabilidade conhecida para esse serviço.")

def varrer_com_nmap(host):
    """ Função que usa o Nmap para escanear portas abertas e identificar serviços e vulnerabilidades """
    nm = nmap.PortScanner()
    print(f"Iniciando varredura em {host}...\n")
    
    # Fazendo varredura nas portas mais comuns
    nm.scan(host, '21-443')  # Varre portas da 21 até a 443
    
    if host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print(f'Status: {nm[host].state()}')
        
        for protocolo in nm[host].all_protocols():
            print(f'\nProtocolo: {protocolo}')
            portas = nm[host][protocolo].keys()
            
            for porta in portas:
                estado = nm[host][protocolo][porta]["state"]
                servico = nm[host][protocolo][porta]["name"]
                print(f"Porta: {porta}\tEstado: {estado}\tServiço: {servico}")
                
                if estado == "open":  # Se a porta está aberta
                    vulnerabilidade = relatorio_vulnerabilidades(servico)
                    print(f"Vulnerabilidade: {vulnerabilidade}")
    else:
        print(f"Não foi possível escanear o host {host}. Verifique o IP e tente novamente.")

if __name__ == "__main__":
    # Solicita o IP ou hostname para escanear
    host = input("Digite o IP ou nome do host para escanear: ")
    varrer_com_nmap(host)
