---
title: 比較メソッド (Lakehouse v2)
description: 比較メソッド — Analyze の式で使用できる比較メソッドです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

Analyze の式では、次の比較メソッドを使用できます。

|カテゴリー&nbsp;&nbsp;&nbsp;&nbsp;|式|構造|例|説明|
|--------------------------------|----------|---------|-------|-----------|
|一般的な用途|>|>|table.column > 23|より大きい|
|一般的な用途|&lt;|&lt;|table.column &lt; 23|より小さい|
|一般的な用途|>=|>=|table.column >= 23|以上|
|一般的な用途|&lt;=|&lt;=|table.column &lt;= 23|以下|
|一般的な用途|==|==|table.column == 23|等しい|
|一般的な用途|!=|!=|table.column != 23|等しくない|
|一般的な用途|and_|and_()|and_(table.a > 23, table.b == u'blue')|AND の SQL 条件を作成します|
|一般的な用途|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|列に SQL の ANY() 条件を適用します|
|一般的な用途|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|SQL の BETWEEN 条件を適用します|
|一般的な用途|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|SQL の LIKE '%%' を適用します|
|一般的な用途|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|SQL の LIKE '%%' を適用します|
|一般的な用途|FALSE|FALSE|FALSE|False、false、FALSE - Python の False の別名です|
|一般的な用途|ilike|ilike|table.column.ilike('%foobar%')|SQL の ILIKE メソッドを適用します|
|一般的な用途|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|値がタプルの値のいずれかに含まれるかどうかをテストします|
|一般的な用途|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|IS NULL のような場合に、SQL の IS を適用します|
|一般的な用途|isnot|isnot|table.column.isnot(None)|IS NOT NULL のような場合に、SQL の IS を適用します|
|一般的な用途|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|SQL の LIKE メソッドを適用します|
|一般的な用途|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|条件を反転します|
|一般的な用途|notilike|notilike|table.column.notilike('%foobar%')|SQL の NOT ILIKE メソッドを適用します|
|一般的な用途|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|IN 条件を反転します|
|一般的な用途|notlike|notlike|table.column.notlike('%foobar%')|SQL の NOT LIKE メソッドを適用します|
|一般的な用途|NULL|NULL|NULL|Null、null、NULL - Python の None の別名です|
|一般的な用途|or_|or_()|or_(table.a > 23, table.b == u'blue')|OR の SQL 条件を作成します|
|一般的な用途|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|SQL の LIKE '%' を適用します|
|一般的な用途|TRUE|TRUE|TRUE|True、true、TRUE - Python の True の別名です|	
