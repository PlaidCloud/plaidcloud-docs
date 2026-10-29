---
title: Métodos de comparación (Lakehouse v2)
description: Métodos de comparación — estos métodos de comparación están disponibles en las expresiones de Analyze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

Estos métodos de comparación están disponibles en las expresiones de Analyze.

|Categoría&nbsp;&nbsp;&nbsp;&nbsp;|Expresión|Estructura|Ejemplo|Descripción|
|--------------------------------|----------|---------|-------|-----------|
|Uso general|>|>|table.column > 23|Mayor que|
|Uso general|&lt;|&lt;|table.column &lt; 23|Menor que|
|Uso general|>=|>=|table.column >= 23|Mayor o igual que|
|Uso general|&lt;=|&lt;=|table.column &lt;= 23|Menor o igual que|
|Uso general|==|==|table.column == 23|Igual a|
|Uso general|!=|!=|table.column != 23|Distinto de|
|Uso general|and_|and_()|and_(table.a > 23, table.b == u'blue')|Crea una condición AND de SQL|
|Uso general|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Aplica la condición ANY() de SQL a una columna|
|Uso general|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Aplica la condición BETWEEN de SQL|
|Uso general|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Aplica el LIKE '%%' de SQL|
|Uso general|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Aplica el LIKE '%%' de SQL|
|Uso general|FALSE|FALSE|FALSE|False, false, FALSE: alias de False en Python|
|Uso general|ilike|ilike|table.column.ilike('%foobar%')|Aplica el método ILIKE de SQL|
|Uso general|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Comprueba si los valores están dentro de una tupla de valores|
|Uso general|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Aplica el IS de SQL para casos como IS NULL|
|Uso general|isnot|isnot|table.column.isnot(None)|Aplica el IS de SQL para casos como IS NOT NULL|
|Uso general|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Aplica el método LIKE de SQL|
|Uso general|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Invierte la condición|
|Uso general|notilike|notilike|table.column.notilike('%foobar%')|Aplica el método NOT ILIKE de SQL|
|Uso general|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Invierte la condición IN|
|Uso general|notlike|notlike|table.column.notlike('%foobar%')|Aplica el método NOT LIKE de SQL|
|Uso general|NULL|NULL|NULL|Null, null, NULL: alias de None en Python|
|Uso general|or_|or_()|or_(table.a > 23, table.b == u'blue')|Crea una condición OR de SQL|
|Uso general|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Aplica el LIKE '%' de SQL|
|Uso general|TRUE|TRUE|TRUE|True, true, TRUE: alias de True en Python|
