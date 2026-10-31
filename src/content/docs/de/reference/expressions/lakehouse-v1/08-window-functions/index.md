---
title: Fensterfunktionen (Lakehouse v1)
description: "SQL-Fensterfunktionen in Lakehouse v1: Berechnungen über Zeilenfenster – Rangfolgen, laufende Summen, Lead und Lag."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## Überblick

Eine Fensterfunktion arbeitet auf einer Gruppe („Fenster“) zusammengehöriger Zeilen.

Für jede Eingabezeile gibt eine Fensterfunktion eine Ausgabezeile zurück, die von der an die Funktion übergebenen Zeile und den Werten der anderen Zeilen im Fenster abhängt.

Es gibt zwei Haupttypen reihenfolgeabhängiger Fensterfunktionen:

* `Rank-related functions`: Rangbezogene Funktionen liefern Informationen auf Grundlage des „Rangs“ einer Zeile. Wenn Sie beispielsweise Filialen absteigend nach dem Jahresgewinn ordnen, erhält die Filiale mit dem höchsten Gewinn Rang 1, die zweitprofitabelste Filiale Rang 2 und so weiter.

* `Window frame functions`: Fensterrahmenfunktionen ermöglichen rollierende Berechnungen, etwa eine laufende Summe oder einen gleitenden Durchschnitt, auf einer Teilmenge der Zeilen im Fenster.

## Liste der Funktionen mit Fensterunterstützung

Die folgende Liste zeigt alle Fensterfunktionen.

| Funktionsname                                                         | Kategorie    | Fenster | Fensterrahmen | Hinweise |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | Allgemein    | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | Allgemein    | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | Allgemein    | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | Allgemein    | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | Allgemein    | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | Allgemein    | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | Allgemein    | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | Allgemein    | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | Allgemein    | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | Allgemein    | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | Allgemein    | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | Allgemein    | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | Allgemein    | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | Allgemein    | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | Allgemein    | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | Allgemein    | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | Allgemein    | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | Allgemein    | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | Allgemein    | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | Allgemein    | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | Rangbezogen  | ✔      |              |       |
| [PERCENT_RANK](percent-rank/)                                         | Rangbezogen  | ✔      | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | Rangbezogen  | ✔      | ✔            |       |
| [RANK](rank)                                                          | Rangbezogen  | ✔      | ✔            |       |
| [ROW_NUMBER](row-number)                                              | Rangbezogen  | ✔      |              |       |
| [NTILE](ntile)                                                        | Rangbezogen  | ✔      |              |       |
| [FIRST_VALUE](first-value)                                            | Rangbezogen   | ✔     | ✔            |       |
| [FIRST](first)                                                        | Rangbezogen 	| ✔     | ✔            |       |
| [LAST_VALUE](last-value)                                              | Rangbezogen 	| ✔     | ✔            |       |
| [LAST](last)                                                          | Rangbezogen 	| ✔     | ✔            |       |
| [NTH_VALUE](nth-value)                                                | Rangbezogen 	| ✔     | ✔            |       |
| [LEAD](lead)                                                          | Rangbezogen 	| ✔     |              |       |
| [LAG](lag)                                                            | Rangbezogen 	| ✔     |              |       |

## Fenstersyntax

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
Das `named window` ist ein Fenster, das in der `WINDOW`-Klausel der `SELECT`-Anweisung definiert wird, z. B.: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

Die `<function>` ist eine von ([Aggregatfunktion](../07-aggregate-functions), Rangfunktion, Wertfunktion).

Die `OVER`-Klausel legt fest, dass die Funktion als Fensterfunktion verwendet wird.

Die Teilklausel `PARTITION BY` ermöglicht es, Zeilen in Untergruppen zu gruppieren, zum Beispiel nach Stadt, nach Jahr usw. Die Klausel `PARTITION BY` ist optional. Sie können eine gesamte Gruppe von Zeilen analysieren, ohne sie in Untergruppen aufzuteilen.

Die Klausel `ORDER BY` sortiert die Zeilen innerhalb des Fensters.

Die Klausel `window frame` legt den Fensterrahmentyp und den Fensterrahmenumfang fest. Die Klausel `window frame` ist optional. Wenn Sie die Klausel `window frame` weglassen, ist der Standard-Fensterrahmentyp `RANGE` und der Standard-Fensterrahmenumfang `UNBOUNDED PRECEDING AND CURRENT ROW`.


## Fensterrahmensyntax

`window frame` kann einer der folgenden Typen sein:

```sql
cumulativeFrame ::=
    {
       { ROWS | RANGE } BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
     | { ROWS | RANGE } BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    }
```

```sql
slidingFrame ::=
    {
       ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN UNBOUNDED PRECEDING AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND UNBOUNDED FOLLOWING
    }
```


## SQL-Beispiele

**Tabelle erstellen**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Daten einfügen**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 75000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 90000),
  (4, 'Sara', 'Williams', 'Sales', 60000),
  (5, 'Tom', 'Brown', 'HR', 82000),
  (6, 'Ava', 'Davis', 'Sales', 62000),
  (7, 'Olivia', 'Taylor', 'IT', 72000),
  (8, 'Emily', 'Anderson', 'HR', 77000),
  (9, 'Sophia', 'Lee', 'Sales', 58000),
  (10, 'Ella', 'Thomas', 'IT', 67000);
```

**Beispiel 1: Mitarbeiter nach Gehalt ranken**

In diesem Beispiel verwenden wir die Funktion RANK(), um Mitarbeiter anhand ihrer Gehälter in absteigender Reihenfolge zu ranken. Das höchste Gehalt erhält Rang 1, das niedrigste Gehalt die höchste Rangnummer.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

Ergebnis:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 3           | Mike       | Johnson   | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 5           | Tom        | Brown     | HR         | 82000  | 3    |
| 8           | Emily      | Anderson  | HR         | 77000  | 4    |
| 1           | John       | Doe       | IT         | 75000  | 5    |
| 7           | Olivia     | Taylor    | IT         | 72000  | 6    |
| 10          | Ella       | Thomas    | IT         | 67000  | 7    |
| 6           | Ava        | Davis     | Sales      | 62000  | 8    |
| 4           | Sara       | Williams  | Sales      | 60000  | 9    |
| 9           | Sophia     | Lee       | Sales      | 58000  | 10   |



**Beispiel 2: Gesamtgehalt pro Abteilung berechnen**

In diesem Beispiel verwenden wir die Funktion SUM() mit PARTITION BY, um das pro Abteilung gezahlte Gesamtgehalt zu berechnen. Jede Zeile zeigt die Abteilung und das Gesamtgehalt dieser Abteilung.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

Ergebnis:

| department | total_salary |
|------------|--------------|
| HR         | 244000       |
| HR         | 244000       |
| HR         | 244000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| Sales      | 180000       |
| Sales      | 180000       |
| Sales      | 180000       |


**Beispiel 3: Laufende Summe der Gehälter pro Abteilung berechnen**

In diesem Beispiel verwenden wir die Funktion SUM() mit einem kumulativen Fensterrahmen, um innerhalb jeder Abteilung eine laufende Summe der Gehälter zu berechnen. Die laufende Summe wird anhand des Gehalts des Mitarbeiters berechnet, sortiert nach employee_id.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

Ergebnis:

| employee_id | first_name | last_name | department | salary | running_total |
|-------------|------------|-----------|------------|--------|---------------|
| 2           | Jane       | Smith     | HR         | 85000  | 85000         |
| 5           | Tom        | Brown     | HR         | 82000  | 167000        |
| 8           | Emily      | Anderson  | HR         | 77000  | 244000        |
| 1           | John       | Doe       | IT         | 75000  | 75000         |
| 3           | Mike       | Johnson   | IT         | 90000  | 165000        |
| 7           | Olivia     | Taylor    | IT         | 72000  | 237000        |
| 10          | Ella       | Thomas    | IT         | 67000  | 304000        |
| 4           | Sara       | Williams  | Sales      | 60000  | 60000         |
| 6           | Ava        | Davis     | Sales      | 62000  | 122000        |
| 9           | Sophia     | Lee       | Sales      | 58000  | 180000        |
