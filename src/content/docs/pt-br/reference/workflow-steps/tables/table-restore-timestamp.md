---
title: Table Restore to Timestamp (etapa)
description: Restaure uma tabela do PlaidCloud no local para o instantâneo mais recente tirado até um determinado momento, como uma etapa de fluxo de trabalho.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Descrição

**Tabela: restaurar para um carimbo de data/hora** substitui uma tabela no local pelo instantâneo mais recente tirado até um determinado momento. Use-a para reverter uma tabela ao estado em que estava no fim de um período ou antes de uma carga que deu errado. A restauração altera a própria tabela, então toda etapa e todo painel que a lê vê as linhas restauradas.

## Restaurar para um ponto no tempo

| Configuração | Obrigatório | O que faz |
| --- | --- | --- |
| Tabela | Sim | A tabela a restaurar. |
| Carimbo de data/hora | Sim | O momento, como um horário ISO-8601, por exemplo `2026-09-30T23:59:59Z`, ou como segundos desde 1970. Um horário sem fuso é UTC. Uma variável de fluxo de trabalho como `{restore_time}` também funciona. |
| Um instantâneo tirado exatamente no carimbo de data/hora é considerado | Não | Ativado por padrão. Desmarque para restaurar somente para um instantâneo tirado antes do carimbo de data/hora. |

Quando nenhum instantâneo foi tirado até o carimbo de data/hora, a etapa termina com um aviso, deixa a tabela como está e o fluxo de trabalho continua. Uma tabela que não é encontrada também termina com um aviso. Em um mecanismo de armazenamento que mantém apenas instantâneos nomeados, a tabela só pode ser restaurada para um instantâneo tirado exatamente no carimbo de data/hora; tire um instantâneo nomeado no momento para o qual você vai querer voltar.

## Relacionados

- [Restaurar tabelas](/pt-br/reference/workflow-steps/import/restore-tables/)
- [Etapas de tabela](/pt-br/reference/workflow-steps/tables/)
