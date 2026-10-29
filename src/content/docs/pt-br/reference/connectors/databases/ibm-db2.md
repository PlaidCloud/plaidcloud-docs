---
title: IBM DB2
description: Configure uma conexão de banco de dados IBM DB2 no PlaidCloud para consultar, importar e exportar dados das suas instâncias do DB2.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/ibm-db2.md
---

**IBM DB2** é o banco de dados corporativo da IBM, comum em ambientes mainframe e de médio porte. Use este conector para ler e gravar tabelas do DB2 a partir de fluxos de trabalho do PlaidCloud. É necessário ter acesso de rede ao listener do DB2; em implantações em mainframe, geralmente é necessário um túnel SSH ou VPN.

## Documentação do Fornecedor
[A documentação do IBM DB2](https://www.ibm.com/support/pages/db2-database-product-documentation).

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você habilitar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativo | Alternância | Indica se a conexão está habilitada. Desative para pausar sem excluir. |
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
| Usar SSO | Alternância | Autentica por single sign-on em vez de usuário e senha. |
| Senha do banco de dados | Senha | Senha para autenticação no banco de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Alternância | Criptografa a conexão com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação de SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Chave de cliente SSL | Texto (várias linhas) | Chave privada do cliente (PEM) para autenticação TLS mútua. |
| Certificado raiz SSL | Texto (várias linhas) | Certificado de CA raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificado SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente usar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Alternância | Encaminha a conexão por um bastion SSH. |
| Host SSH | Texto | Nome do host do bastion SSH. |
| Porta SSH | Número | Porta do bastion SSH (padrão 22). |
| Usuário SSH | Texto | Nome de usuário do bastion SSH. |
| Senha SSH | Senha | Senha do bastion SSH (se a autenticação por senha for usada). |
| Usar certificado SSH | Alternância | Autentica no bastion SSH com uma chave privada em vez de senha. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para autenticação no bastion. |
| Chave de host SSH | Texto (várias linhas) | Chave de host SSH esperada para verificar a impressão digital do bastion. |
