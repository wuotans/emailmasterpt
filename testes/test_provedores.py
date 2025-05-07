import pytest
from emailmasterpt import ProvedorGmail, ProvedorOutlook, ProvedorSMTP

def test_provedor_gmail():
    provedor = ProvedorGmail("usuario@gmail.com", "senha")
    assert provedor.usuario == "usuario@gmail.com"
    assert provedor.senha == "senha"
    assert provedor.host == "smtp.gmail.com"
    assert provedor.porta == 587

def test_provedor_outlook():
    provedor = ProvedorOutlook("usuario@outlook.com", "senha")
    assert provedor.usuario == "usuario@outlook.com"
    assert provedor.senha == "senha"
    assert provedor.host == "smtp.office365.com"
    assert provedor.porta == 587

def test_provedor_smtp_personalizado():
    provedor = ProvedorSMTP("usuario@empresa.com", "senha", "smtp.empresa.com", 587)
    assert provedor.usuario == "usuario@empresa.com"
    assert provedor.senha == "senha"
    assert provedor.host == "smtp.empresa.com"
    assert provedor.porta == 587