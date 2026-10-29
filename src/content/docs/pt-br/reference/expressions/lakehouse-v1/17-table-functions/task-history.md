---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY — exibe o histórico de execução de tarefas de acordo com as variáveis informadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Exibe o histórico de execução de tarefas de acordo com as variáveis informadas.

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

Intervalo de tempo (no formato TIMESTAMP_LTZ), dentro dos últimos 7 dias, em que a execução da tarefa foi agendada. Se o intervalo de tempo não estiver dentro dos últimos 7 dias, um erro é retornado.

* Se `SCHEDULED_TIME_RANGE_END` não for especificado, a função retorna as tarefas que já foram concluídas, que estão em execução ou que estão agendadas para o futuro.
* Se `SCHEDULED_TIME_RANGE_END` for CURRENT_TIMESTAMP, a função retorna as tarefas que já foram concluídas ou que estão em execução. Observe que uma tarefa executada imediatamente antes do horário atual ainda pode ser identificada como agendada.
* Para consultar apenas as tarefas que já foram concluídas ou que estão em execução, inclua `WHERE query_id IS NOT NULL` como filtro. A coluna QUERY_ID na saída de TASK_HISTORY só é preenchida quando uma tarefa começa a ser executada.

Se nenhum horário de início ou de término for especificado, as tarefas mais recentes são retornadas, até o valor de RESULT_LIMIT especificado.

`RESULT_LIMIT => <integer>`

Um número que especifica o máximo de linhas retornadas pela função.

Se o número de linhas correspondentes for maior que esse limite, as execuções de tarefa com o carimbo de data/hora mais recente são retornadas, até o limite especificado.

Intervalo: `1` a `10000`

Padrão: `100`.

`TASK_NAME => <string>`

Uma string que não diferencia maiúsculas de minúsculas e especifica uma tarefa. Somente nomes de tarefa não qualificados são aceitos. Somente as execuções da tarefa especificada são retornadas. Observe que, se várias tarefas tiverem o mesmo nome, a função retorna o histórico de cada uma delas.

`ERROR_ONLY => { TRUE | FALSE }`

Quando definido como TRUE, esta função retorna apenas as execuções de tarefa que falharam ou foram canceladas.

`ROOT_TASK_ID => <string>`

Identificador exclusivo da tarefa raiz em um grafo de tarefas. Esse ID corresponde ao valor da coluna ID na saída de SHOW TASKS para a mesma tarefa. Especifique ROOT_TASK_ID para mostrar o histórico da tarefa raiz e de quaisquer tarefas filhas que façam parte do grafo de tarefas.

## Observações de uso
* Esta função retorna no máximo 10.000 linhas, definidas pelo valor do argumento RESULT_LIMIT. O valor padrão é 100.
* Esta função retorna resultados somente para a função ACCOUNTADMIN.


## Exemplos de SQL

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
A consulta SQL acima recupera todos os registros do histórico de tarefas da função TASK_HISTORY, ordenados pela coluna scheduled_time (máximo de 10.000).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

A consulta SQL acima recupera todos os registros do histórico de tarefas da função TASK_HISTORY em que o intervalo de tempo agendado começa em '2022-01-02T01:12:00-07:00' e termina em '2022-01-02T01:12:30-07:00'. Isso significa que ela retornará as tarefas que foram agendadas para execução dentro dessa janela específica de 30 segundos. O resultado incluirá os detalhes das tarefas que atendem a esse critério.
