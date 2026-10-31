---
title: Métodos de comparação (Lakehouse v2)
description: Métodos de comparação — estes métodos de comparação estão disponíveis nas expressões do Analyze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

Estes métodos de comparação estão disponíveis nas expressões do Analyze.

|Categoria&nbsp;&nbsp;&nbsp;&nbsp;|Expressão|Estrutura|Exemplo|Descrição|
|--------------------------------|----------|---------|-------|-----------|
|Utilização geral|>|>|table.column > 23|Maior que|
|Utilização geral|&lt;|&lt;|table.column &lt; 23|Menor que|
|Utilização geral|>=|>=|table.column >= 23|Maior ou igual a|
|Utilização geral|&lt;=|&lt;=|table.column &lt;= 23|Menor ou igual a|
|Utilização geral|==|==|table.column == 23|Igual a|
|Utilização geral|!=|!=|table.column != 23|Diferente de|
|Utilização geral|and_|and_()|and_(table.a > 23, table.b == u'blue')|Cria uma condição SQL AND|
|Utilização geral|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Aplica a condição SQL ANY() a uma coluna|
|Utilização geral|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Aplica a condição SQL BETWEEN|
|Utilização geral|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Aplica o SQL LIKE '%%'|
|Utilização geral|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Aplica o SQL LIKE '%%'|
|Utilização geral|FALSE|FALSE|FALSE|False, false, FALSE - alias de Python False|
|Utilização geral|ilike|ilike|table.column.ilike('%foobar%')|Aplica o método SQL ILIKE|
|Utilização geral|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Testa se os valores pertencem a um tuplo de valores|
|Utilização geral|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Aplica o IS do SQL para casos como IS NULL|
|Utilização geral|isnot|isnot|table.column.isnot(None)|Aplica o IS do SQL para casos como IS NOT NULL|
|Utilização geral|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Aplica o método SQL LIKE|
|Utilização geral|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Inverte a condição|
|Utilização geral|notilike|notilike|table.column.notilike('%foobar%')|Aplica o método SQL NOT ILIKE|
|Utilização geral|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Inverte a condição IN|
|Utilização geral|notlike|notlike|table.column.notlike('%foobar%')|Aplica o método SQL NOT LIKE|
|Utilização geral|NULL|NULL|NULL|Null, null, NULL - alias de Python None|
|Utilização geral|or_|or_()|or_(table.a > 23, table.b == u'blue')|Cria uma condição SQL OR|
|Utilização geral|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Aplica o SQL LIKE '%'|
|Utilização geral|TRUE|TRUE|TRUE|True, true, TRUE - alias de Python True|
