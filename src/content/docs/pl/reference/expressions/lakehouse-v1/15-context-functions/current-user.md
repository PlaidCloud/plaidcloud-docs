---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER — zwraca kombinację nazwy użytkownika i nazwy hosta dla konta, którego serwer.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Zwraca kombinację nazwy użytkownika i nazwy hosta dla konta, którego serwer użył do uwierzytelnienia bieżącego klienta. To konto określa Twoje uprawnienia dostępu. Zwracana wartość jest ciągiem znaków w zestawie znaków utf8.

## Składnia Analyze

```python
func.current_user()
```

## Przykłady Analyze

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## Składnia SQL

```sql
CURRENT_USER()
```

## Przykłady SQL

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
