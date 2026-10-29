---
title: Conector Google BigQuery
description: Configure uma conexão com o Google BigQuery no PlaidCloud para executar consultas analíticas e integrar dados em grande escala aos fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## Documentação da conexão
[A documentação do Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está ativada. Desative para pausá-la sem excluí-la. |
| Banco somente leitura | Alternância | Restringe a conexão a operações somente leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Conexão do BigQuery

| Campo | Obrigatório | Descrição |
|---|---|---|
| Projeto | Sim | O projeto do Google Cloud que contém o conjunto de dados. |
| Conjunto de dados | Sim | O conjunto de dados do BigQuery a ser lido e gravado. |
| Tabela | Sim | Uma tabela do conjunto de dados. |

### Credenciais de autenticação

| Campo | Obrigatório | Descrição |
|---|---|---|
| Chave da conta de serviço (JSON) | Sim | Cole o arquivo de chave JSON completo de uma conta de serviço do Google que possa ler o conjunto de dados. Conceda acesso de gravação somente se quiser gravar no conjunto de dados. A chave é somente de gravação: deixe o campo em branco ao editar para manter a chave salva. |

A conexão se autentica somente com a chave da conta de serviço que você fornecer. A etapa [Importar SQL](/pt-br/reference/workflow-steps/import/import-sql/) lê o BigQuery por essa conexão, e a etapa [Export External Database Tables](/pt-br/reference/workflow-steps/export/export-external-tables/) grava nela com um job de carga do BigQuery.
