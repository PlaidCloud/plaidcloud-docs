---
title: Apache Hive
description: Configure uma conexão de data lake do Apache Hive no PlaidCloud para consultar e integrar dados em grande escala armazenados em ecossistemas Hadoop.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/hive.md
---

O **Apache Hive** é a camada SQL sobre o armazenamento distribuído no estilo Hadoop, comum em implantações mais antigas de data lakes. Use este conector para ler e gravar tabelas do Hive. A autenticação varia conforme a implantação — os modos mais comuns são LDAP, Kerberos ou sem autenticação em redes internas; verifique a configuração do seu metastore do Hive.

## Documentação de origem
[Documentação do Apache Hive](https://hive.apache.org/docs/latest/).

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
