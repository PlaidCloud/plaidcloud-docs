---
title: Métodos de comparação (Lakehouse v1)
description: Métodos de comparação — estes métodos de comparação estão disponíveis nas expressões do Analyze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/comparisons.md
---

Estes métodos de comparação estão disponíveis nas expressões do Analyze.

|Categoria&nbsp;&nbsp;&nbsp;&nbsp;|Expressão|Estrutura|Exemplo|Descrição|
|--------------------------------|----------|---------|-------|-----------|
|Uso geral|>|>|table.column > 23|Maior que|
|Uso geral|&lt;|&lt;|table.column &lt; 23|Menor que|
|Uso geral|>=|>=|table.column >= 23|Maior ou igual a|
|Uso geral|&lt;=|&lt;=|table.column &lt;= 23|Menor ou igual a|
|Uso geral|==|==|table.column == 23|Igual a|
|Uso geral|!=|!=|table.column != 23|Diferente de|
|Uso geral|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[Mais exemplos](../and)|Cria uma condição AND em SQL|
|Uso geral|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Aplica a condição SQL ANY() a uma coluna|
|Uso geral|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Aplica a condição SQL BETWEEN|
|Uso geral|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Aplica o SQL LIKE '%%'|
|Uso geral|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Aplica o SQL LIKE '%%'|
|Uso geral|FALSE|FALSE|FALSE|False, false, FALSE - Alias de False do Python|
|Uso geral|ilike|ilike|table.column.ilike('%foobar%')|Aplica o método SQL ILIKE|
|Uso geral|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Testa se os valores estão em uma tupla de valores|
|Uso geral|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Aplica o IS do SQL para casos como IS NULL|
|Uso geral|isnot|isnot|table.column.isnot(None)|Aplica o IS do SQL para casos como IS NOT NULL|
|Uso geral|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Aplica o método SQL LIKE|
|Uso geral|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Inverte a condição|
|Uso geral|notilike|notilike|table.column.notilike('%foobar%')|Aplica o método SQL NOT ILIKE|
|Uso geral|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Inverte a condição IN|
|Uso geral|notlike|notlike|table.column.notlike('%foobar%')|Aplica o método SQL NOT LIKE|
|Uso geral|NULL|NULL|NULL|Null, null, NULL - Alias de None do Python|
|Uso geral|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[Mais exemplos](../or)|Cria uma condição OR em SQL|
|Uso geral|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Aplica o SQL LIKE '%'|
|Uso geral|TRUE|TRUE|TRUE|True, true, TRUE - Alias de True do Python|	
|Expressões matemáticas|+|+|+|adição, por exemplo, 2+3=5|
|Expressões matemáticas|–|–|-|subtração, por exemplo, 2–3=-1|
|Expressões matemáticas|*|*|*|multiplicação, por exemplo, 2*3=6|
|Expressões matemáticas|/|/|/|divisão|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('%')`|módulo (resto), por exemplo, 5%4=1|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('^')`|exponenciação, por exemplo, 2.0^3.0=8|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('!')`|fatorial, por exemplo, 5!=120|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('&')`|AND bit a bit, por exemplo, 91&15=11|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('#')`|XOR bit a bit, por exemplo, 17 # 5=20|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('~')`|NOT bit a bit, por exemplo, ~1=-2|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('&lt;&lt;')`|deslocamento de bits à esquerda, por exemplo, 1&lt;&lt;4=16|
|Expressões matemáticas|column.op|`column.op(operator)`|`column.op('>>')`|deslocamento de bits à direita, por exemplo, 8>>2=2|
