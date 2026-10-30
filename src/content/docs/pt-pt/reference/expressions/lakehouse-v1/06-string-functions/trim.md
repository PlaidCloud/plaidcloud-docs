---
title: TRIM (Lakehouse v1)
description: TRIM — devolve a cadeia de caracteres sem as ocorrências iniciais ou finais da cadeia a remover especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Devolve a cadeia de caracteres sem as ocorrências iniciais ou finais da cadeia a remover especificada. Se a cadeia a remover
for omitida, são removidos os espaços.

A função do Analyze remove automaticamente os espaços iniciais e finais.

## Sintaxe do Analyze

```python
func.trim(str)
```

## Exemplos do Analyze

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## Exemplos de SQL

Tenha em atenção que TODOS os exemplos desta secção devolvem a cadeia de caracteres 'databend'.

O exemplo seguinte remove a cadeia inicial e final 'xxx' da cadeia 'xxxdatabendxxx':

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

O exemplo seguinte remove a cadeia inicial 'xxx' da cadeia 'xxxdatabend':

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
O exemplo seguinte remove a cadeia final 'xxx' da cadeia 'databendxxx':

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Se não for especificada nenhuma cadeia a remover, a função remove todos os espaços iniciais e finais. Os exemplos seguintes removem os espaços iniciais e/ou finais:

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
