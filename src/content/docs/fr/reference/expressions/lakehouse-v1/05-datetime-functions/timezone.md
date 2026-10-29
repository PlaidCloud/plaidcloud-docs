---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — renvoie le fuseau horaire de la connexion en cours.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Renvoie le fuseau horaire de la connexion en cours. 

PlaidCloud Lakehouse utilise UTC (temps universel coordonné) comme fuseau horaire par défaut et vous permet de le remplacer par celui de votre position géographique. Pour connaître les valeurs que vous pouvez affecter au paramètre `timezone`, consultez https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Voir les exemples ci-dessous pour plus de détails.

## Syntaxe Analyze

```python
func.timezone()
```

## Exemples Analyze

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
SELECT TIMEZONE();
```

## Exemples SQL

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
