---
title: Comparison Methods
---

These comparison methods are available in Analyze expressions.

|Category&nbsp;&nbsp;&nbsp;&nbsp;|Expression|Structure|Example|Description|
|-----------|----------|---------|-------|-----------|
|General Usage|>|>|table.column > 23|Greater Than|
|General Usage|<|<|table.column < 23|Less Than|
|General Usage|>=|>=|table.column >= 23|Greater than or equal to|
|General Usage|<=|<=|table.column <= 23|Less than or equal to|
|General Usage|==|==|table.column == 23|Equal to|
|General Usage|!=|!=|table.column != 23|Not Equal to|
|General Usage|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[Additional Examples](../and)|Creates an AND SQL condition|
|General Usage|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Applies the SQL ANY() condition to a column|
|General Usage|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between({start_date}, {end_date})|Applies the SQL BETWEEN condition|
|General Usage|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Applies the SQL LIKE '%%'|
|General Usage|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Applies the SQL LIKE '%%'|
|General Usage|FALSE|FALSE|FALSE|False, false, FALSE - Alias for Python False|
|General Usage|ilike|ilike|table.column.ilike('%foobar%')|Applies the SQL ILIKE method|
|General Usage|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Test if values are with a tuple of values|
|General Usage|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Applies the SQL is the IS for things like IS NULL|
|General Usage|isnot|isnot|table.column.isnot(None)|Applies the SQL is the IS for things like IS NOT NULL|
|General Usage|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Applies the SQL LIKE method|
|General Usage|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Inverts the condition|
|General Usage|notilike|notilike|table.column.notilike('%foobar%')|Applies the SQL NOT ILIKE method|
|General Usage|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Inverts the IN condition|
|General Usage|notlike|notlike|table.column.notlike('%foobar%')|Applies the SQL NOT LIKE method|
|General Usage|NULL|NULL|NULL|Null, null, NULL - Alias for Python None|
|General Usage|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[Additional Examples](../or)|Creates an OR SQL condition|
|General Usage|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Applies the SQL LIKE '%'|
|General Usage|TRUE|TRUE|TRUE|True, true, TRUE - Alias for Python True|	
|Math Expressions|+|+|+|2+3=5|addition|
|Math Expressions|–|–|-|2–3=-1|subtraction|
|Math Expressions|*|*|*|2*3=6|multiplication|
|Math Expressions|/|/|/|4/2=2|division (integer division truncates results)|
|Math Expressions|column.op|column.op(operator)|column.op('%')|5%4=1|modulo (remainder)|
|Math Expressions|column.op|column.op(operator)|column.op('^')|2.0^3.0=8|exponentiation|
|Math Expressions|column.op|column.op(operator)|column.op('!')|5!=120|factorial|
|Math Expressions|column.op|column.op(operator)|column.op('!!')|!!5=120|factorial (prefix operator)|
|Math Expressions|column.op|column.op(operator)|column.op('@')|@-5.0=5|absolute value|
|Math Expressions|column.op|column.op(operator)|column.op('&')|91&15=11|bitwise AND|
|Math Expressions|column.op|column.op(operator)|column.op('#')|17##5=20|bitwise XOR|
|Math Expressions|column.op|column.op(operator)|column.op('~')|~1=-2|bitwise NOT|
|Math Expressions|column.op|column.op(operator)|column.op('<<')|1<<4=16|bitwise shift left|
|Math Expressions|column.op|column.op(operator)|column.op('>>')|8>>2=2|bitwise shift right|
