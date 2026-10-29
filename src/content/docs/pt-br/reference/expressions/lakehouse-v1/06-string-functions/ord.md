---
title: ORD (Lakehouse v1)
description: ORD — retorna o código do caractere mais à esquerda de uma string (valor ASCII para um byte, valor calculado para multibyte).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

Se o caractere mais à esquerda não for um caractere multibyte, ORD() retorna o mesmo valor da função ASCII().

Se o caractere mais à esquerda da string str for um caractere multibyte, retorna o código desse caractere,
calculado a partir dos valores numéricos dos bytes que o compõem usando esta fórmula:

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

| Argumentos | Descrição |
|-----------|-------------|
| `<str>`   | A string.   |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
