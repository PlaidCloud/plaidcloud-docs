---
title: Formato de tabela aberta Apache Hive
description: Configure uma conexão com um catálogo Apache Hive no PlaidCloud para consultas em formato de tabela aberta por meio do serviço PlaidCloud Lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/open-tables/hive.md
---

## Documentação do catálogo
[Documentação do Apache Hive](https://hive.apache.org/docs/latest/).

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está ativada. Desative para pausá-la sem excluí-la. |
| Banco somente leitura | Alternância | Restringe a conexão a operações somente leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Conexão

| Campo | Tipo | Descrição |
|---|---|---|
| Host do banco | Texto | Nome do host ou endereço IP do servidor de banco de dados. |
| Porta do banco | Número | Número da porta da conexão com o banco de dados. |
| Catálogo do banco | Texto | Banco de dados, catálogo ou esquema ao qual se conectar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Usuário do banco | Texto | Nome de usuário para autenticação no banco de dados. |
| Usar SSO | Alternância | Autentica por logon único (SSO) em vez de nome de usuário e senha. |
| Senha do banco | Senha | Senha para autenticação no banco de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Alternância | Criptografa a conexão com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Chave de cliente SSL | Texto (várias linhas) | Chave privada do cliente (PEM) para autenticação TLS mútua. |
| Certificado raiz SSL | Texto (várias linhas) | Certificado de CA raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificado SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente usar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Alternância | Encaminha a conexão por um bastion SSH. |
| Host SSH | Texto | Nome do host do bastion SSH. |
| Porta SSH | Número | Porta do bastion SSH (padrão: 22). |
| Usuário SSH | Texto | Nome de usuário do bastion SSH. |
| Senha SSH | Senha | Senha do bastion SSH (se a autenticação por senha for usada). |
| Usar certificado SSH | Alternância | Autentica no bastion SSH com uma chave privada em vez de senha. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para autenticação no bastion. |
| Chave de host SSH | Texto (várias linhas) | Chave de host SSH esperada para verificar a impressão digital do bastion. |
