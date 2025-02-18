import pytest
from fastapi import status

def test_create_empresa(client, clean_db):
    response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["nome"] == "Empresa Teste"


def test_read_empresas(client, clean_db):

    client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )

    response = client.get("/empresas/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_read_empresa(client, clean_db):
   
    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    empresa_id = create_response.json()["id"]

    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["nome"] == "Empresa Teste"


def test_update_empresa(client, clean_db):

    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    empresa_id = create_response.json()["id"]

    response = client.put(
        f"/empresas/{empresa_id}",
        json={
            "nome": "Empresa Atualizada",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["nome"] == "Empresa Atualizada"


def test_delete_empresa(client, clean_db):

    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12345678901234",
            "endereco": "Rua Teste",
            "email": "teste@teste.com",
            "telefone": "123456789",
        },
    )
    empresa_id = create_response.json()["id"]

    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND