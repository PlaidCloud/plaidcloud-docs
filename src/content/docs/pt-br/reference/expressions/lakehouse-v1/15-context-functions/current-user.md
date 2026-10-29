---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER — retorna a combinação de nome de usuário e nome de host da conta que o servidor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Retorna a combinação de nome de usuário e nome de host da conta que o servidor usou para autenticar o cliente atual. Essa conta determina seus privilégios de acesso. O valor retornado é uma string no conjunto de caracteres utf8.

## Sintaxe no Analyze

```python
func.current_user()
```

## Exemplos no Analyze

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
