---
title: Vergleichsmethoden (Lakehouse v2)
description: Vergleichsmethoden – diese Vergleichsmethoden stehen in Analyze-Ausdrücken zur Verfügung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

Diese Vergleichsmethoden stehen in Analyze-Ausdrücken zur Verfügung.

|Kategorie&nbsp;&nbsp;&nbsp;&nbsp;|Ausdruck|Struktur|Beispiel|Beschreibung|
|--------------------------------|----------|---------|-------|-----------|
|Allgemeine Verwendung|>|>|table.column > 23|Größer als|
|Allgemeine Verwendung|&lt;|&lt;|table.column &lt; 23|Kleiner als|
|Allgemeine Verwendung|>=|>=|table.column >= 23|Größer als oder gleich|
|Allgemeine Verwendung|&lt;=|&lt;=|table.column &lt;= 23|Kleiner als oder gleich|
|Allgemeine Verwendung|==|==|table.column == 23|Gleich|
|Allgemeine Verwendung|!=|!=|table.column != 23|Ungleich|
|Allgemeine Verwendung|and_|and_()|and_(table.a > 23, table.b == u'blue')|Erstellt eine SQL-UND-Bedingung (AND)|
|Allgemeine Verwendung|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Wendet die SQL-Bedingung ANY() auf eine Spalte an|
|Allgemeine Verwendung|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Wendet die SQL-Bedingung BETWEEN an|
|Allgemeine Verwendung|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Wendet das SQL-LIKE '%%' an|
|Allgemeine Verwendung|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Wendet das SQL-LIKE '%%' an|
|Allgemeine Verwendung|FALSE|FALSE|FALSE|False, false, FALSE – Alias für Python False|
|Allgemeine Verwendung|ilike|ilike|table.column.ilike('%foobar%')|Wendet die SQL-Methode ILIKE an|
|Allgemeine Verwendung|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Prüft, ob Werte in einem Tupel von Werten enthalten sind|
|Allgemeine Verwendung|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Wendet das SQL-IS an, z. B. für IS NULL|
|Allgemeine Verwendung|isnot|isnot|table.column.isnot(None)|Wendet das SQL-IS an, z. B. für IS NOT NULL|
|Allgemeine Verwendung|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Wendet die SQL-Methode LIKE an|
|Allgemeine Verwendung|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Kehrt die Bedingung um|
|Allgemeine Verwendung|notilike|notilike|table.column.notilike('%foobar%')|Wendet die SQL-Methode NOT ILIKE an|
|Allgemeine Verwendung|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Kehrt die IN-Bedingung um|
|Allgemeine Verwendung|notlike|notlike|table.column.notlike('%foobar%')|Wendet die SQL-Methode NOT LIKE an|
|Allgemeine Verwendung|NULL|NULL|NULL|Null, null, NULL – Alias für Python None|
|Allgemeine Verwendung|or_|or_()|or_(table.a > 23, table.b == u'blue')|Erstellt eine SQL-ODER-Bedingung (OR)|
|Allgemeine Verwendung|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Wendet das SQL-LIKE '%' an|
|Allgemeine Verwendung|TRUE|TRUE|TRUE|True, true, TRUE – Alias für Python True|	
