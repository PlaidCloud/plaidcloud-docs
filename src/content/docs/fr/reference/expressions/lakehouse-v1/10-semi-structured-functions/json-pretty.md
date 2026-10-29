---
title: JSON_PRETTY (Lakehouse v1)
description: JSON_PRETTY — met en forme des données JSON pour les rendre plus lisibles et plus présentables.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-pretty.md
---

Met en forme des données JSON pour les rendre plus lisibles et plus présentables. Elle ajoute automatiquement l'indentation, les sauts de ligne et d'autres éléments de mise en forme aux données JSON pour une meilleure représentation visuelle.

## Syntaxe Analyze

```python
func.json_pretty(<json_string>)
```

## Exemples Analyze

```python
func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                               │
│   "location": "City",                                                                           │
│   "person": {                                                                                   │
│     "age": 25,                                                                                  │
│     "name": "Bob"                                                                               │
│   }                                                                                             │
│ }                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
JSON_PRETTY(<json_string>)
```

## Type de retour

Chaîne.

## Exemples SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

---
┌──────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"name":"alice","age":30}')) │
│                        String                        │
├──────────────────────────────────────────────────────┤
│ {                                                    │
│   "age": 30,                                         │
│   "name": "Alice"                                    │
│ }                                                    │
└──────────────────────────────────────────────────────┘

SELECT JSON_PRETTY(PARSE_JSON('{"person": {"name": "Bob", "age": 25}, "location": "City"}'));

---
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                        │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                     │
│   "location": "City",                                                                 │
│   "person": {                                                                         │
│     "age": 25,                                                                        │
│     "name": "Bob"                                                                     │
│   }                                                                                   │
│ }                                                                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
