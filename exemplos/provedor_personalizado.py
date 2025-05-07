from emailmasterpt import EmailMasterPT, ProvedorSMTP

# Configurar provedor SMTP personalizado
provedor = ProvedorSMTP(
    usuario="usuario@seudominio.com",
    senha="sua-senha",
    host="smtp.seudominio.com",
    porta=587
)

# Inicializar EmailMasterPT
email = EmailMasterPT(provedor)

# Enviar email
email.enviar_email(
    destinatario="destinatario@exemplo.com",
    assunto="Email com Provedor Personalizado",
    corpo="Este email foi enviado usando um provedor SMTP personalizado.",
    cc=["cc@exemplo.com"],
    anexos=["/caminho/para/arquivo.pdf"]
)

print("Email enviado com sucesso usando provedor personalizado!")