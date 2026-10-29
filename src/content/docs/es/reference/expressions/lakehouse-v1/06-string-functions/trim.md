---
title: TRIM (Lakehouse v1)
description: "TRIM: devuelve la cadena sin las apariciones iniciales ni finales de la cadena de eliminación especificada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

Devuelve la cadena sin las apariciones iniciales ni finales de la cadena de eliminación especificada. Si se omite la cadena de eliminación,
se quitan los espacios.

La función de Analyze recorta automáticamente los espacios iniciales y finales.

## Sintaxis de Analyze

```python
func.trim(str)
```

## Ejemplos de Analyze

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## Ejemplos de SQL

Tenga en cuenta que TODOS los ejemplos de esta sección devuelven la cadena 'databend'.

El siguiente ejemplo elimina la cadena inicial y final 'xxx' de la cadena 'xxxdatabendxxx':

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

El siguiente ejemplo elimina la cadena inicial 'xxx' de la cadena 'xxxdatabend':

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
El siguiente ejemplo elimina la cadena final 'xxx' de la cadena 'databendxxx':

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

Si no se especifica una cadena de eliminación, la función quita todos los espacios iniciales y finales. Los siguientes ejemplos quitan los espacios iniciales y finales, o solo unos u otros:

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
