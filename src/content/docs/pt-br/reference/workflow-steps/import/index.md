---
title: Etapas de importação
description: Etapas de fluxo de trabalho que trazem dados de origens externas para tabelas de projeto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Etapas de fluxo de trabalho que trazem dados de origens externas para tabelas de projeto.

Uma importação de arquivo verifica a consulta que carrega sua tabela de destino antes de ser executada. Uma consulta que contenha qualquer coisa além de uma instrução SQL simples sobre colunas tipadas é recusada antes de a tabela de destino ser criada, substituída ou carregada, de modo que a tabela permanece exatamente como estava.

Um arquivo de origem ausente não é um erro. A importação emite um aviso com o caminho e deixa a tabela de destino vazia, com suas colunas declaradas, de modo que as etapas seguintes leiam zero linhas. Isso se aplica às importações de CSV, Excel, JSON, largura fixa, YXDB, dBASE, ORC, Avro, Parquet, XML e extração Db2. Uma importação de XML com tags cria uma tabela vazia apenas para cada tag que declara campos. As importações de arquivo compactado e de Access também emitem aviso, mas não declaram colunas, portanto não criam nenhuma tabela. Uma importação de arquivo compactado que encontra seus arquivos por pesquisa de documentos não emite aviso de arquivo ausente.

O mesmo vale antes de uma etapa ser executada. **Preencher** no mapeamento de uma importação de arquivo, e a leitura das colunas de um arquivo pela API REST ou por um assistente de IA, respondem *Nada para preencher* (uma lista de colunas vazia pela API) com um aviso que informa o caminho quando o arquivo está ausente ou vazio, em vez de um erro. Importar um arquivo ausente para uma nova tabela ou etapa a partir de Documentos não cria nada, marca o arquivo como **ignorado** e exibe um aviso que informa o caminho.

## Etapas

- [Importar Access](/pt-br/reference/workflow-steps/import/import-access/)
- [Importar Alteryx YXDB](/pt-br/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Importar arquivo compactado](/pt-br/reference/workflow-steps/import/import-archive/)
- [Importar Avro](/pt-br/reference/workflow-steps/import/import-avro/)
- [Importar CSV](/pt-br/reference/workflow-steps/import/import-csv/)
- [Importar Delta Lake](/pt-br/reference/workflow-steps/import/import-delta/)
- [Importar extração DB2](/pt-br/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE](/pt-br/reference/workflow-steps/import/import-dbf/)
- [Importar Excel](/pt-br/reference/workflow-steps/import/import-excel/)
- [Import Delimited](/pt-br/reference/workflow-steps/import/import-delimited/)
- [Importar tabelas de banco de dados externo](/pt-br/reference/workflow-steps/import/import-external-database-tables/)
- [Importar largura fixa](/pt-br/reference/workflow-steps/import/import-fixed-width/)
- [Import Google BigQuery](/pt-br/reference/workflow-steps/import/import-google-bigquery/)
- [Importar Planilha Google](/pt-br/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF](/pt-br/reference/workflow-steps/import/import-hdf/)
- [Importar JSON](/pt-br/reference/workflow-steps/import/import-json/)
- [Importar Kafka](/pt-br/reference/workflow-steps/import/import-kafka/)
- [Importar Monday](/pt-br/reference/workflow-steps/import/import-monday/)
- [Importar MongoDB](/pt-br/reference/workflow-steps/import/import-mongodb/)
- [Importar ORC](/pt-br/reference/workflow-steps/import/import-orc/)
- [Importar Parquet](/pt-br/reference/workflow-steps/import/import-parquet/)
- [Import Project Table](/pt-br/reference/workflow-steps/import/import-project-table/)
- [Import Quandl](/pt-br/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source](/pt-br/reference/workflow-steps/import/import-singer/)
- [Import SPSS](/pt-br/reference/workflow-steps/import/import-spss/)
- [Importar SQL](/pt-br/reference/workflow-steps/import/import-sql/)
- [Import Stata](/pt-br/reference/workflow-steps/import/import-stata/)
- [Importar XML](/pt-br/reference/workflow-steps/import/import-xml/)
- [Restaurar tabelas](/pt-br/reference/workflow-steps/import/restore-tables/)
