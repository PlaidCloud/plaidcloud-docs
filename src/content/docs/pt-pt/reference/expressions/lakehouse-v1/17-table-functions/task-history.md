---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY — apresenta o histórico de execução de tarefas de acordo com as variáveis indicadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Apresenta o histórico de execução de tarefas de acordo com as variáveis indicadas.

## Sintaxe SQL
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## Argumentos

Todos os argumentos são opcionais.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

Intervalo de tempo (no formato TIMESTAMP_LTZ), nos últimos 7 dias, em que a execução da tarefa foi agendada. Se o intervalo de tempo não estiver dentro dos últimos 7 dias, é devolvido um erro.

* Se `SCHEDULED_TIME_RANGE_END` não for especificado, a função devolve as tarefas que já foram concluídas, que estão em execução ou que estão agendadas para o futuro.
* Se `SCHEDULED_TIME_RANGE_END` for CURRENT_TIMESTAMP, a função devolve as tarefas que já foram concluídas ou que estão em execução. Tenha em atenção que uma tarefa executada imediatamente antes da hora atual pode ainda ser identificada como agendada.
* Para consultar apenas as tarefas que já foram concluídas ou que estão em execução, inclua `WHERE query_id IS NOT NULL` como filtro. A coluna QUERY_ID na saída de TASK_HISTORY só é preenchida quando uma tarefa começou a ser executada.

Se não for especificada hora de início nem de fim, são devolvidas as tarefas mais recentes, até ao valor RESULT_LIMIT especificado.

`RESULT_LIMIT => <integer>`

Um número que especifica o número máximo de linhas devolvidas pela função.

Se o número de linhas correspondentes for superior a este limite, são devolvidas as execuções de tarefas com o carimbo de data/hora mais recente, até ao limite especificado.

Intervalo: `1` a `10000`

Predefinição: `100`.

`TASK_NAME => <string>`

Uma cadeia de caracteres, sem distinção entre maiúsculas e minúsculas, que especifica uma tarefa. Só são suportados nomes de tarefas não qualificados. São devolvidas apenas as execuções da tarefa especificada. Tenha em atenção que, se várias tarefas tiverem o mesmo nome, a função devolve o histórico de cada uma delas.

`ERROR_ONLY => { TRUE | FALSE }`

Quando definido como TRUE, esta função devolve apenas as execuções de tarefas que falharam ou foram canceladas.

`ROOT_TASK_ID => <string>`

Identificador único da tarefa raiz num grafo de tarefas. Este ID corresponde ao valor da coluna ID na saída de SHOW TASKS para a mesma tarefa. Especifique ROOT_TASK_ID para mostrar o histórico da tarefa raiz e de quaisquer tarefas subordinadas que façam parte do grafo de tarefas.

## Notas de utilização
* Esta função devolve, no máximo, 10 000 linhas, definidas no valor do argumento RESULT_LIMIT. O valor predefinido é 100.
* Esta função só devolve resultados para a função ACCOUNTADMIN.


## Exemplos de SQL

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
A consulta SQL acima obtém todos os registos do histórico de tarefas da função TASK_HISTORY, ordenados pela coluna scheduled_time (máximo de 10 000).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

A consulta SQL acima obtém todos os registos do histórico de tarefas da função TASK_HISTORY em que o intervalo de tempo agendado começa em '2022-01-02T01:12:00-07:00' e termina em '2022-01-02T01:12:30-07:00'. Isto significa que devolve as tarefas que estavam agendadas para execução nesta janela específica de 30 segundos. O resultado inclui os detalhes das tarefas que correspondem a este critério.
