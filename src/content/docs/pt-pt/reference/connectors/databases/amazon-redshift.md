---
title: Amazon Redshift
description: Configure uma ligação de base de dados Amazon Redshift no PlaidCloud para consultar, importar e exportar dados com o seu armazém de dados Redshift.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

O **Amazon Redshift** é o armazém de dados gerido na nuvem da AWS, concebido para cargas de trabalho analíticas sobre grandes conjuntos de dados. Utilize este conector para ler e escrever tabelas do Redshift a partir de fluxos de trabalho do PlaidCloud. O conector utiliza o protocolo de comunicação do PostgreSQL; a autenticação utiliza credenciais de base de dados padrão ou credenciais temporárias baseadas em IAM.

## Documentação do fornecedor
Consulte a [documentação do Amazon Redshift](https://docs.aws.amazon.com/redshift/) para guias e material de referência.

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. Os que são obrigatórios ou opcionais dependem das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Name | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Is active | Interruptor | Indica se a ligação está ativada. Desative para a suspender sem a eliminar. |
| Db read only | Interruptor | Restringe a ligação a operações só de leitura. |
| Access type | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Ligação

| Campo | Tipo | Descrição |
|---|---|---|
| Db host | Texto | Nome de anfitrião ou endereço IP do servidor de base de dados. |
| Db port | Número | Número da porta da ligação à base de dados. |
| Db catalog | Texto | Base de dados, catálogo ou esquema ao qual ligar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Db user | Texto | Nome de utilizador para a autenticação na base de dados. |
| Use sso | Interruptor | Autentica através de início de sessão único em vez de nome de utilizador/palavra-passe. |
| Db password | Palavra-passe | Palavra-passe para a autenticação na base de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Use ssl | Interruptor | Cifra a ligação com SSL/TLS. |
| Ssl mode | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Ssl auth client key | Texto (várias linhas) | Chave privada de cliente (PEM) para autenticação TLS mútua. |
| Ssl auth root cert | Texto (várias linhas) | Certificado de AC de raiz (PEM) para verificar o certificado do servidor. |
| Ssl auth cert revoke | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente utilizar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Use ssh | Interruptor | Encaminha a ligação através de um bastião SSH. |
| Ssh host | Texto | Nome de anfitrião do bastião SSH. |
| Ssh port | Número | Porta do bastião SSH (predefinição: 22). |
| Ssh user | Texto | Nome de utilizador do bastião SSH. |
| Ssh password | Palavra-passe | Palavra-passe do bastião SSH (se for utilizada autenticação por palavra-passe). |
| Use ssh cert | Interruptor | Autentica no bastião SSH com uma chave privada em vez de palavra-passe. |
| Ssh private key | Texto (várias linhas) | Chave privada SSH (PEM) para a autenticação no bastião. |
| Ssh host key | Texto (várias linhas) | Chave de anfitrião SSH esperada para verificar a impressão digital do bastião. |
