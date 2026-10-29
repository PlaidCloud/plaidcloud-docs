---
title: Amazon Athena
description: Configure uma ligação do Amazon Athena no PlaidCloud para executar consultas sem servidor sobre dados armazenados em contentores do Amazon S3.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-athena.md
---

**Amazon Athena** é o motor de consultas sem servidor da AWS sobre dados alojados no S3, faturado por consulta. Utilize este conector para executar consultas do Athena a partir de fluxos de trabalho do PlaidCloud — útil para combinar data lakes do S3 com tabelas de projetos do PlaidCloud. A autenticação utiliza chaves de acesso da AWS ou a assunção de funções IAM.

## Documentação de origem
[Documentação do Amazon Athena](https://docs.aws.amazon.com/athena/).

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. O facto de serem obrigatórios ou opcionais depende das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Ativa | Interruptor | Se a ligação está ativada. Desative para a pausar sem a eliminar. |
| BD só de leitura | Interruptor | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Ligação

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião da BD | Texto | Nome do anfitrião ou endereço IP do servidor da base de dados. |
| Porta da BD | Número | Número da porta da ligação à base de dados. |
| Catálogo da BD | Texto | Base de dados, catálogo ou esquema ao qual ligar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Utilizador da BD | Texto | Nome de utilizador para a autenticação na base de dados. |
| Usar SSO | Interruptor | Autentica através de início de sessão único em vez de nome de utilizador e palavra-passe. |
| Palavra-passe da BD | Palavra-passe | Palavra-passe para a autenticação na base de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Interruptor | Cifra a ligação com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (várias linhas) | Certificado de cliente (PEM) para a autenticação TLS mútua. |
| Chave de cliente SSL | Texto (várias linhas) | Chave privada de cliente (PEM) para a autenticação TLS mútua. |
| Certificado de raiz SSL | Texto (várias linhas) | Certificado da AC de raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificados SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente utilizar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Interruptor | Encaminha a ligação através de um bastião SSH. |
| Anfitrião SSH | Texto | Nome do anfitrião do bastião SSH. |
| Porta SSH | Número | Porta do bastião SSH (predefinição: 22). |
| Utilizador SSH | Texto | Nome de utilizador do bastião SSH. |
| Palavra-passe SSH | Palavra-passe | Palavra-passe do bastião SSH (se for utilizada autenticação por palavra-passe). |
| Usar certificado SSH | Interruptor | Autentica no bastião SSH com uma chave privada em vez de palavra-passe. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para a autenticação no bastião. |
| Chave de anfitrião SSH | Texto (várias linhas) | Chave de anfitrião SSH esperada, para a verificação da impressão digital do bastião. |
