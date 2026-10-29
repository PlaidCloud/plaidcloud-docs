---
title: Export to ORC (etapa)
description: Exporte tabelas de projeto do PlaidCloud para uma conta de documentos como arquivos Apache ORC, em formato colunar e com o codec de compactação que você escolher.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Descrição

Grava tabelas de projeto em uma conta de documentos como arquivos [Apache ORC](https://orc.apache.org/), um arquivo para cada tabela. ORC é um formato colunar lido pelo Hive, pelo Spark e pela maioria das plataformas de dados em nuvem, com o esquema contido no próprio arquivo. Use-a em conjunto com [Importar ORC](/pt-br/reference/workflow-steps/import/import-orc/).

O formulário da etapa tem uma página **Parâmetros do arquivo** para o arquivo de destino, o prefixo, a compactação e o que acontece quando o arquivo existe, e uma página **Parâmetros do registro** que lista as tabelas a exportar, cada uma com sua própria seleção de dados da tabela e seus filtros de dados. [Fluxos de trabalho do KNIME migrados](/pt-br/guides/workflows/migrate-knime-workflows/) usam esta etapa para gravadores de ORC.

## Configuração

* **Arquivo de destino** (`output_file`) — a conta de documentos e a pasta em que os arquivos são gravados.
* **Prefixo do arquivo de destino** (`file_name`) — o prefixo do arquivo. Cada tabela é gravada como `<prefix><table name>.orc`.
* **Opção de compactação** (`compression`) — o codec ORC usado dentro do arquivo: **Snappy**, **zlib**, **gzip** (gravado como `zlib`), **Zstandard** ou **LZ4**. **Nenhum** grava o arquivo sem compactação.
* **Parâmetros do registro** (`frames`) — as tabelas a exportar. Cada frame tem suas próprias configurações de tabela; uma configuração em nível de tabela colocada no topo da etapa, em vez de dentro de um frame, não é lida.
  * `id` — o rótulo da tabela nos avisos.
  * `source` — a tabela de projeto a exportar. Cada arquivo recebe o nome a partir dela.
  * `source_columns` e `target_columns` — as colunas lidas e as colunas gravadas, com eventual renomeação, tipo e agregação por coluna.
  * `source_where` — um filtro sobre as linhas de origem.
  * `aggregate` e `aggregation_type` — resumem as linhas; `aggregation_type` é o resumo aplicado às colunas que não definem o seu próprio.
  * `having` — um filtro sobre as linhas resumidas.
  * `distinct` — grava somente linhas distintas.
  * `use_target_slicer`, `limit_target_start` e `limit_target_end` — gravam somente as linhas da posição inicial até a posição final do resultado.
  * `sort_columns` — definido com um assistente de IA ou pela API REST para ordenar as linhas gravadas por estas colunas de origem, começando pela primeira chave, cada uma como `{source, ascending, nulls}`. Uma coluna-chave não precisa ser gravada. `nulls` assume o padrão `first` em ordem crescente e `last` em ordem decrescente. Não é usado com `aggregate` ou `distinct`.
* **Um arquivo que já existe** (`if_exists`), em **Se o arquivo existir** — **Sobrescrevê-lo** (`overwrite`, padrão) substitui um arquivo que já existe; **Fazer a etapa falhar sem gravar nada** (`fail`) interrompe a etapa, sem gravar nada, quando um arquivo que ela gravaria já existe.

## Relacionados

- [Etapas de exportação](/pt-br/reference/workflow-steps/export/)
- [Importar ORC](/pt-br/reference/workflow-steps/import/import-orc/)
- [Export to Parquet (etapa)](/pt-br/reference/workflow-steps/export/export-to-parquet/)
