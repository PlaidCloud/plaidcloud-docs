---
title: MongoDB
description: Configure uma conexão do MongoDB no PlaidCloud para ler coleções em tabelas e gravar tabelas de volta como documentos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/mongodb.md
---

**MongoDB** é um banco de dados de documentos. Use esta conexão com [Importar MongoDB](/pt-br/reference/workflow-steps/import/import-mongodb/) para ler uma coleção, ou o resultado de um pipeline de agregação, em uma tabela, e com [Exportar MongoDB](/pt-br/reference/workflow-steps/export/export-mongodb/) para gravar uma tabela de volta como documentos. Para criar uma, escolha **MongoDB** como o tipo de conexão.

## Documentação do Fornecedor
[A documentação do MongoDB](https://www.mongodb.com/docs/).

## Configuração

### Conexão do MongoDB

| Campo | Obrigatório | Descrição |
|---|---|---|
| Host | Sim | O nome do host do servidor. |
| Usar um endereço SRV (mongodb+srv://, sem porta) | Não | Conecta por uma lista de sementes DNS, como faz o MongoDB Atlas. A porta não é usada. |
| Porta | Não | A porta do servidor. O padrão é `27017`. |
| Banco de dados padrão | Não | O banco de dados que uma etapa usa quando não informa nenhum. |

### Credenciais de autenticação

| Campo | Descrição |
|---|---|
| Usuário | O usuário com o qual se conectar. |
| Senha | A senha do usuário (somente gravação). |

### Opções

| Campo | Descrição |
|---|---|
| Opções de conexão | Opções de URI do MongoDB unidas por `&`, como `authSource=admin&tls=true`. Somente as opções que o PlaidCloud permite são aceitas. Deixe em branco ao editar para manter as opções salvas. |

### TLS

| Campo | Descrição |
|---|---|
| Certificado de CA (PEM) | A autoridade certificadora que assinou os certificados dos servidores, quando não for uma autoridade pública. Deixe em branco ao editar para manter o certificado salvo. |
