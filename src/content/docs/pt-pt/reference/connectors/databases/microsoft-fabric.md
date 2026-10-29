---
title: Microsoft Fabric
description: Configure uma ligação ao Microsoft Fabric no PlaidCloud para integrar capacidades de análise, armazenamento de dados e lakehouse.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/microsoft-fabric.md
---

O **Microsoft Fabric** combina o Power BI, o Synapse e o Data Factory numa plataforma de análise unificada. Utilize este conector para aceder a armazéns e lakehouses do Fabric como origens relacionais a partir de fluxos de trabalho do PlaidCloud. A autenticação é feita através de um ponto final compatível com SQL Server e das credenciais do seu inquilino Microsoft.

## Documentação do fabricante
[A documentação do Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/).

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. A obrigatoriedade de cada campo depende das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Interruptor | Indica se a ligação está ativada. Desative-a para a suspender sem a eliminar. |
| Db só de leitura | Interruptor | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Ligação

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião da Db | Texto | Nome do anfitrião ou endereço IP do servidor de base de dados. |
| Porta da Db | Número | Número da porta para a ligação à base de dados. |
| Catálogo da Db | Texto | Base de dados, catálogo ou esquema a que ligar. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Utilizador da Db | Texto | Nome de utilizador para a autenticação na base de dados. |
| Palavra-passe da Db | Palavra-passe | Palavra-passe para a autenticação na base de dados. |

### SSL / TLS

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSL | Interruptor | Encripta a ligação com SSL/TLS. |
| Modo SSL | Seleção | Modo de verificação SSL (por exemplo, disable, require, verify-ca, verify-full). |
| Certificado de cliente SSL | Texto (várias linhas) | Certificado de cliente (PEM) para autenticação TLS mútua. |
| Chave de cliente SSL | Texto (várias linhas) | Chave privada do cliente (PEM) para autenticação TLS mútua. |
| Certificado raiz SSL | Texto (várias linhas) | Certificado CA raiz (PEM) para verificar o certificado do servidor. |
| Revogação de certificados SSL | Texto (várias linhas) | Lista de revogação de certificados, se o seu ambiente utilizar uma. |

### Túnel SSH

| Campo | Tipo | Descrição |
|---|---|---|
| Usar SSH | Interruptor | Estabelece o túnel da ligação através de um bastião SSH. |
| Anfitrião SSH | Texto | Nome do anfitrião do bastião SSH. |
| Porta SSH | Número | Porta do bastião SSH (predefinição: 22). |
| Utilizador SSH | Texto | Nome de utilizador do bastião SSH. |
| Palavra-passe SSH | Palavra-passe | Palavra-passe do bastião SSH (se for utilizada autenticação por palavra-passe). |
| Usar certificado SSH | Interruptor | Autentica no bastião SSH com uma chave privada em vez de palavra-passe. |
| Chave privada SSH | Texto (várias linhas) | Chave privada SSH (PEM) para a autenticação no bastião. |
| Chave de anfitrião SSH | Texto (várias linhas) | Chave de anfitrião SSH esperada para verificar a impressão digital do bastião. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| Confiar nos certificados | Interruptor | — |
| Tipo de driver | Seleção | — |
| Autenticação de utilizador | Interruptor | — |
