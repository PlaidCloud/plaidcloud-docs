---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — extrai uma string com um número específico de caracteres a partir de uma posição determinada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Extrai uma string com um número específico de caracteres a partir de uma posição determinada de uma string informada.

- As formas sem o argumento `len` retornam uma substring da string `str` a partir da posição `pos`.
- As formas com o argumento `len` retornam uma substring com `len` caracteres de comprimento da string `str`, a partir da posição `pos`.

Também é possível usar um valor negativo para `pos`. Nesse caso, o início da substring fica a pos caracteres do fim da string, e não do início. Um valor negativo pode ser usado para `pos` em qualquer uma das formas desta função. Um valor 0 para `pos` retorna uma string vazia. A posição do primeiro caractere da string da qual a substring será extraída é contada como 1.

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

| Argumentos | Descrição                                                                                                  |
|-----------|-------------------------------------------------------------------------------------------------------------|
| `<str>`   | A string principal da qual os caracteres serão extraídos                                                    |
| `<pos>`   | A posição (começando em 1) em que a substring começa. Se negativa, conta a partir do fim                    |
| `<len>`   | O comprimento máximo da substring a extrair                                                                 |

## Aliases

- [SUBSTRING](../substring)
- [MID](../mid)

## Tipo de retorno

VARCHAR

## Exemplos de SQL

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
