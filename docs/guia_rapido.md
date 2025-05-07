# Guia Rápido do EmailMasterPT

## Instalação

```bash
pip install emailmasterpt

```

## Configuração Inicial

### 1. Importar e Configurar Provedor

```python
from emailmasterpt import ProvedorGmail, ProvedorOutlook, ProvedorSMTP

# Para Gmail
provedor_gmail = ProvedorGmail("seu@gmail.com", "sua-senha")

# Para Outlook
provedor_outlook = ProvedorOutlook("seu@outlook.com", "sua-senha")

# Para SMTP Personalizado
provedor_custom = ProvedorSMTP(
    usuario="usuario@empresa.com",
    senha="sua-senha",
    host="smtp.empresa.com",
    porta=587
)
```

### 2. Criar Instância do EmailMasterPT

```python
from emailmasterpt import EmailMasterPT

email = EmailMasterPT(provedor_gmail)
```

## Enviando Emails
### Email Básico

```python
email.enviar_email(
    destinatario="cliente@exemplo.com",
    assunto="Bem-vindo",
    corpo="Obrigado por se cadastrar!"
)
```

### Email com Anexos

```python
email.enviar_email(
    destinatario="relatorios@exemplo.com",
    assunto="Relatório Mensal",
    corpo="Segue o relatório em anexo.",
    anexos=["relatorio.pdf", "dados.xlsx"]
)
```

### Email para Múltiplos Destinatários

```python

email.enviar_email(
    destinatario=["time@exemplo.com", "gerencia@exemplo.com"],
    assunto="Atualização do Projeto",
    corpo="Status atual do projeto...",
    cc="coordenacao@exemplo.com",
    cco="backup@exemplo.com"
)
```

### Múltiplos Destinatários

```python
email.enviar_email(
    destinatario=["dest1@exemplo.com", "dest2@exemplo.com"],
    assunto="E-mail para Múltiplos Destinatários",
    corpo="Olá a todos!",
    cc="copiado@exemplo.com",  # Cópia
    cco=["oculto1@exemplo.com", "oculto2@exemplo.com"]  # Cópia oculta
)
```

## Agendando Emails

### 1. Criar Agendador

```python
from emailmasterpt import AgendadorEmails
from datetime import datetime, timedelta

agendador = AgendadorEmails()
```

### 2. Agendar Email

```python
# Agendar para daqui a 2 horas
data_envio = datetime.now() + timedelta(hours=2)

agendador.agendar_email(
    email,
    data_envio,
    destinatario="lembretes@exemplo.com",
    assunto="Reunião Importante",
    corpo="Não se esqueça da reunião às 15h"
)
```
### 3. Gerenciar Agendamentos

```python
# Listar emails agendados
for tarefa in agendador.listar_emails_agendados():
    print(f"ID: {tarefa['id']}, Envio: {tarefa['proximo_envio']}")

# Cancelar agendamento
agendador.cancelar_email("id_do_agendamento")
```
