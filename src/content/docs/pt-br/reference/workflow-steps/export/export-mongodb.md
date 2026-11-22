---
title: Exportar MongoDB
description: Grave uma tabela do PlaidCloud em uma coleção do MongoDB como documentos inseridos, substituídos, atualizados ou inseridos com upsert.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Descrição

Grava cada linha de uma tabela de projeto em uma coleção do MongoDB como um documento. A coleção é criada quando não existe. A etapa acessa o MongoDB por meio de uma [conexão do MongoDB](/pt-br/reference/connectors/databases/mongodb/).

## Origem e destino

| Configuração | Obrigatória | O que faz |
| --- | --- | --- |
| Tabela de origem | Sim | A tabela a gravar. |
| Conexão do MongoDB | Sim | A conexão por meio da qual gravar. |
| Banco de dados | Não | O banco de dados em que gravar. Deixe em branco para usar o **Banco de dados padrão** da conexão. |
| Coleção | Sim | A coleção em que gravar. |

## Opções de gravação

| Configuração | O que faz |
| --- | --- |
| Modo de gravação | **Inserir um documento por linha** (o padrão), **Substituir o documento correspondente**, **Atualizar os campos do documento correspondente**, **Substituir o documento correspondente ou inserir** ou **Atualizar os campos do documento correspondente ou inserir**. |
| Colunas de correspondência | As colunas, separadas por vírgula, que identificam um documento. Obrigatórias em todos os modos, exceto inserir. |
| Excluir todos os documentos da coleção antes de gravar | Esvazia a coleção primeiro, de modo que ela contenha apenas as linhas desta execução. |
| Parar na primeira gravação com falha | Para no primeiro documento que o MongoDB recusa. Desmarque para continuar com os demais. |
| Aguardar a gravação chegar ao journal | Aguarda até que o MongoDB tenha gravado cada lote em seu journal. |
| Write Concern | Em branco para o da conexão, um número de servidores ou `majority`. |
| Documentos por solicitação | Quantos documentos são enviados em cada solicitação. |

Inserir adiciona os documentos novamente a cada execução da etapa. Os modos que substituem ou atualizam deixam a coleção igual, não importa quantas vezes a etapa seja executada; use um deles quando um fluxo de trabalho puder ser executado duas vezes sobre as mesmas linhas.

## Quando a origem está ausente ou vazia

A etapa não falha quando não há nada para gravar. Ela é concluída com sucesso e registra um aviso que nomeia a coleção ou a tabela:

- **A tabela de origem não existe.** O aviso é `No table found for path "…", so nothing was written to collection …`, e a coleção permanece como estava, mesmo com **Excluir todos os documentos da coleção antes de gravar** ativado.
- **A tabela de origem não tem colunas.** Sem colunas de origem ou de destino mapeadas, a etapa grava todas as colunas da tabela, então isso se aplica a uma tabela que não tem nenhuma. O aviso é `Table … has no columns; nothing was written to collection …`.
- **A tabela de origem não tem linhas.** O aviso é `The table has no rows; nothing was written to …`. Com **Excluir todos os documentos da coleção antes de gravar** ativado, a coleção é esvaziada e o aviso informa isso: `… was emptied and nothing was written to it`.

## Relacionados

- [Importar MongoDB](/pt-br/reference/workflow-steps/import/import-mongodb/)
- [Conexão do MongoDB](/pt-br/reference/connectors/databases/mongodb/)
