---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — Wandelt eine IPv4-Adresse als Zeichenfolge in einen numerischen Wert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

Wandelt eine IPv4-Adresse als Zeichenfolge in einen numerischen Wert um.

## Analyze-Syntax

```python
func.inet_aton(<ip_str>)
```

## Analyze-Beispiele

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## SQL-Syntax

```sql
INET_ATON(<ip_str>)
```

## SQL-Beispiele

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
