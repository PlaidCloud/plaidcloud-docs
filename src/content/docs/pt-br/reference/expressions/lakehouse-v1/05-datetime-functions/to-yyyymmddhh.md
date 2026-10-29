---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH — formata uma data ou timestamp como uma representação em string no formato "YYYYMMDDHH".
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

Formata uma data ou timestamp como uma representação em string no formato "YYYYMMDDHH" (ano, mês, dia, hora).

## Sintaxe do Analyze

```python
func.to_yyyymmddhh(<expr>)
```

## Exemplos do Analyze

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YYYYMMDDHH(<expr>)
```

## Argumentos

| Argumentos | Descrição     |
|-----------|---------------|
| `<expr>`  | data/datetime |

## Tipo de retorno

Retorna um inteiro sem sinal de 64 bits (UInt64) no formato "YYYYMMDDHH".

## Exemplos de SQL

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
