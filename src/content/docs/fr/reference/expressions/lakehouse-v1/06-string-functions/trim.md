---
title: TRIM (Lakehouse v1)
description: "TRIM : renvoie la chaîne sans les occurrences initiales ou finales de la chaîne à retirer spécifiée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Renvoie la chaîne sans les occurrences initiales ou finales de la chaîne à retirer spécifiée. Si la chaîne à retirer
est omise, les espaces sont supprimés.

La fonction Analyze supprime automatiquement les espaces initiaux et finaux.

## Syntaxe Analyze

```python
func.trim(str)
```

## Exemples Analyze

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## Exemples SQL

À noter : TOUS les exemples de cette section renvoient la chaîne 'databend'.

L'exemple suivant supprime la chaîne 'xxx' au début et à la fin de la chaîne 'xxxdatabendxxx' :

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

L'exemple suivant supprime la chaîne 'xxx' au début de la chaîne 'xxxdatabend' :

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
L'exemple suivant supprime la chaîne 'xxx' à la fin de la chaîne 'databendxxx' :

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Si aucune chaîne à retirer n'est spécifiée, la fonction supprime tous les espaces initiaux et finaux. Les exemples suivants suppriment les espaces initiaux et/ou finaux :

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
