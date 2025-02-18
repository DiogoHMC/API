import pytest
from fastapi import status


def test_create_obrigacao_acessoria(client, clean_db):

    empresa_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    empresa_id = empresa_response.json()["id"]

    response = client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["nome"] == "Obrigação Teste"


def test_read_obrigacoes(client, clean_db):

    empresa_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    empresa_id = empresa_response.json()["id"]

    client.post(
        "/obrigacoes/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id,
        },
    )

    response = client.get("/obrigacoes/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1