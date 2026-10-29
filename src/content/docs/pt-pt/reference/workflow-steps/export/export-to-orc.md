---
title: Export to ORC
description: Exporte tabelas de projeto do PlaidCloud para uma conta de documentos como ficheiros Apache ORC, em formato colunar e com o codec de compressão que escolher.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Descrição

Escreve tabelas de projeto numa conta de documentos como ficheiros [Apache ORC](https://orc.apache.org/), um ficheiro por tabela. O ORC é um formato colunar lido pelo Hive, pelo Spark e pela maioria das plataformas de dados na nuvem, com o esquema incluído no ficheiro. Combine-o com [Import ORC](/pt-pt/reference/workflow-steps/import/import-orc/).

O formulário do passo tem uma página **Parâmetros do ficheiro** para o ficheiro de destino, o prefixo, a compressão e o que acontece quando o ficheiro existe, e uma página **Parâmetros do registo** que lista as tabelas a exportar, cada uma com a sua própria seleção de dados da tabela e filtros de dados. Os [fluxos de trabalho KNIME migrados](/pt-pt/guides/workflows/migrate-knime-workflows/) utilizam este passo para os escritores de ORC.

## Configuração

* **Ficheiro de destino** (`output_file`) — a conta de documentos e a pasta onde os ficheiros são escritos.
* **Prefixo do ficheiro de destino** (`file_name`) — o prefixo do ficheiro. Cada tabela é escrita como `<prefix><table name>.orc`.
* **Opção de compressão** (`compression`) — o codec ORC utilizado dentro do ficheiro: **Snappy**, **zlib**, **gzip** (escrito como `zlib`), **Zstandard** ou **LZ4**. **Nenhum** escreve o ficheiro sem compressão.
* **Parâmetros do registo** (`frames`) — as tabelas a exportar. Cada frame tem as suas próprias definições de tabela; uma definição ao nível da tabela colocada no topo do passo em vez de dentro de um frame não é lida.
  * `id` — a etiqueta da tabela nos avisos.
  * `source` — a tabela de projeto a exportar. Cada ficheiro recebe o nome a partir dela.
  * `source_columns` e `target_columns` — as colunas lidas e as colunas escritas, com eventual mudança de nome, tipo e agregação por coluna.
  * `source_where` — um filtro sobre as linhas de origem.
  * `aggregate` e `aggregation_type` — resumem as linhas; `aggregation_type` é o resumo aplicado às colunas que não definem o seu próprio.
  * `having` — um filtro sobre as linhas resumidas.
  * `distinct` — escreve apenas linhas distintas.
  * `use_target_slicer`, `limit_target_start` e `limit_target_end` — escrevem apenas as linhas desde a posição inicial até à posição final do resultado.
  * `sort_columns` — defina-o com um assistente de IA ou com a API REST para ordenar as linhas escritas por estas colunas de origem, começando pela primeira chave, cada uma `{source, ascending, nulls}`. Não é necessário que uma coluna-chave seja escrita. `nulls` assume por predefinição `first` em ordem ascendente e `last` em ordem descendente. Não é utilizado com `aggregate` nem com `distinct`.
* **Um ficheiro que já existe** (`if_exists`), em **Se o ficheiro existir** — **Sobrescrevê-lo** (`overwrite`, predefinição) substitui um ficheiro que já exista; **Fazer a etapa falhar sem escrever nada** (`fail`) interrompe o passo, sem escrever nada, quando já existe um ficheiro que seria escrito.

## Relacionados

- [Passos de exportação](/pt-pt/reference/workflow-steps/export/)
- [Import ORC](/pt-pt/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/pt-pt/reference/workflow-steps/export/export-to-parquet/)
