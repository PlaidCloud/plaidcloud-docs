---
title: Den neuesten Datensatz in einer großen Versionsverlaufstabelle auswählen
description: Erfahren Sie, wie Sie in PlaidCloud mit optimierten Abfragetechniken effizient den neuesten Datensatz aus großen Verlaufstabellen auswählen.
sidebar:
  label: Den neuesten Datensatz in einer großen Versionsverlaufstabelle auswählen
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Herausforderung

Es liegt eine Tabelle vor, die viele Versionen jedes Datensatzes enthält, Sie müssen aber die neueste Version verwenden.

## Erläuterung

Dieses Problem ließe sich lösen, indem Sie die ID und das MAX-Aktualisierungsdatum in eine temporäre Tabelle auswählen. Diese temporäre Tabelle könnte dann per INNER JOIN wieder mit der Verlaufstabelle verknüpft werden, um das Ergebnis zu erhalten. Leider erfordert das zwei Schritte und das Speichern einer Zwischentabelle, die keine andere Funktion hat, als die letzte Aktualisierung zu finden.

Die elegantere Lösung, diesen Vorgang in einer einzigen Abfrage auszuführen, verwendet eine Fensterfunktion mit Sortierung plus einen Filter.

## Lösung

### Die Versionsverlaufstabelle

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Einrichtung des Schritts
Erstellen Sie mit einem Extract-Schritt einen Fensterfunktionsausdruck in einer Spalte namens `Rank`, etwa so:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

Legen Sie auf der Registerkarte „Filter“ im Extract-Schritt einen Filter wie den folgenden fest:

```python
table.Rank == 1
```

### Das Ergebnis

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

Dieser Ansatz ist sehr effizient und ermöglicht es, den neuesten Datensatz in einer Verlaufstabelle mit mehreren Versionen in einem einzigen Schritt auszuwählen. Er funktioniert, indem jeder Datensatz innerhalb der Gruppe `employee_id` nach `update_date` eingestuft und dann nur der erste Datensatz ausgewählt wird.

Wenn mehrere Spalten den eindeutigen Zeilenschlüssel bilden, können Sie sie dem Argument `partition_by` als Liste hinzufügen, etwa so:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Wenn Sie nach mehreren Spalten sortieren müssen, können Sie das ebenfalls mit einer Liste von Spalten umsetzen, etwa so:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
