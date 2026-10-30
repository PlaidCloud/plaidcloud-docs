---
title: INSERT (Lakehouse v1)
description: INSERT — devolve a cadeia de caracteres str, com a subcadeia que começa na posição pos e tem len caracteres substituída por newstr.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

Devolve a cadeia de caracteres str, com a subcadeia que começa na posição pos e tem len caracteres de comprimento substituída pela cadeia de caracteres newstr. Devolve a cadeia original se pos não estiver dentro do comprimento da cadeia. Substitui o resto da cadeia a partir da posição pos se len não estiver dentro do comprimento do resto da cadeia. Devolve NULL se qualquer argumento for NULL.

## Sintaxe do Analyze

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Exemplos do Analyze

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## Argumentos

| Argumentos | Descrição                    |
|------------|------------------------------|
| `<str>`    | A cadeia de caracteres.      |
| `<pos>`    | A posição.                   |
| `<len>`    | O comprimento.               |
| `<newstr>` | A nova cadeia de caracteres. |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
