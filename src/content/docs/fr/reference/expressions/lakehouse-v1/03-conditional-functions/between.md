---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN : vrai si une valeur numérique, une chaîne ou une date se situe à l'intérieur (ou à l'extérieur) de la plage donnée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Renvoie `true` si la valeur numérique ou la chaîne ` <expr>` donnée se situe entre les limites inférieure et supérieure définies.

## Syntaxe Analyze

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Exemples Analyze

```python
table.column.between(0, 5)
```

## Syntaxe SQL

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## Exemples SQL

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
