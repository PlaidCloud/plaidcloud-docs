---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — devolve a subcadeia da cadeia de caracteres expr que corresponde à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Devolve a subcadeia da cadeia de caracteres `expr` que corresponde à expressão regular especificada pelo padrão `pat`, ou NULL se não houver correspondência. Se expr ou pat for NULL, o valor devolvido é NULL.

## Sintaxe do Analyze

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Exemplos do Analyze

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Argumentos

| Argumentos | Descrição                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------|
| expr       | A cadeia de caracteres expr a corresponder                                                                         |
| pat        | A expressão regular                                                                                                |
| pos        | Opcional. A posição em expr a partir da qual iniciar a pesquisa. Se omitido, o valor predefinido é 1.              |
| occurrence | Opcional. Qual a ocorrência de uma correspondência a pesquisar. Se omitido, o valor predefinido é 1.               |
| match_type | Opcional. Uma cadeia de caracteres que especifica como efetuar a correspondência. O significado é o descrito para REGEXP_LIKE(). |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
