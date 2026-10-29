---
title: TRIM (Lakehouse v1)
description: TRIM — zwraca ciąg znaków bez początkowych i końcowych wystąpień podanego ciągu do usunięcia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Zwraca ciąg znaków bez początkowych i końcowych wystąpień podanego ciągu do usunięcia. Jeśli ciąg do usunięcia
zostanie pominięty, usuwane są spacje.

Funkcja Analyze automatycznie przycina zarówno początkowe, jak i końcowe spacje.

## Składnia Analyze

```python
func.trim(str)
```

## Przykłady Analyze

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## Składnia SQL

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## Przykłady SQL

Uwaga: WSZYSTKIE przykłady w tej sekcji zwracają ciąg znaków 'databend'.

Poniższy przykład usuwa początkowy i końcowy ciąg 'xxx' z ciągu 'xxxdatabendxxx':

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

Poniższy przykład usuwa początkowy ciąg 'xxx' z ciągu 'xxxdatabend':

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
Poniższy przykład usuwa końcowy ciąg 'xxx' z ciągu 'databendxxx':

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Jeśli nie podano ciągu do usunięcia, funkcja usuwa wszystkie początkowe i końcowe spacje. Poniższe przykłady usuwają początkowe i (lub) końcowe spacje:

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
