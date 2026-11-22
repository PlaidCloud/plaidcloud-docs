---
title: Etapas de exportação
description: Etapas de fluxo de trabalho que gravam tabelas de projeto em destinos externos — formatos de arquivo, contas de documentos e bancos de dados externos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

Etapas de fluxo de trabalho que gravam tabelas de projeto em destinos externos — formatos de arquivo, contas de documentos e bancos de dados externos.

## Etapas

- [Arquivar tabelas](/pt-br/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables (etapa)](/pt-br/reference/workflow-steps/export/export-external-tables/)
- [Exportar Kafka](/pt-br/reference/workflow-steps/export/export-kafka/)
- [Exportar MongoDB](/pt-br/reference/workflow-steps/export/export-mongodb/)
- [Exportar arquivo do projeto](/pt-br/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table (etapa)](/pt-br/reference/workflow-steps/export/export-project-table/)
- [Export Quandl (etapa)](/pt-br/reference/workflow-steps/export/export-quandl/)
- [Exportar SQL](/pt-br/reference/workflow-steps/export/export-sql/)
- [Export Templated (etapa)](/pt-br/reference/workflow-steps/export/export-templated/)
- [Export to Avro (etapa)](/pt-br/reference/workflow-steps/export/export-to-avro/)
- [Export to CSV (etapa)](/pt-br/reference/workflow-steps/export/export-to-csv/)
- [Export to Excel (etapa)](/pt-br/reference/workflow-steps/export/export-to-excel/)
- [Export to Excel Sheets (etapa)](/pt-br/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export to Google Spreadsheet (etapa)](/pt-br/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export to HDF (etapa)](/pt-br/reference/workflow-steps/export/export-to-hdf/)
- [Export to JSON (etapa)](/pt-br/reference/workflow-steps/export/export-to-json/)
- [Export to ORC (etapa)](/pt-br/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet (etapa)](/pt-br/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF (etapa)](/pt-br/reference/workflow-steps/export/export-to-pdf/)
- [Export to Table Archive (etapa)](/pt-br/reference/workflow-steps/export/export-to-table-archive/)
- [Export to XML (etapa)](/pt-br/reference/workflow-steps/export/export-to-xml/)
- [Lançar documentos](/pt-br/reference/workflow-steps/export/post-documents/) — lance uma tabela de documentos em qualquer sistema ERP que você tenha configurado
- [Exportação de arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau (etapa)](/pt-br/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export (etapa)](/pt-br/reference/workflow-steps/export/export-hyper/)

## Colunas gravadas

A maioria das etapas de exportação grava todas as colunas da tabela de origem, como a tabela está quando a etapa é executada e na ordem das colunas da tabela, quando o Data Mapper não lista colunas de destino, ou seja, quando a tabela à direita na guia **Colunas** está vazia. Uma etapa deixada com a configuração pela metade, portanto, exporta a tabela inteira para o destino em vez de falhar, então verifique o Data Mapper antes de executar uma exportação para um destino externo.

Se nenhuma coluna estiver mapeada e a tabela de origem não tiver nenhuma, uma exportação de CSV, JSON, SQL, Excel, PDF, Google Spreadsheet ou Kafka não grava nada e termina com um aviso. Em uma exportação de várias tabelas, como XML, Parquet, ORC, Avro ou Excel Sheets, essa tabela é ignorada com um aviso que a cita. Export MongoDB, Export External Database Tables, Tableau Hyper Export, Spatial File Export e Run SAP PCM Hyper Loader fazem o mesmo: são concluídos com sucesso e registram um aviso que nomeia a origem ou o destino, e uma tabela externa mantém as linhas anteriores.
