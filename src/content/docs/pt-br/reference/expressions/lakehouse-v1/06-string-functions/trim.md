---
title: TRIM (Lakehouse v1)
description: TRIM — retorna a string sem ocorrências iniciais ou finais da string de remoção especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Retorna a string sem ocorrências iniciais ou finais da string de remoção especificada. Se a string de remoção
for omitida, os espaços são removidos.

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

Observação: TODOS os exemplos desta seção retornam a string 'databend'.

O exemplo a seguir remove a string 'xxx' do início e do final da string 'xxxdatabendxxx':

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

O exemplo a seguir remove a string 'xxx' do início da string 'xxxdatabend':

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
O exemplo a seguir remove a string 'xxx' do final da string 'databendxxx':

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Se nenhuma string de remoção for especificada, a função remove todos os espaços iniciais e finais. Os exemplos a seguir removem os espaços iniciais e/ou finais:

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
