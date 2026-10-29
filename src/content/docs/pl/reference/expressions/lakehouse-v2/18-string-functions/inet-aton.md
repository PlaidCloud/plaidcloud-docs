---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — zamienia ciąg z adresem IPv4 na wartość liczbową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

Zamienia ciąg z adresem IPv4 na wartość liczbową.

## Składnia Analyze

```python
func.inet_aton(<ip_str>)
```

## Przykłady Analyze

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## Składnia SQL

```sql
INET_ATON(<ip_str>)
```

## Przykłady SQL

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
