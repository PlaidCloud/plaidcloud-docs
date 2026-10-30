---
title: ORD (Lakehouse v1)
description: ORD — devolve o código do caráter mais à esquerda de uma cadeia de caracteres (valor ASCII para um byte, valor calculado para vários bytes).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Se o caráter mais à esquerda não for um caráter multibyte, ORD() devolve o mesmo valor que a função ASCII().

Se o caráter mais à esquerda da cadeia de caracteres str for um caráter multibyte, devolve o código desse caráter,
calculado a partir dos valores numéricos dos bytes que o compõem através desta fórmula:

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Sintaxe do Analyze

```python
func.ord(<str>)
```

## Exemplos do Analyze

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## Sintaxe SQL

```sql
ORD(<str>)
```

## Argumentos

| Argumentos | Descrição               |
|-----------|-------------------------|
| `<str>`   | A cadeia de caracteres. |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
