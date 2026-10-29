---
title: Formato de tabela aberta Apache Hive
description: Configure uma ligação a um catálogo Apache Hive no PlaidCloud para consultas em formato de tabela aberta através do serviço PlaidCloud Lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Documentação do catálogo
[Documentação do Apache Hive](https://hive.apache.org/docs/latest/).

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. Os campos obrigatórios e opcionais dependem das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Comutador | Indica se a ligação está ativada. Desative para a suspender sem a eliminar. |
| Só de leitura na BD | Comutador | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Ligação

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião da BD | Texto | Nome do anfitrião ou endereço IP do servidor de base de dados. |
| Porta da BD | Número | Número da porta da ligação à base de dados. |
| Catálogo da BD | Texto | Base de dados, catálogo ou esquema ao qual se ligar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Utilizador da BD | Texto | Nome de utilizador para a autenticação na base de dados. |
| Usar SSO | Comutador | Autentica através de início de sessão único em vez de nome de utilizador/palavra-passe. |
| Palavra-passe da BD | Palavra-passe | Palavra-passe para a autenticação na base de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Comutador | Cifra a ligação com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Chave de cliente SSL | Texto (várias linhas) | Chave privada de cliente (PEM) para autenticação TLS mútua. |
| Certificado raiz SSL | Texto (várias linhas) | Certificado CA raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificados SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente utilizar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Comutador | Estabelece um túnel da ligação através de um bastion SSH. |
| Anfitrião SSH | Texto | Nome do anfitrião do bastion SSH. |
| Porta SSH | Número | Porta do bastion SSH (predefinição: 22). |
| Utilizador SSH | Texto | Nome de utilizador do bastion SSH. |
| Palavra-passe SSH | Palavra-passe | Palavra-passe do bastion SSH (se for utilizada autenticação por palavra-passe). |
| Usar certificado SSH | Comutador | Autentica no bastion SSH com uma chave privada em vez de uma palavra-passe. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para autenticação no bastion. |
| Chave de anfitrião SSH | Texto (várias linhas) | Chave de anfitrião SSH esperada para verificação da impressão digital do bastion. |
