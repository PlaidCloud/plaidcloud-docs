---
title: 비교 메서드 (Lakehouse v1)
description: 비교 메서드 — Analyze 식에서 사용할 수 있는 비교 메서드입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/comparisons.md
---

Analyze 식에서 다음 비교 메서드를 사용할 수 있습니다.

|범주&nbsp;&nbsp;&nbsp;&nbsp;|식|구조|예시|설명|
|--------------------------------|----------|---------|-------|-----------|
|일반 사용|>|>|table.column > 23|보다 큼|
|일반 사용|&lt;|&lt;|table.column &lt; 23|보다 작음|
|일반 사용|>=|>=|table.column >= 23|크거나 같음|
|일반 사용|&lt;=|&lt;=|table.column &lt;= 23|작거나 같음|
|일반 사용|==|==|table.column == 23|같음|
|일반 사용|!=|!=|table.column != 23|같지 않음|
|일반 사용|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[추가 예시](../and)|AND SQL 조건을 만듭니다|
|일반 사용|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|열에 SQL ANY() 조건을 적용합니다|
|일반 사용|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|SQL BETWEEN 조건을 적용합니다|
|일반 사용|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|SQL LIKE '%%'를 적용합니다|
|일반 사용|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|SQL LIKE '%%'를 적용합니다|
|일반 사용|FALSE|FALSE|FALSE|False, false, FALSE - Python False의 별칭|
|일반 사용|ilike|ilike|table.column.ilike('%foobar%')|SQL ILIKE 메서드를 적용합니다|
|일반 사용|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|값이 튜플의 값 중 하나인지 테스트합니다|
|일반 사용|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|IS NULL과 같은 경우에 SQL IS를 적용합니다|
|일반 사용|isnot|isnot|table.column.isnot(None)|IS NOT NULL과 같은 경우에 SQL IS를 적용합니다|
|일반 사용|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|SQL LIKE 메서드를 적용합니다|
|일반 사용|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|조건을 반전합니다|
|일반 사용|notilike|notilike|table.column.notilike('%foobar%')|SQL NOT ILIKE 메서드를 적용합니다|
|일반 사용|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|IN 조건을 반전합니다|
|일반 사용|notlike|notlike|table.column.notlike('%foobar%')|SQL NOT LIKE 메서드를 적용합니다|
|일반 사용|NULL|NULL|NULL|Null, null, NULL - Python None의 별칭|
|일반 사용|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[추가 예시](../or)|OR SQL 조건을 만듭니다|
|일반 사용|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|SQL LIKE '%'를 적용합니다|
|일반 사용|TRUE|TRUE|TRUE|True, true, TRUE - Python True의 별칭|	
|수학 식|+|+|+|덧셈, 예: 2+3=5|
|수학 식|–|–|-|뺄셈, 예: 2–3=-1|
|수학 식|*|*|*|곱셈, 예: 2*3=6|
|수학 식|/|/|/|나눗셈|
|수학 식|column.op|`column.op(operator)`|`column.op('%')`|나머지(모듈로), 예: 5%4=1|
|수학 식|column.op|`column.op(operator)`|`column.op('^')`|거듭제곱, 예: 2.0^3.0=8|
|수학 식|column.op|`column.op(operator)`|`column.op('!')`|팩토리얼, 예: 5!=120|
|수학 식|column.op|`column.op(operator)`|`column.op('&')`|비트 AND, 예: 91&15=11|
|수학 식|column.op|`column.op(operator)`|`column.op('#')`|비트 XOR, 예: 17 # 5=20|
|수학 식|column.op|`column.op(operator)`|`column.op('~')`|비트 NOT, 예: ~1=-2|
|수학 식|column.op|`column.op(operator)`|`column.op('&lt;&lt;')`|비트 왼쪽 시프트, 예: 1&lt;&lt;4=16|
|수학 식|column.op|`column.op(operator)`|`column.op('>>')`|비트 오른쪽 시프트, 예: 8>>2=2|
