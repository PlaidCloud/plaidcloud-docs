---
title: 比较方法（Lakehouse v1）
description: 比较方法——Analyze 表达式中可用的比较方法。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/comparisons.md
---

Analyze 表达式中可使用以下比较方法。

|类别&nbsp;&nbsp;&nbsp;&nbsp;|表达式|结构|示例|说明|
|--------------------------------|----------|---------|-------|-----------|
|通用|>|>|table.column > 23|大于|
|通用|&lt;|&lt;|table.column &lt; 23|小于|
|通用|>=|>=|table.column >= 23|大于或等于|
|通用|&lt;=|&lt;=|table.column &lt;= 23|小于或等于|
|通用|==|==|table.column == 23|等于|
|通用|!=|!=|table.column != 23|不等于|
|通用|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[更多示例](../and)|创建 AND SQL 条件|
|通用|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|对列应用 SQL ANY() 条件|
|通用|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|应用 SQL BETWEEN 条件|
|通用|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|应用 SQL LIKE '%%'|
|通用|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|应用 SQL LIKE '%%'|
|通用|FALSE|FALSE|FALSE|False、false、FALSE——Python False 的别名|
|通用|ilike|ilike|table.column.ilike('%foobar%')|应用 SQL ILIKE 方法|
|通用|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|测试值是否在元组所列的值之中|
|通用|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|应用 SQL 的 IS，用于 IS NULL 等场景|
|通用|isnot|isnot|table.column.isnot(None)|应用 SQL 的 IS，用于 IS NOT NULL 等场景|
|通用|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|应用 SQL LIKE 方法|
|通用|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|对条件取反|
|通用|notilike|notilike|table.column.notilike('%foobar%')|应用 SQL NOT ILIKE 方法|
|通用|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|对 IN 条件取反|
|通用|notlike|notlike|table.column.notlike('%foobar%')|应用 SQL NOT LIKE 方法|
|通用|NULL|NULL|NULL|Null、null、NULL——Python None 的别名|
|通用|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[更多示例](../or)|创建 OR SQL 条件|
|通用|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|应用 SQL LIKE '%'|
|通用|TRUE|TRUE|TRUE|True、true、TRUE——Python True 的别名|	
|数学表达式|+|+|+|加法，例如 2+3=5|
|数学表达式|–|–|-|减法，例如 2–3=-1|
|数学表达式|*|*|*|乘法，例如 2*3=6|
|数学表达式|/|/|/|除法|
|数学表达式|column.op|`column.op(operator)`|`column.op('%')`|取模（余数），例如 5%4=1|
|数学表达式|column.op|`column.op(operator)`|`column.op('^')`|乘方，例如 2.0^3.0=8|
|数学表达式|column.op|`column.op(operator)`|`column.op('!')`|阶乘，例如 5!=120|
|数学表达式|column.op|`column.op(operator)`|`column.op('&')`|按位与，例如 91&15=11|
|数学表达式|column.op|`column.op(operator)`|`column.op('#')`|按位异或，例如 17 # 5=20|
|数学表达式|column.op|`column.op(operator)`|`column.op('~')`|按位非，例如 ~1=-2|
|数学表达式|column.op|`column.op(operator)`|`column.op('&lt;&lt;')`|按位左移，例如 1&lt;&lt;4=16|
|数学表达式|column.op|`column.op(operator)`|`column.op('>>')`|按位右移，例如 8>>2=2|
