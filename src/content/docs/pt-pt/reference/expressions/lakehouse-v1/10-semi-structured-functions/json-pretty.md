---
title: JSON_PRETTY (Lakehouse v1)
description: JSON_PRETTY — formata dados JSON, tornando-os mais legíveis e apresentáveis.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-pretty.md
---

Formata dados JSON, tornando-os mais legíveis e apresentáveis. Adiciona automaticamente indentação, quebras de linha e outra formatação aos dados JSON para uma melhor representação visual.

## Sintaxe do Analyze

```python
func.json_pretty(<json_string>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
JSON_PRETTY(<json_string>)
```

## Tipo de retorno

Cadeia.

## Exemplos de SQL

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
