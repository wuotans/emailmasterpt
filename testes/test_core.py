import pytest
from emailmasterpt import EmailMasterPT, ProvedorGmail
from emailmasterpt.excecoes import ErroEnvioEmail

@pytest.fixture
def email_master():
    provedor = ProvedorGmail("teste@teste.com", "senha")
    return EmailMasterPT(provedor)

def test_enviar_email_simples(email_master, mocker):
    mock_smtp = mocker.patch('smtplib.SMTP')
    mock_server = mock_smtp.return_value
    
    email_master.enviar_email(
        destinatario="dest@teste.com",
        assunto="Teste",
        corpo="Corpo de teste"
    )
    
    mock_server.sendmail.assert_called_once()

def test_enviar_email_com_anexos(email_master, mocker, tmp_path):
    mock_smtp = mocker.patch('smtplib.SMTP')
    
    # Criar arquivo temporário para teste
    arquivo_teste = tmp_path / "teste.txt"
    arquivo_teste.write_text("conteúdo de teste")
    
    email_master.enviar_email(
        destinatario="dest@teste.com",
        assunto="Teste",
        corpo="Corpo de teste",
        anexos=[str(arquivo_teste)]
    )

def test_enviar_email_multiplos_destinatarios(email_master, mocker):
    mock_smtp = mocker.patch('smtplib.SMTP')
    
    email_master.enviar_email(
        destinatario=["dest1@teste.com", "dest2@teste.com"],
        assunto="Teste",
        corpo="Corpo de teste",
        cc="cc@teste.com",
        cco=["cco1@teste.com", "cco2@teste.com"]
    )

def test_erro_envio_email(email_master, mocker):
    mock_smtp = mocker.patch('smtplib.SMTP')
    mock_server = mock_smtp.return_value
    mock_server.sendmail.side_effect = Exception("Erro simulado")
    
    with pytest.raises(ErroEnvioEmail):
        email_master.enviar_email(
            destinatario="dest@teste.com",
            assunto="Teste",
            corpo="Corpo de teste"
        )