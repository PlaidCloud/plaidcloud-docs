---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE wandelt einen Wert in sein Nullable-Äquivalent um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

Wandelt einen Wert in sein Nullable-Äquivalent um.

Wenn Sie diese Funktion auf einen Wert anwenden, prüft sie, ob der Wert bereits NULL-Werte aufnehmen kann. Kann der Wert bereits NULL-Werte aufnehmen, gibt die Funktion den Wert unverändert zurück.

Kann der Wert dagegen keine NULL-Werte aufnehmen, ändert die Funktion TO_NULLABLE den Wert so, dass er NULL-Werte aufnehmen kann. Dazu wird der Wert in eine Struktur eingebettet, die NULL-Werte aufnehmen kann. Der Wert kann dadurch künftig NULL-Werte enthalten.

## Analyze-Syntax

```python
func.to_nullable(x);
```

## Analyze-Beispiele

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## SQL-Syntax

```sql
TO_NULLABLE(x);
```

## Argumente

| Argumente | Beschreibung               |
|-----------|----------------------------|
| x         | Der ursprüngliche Wert.    |


## Rückgabetyp

Gibt einen Wert desselben Datentyps wie der Eingabewert zurück, der in einen Nullable-Container eingebettet ist, falls der Eingabewert nicht bereits Nullable ist.

## SQL-Beispiele

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
