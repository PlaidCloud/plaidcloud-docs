---
title: Amazon Redshift
description: Configure uma conexão de banco de dados Amazon Redshift no PlaidCloud para consultar, importar e exportar dados com seu data warehouse Redshift.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/amazon-redshift.md
---

O **Amazon Redshift** é o data warehouse gerenciado em nuvem da AWS, projetado para cargas de trabalho analíticas sobre grandes conjuntos de dados. Use este conector para ler e gravar tabelas do Redshift a partir de fluxos de trabalho do PlaidCloud. O conector usa o protocolo de rede do PostgreSQL; a autenticação usa credenciais de banco de dados padrão ou credenciais temporárias baseadas em IAM.

## Documentação do fornecedor
Consulte a [documentação do Amazon Redshift](https://docs.aws.amazon.com/redshift/) para obter guias e material de referência.

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias opcional ou observações sobre a conexão. |
| Is active | Alternância | Indica se a conexão está ativada. Desative para pausar sem excluir. |
| Db read only | Alternância | Restringe a conexão a operações somente leitura. |
| Access type | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Conexão

| Campo | Tipo | Descrição |
|---|---|---|
| Db host | Texto | Nome do host ou endereço IP do servidor de banco de dados. |
| Db port | Número | Número da porta da conexão com o banco de dados. |
| Db catalog | Texto | Banco de dados, catálogo ou esquema ao qual se conectar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Db user | Texto | Nome de usuário para autenticação no banco de dados. |
| Use sso | Alternância | Autentica por logon único em vez de usuário e senha. |
| Db password | Senha | Senha para autenticação no banco de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Use ssl | Alternância | Criptografa a conexão com SSL/TLS. |
| Ssl mode | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Ssl auth client key | Texto (várias linhas) | Chave privada do cliente (PEM) para autenticação TLS mútua. |
| Ssl auth root cert | Texto (várias linhas) | Certificado de CA raiz (PEM) para verificar o certificado do servidor. |
| Ssl auth cert revoke | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente usar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Use ssh | Alternância | Encapsula a conexão em um túnel por um bastion SSH. |
| Ssh host | Texto | Nome do host do bastion SSH. |
| Ssh port | Número | Porta do bastion SSH (padrão 22). |
| Ssh user | Texto | Nome de usuário do bastion SSH. |
| Ssh password | Senha | Senha do bastion SSH (se a autenticação por senha for usada). |
| Use ssh cert | Alternância | Autentica no bastion SSH com uma chave privada em vez de senha. |
| Ssh private key | Texto (várias linhas) | Chave privada SSH (PEM) para autenticação no bastion. |
| Ssh host key | Texto (várias linhas) | Chave de host SSH esperada para verificar a impressão digital do bastion. |
