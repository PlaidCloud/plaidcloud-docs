---
title: 比较方法（Lakehouse v2）
description: 比较方法：以下比较方法可用于 Analyze 表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

以下比较方法可用于 Analyze 表达式。

|类别&nbsp;&nbsp;&nbsp;&nbsp;|表达式|结构|示例|说明|
|--------------------------------|----------|---------|-------|-----------|
|常规用法|>|>|table.column > 23|大于|
|常规用法|&lt;|&lt;|table.column &lt; 23|小于|
|常规用法|>=|>=|table.column >= 23|大于或等于|
|常规用法|&lt;=|&lt;=|table.column &lt;= 23|小于或等于|
|常规用法|==|==|table.column == 23|等于|
|常规用法|!=|!=|table.column != 23|不等于|
|常规用法|and_|and_()|and_(table.a > 23, table.b == u'blue')|创建 AND SQL 条件|
|常规用法|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|对列应用 SQL ANY() 条件|
|常规用法|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|应用 SQL BETWEEN 条件|
|常规用法|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|应用 SQL LIKE '%%'|
|常规用法|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|应用 SQL LIKE '%%'|
|常规用法|FALSE|FALSE|FALSE|False、false、FALSE：Python False 的别名|
|常规用法|ilike|ilike|table.column.ilike('%foobar%')|应用 SQL ILIKE 方法|
|常规用法|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|测试值是否在元组包含的值之中|
|常规用法|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|应用 SQL 的 IS，用于 IS NULL 等场景|
|常规用法|isnot|isnot|table.column.isnot(None)|应用 SQL 的 IS，用于 IS NOT NULL 等场景|
|常规用法|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|应用 SQL LIKE 方法|
|常规用法|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|反转条件|
|常规用法|notilike|notilike|table.column.notilike('%foobar%')|应用 SQL NOT ILIKE 方法|
|常规用法|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|反转 IN 条件|
|常规用法|notlike|notlike|table.column.notlike('%foobar%')|应用 SQL NOT LIKE 方法|
|常规用法|NULL|NULL|NULL|Null、null、NULL：Python None 的别名|
|常规用法|or_|or_()|or_(table.a > 23, table.b == u'blue')|创建 OR SQL 条件|
|常规用法|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|应用 SQL LIKE '%'|
|常规用法|TRUE|TRUE|TRUE|True、true、TRUE：Python True 的别名|
