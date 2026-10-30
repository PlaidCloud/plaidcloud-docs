---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — convertit une adresse IPv4 sous forme de chaîne en valeur numérique.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

Convertit une adresse IPv4 sous forme de chaîne en valeur numérique.

## Syntaxe Analyze

```python
func.inet_aton(<ip_str>)
```

## Exemples Analyze

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## Syntaxe SQL

```sql
INET_ATON(<ip_str>)
```

## Exemples SQL

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
