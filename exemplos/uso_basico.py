from emailmasterpt import EmailMasterPT, ProvedorGmail

# Configurar provedor Gmail
provedor = ProvedorGmail("seu@gmail.com", "sua-senha")
email = EmailMasterPT(provedor)

# Enviar email simples
email.enviar_email(
    destinatario="destinatario@exemplo.com",
    assunto="Primeiro Email",
    corpo="Olá, este é meu primeiro email usando EmailMasterPT!"
)

# Enviar email com anexos e cópias
email.enviar_email(
    destinatario=["dest1@exemplo.com", "dest2@exemplo.com"],
    assunto="Email com Anexos",
    corpo="Confira os arquivos anexados.",
    cc="cc@exemplo.com",
    cco=["cco1@exemplo.com", "cco2@exemplo.com"],
    anexos=["/caminho/para/arquivo1.pdf", "/caminho/para/arquivo2.jpg"]
)

print("Emails enviados com sucesso!")