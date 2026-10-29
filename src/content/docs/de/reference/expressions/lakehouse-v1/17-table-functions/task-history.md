---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY zeigt den Ausführungsverlauf von Tasks anhand der angegebenen Variablen an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Zeigt den Ausführungsverlauf von Tasks anhand der angegebenen Variablen an.

## SQL-Syntax
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## Argumente

Alle Argumente sind optional.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

Zeitraum (im Format TIMESTAMP_LTZ) innerhalb der letzten 7 Tage, in dem die Ausführung des Tasks geplant war. Liegt der Zeitraum nicht innerhalb der letzten 7 Tage, wird ein Fehler zurückgegeben.

* Wenn `SCHEDULED_TIME_RANGE_END` nicht angegeben ist, gibt die Funktion Tasks zurück, die bereits abgeschlossen sind, derzeit ausgeführt werden oder für die Zukunft geplant sind.
* Wenn `SCHEDULED_TIME_RANGE_END` den Wert CURRENT_TIMESTAMP hat, gibt die Funktion Tasks zurück, die bereits abgeschlossen sind oder derzeit ausgeführt werden. Beachten Sie, dass ein Task, der unmittelbar vor dem aktuellen Zeitpunkt ausgeführt wird, möglicherweise noch als geplant erkannt wird.
* Um nur Tasks abzufragen, die bereits abgeschlossen sind oder derzeit ausgeführt werden, nehmen Sie `WHERE query_id IS NOT NULL` als Filter auf. Die Spalte QUERY_ID in der Ausgabe von TASK_HISTORY wird erst gefüllt, wenn ein Task zu laufen begonnen hat.

Wenn weder Start- noch Endzeitpunkt angegeben sind, werden die neuesten Tasks zurückgegeben, bis zum angegebenen Wert von RESULT_LIMIT.

`RESULT_LIMIT => <integer>`

Eine Zahl, die die maximale Anzahl der von der Funktion zurückgegebenen Zeilen angibt.

Ist die Anzahl der passenden Zeilen größer als dieses Limit, werden die Task-Ausführungen mit dem neuesten Zeitstempel bis zum angegebenen Limit zurückgegeben.

Bereich: `1` bis `10000`

Standard: `100`.

`TASK_NAME => <string>`

Eine Zeichenfolge ohne Beachtung der Groß- und Kleinschreibung, die einen Task angibt. Es werden nur nicht qualifizierte Task-Namen unterstützt. Es werden nur Ausführungen des angegebenen Tasks zurückgegeben. Beachten Sie, dass die Funktion den Verlauf jedes dieser Tasks zurückgibt, wenn mehrere Tasks denselben Namen haben.

`ERROR_ONLY => { TRUE | FALSE }`

Bei TRUE gibt diese Funktion nur Task-Ausführungen zurück, die fehlgeschlagen sind oder abgebrochen wurden.

`ROOT_TASK_ID => <string>`

Eindeutiger Bezeichner des Root-Tasks in einem Task-Graphen. Diese ID entspricht dem Wert der Spalte ID in der Ausgabe von SHOW TASKS für denselben Task. Geben Sie ROOT_TASK_ID an, um den Verlauf des Root-Tasks und aller untergeordneten Tasks anzuzeigen, die Teil des Task-Graphen sind.

## Hinweise zur Verwendung
* Diese Funktion gibt höchstens 10.000 Zeilen zurück, festgelegt über den Wert des Arguments RESULT_LIMIT. Der Standardwert ist 100.
* Diese Funktion gibt nur für die Rolle ACCOUNTADMIN Ergebnisse zurück.


## SQL-Beispiele

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
Die obige SQL-Abfrage ruft alle Datensätze des Task-Verlaufs aus der Funktion TASK_HISTORY ab, sortiert nach der Spalte scheduled_time (höchstens 10.000).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

Die obige SQL-Abfrage ruft alle Datensätze des Task-Verlaufs aus der Funktion TASK_HISTORY ab, deren geplanter Zeitraum am '2022-01-02T01:12:00-07:00' beginnt und am '2022-01-02T01:12:30-07:00' endet. Sie gibt also die Tasks zurück, deren Ausführung innerhalb dieses bestimmten 30-Sekunden-Zeitfensters geplant war. Das Ergebnis enthält die Details der Tasks, die diese Kriterien erfüllen.
