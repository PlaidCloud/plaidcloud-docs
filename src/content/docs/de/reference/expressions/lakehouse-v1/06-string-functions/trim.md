---
title: TRIM (Lakehouse v1)
description: TRIM – gibt die Zeichenfolge ohne führende oder nachgestellte Vorkommen der angegebenen Entfernungszeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Gibt die Zeichenfolge ohne führende oder nachgestellte Vorkommen der angegebenen Entfernungszeichenfolge zurück. Wenn die Entfernungszeichenfolge
weggelassen wird, werden Leerzeichen entfernt.

Die Analyze-Funktion entfernt automatisch sowohl führende als auch nachgestellte Leerzeichen.

## Analyze-Syntax

```python
func.trim(str)
```

## Analyze-Beispiele

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## SQL-Beispiele

Bitte beachten Sie, dass ALLE Beispiele in diesem Abschnitt die Zeichenfolge 'databend' zurückgeben.

Das folgende Beispiel entfernt die führende und nachgestellte Zeichenfolge 'xxx' aus der Zeichenfolge 'xxxdatabendxxx':

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

Das folgende Beispiel entfernt die führende Zeichenfolge 'xxx' aus der Zeichenfolge 'xxxdatabend':

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
Das folgende Beispiel entfernt die nachgestellte Zeichenfolge 'xxx' aus der Zeichenfolge 'databendxxx':

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Wenn keine Entfernungszeichenfolge angegeben ist, entfernt die Funktion alle führenden und nachgestellten Leerzeichen. Die folgenden Beispiele entfernen die führenden und/oder nachgestellten Leerzeichen:

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
