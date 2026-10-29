---
title: Metody porównania (Lakehouse v1)
description: Metody porównania — te metody porównania są dostępne w wyrażeniach Analyze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/comparisons.md
---

Te metody porównania są dostępne w wyrażeniach Analyze.

|Kategoria&nbsp;&nbsp;&nbsp;&nbsp;|Wyrażenie|Struktura|Przykład|Opis|
|--------------------------------|----------|---------|-------|-----------|
|Zastosowanie ogólne|>|>|table.column > 23|Większe niż|
|Zastosowanie ogólne|&lt;|&lt;|table.column &lt; 23|Mniejsze niż|
|Zastosowanie ogólne|>=|>=|table.column >= 23|Większe lub równe|
|Zastosowanie ogólne|&lt;=|&lt;=|table.column &lt;= 23|Mniejsze lub równe|
|Zastosowanie ogólne|==|==|table.column == 23|Równe|
|Zastosowanie ogólne|!=|!=|table.column != 23|Różne od|
|Zastosowanie ogólne|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[Dodatkowe przykłady](../and)|Tworzy warunek SQL AND|
|Zastosowanie ogólne|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Stosuje warunek SQL ANY() do kolumny|
|Zastosowanie ogólne|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Stosuje warunek SQL BETWEEN|
|Zastosowanie ogólne|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Stosuje SQL LIKE '%%'|
|Zastosowanie ogólne|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Stosuje SQL LIKE '%%'|
|Zastosowanie ogólne|FALSE|FALSE|FALSE|False, false, FALSE — alias wartości False z Pythona|
|Zastosowanie ogólne|ilike|ilike|table.column.ilike('%foobar%')|Stosuje metodę SQL ILIKE|
|Zastosowanie ogólne|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Sprawdza, czy wartość należy do krotki wartości|
|Zastosowanie ogólne|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Stosuje operator SQL IS, na przykład dla IS NULL|
|Zastosowanie ogólne|isnot|isnot|table.column.isnot(None)|Stosuje operator SQL IS, na przykład dla IS NOT NULL|
|Zastosowanie ogólne|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Stosuje metodę SQL LIKE|
|Zastosowanie ogólne|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Odwraca warunek|
|Zastosowanie ogólne|notilike|notilike|table.column.notilike('%foobar%')|Stosuje metodę SQL NOT ILIKE|
|Zastosowanie ogólne|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Odwraca warunek IN|
|Zastosowanie ogólne|notlike|notlike|table.column.notlike('%foobar%')|Stosuje metodę SQL NOT LIKE|
|Zastosowanie ogólne|NULL|NULL|NULL|Null, null, NULL — alias wartości None z Pythona|
|Zastosowanie ogólne|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[Dodatkowe przykłady](../or)|Tworzy warunek SQL OR|
|Zastosowanie ogólne|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Stosuje SQL LIKE '%'|
|Zastosowanie ogólne|TRUE|TRUE|TRUE|True, true, TRUE — alias wartości True z Pythona|	
|Wyrażenia matematyczne|+|+|+|dodawanie, np. 2+3=5|
|Wyrażenia matematyczne|–|–|-|odejmowanie, np. 2–3=-1|
|Wyrażenia matematyczne|*|*|*|mnożenie, np. 2*3=6|
|Wyrażenia matematyczne|/|/|/|dzielenie|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('%')`|modulo (reszta z dzielenia), np. 5%4=1|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('^')`|potęgowanie, np. 2.0^3.0=8|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('!')`|silnia, np. 5!=120|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('&')`|bitowe AND, np. 91&15=11|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('#')`|bitowe XOR, np. 17 # 5=20|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('~')`|bitowe NOT, np. ~1=-2|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('&lt;&lt;')`|przesunięcie bitowe w lewo, np. 1&lt;&lt;4=16|
|Wyrażenia matematyczne|column.op|`column.op(operator)`|`column.op('>>')`|przesunięcie bitowe w prawo, np. 8>>2=2|
