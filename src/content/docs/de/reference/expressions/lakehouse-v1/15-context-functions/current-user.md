---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER gibt die Kombination aus Benutzername und Hostname für das Konto zurück, mit dem der Server den aktuellen Client authentifiziert hat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Gibt die Kombination aus Benutzername und Hostname für das Konto zurück, mit dem der Server den aktuellen Client authentifiziert hat. Dieses Konto bestimmt Ihre Zugriffsrechte. Der Rückgabewert ist eine Zeichenfolge im Zeichensatz utf8.

## Analyze-Syntax

```python
func.current_user()
```

## Analyze-Beispiele

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## SQL-Syntax

```sql
CURRENT_USER()
```

## SQL-Beispiele

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
