import pytest
from datetime import datetime, timedelta
from emailmasterpt import AgendadorEmails, EmailMasterPT, ProvedorGmail

@pytest.fixture
def agendador():
    return AgendadorEmails()

@pytest.fixture
def email_master():
    provedor = ProvedorGmail("teste@teste.com", "senha")
    return EmailMasterPT(provedor)

def test_agendar_email(agendador, email_master):
    data_envio = datetime.now() + timedelta(minutes=10)
    id_tarefa = agendador.agendar_email(
        email_master,
        data_envio,
        destinatario="teste@teste.com",
        assunto="Teste",
        corpo="Corpo de teste"
    )
    
    assert id_tarefa in agendador.listar_emails_agendados()
    agendador.cancelar_email(id_tarefa)

def test_listar_emails_agendados(agendador, email_master):
    data_envio = datetime.now() + timedelta(minutes=5)
    id_tarefa = agendador.agendar_email(
        email_master,
        data_envio,
        destinatario="teste@teste.com",
        assunto="Teste",
        corpo="Corpo de teste"
    )
    
    emails = agendador.listar_emails_agendados()
    assert len(emails) == 1
    assert emails[0]['id'] == id_tarefa
    
    agendador.cancelar_email(id_tarefa)

def test_cancelar_email(agendador, email_master):
    data_envio = datetime.now() + timedelta(minutes=15)
    id_tarefa = agendador.agendar_email(
        email_master,
        data_envio,
        destinatario="teste@teste.com",
        assunto="Teste",
        corpo="Corpo de teste"
    )
    
    agendador.cancelar_email(id_tarefa)
    assert id_tarefa not in [t['id'] for t in agendador.listar_emails_agendados()]