---
title: Passo Table Restore to Timestamp
description: Restaure uma tabela do PlaidCloud no local para o seu instantâneo mais recente tirado até um determinado momento, como passo de fluxo de trabalho.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Descrição

**Tabela: restaurar para um carimbo de data/hora** substitui uma tabela no local pelo seu instantâneo mais recente tirado até um determinado momento. Utilize-o para repor uma tabela no estado em que se encontrava no fim de um período, ou antes de um carregamento que correu mal. A restauração altera a própria tabela, pelo que todos os passos e painéis de controlo que a leem veem as linhas restauradas.

## Restaurar para um momento no tempo

| Definição | Obrigatório | O que faz |
| --- | --- | --- |
| Tabela | Sim | A tabela a restaurar. |
| Carimbo de data/hora | Sim | O momento, como hora ISO-8601, por exemplo `2026-09-30T23:59:59Z`, ou em segundos desde 1970. Uma hora sem fuso é UTC. Uma variável de fluxo de trabalho como `{restore_time}` também funciona. |
| Conta um instantâneo tirado exatamente no carimbo de data/hora | Não | Ativado por predefinição. Desative-o para restaurar apenas para um instantâneo tirado antes do carimbo de data/hora. |

Quando não foi tirado nenhum instantâneo até ao carimbo de data/hora, o passo termina com um aviso, deixa a tabela como está e o fluxo de trabalho continua. Uma tabela que não é encontrada também termina com um aviso. Num motor de armazenamento que mantém apenas instantâneos com nome, a tabela só pode ser restaurada para um instantâneo tirado exatamente no carimbo de data/hora; tire um instantâneo com nome no momento para o qual pretende voltar.

## Relacionado

- [Restaurar tabelas](/pt-pt/reference/workflow-steps/import/restore-tables/)
- [Passos de tabelas](/pt-pt/reference/workflow-steps/tables/)
