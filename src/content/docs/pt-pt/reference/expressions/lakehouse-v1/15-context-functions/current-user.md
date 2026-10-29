---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER — devolve a combinação de nome de utilizador e nome de anfitrião da conta que o servidor utilizou para autenticar o cliente atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Devolve a combinação de nome de utilizador e nome de anfitrião da conta que o servidor utilizou para autenticar o cliente atual. Esta conta determina os seus privilégios de acesso. O valor devolvido é uma cadeia de caracteres no conjunto de carateres utf8.

## Sintaxe do Analyze

```python
func.current_user()
```

## Exemplos do Analyze

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## Sintaxe SQL

```sql
CURRENT_USER()
```

## Exemplos de SQL

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
