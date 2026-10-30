---
title: Méthodes de comparaison (Lakehouse v2)
description: Méthodes de comparaison — ces méthodes de comparaison sont disponibles dans les expressions Analyze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/comparisons.md
---

Ces méthodes de comparaison sont disponibles dans les expressions Analyze.

|Catégorie&nbsp;&nbsp;&nbsp;&nbsp;|Expression|Structure|Exemple|Description|
|--------------------------------|----------|---------|-------|-----------|
|Usage général|>|>|table.column > 23|Supérieur à|
|Usage général|&lt;|&lt;|table.column &lt; 23|Inférieur à|
|Usage général|>=|>=|table.column >= 23|Supérieur ou égal à|
|Usage général|&lt;=|&lt;=|table.column &lt;= 23|Inférieur ou égal à|
|Usage général|==|==|table.column == 23|Égal à|
|Usage général|!=|!=|table.column != 23|Différent de|
|Usage général|and_|and_()|and_(table.a > 23, table.b == u'blue')|Crée une condition SQL AND|
|Usage général|any_|any_()|table.column.any(('red', 'blue', 'yellow'))|Applique la condition SQL ANY() à une colonne|
|Usage général|between|between|table.column.between(23, 46)<br><br>get_column(table, 'LAST_CHANGED_DATE').between(\{start_date}, \{end_date})|Applique la condition SQL BETWEEN|
|Usage général|contains|contains|table.column.contains('mno')<br><br>table.SOURCE_SYSTEM.contains('TEST')|Applique le SQL LIKE '%%'|
|Usage général|endswith|endswith|table.column.endswith('xyz')<br><br>table.Parent.endswith(':EBITX')<br><br>table.PERIOD.endswith("01")|Applique le SQL LIKE '%%'|
|Usage général|FALSE|FALSE|FALSE|False, false, FALSE - alias de Python False|
|Usage général|ilike|ilike|table.column.ilike('%foobar%')|Applique la méthode SQL ILIKE|
|Usage général|in_|in_()|table.column.in_((1, 2, 3))<br><br>get_column(table, 'Source Country').in_(['CN','SG','BR'])<br><br>table.MONTH.in_(['01','02','03','04','05','06','07','08','09'])|Teste si les valeurs figurent dans un tuple de valeurs|
|Usage général|is_|is_|table.column.is_(None)<br><br>get_column(table, 'Min SafetyStock').is_(None)<br><br>get_column(table, 'date_pod').is_(None)|Applique le IS SQL, par exemple pour IS NULL|
|Usage général|isnot|isnot|table.column.isnot(None)|Applique le IS SQL, par exemple pour IS NOT NULL|
|Usage général|like|like|table.column.like('%foobar%')<br><br>table.SOURCE_SYSTEM.like('%Adjustments%')|Applique la méthode SQL LIKE|
|Usage général|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))|Inverse la condition|
|Usage général|notilike|notilike|table.column.notilike('%foobar%')|Applique la méthode SQL NOT ILIKE|
|Usage général|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Inverse la condition IN|
|Usage général|notlike|notlike|table.column.notlike('%foobar%')|Applique la méthode SQL NOT LIKE|
|Usage général|NULL|NULL|NULL|Null, null, NULL - alias de Python None|
|Usage général|or_|or_()|or_(table.a > 23, table.b == u'blue')|Crée une condition SQL OR|
|Usage général|startswith|startswith|table.column.startswith('abc')<br><br>get_column(table, 'Zip Code').startswith('9')<br><br>get_column(table1, 'GL Account').startswith('CORP')|Applique le SQL LIKE '%'|
|Usage général|TRUE|TRUE|TRUE|True, true, TRUE - alias de Python True|
