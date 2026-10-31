---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — extrai uma cadeia de caracteres com um número específico de caracteres a partir de uma determinada posição.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Extrai uma cadeia de caracteres com um número específico de caracteres a partir de uma determinada posição de uma cadeia de caracteres indicada.

- As formas sem o argumento `len` devolvem uma subcadeia da cadeia `str` a começar na posição `pos`.
- As formas com o argumento `len` devolvem uma subcadeia com `len` caracteres de comprimento da cadeia `str`, a começar na posição `pos`.

Também é possível utilizar um valor negativo para `pos`. Neste caso, o início da subcadeia situa-se a pos caracteres do fim da cadeia, em vez do início. Pode ser utilizado um valor negativo para `pos` em qualquer uma das formas desta função. Um valor 0 para `pos` devolve uma cadeia de caracteres vazia. A posição do primeiro caráter da cadeia de onde a subcadeia vai ser extraída é contada como 1.

## Sintaxe do Analyze

```python
func.substr(<str>, <pos>, <len>)
```

## Exemplos do Analyze

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## Argumentos

| Argumentos | Descrição                                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------|
| `<str>`   | A cadeia de caracteres principal de onde os caracteres vão ser extraídos                                     |
| `<pos>`   | A posição (a começar em 1) em que a subcadeia deve começar. Se for negativa, conta a partir do fim           |
| `<len>`   | O comprimento máximo da subcadeia a extrair                                                                  |

## Aliases

- [SUBSTRING](../substring)
- [MID](../mid)

## Tipo de Retorno

VARCHAR

## Exemplos SQL

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
