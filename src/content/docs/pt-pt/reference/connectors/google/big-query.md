---
title: Conector Google BigQuery
description: Configure uma ligação ao Google BigQuery no PlaidCloud para executar consultas analíticas e integrar dados de grande escala nos fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Documentação da ligação
[A documentação do Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. Os campos obrigatórios e opcionais dependem das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Comutador | Indica se a ligação está ativada. Desative para a suspender sem a eliminar. |
| Só de leitura na BD | Comutador | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Ligação BigQuery

| Campo | Obrigatório | Descrição |
|---|---|---|
| Projeto | Sim | O projeto Google Cloud que contém o conjunto de dados. |
| Conjunto de dados | Sim | O conjunto de dados BigQuery a ler e a escrever. |
| Tabela | Sim | Uma tabela do conjunto de dados. |

### Credenciais de autenticação

| Campo | Obrigatório | Descrição |
|---|---|---|
| Chave da conta de serviço (JSON) | Sim | Cole o ficheiro de chave JSON completo de uma conta de serviço Google que possa ler o conjunto de dados. Conceda-lhe acesso de escrita apenas se pretender escrever no conjunto de dados. A chave é só de escrita: deixe-a em branco ao editar para manter a chave guardada. |

A ligação autentica-se apenas com a chave da conta de serviço que indicar. O passo [Importar SQL](/pt-pt/reference/workflow-steps/import/import-sql/) lê o BigQuery através desta ligação, e o passo [Export External Database Tables](/pt-pt/reference/workflow-steps/export/export-external-tables/) escreve nele com uma tarefa de carregamento do BigQuery.
