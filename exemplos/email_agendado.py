from emailmasterpt import EmailMasterPT, ProvedorGmail, AgendadorEmails
from datetime import datetime, timedelta

# Configurar provedor
provedor = ProvedorGmail("seu@gmail.com", "sua-senha")
email = EmailMasterPT(provedor)

# Criar agendador
agendador = AgendadorEmails()

# Agendar email para daqui a 1 hora
data_envio = datetime.now() + timedelta(hours=1)

id_tarefa = agendador.agendar_email(
    email,
    data_envio,
    destinatario="destinatario@exemplo.com",
    assunto="Email Agendado",
    corpo="Este email foi agendado com sucesso!",
    anexos=["/caminho/para/arquivo.pdf"]
)

print(f"Email agendado com ID: {id_tarefa}")

# Listar emails agendados
print("\nEmails agendados:")
for tarefa in agendador.listar_emails_agendados():
    print(f"ID: {tarefa['id']}, Próximo envio: {tarefa['proximo_envio']}")

# Manter o programa rodando para o agendador funcionar
try:
    while True:
        pass
except KeyboardInterrupt:
    agendador.encerrar()