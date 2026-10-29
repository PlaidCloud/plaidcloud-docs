---
title: 比較メソッド（Lakehouse v1）
description: 比較メソッド — Analyze の式で使用できる比較メソッドです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/comparisons.md
---

Analyze の式では、次の比較メソッドを使用できます。

|カテゴリ&nbsp;&nbsp;&nbsp;&nbsp;|式|構造|例|説明|
|--------------------------------|----------|---------|-------|-----------|
|一般的な使用|>|>|table.column > 23|より大きい|
|一般的な使用|&lt;|&lt;|table.column &lt; 23|より小さい|
|一般的な使用|>=|>=|table.column >= 23|以上|
|一般的な使用|&lt;=|&lt;=|table.column &lt;= 23|以下|
|一般的な使用|==|==|table.column == 23|等しい|
|一般的な使用|!=|!=|table.column != 23|等しくない|
|一般的な使用|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[その他の例](../and)|SQL の AND 条件を作成します|
|一般的な使用|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|列に SQL の ANY() 条件を適用します|
|一般的な使用|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|SQL の BETWEEN 条件を適用します|
|一般的な使用|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|SQL の LIKE '%%' を適用します|
|一般的な使用|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|SQL の LIKE '%%' を適用します|
|一般的な使用|FALSE|FALSE|FALSE|False、false、FALSE - Python の False のエイリアスです|
|一般的な使用|ilike|ilike|table.column.ilike('%foobar%')|SQL の ILIKE メソッドを適用します|
|一般的な使用|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|値がタプルに含まれる値のいずれかであるかをテストします|
|一般的な使用|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|IS NULL などで使用する SQL の IS を適用します|
|一般的な使用|isnot|isnot|table.column.isnot(None)|IS NOT NULL などで使用する SQL の IS を適用します|
|一般的な使用|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|SQL の LIKE メソッドを適用します|
|一般的な使用|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|条件を反転します|
|一般的な使用|notilike|notilike|table.column.notilike('%foobar%')|SQL の NOT ILIKE メソッドを適用します|
|一般的な使用|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|IN 条件を反転します|
|一般的な使用|notlike|notlike|table.column.notlike('%foobar%')|SQL の NOT LIKE メソッドを適用します|
|一般的な使用|NULL|NULL|NULL|Null、null、NULL - Python の None のエイリアスです|
|一般的な使用|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[その他の例](../or)|SQL の OR 条件を作成します|
|一般的な使用|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|SQL の LIKE '%' を適用します|
|一般的な使用|TRUE|TRUE|TRUE|True、true、TRUE - Python の True のエイリアスです|	
|数式|+|+|+|加算（例：2+3=5）|
|数式|–|–|-|減算（例：2–3=-1）|
|数式|*|*|*|乗算（例：2*3=6）|
|数式|/|/|/|除算|
|数式|column.op|`column.op(operator)`|`column.op('%')`|剰余（余り）（例：5%4=1）|
|数式|column.op|`column.op(operator)`|`column.op('^')`|べき乗（例：2.0^3.0=8）|
|数式|column.op|`column.op(operator)`|`column.op('!')`|階乗（例：5!=120）|
|数式|column.op|`column.op(operator)`|`column.op('&')`|ビット単位の AND（例：91&15=11）|
|数式|column.op|`column.op(operator)`|`column.op('#')`|ビット単位の XOR（例：17 # 5=20）|
|数式|column.op|`column.op(operator)`|`column.op('~')`|ビット単位の NOT（例：~1=-2）|
|数式|column.op|`column.op(operator)`|`column.op('&lt;&lt;')`|ビット単位の左シフト（例：1&lt;&lt;4=16）|
|数式|column.op|`column.op(operator)`|`column.op('>>')`|ビット単位の右シフト（例：8>>2=2）|
