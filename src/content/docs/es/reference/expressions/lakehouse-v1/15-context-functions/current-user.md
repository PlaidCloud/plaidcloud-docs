---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER devuelve la combinación de nombre de usuario y nombre de host de la cuenta que el servidor utilizó para autenticar al cliente actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Devuelve la combinación de nombre de usuario y nombre de host de la cuenta que el servidor utilizó para autenticar al cliente actual. Esta cuenta determina sus privilegios de acceso. El valor devuelto es una cadena en el juego de caracteres utf8.

## Sintaxis de Analyze

```python
func.current_user()
```

## Ejemplos de Analyze

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_USER()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
