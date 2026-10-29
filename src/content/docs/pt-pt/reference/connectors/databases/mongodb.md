---
title: MongoDB
description: Configure uma ligação ao MongoDB no PlaidCloud para ler coleções para tabelas e escrever tabelas de volta como documentos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

O **MongoDB** é uma base de dados de documentos. Utilize esta ligação com [Importar MongoDB](/pt-pt/reference/workflow-steps/import/import-mongodb/) para ler uma coleção, ou o resultado de um pipeline de agregação, para uma tabela, e com [Exportar MongoDB](/pt-pt/reference/workflow-steps/export/export-mongodb/) para escrever uma tabela de volta como documentos. Para criar uma, escolha **MongoDB** como tipo de ligação.

## Documentação do fabricante
[A documentação do MongoDB](https://www.mongodb.com/docs/).

## Configuração

### Ligação MongoDB

| Campo | Obrigatório | Descrição |
|---|---|---|
| Anfitrião | Sim | O nome do anfitrião do servidor. |
| Usar um endereço SRV (mongodb+srv://, sem porta) | Não | Liga através de uma lista de sementes DNS, como faz o MongoDB Atlas. A porta não é utilizada. |
| Porta | Não | A porta do servidor. A predefinição é `27017`. |
| Base de dados predefinida | Não | A base de dados que um passo utiliza quando não indica nenhuma. |

### Credenciais de autenticação

| Campo | Descrição |
|---|---|
| Utilizador | O utilizador com o qual estabelecer a ligação. |
| Palavra-passe | A palavra-passe do utilizador (só de escrita). |

### Opções

| Campo | Descrição |
|---|---|
| Opções de ligação | Opções de URI do MongoDB unidas por `&`, como `authSource=admin&tls=true`. Só são aceites as opções permitidas pelo PlaidCloud. Deixe em branco ao editar para manter as opções guardadas. |

### TLS

| Campo | Descrição |
|---|---|
| Certificado CA (PEM) | A autoridade de certificação que assinou os certificados dos servidores, quando não é uma autoridade pública. Deixe em branco ao editar para manter o certificado guardado. |
