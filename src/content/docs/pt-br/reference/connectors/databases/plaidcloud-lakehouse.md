---
title: PlaidCloud Lakehouse
description: Configure a conexão de banco de dados do PlaidCloud Lakehouse para consultas e análises de alto desempenho nos dados do seu lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/plaidcloud-lakehouse.md
---

O **PlaidCloud Lakehouse** é o armazenamento de dados analítico integrado presente em todo espaço de trabalho do PlaidCloud. Este conector é usado principalmente para ler o lakehouse de um espaço de trabalho a partir de outro, ou para compartilhar dados entre tenants em implantações multi-tenant. Dentro de um único espaço de trabalho, as tabelas do projeto são acessíveis diretamente, sem precisar deste conector.

## Documentação do Fornecedor
Há muito pouca configuração necessária para usar o PlaidCloud Lakehouse integrado.  A [documentação do serviço](https://docs.plaidcloud.com/docs/plaidcloud/analyze/dw/getting-started/).

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

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| Servidor | Texto | — |
| Lakehouse | Número | — |
