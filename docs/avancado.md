# Guia Avançado do EmailMasterPT

## Configurações Personalizadas

### Timeout de Conexão

```python
from emailmasterpt import EmailMasterPT, ProvedorGmail
import smtplib

provedor = ProvedorGmail("seu@gmail.com", "sua-senha")
email = EmailMasterPT(provedor)

# Configurar timeout (em segundos)
email.servidor.timeout = 30  # Antes de chamar conectar()
```

### SSL/TLS Personalizado

```python
import ssl
from emailmasterpt import ProvedorSMTP

# Criar contexto SSL personalizado
contexto_ssl = ssl.create_default_context()
contexto_ssl.protocol = ssl.PROTOCOL_TLSv1_2

provedor = ProvedorSMTP("usuario@empresa.com", "senha", "smtp.empresa.com", 465)
email = EmailMasterPT(provedor)

# Usar SSL diretamente (para porta 465)
email.servidor = smtplib.SMTP_SSL(provedor.host, provedor.porta, context=contexto_ssl)

```

## Gerenciamento de Conexões Persistentes


```python
# Manter conexão aberta para múltiplos envios
try:
    email.conectar()
    
    # Enviar vários emails
    for i in range(5):
        email.enviar_email(
            destinatario=f"dest{i}@exemplo.com",
            assunto=f"Email {i}",
            corpo="Conteúdo do email",
            manter_conexao=True  # Não desconectar após enviar
        )
finally:
    email.desconectar()
```

## Templates de E-mail

```python 
from string import Template

# Criar template
template = Template("""
Olá $nome,

Seu pedido #$pedido_id foi processado.

Atenciosamente,
$empresa
""")

# Preencher template
corpo_email = template.substitute(
    nome="João Silva",
    pedido_id="12345",
    empresa="Sua Loja"
)

email.enviar_email(
    destinatario="cliente@exemplo.com",
    assunto="Status do Pedido",
    corpo=corpo_email
)
```

## Agendamento Avançado
### Agendar com Timezone

```python
from datetime import datetime
from pytz import timezone
from emailmasterpt import AgendadorEmails

agendador = AgendadorEmails()

# Definir timezone
tz = timezone('America/Sao_Paulo')
data_envio = datetime.now(tz).replace(hour=9, minute=0) + timedelta(days=1)

agendador.agendar_email(
    email,
    data_envio,
    destinatario="dest@exemplo.com",
    assunto="Reunião Diária",
    corpo="Lembrete da reunião das 9h"
)

```

### Agendamento Recorrente (Beta)

```python
from apscheduler.triggers.cron import CronTrigger

# Configurar agendamento recorrente (toda segunda-feira às 8h)
trigger = CronTrigger(day_of_week='mon', hour=8)

agendador.agendador.add_job(
    email.enviar_email,
    trigger,
    args=["equipe@exemplo.com", "Relatório Semanal", "Segue o relatório..."],
    id="relatorio_semanal"
)
```

### Tratamento de Erros Avançado

```python

from emailmasterpt.excecoes import ErroEnvioEmail, ErroConexao
from smtplib import SMTPException

try:
    email.enviar_email(...)
except ErroConexao as e:
    print(f"Falha na conexão: {e}")
    # Tentar reconectar ou usar fallback
except ErroEnvioEmail as e:
    print(f"Erro no envio: {e}")
    # Registrar falha ou tentar novamente
except SMTPException as e:
    print(f"Erro SMTP: {e}")
    # Tratar erros específicos do SMTP
except Exception as e:
    print(f"Erro inesperado: {e}")
    # Tratamento genérico
```

## Logging e Monitoramento

```python
import logging
from emailmasterpt import EmailMasterPT

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('emailmasterpt')

# Registrar eventos
email = EmailMasterPT(provedor)
email.enviar_email = lambda *args, **kwargs: (
    logger.info("Enviando email..."),
    EmailMasterPT.enviar_email(email, *args, **kwargs),
    logger.info("Email enviado")
)

```

### Persistência de Agendamentos

```python
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from emailmasterpt import AgendadorEmails

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

agendador = AgendadorEmails(jobstores=jobstores)
# Os agendamentos serão mantidos após reiniciar o aplicativo

```

## Boas Práticas

### 1. Gerenciamento de Credenciais:
    - Nunca armazene senhas diretamente no código
    - Use variáveis de ambiente ou sistemas de gestão de segredos

### 2. Performance:
    - Reutilize conexões para múltiplos envios
    - Use threads para envios em massa

### 3. Resiliência:
    - Implemente retry para falhas temporárias
    - Tenha um provedor secundário como fallback
