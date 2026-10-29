---
title: Amazon Athena
description: Configure uma conexão do Amazon Athena no PlaidCloud para executar consultas sem servidor em dados armazenados em buckets do Amazon S3.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-athena.md
---

O **Amazon Athena** é o mecanismo de consultas sem servidor da AWS sobre dados hospedados no S3, cobrado por consulta. Use este conector para executar consultas do Athena a partir de fluxos de trabalho do PlaidCloud — útil para combinar data lakes do S3 com tabelas de projeto do PlaidCloud. A autenticação usa chaves de acesso da AWS ou assunção de função do IAM.

## Documentação de origem
[Documentação do Amazon Athena](https://docs.aws.amazon.com/athena/).

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você habilitar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias opcional ou observações sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está habilitada. Desabilite para pausar sem excluir. |
| Banco de dados somente leitura | Alternância | Restringe a conexão a operações somente leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Conexão

| Campo | Tipo | Descrição |
|---|---|---|
| Host do banco de dados | Texto | Nome do host ou endereço IP do servidor de banco de dados. |
| Porta do banco de dados | Número | Número da porta da conexão com o banco de dados. |
| Catálogo do banco de dados | Texto | Banco de dados, catálogo ou esquema ao qual se conectar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Usuário do banco de dados | Texto | Nome de usuário para autenticação no banco de dados. |
| Usar SSO | Alternância | Autentica por logon único em vez de usuário e senha. |
| Senha do banco de dados | Senha | Senha para autenticação no banco de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Alternância | Criptografa a conexão com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente de autenticação SSL | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Chave de cliente de autenticação SSL | Texto (várias linhas) | Chave privada do cliente (PEM) para autenticação TLS mútua. |
| Certificado raiz de autenticação SSL | Texto (várias linhas) | Certificado de CA raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificado de autenticação SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente usar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Alternância | Encapsula a conexão em um túnel por um bastion SSH. |
| Host SSH | Texto | Nome do host do bastion SSH. |
| Porta SSH | Número | Porta do bastion SSH (padrão 22). |
| Usuário SSH | Texto | Nome de usuário do bastion SSH. |
| Senha SSH | Senha | Senha do bastion SSH (se a autenticação por senha for usada). |
| Usar certificado SSH | Alternância | Autentica no bastion SSH com uma chave privada em vez de senha. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para autenticação no bastion. |
| Chave de host SSH | Texto (várias linhas) | Chave de host SSH esperada para verificar a impressão digital do bastion. |
