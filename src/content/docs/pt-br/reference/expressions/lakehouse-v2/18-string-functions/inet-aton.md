---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — Converte uma string de endereço IPv4 em um valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

Converte uma string de endereço IPv4 em um valor numérico.

## Sintaxe do Analyze

```python
func.inet_aton(<ip_str>)
```

## Exemplos do Analyze

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## Sintaxe SQL

```sql
INET_ATON(<ip_str>)
```

## Exemplos de SQL

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
