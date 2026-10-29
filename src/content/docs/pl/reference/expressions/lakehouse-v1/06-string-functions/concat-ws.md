---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS — nazwa pochodzi od Concatenate With Separator (łączenie z separatorem) i jest specjalną formą funkcji CONCAT().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() to skrót od Concatenate With Separator (łączenie z separatorem) i jest specjalną formą funkcji CONCAT(). Pierwszy argument jest separatorem dla pozostałych argumentów. Separator jest dodawany między łączonymi ciągami znaków. Separatorem może być ciąg znaków, podobnie jak pozostałe argumenty. Jeśli separator ma wartość NULL, wynikiem jest NULL.

CONCAT_WS() nie pomija pustych ciągów znaków. Pomija jednak wszystkie wartości NULL występujące po argumencie separatora.

## Składnia Analyze

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Przykłady Analyze

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## Argumenty

| Argumenty     | Opis                |
|---------------| ------------------- |
| `<separator>` | kolumna tekstowa    |
| `<expr1>`     | kolumna z wartością |

## Typ zwracany

Wartość typu danych `VARCHAR` lub typ danych `NULL`.

## Przykłady SQL

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
