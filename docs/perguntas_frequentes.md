# Perguntas Frequentes - EmailMasterPT


## 1. Erro ao conectar com o Gmail

**Problema**: Recebo o erro "ErroConexao: Falha ao conectar ao servidor".

**Soluções**:
- Verifique se o "Acesso a apps menos seguros" está ativado na conta Google
- Gere uma "Senha de App" se usar verificação em duas etapas
- Verifique se há bloqueios por firewall ou antivírus

### 2. Timeout na conexão

**Problema**: A conexão demora muito ou falha por timeout.

**Solução**:
```python
email = EmailMasterPT(provedor)
email.servidor.timeout = 30  # Aumentar timeout para 30 segundos
```
### 3. Emails não estão sendo entregues

**Problema**: O código executa sem erros mas o destinatário não recebe.

**Verifique**:
- A pasta de spam do destinatário
- Se o domínio do remetente não está bloqueado
- Os logs do servidor SMTP (se disponível)
  
### 4. Limite de tamanho para anexos

**Pergunta**: Qual o tamanho máximo para anexos?
**Resposta**: O limite depende do provedor:
- Gmail: 25MB
- Outlook: 20MB
- SMTP personalizado: Consulte seu administrador

### 5. Emails agendados não são enviados

**Problema**: O programa é encerrado antes do horário agendado.

**Solução**: Mantenha o programa em execução ou use um agendador externo como:
- Servidores (ex: Flask, Django com celery)
- CRON jobs (Linux)
- Agendador de Tarefas (Windows)

### 6. Como verificar emails agendados?

```python
agendador = AgendadorEmails()
tarefas = agendador.listar_emails_agendados()
for tarefa in tarefas:
    print(f"ID: {tarefa['id']}, Horário: {tarefa['proximo_envio']}")
```

### 7. Como usar com meu próprio servidor SMTP?

```python
provedor = ProvedorSMTP(
    usuario="seu@dominio.com",
    senha="sua-senha",
    host="smtp.dominio.com",
    porta=587  # Ou 465 para SSL
)
```

### 8. Posso usar sem TLS/SSL?

**Resposta**: Não recomendado por questões de segurança, mas possível com:
```python
provedor = ProvedorSMTP(..., porta=25)
email.servidor.starttls()  # Remova esta linha
```

### 9. Como gerenciar credenciais com segurança?

**Recomendações**:
- Use variáveis de ambiente:

```python
import os
provedor = ProvedorGmail(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
```
- Utilize serviços como AWS Secrets Manager ou HashiCorp Vault
- Nunca comite credenciais em repositórios Git
  
### 10. Como enviar para muitos destinatários?

**Solução**: Use batches e intervalos para evitar bloqueios:
```python
import time

destinatarios = [...]  # Lista grande de emails

for i in range(0, len(destinatarios), 50):  # Envia em grupos de 50
    grupo = destinatarios[i:i+50]
    email.enviar_email(destinatario=grupo, ...)
    time.sleep(10)  # Espera 10 segundos entre batches
```
