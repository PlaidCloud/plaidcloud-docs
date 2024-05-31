---
title: Expression Library
slug: Expression_Library
weight: 1.0
description: A reference library of all expressions that can be used in PlaidCloud
date: 2022-06-07T07:39:48
---

## Description

An expression is a basic function that does a conversion, calculation, cast to another data type, or other action on data in a column or in a dashboard chart object. Examples are `startswith`, `max`, or `current_date`. PlaidCloud expressions are based on PostgreSQL. For a more in depth tutorial or reference guide, please see: [tutorial](https://www.postgresqltutorial.com/)

There are three primary areas to apply expressions - metrics and calculated columns in datasets, and chart objects in dashboards.

## Navigating to a dataset
In order to view and edit metrics and calculated expressions:
1.  Sign into plaidcloud.com and navigate to Dasboards. Select the dashboard you want to work in.
2.  Select Data > Datasets from the menu.
3.  Search for a dataset to view or modify
4.  Hover over the dataset with the cursor and you will see icons in the actions column.
5.  Click the `edit` icon beneath `Actions`

## Viewing a chart object and adding an expression
You can add expressions to chart objects on a dashboard. For example, if you want to add an expression to a table object (a calculated column), you can:
1. Open the chart object by opening a dashboard, clicking on the three dot icon, and selecting "View chart in Explore".
2. Now that you are editing the chart, you can add a new Dimension or Metric, and do a `SIMPLE` expression, or a `CUSTOM SQL` expression

Now that you have located where you want to add an expression, you can use the table below as a guide to determining what expression you are looking for.<br><br>

|Category&nbsp;&nbsp;&nbsp;&nbsp;|Expression|Structure|Example|Description|
|-----------|----------|---------|-------|-----------|
|Conditional|case|case((expression, truevalue), else_ = falsevalue)|case((table.first_name.isnot(None), func.concat(table.first_name, table.last_name)), else_ = table.last_name)<br>[Additional Examples](#case-examples)|a switch or a conditional control structure that allows the program to evaluate an expression and perform different actions based on the value of that expression|
|Conditional|coalesce|func.coalesce(column1, column2, ...)|func.coalesce(table.nickname, table.first_name)<br>[Additional Examples](#coalesce-examples)|Returns the first non-null value in a set of columns. In the example, if there is a nickname it returns that, otherwise it returns the first name.|
|Conversion|cast|func.cast(value, datatype)|func.cast(123, Text)<br>[Additional Examples](#func-cast-type-conversions)|Converts the value to a specific data type. In the example, it takes an Integer (123) and returns it as a string "123".|
|Conversion|to_char|func.to_char(timestamp, text)<br>[See More](#func-to-data-type-conversions)|func.to_char(current_timestamp, 'HH12:MI:S S')<br>[Additional Examples](#func-to-data-type-conversions)|Converts an object type to a char (text). In the example, it converts a timestamp to text|
|Conversion|to_date|func.to_date(text, format)|func.to_date(table.Created_on, 'DD-MM-YYYY')|Convert a text field into a date formatted how you like|
|Conversion|to_number|func.to_number(text, format)|func.to_number ('12,454.8 -', '99G999D9S')|Convert a string to a numeric value|
|Conversion|to_timestamp|func.to_timestamp(text, format)<br>[See More](#func-to-data-type-conversions)|func.to_timestamp('05 Dec 2000', 'DD Mon YYYY')<br>[Additional Examples](#func-to-data-type-conversions)|Convert a string to a timestamp|
|Time|age|func.age(timestamp, timestamp)|age(timestamp ‘2001-04-1 0’, timestamp ‘1957-06-1 3’)=43 years 9 months 27 days|Subtracts the second timestamp from the first one and returns an interval as a result|
|Time|age|func.age(timestamp)|age(timestamp ‘1957-06-1 3’)=43 years 8 months 3 days|Returns the interval between the current date and the argument provided|
|Time|clock_timestamp|func.clock_timestamp()|func.clock_timestamp()|Returns a timestamp for the current date and time which changes during execution|
|Time|current_date|func.current_date()|func.current_date()<br><br>get_column(table, 'Created On')>=(func.current_date()-120)|Returns the a date object with the current date|
|Time|current_time|func.current_time()|func.current_time()|Returns a time object with the current time and timezone|
|Time|current_timestamp|func.current_timestamp()|func.current_timestamp()|Returns a timestamp object with the current date and time at the beginning of execution|
|Time|date_part|func.date_part(text, timestamp)|func.date_part('hour', timestamp '2001-02-1 6 20:38:40')=20|Returns the part of the timestamp you are looking for (month, year, etc.)<br>[See more options](#date-and-time-formatting)|
|Time|date_part|func.date_part(text, interval)|func.date_part('month', interval '2 years 3 months')=3|Returns the part of the interval you are looking for (month, year, etc.)<br>[See more options](#date-and-time-formatting)|
|Time|date_trunc|func.date_trunc(text, timestamp)|func.date_trunc('hour', timestamp '2001-02-1 6 20:38:40')=36938.8333333333<br>[Additional Examples](#other-date-time-examples)|Truncate to specified precision|
|Time|extract|func.extract(field from timestamp)|func.extract(hour from timestamp '2001-02-1 6 20:38:40')=20|Get a field of a timestamp or an interval e.g., year, month, day, etc.|
|Time|extract|func.extract(field from interval)|func.extract(month from interval '2 years 3 months')=3|Get a field of a timestamp or an interval e.g., year, month, day, etc.|
|Time|isfinite|func.isfinite(timestamp)|func.isfinite(timestamp '2001-02-1 6 21:28:30')=TRUE|Check if a date, a timestamp, or an interval is finite or not (not +/-infinity)|
|Time|isfinite|func.isfinite(interval)|func.isfinite(interval '4 hours')=TRUE|Check if a date, a timestamp, or an interval is finite or not (not +/-infinity)|
|Time|justify_days|func.justify_days(interval)|func.justify_days(interval '30 days')=1 month|Adjust interval so 30-day time periods are represented as months|
|Time|justify_hours|func.justify_hours(interval)|func.justify_hours(interval '24 hours')=1 day|Adjust interval so 24-hour time periods are represented as days|
|Time|justify_interval|func.justify_interval(interval)|func.justify_interval(interval '1 mon -1 hour')=29 days 23:00:00|Adjust interval using justify_days and justify_hours, with additional sign adjustments|
|Time|now|func.now()|func.now()|Return the date and time with time zone at which the current transaction start|		
|Time|statement_timestamp|func.statement_timestamp()|func.statement_timestamp()|Return the current date and time at which the current statement executes|		
|Time|timeofday|func.timeofday()|func.timeofday()|Return the current date and time, like clock_timestamp, as a text string|
|Time|transaction_timestamp|func.transaction_timestamp()|func.transaction_timestamp()|Return the date and time with time zone at which the current transaction start|
|General Usage|>|>|table.column > 23|Greater Than|
|General Usage|<|<|table.column < 23|Less Than|
|General Usage|>=|>=|table.column >= 23|Greater than or equal to|
|General Usage|<=|<=|table.column <= 23|Less than or equal to|
|General Usage|==|==|table.column == 23|Equal to|
|General Usage|!=|!=|table.column != 23|Not Equal to|
|General Usage|and_|and_()|and_(table.a > 23, table.b == u'blue')<br>[Additional Examples](#and-operator)|Creates an AND SQL condition|
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
|General Usage|not_|not_()|not_(and_(table.a > 23, table.b == u'blue'))<br>[Additional Examples](#not-operator)|Inverts the condition|
|General Usage|notilike|notilike|table.column.notilike('%foobar%')|Applies the SQL NOT ILIKE method|
|General Usage|notin|notin|table.column.notin((1, 2, 3))<br><br>table.LE.notin_(['12345','67890'])|Inverts the IN condition|
|General Usage|notlike|notlike|table.column.notlike('%foobar%')|Applies the SQL NOT LIKE method|
|General Usage|NULL|NULL|NULL|Null, null, NULL - Alias for Python None|
|General Usage|or_|or_()|or_(table.a > 23, table.b == u'blue')<br>[Additional Examples](#or-operator)|Creates an OR SQL condition|
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
|Math Functions|abs|func.abs(x)|abs(-17.4)=17.4<br><br>func.abs(get_column(table, 'RPA Value'))|absolute value (return type: Same as input)|	
|Math Functions|cbrt|func.cbrt(dp)|cbrt(27.0)=3|cube root (return type: Big Float)|
|Math Functions|ceil|func.ceil(dp or numeric)|ceil(-42.8)=-42<br><br>func.ceil(func.extract('seconds', table.OutlierTime) / 60)|smallest integer not less than argument (return type: Same as input)|	
|Math Functions|ceiling|func.ceiling(dp or numeric)|ceiling(-95.3)=-95|smallest integer not less than argument (return type: Same as input)|
|Math Functions|degrees|func.degrees(dp)|degrees(0.5)=28.6478897565412|radians to degrees (return type: Big Float)|
|Math Functions|exp|func.exp(dp or numeric)|exp(1.0)=2.71828182845905|exponential (return type: Same as input)|
|Math Functions|floor|func.floor(dp or numeric)|floor(-42.8)=-43|largest integer not greater than argument (return type: Same as input)|	
|Math Functions|greatest|func.greatest(value …)||Select the largest value from a list. NULL values in the list are ignored. The result will be NULL only if all values are NULL. (return type: Same as input)|
|Math Functions|least|func.least(value…)||Select the smallest value from a list. NULL values in the list are ignored. The result will be NULL only if all values are NULL. (return type: Same as input)|
|Math Functions|ln|func.ln(dp or numeric)|ln(2.0)=0.693147180559945|natural logarithm (return type: Same as input)|	
|Math Functions|log|func.log(dp or numeric)|log(100.0)=2|base 10 logarithm (return type: Same as input)|	
|Math Functions|log|func.log(b numeric, x numeric)|log(2.0,64.0)=6|logarithm to base b (return type: Numeric)|	
|Math Functions|mod|func.mod(y, x)|mod(9,4)=1|remainder of y/x (return type: Same as input)|	
|Math Functions|pi|func.pi()|pi()=3.14159265358979|“π” constant (return type: Big Float)|
|Math Functions|power|func.power(a dp, b dp)|power(9.0,3.0)=729|a raised to the power of b (return type: Big Float)|
|Math Functions|power|func.power(a numeric, b numeric)|power(9.0,3.0)=729|a raised to the power of b (return type: Numeric)|
|Math Functions|radians|func.radians(dp)|radians(4 5.0)=0.785398163397448|degrees to radians (return type: Big Float)|
|Math Functions|random|func.random()|random()|random value in the range 0.0 <= x < 1.0 (return type: Big Float)|
|Math Functions|round|func.round(dp or numeric)|round(42.4)=42|round to nearest integer (return type: Same as input)|
|Math Functions|round|func.round(v numeric, s int)|round(42.4382, 2)=42.44<br><br>func.round(table.RATE, 5)<br><br>func.round((get_column(table, 'Order Quantity')/3), 0)|round to s decimal places (return type: Numeric)|
|Math Functions|safe_divide|func.safe_divide(numerator numeric, denominator numeric, divide_by_zero_value)|func.safe_divide(get_column(table, 'VALUE__MC'), table.RATE, 0.0)<br><br>func.safe_divide(get_column(table, 'Total_Weight'), (table.PickHours + table.BreakHours), 0.00)|Equivalent to the division operator (X / Y), but returns NULL if an error occurs, such as a division by zero error|
|Math Functions|setseed|func.setseed(dp)|setseed(0 .54823)=1177314959|set seed for subsequent random() calls (value between 0 and 1.0) (return type: Integer)|
|Math Functions|sign|func.sign(dp or numeric)|sign(-8.4)=-1|sign of the argument (-1, 0, +1) (return type: Same as input)|
|Math Functions|sqrt|func.sqrt(dp or numeric)|sqrt(2.0)=1.4142135623731|square root (return type: Same as input)|
|Math Functions|trunc|func.trunc(dp or numeric)|trunc(42. 8)=42|truncate toward zero (return type: Same as input)|
|Math Functions|trunc|func.trunc(v numeric, s int)|trunc(42.4382, 2)=42.43|truncate to s decimal places (return type: Numeric)|	
|Math Functions|width_bucket|func.width_bucket( op numeric, b1 numeric, b2 numeric, count int)|width_bucket(5.35, 0.024, 10.06, 5)=3|return the bucket to which operand would be assigned in an equidepth histogram with count buckets, in the range b1 to b2 (return type: Integer)|
|Math Trig|acos|func.acos(x)||inverse cosine|
|Math Trig|asin|func.asin(x)||inverse sine|
|Math Trig|atan|func.atan(x)||inverse tangent|
|Math Trig|atan2|func.atan2(x,y)||inverse tangent of x/y|
|Math Trig|cos|func.cos(x)||cosine|
|Math Trig|cot|func.cot(x)||cotangent|
|Math Trig|sin|func.sin(x)||sine|
|Math Trig|tan|func.tan(x)||tangent|
|Geometry / PostGIS|ST_3DMakeBox|box3d ST_3DMakeBox(geometry point3DLowLeftBottom, geometry point3DUpRightTop);|[Example](https://postgis.net/docs/manual-2.2/ST_3DMakeBox.html)|Creates a BOX3D defined by the given 3d point geometries.|
|Geometry / PostGIS|ST_BdMPolyFromText|geometry ST_BdMPolyFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_BdMPolyFromText.html)|Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString text representation Well-Known text representation.|
|Geometry / PostGIS|ST_BdPolyFromText|geometry ST_BdPolyFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_BdPolyFromText.html)|Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString Well-Known text representation.|
|Geometry / PostGIS|ST_Box2dFromGeoHash|box2d ST_Box2dFromGeoHash(text geohash, integer precision=full_precision_of_geohash);|[Example](https://postgis.net/docs/manual-2.2/ST_Box2dFromGeoHash.html)|Return a BOX2D from a GeoHash string.|
|Geometry / PostGIS|ST_GeogFromText|geography ST_GeogFromText(text EWKT);|[Example](https://postgis.net/docs/manual-2.2/ST_GeogFromText.html)|Return a specified geography value from Well-Known Text representation or extended (WKT).|
|Geometry / PostGIS|ST_GeogFromWKB|geography ST_GeogFromWKB(bytea wkb);|[Example](https://postgis.net/docs/manual-2.2/ST_GeogFromWKB.html)|Creates a geography instance from a Well-Known Binary geometry representation (WKB) or extended Well Known Binary (EWKB).|
|Geometry / PostGIS|ST_GeographyFromText|geography ST_GeographyFromText(text EWKT);|[Example](https://postgis.net/docs/manual-2.2/ST_GeographyFromText.html)|Return a specified geography value from Well-Known Text representation or extended (WKT).|
|Geometry / PostGIS|ST_GeomCollFromText|geometry ST_GeomCollFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomCollFromText.html)|Makes a collection Geometry from collection WKT with the given SRID. If SRID is not given, it defaults to 0.|
|Geometry / PostGIS|ST_GeometryFromText|geometry ST_GeometryFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeometryFromText.html)|Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText|
|Geometry / PostGIS|ST_GeomFromEWKB|geometry ST_GeomFromEWKB(bytea EWKB);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromEWKB.html)|Return a specified ST_Geometry value from Extended Well-Known Binary representation (EWKB).|
|Geometry / PostGIS|ST_GeomFromEWKT|geometry ST_GeomFromEWKT(text EWKT);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromEWKT.html)|Return a specified ST_Geometry value from Extended Well-Known Text representation (EWKT).|
|Geometry / PostGIS|ST_GeomFromGeoHash|geometry ST_GeomFromGeoHash(text geohash, integer precision=full_precision_of_geohash);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromGeoHash.html)|Return a geometry from a GeoHash string.|
|Geometry / PostGIS|ST_GeomFromGML|geometry ST_GeomFromGML(text geomgml, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromGML.html)|Takes as input GML representation of geometry and outputs a PostGIS geometry object|
|Geometry / PostGIS|ST_GeomFromGML|geometry ST_GeomFromGML(text geomgml, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromGML.html)|Takes as input GML representation of geometry and outputs a PostGIS geometry object|
|Geometry / PostGIS|ST_GeomFromKML|geometry ST_GeomFromKML(text geomkml);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromKML.html)|Takes as input KML representation of geometry and outputs a PostGIS geometry object|
|Geometry / PostGIS|ST_GeomFromText|geometry ST_GeomFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromText.html)|Return a specified ST_Geometry value from Well-Known Text representation (WKT).|
|Geometry / PostGIS|ST_GeomFromWKB|geometry ST_GeomFromWKB(bytea geom, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GeomFromWKB.html)|Creates a geometry instance from a Well-Known Binary geometry representation (WKB) and optional SRID.|
|Geometry / PostGIS|ST_GMLToSQL|geometry ST_GMLToSQL(text geomgml, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_GMLToSQL.html)|Return a specified ST_Geometry value from GML representation. This is an alias name for ST_GeomFromGML|
|Geometry / PostGIS|ST_LineFromEncodedPolyline|geometry ST_LineFromEncodedPolyline(text polyline, integer precision=5);|[Example](https://postgis.net/docs/manual-2.2/ST_LineFromEncodedPolyline.html)|Creates a LineString from an Encoded Polyline.|
|Geometry / PostGIS|ST_LineFromMultiPoint|geometry ST_LineFromMultiPoint(geometry aMultiPoint);|[Example](https://postgis.net/docs/manual-2.2/ST_LineFromMultiPoint.html)|Creates a LineString from a MultiPoint geometry.|
|Geometry / PostGIS|ST_LineFromText|geometry ST_LineFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_LineFromText.html)|Makes a Geometry from WKT representation with the given SRID. If SRID is not given, it defaults to 0.|
|Geometry / PostGIS|ST_LineFromWKB|geometry ST_LineFromWKB(bytea WKB, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_LineFromWKB.html)|Makes a LINESTRING from WKB with the given SRID|
|Geometry / PostGIS|ST_LinestringFromWKB|geometry ST_LinestringFromWKB(bytea WKB, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_LinestringFromWKB.html)|Makes a geometry from WKB with the given SRID.|
|Geometry / PostGIS|ST_MakeBox2D|box2d ST_MakeBox2D(geometry pointLowLeft, geometry pointUpRight);|[Example](https://postgis.net/docs/manual-2.2/ST_MakeBox2D.html)|Creates a BOX2D defined by the given point geometries.|
|Geometry / PostGIS|ST_MakeEnvelope|geometry ST_MakeEnvelope(double precision xmin, double precision ymin, double precision xmax, double precision ymax, integer srid=unknown);|[Example](https://postgis.net/docs/manual-2.2/ST_MakeEnvelope.html)|Creates a rectangular Polygon formed from the given minimums and maximums. Input values must be in SRS specified by the SRID|
|Geometry / PostGIS|ST_MakeLine|geometry ST_MakeLine(geometry geom1, geometry geom2);|[Example](https://postgis.net/docs/manual-2.2/ST_MakeLine.html)|Creates a Linestring from point or line geometries.|
|Geometry / PostGIS|ST_MakePoint|geometry ST_MakePoint(double precision x, double precision y, double precision z, double precision m);|[Example](https://postgis.net/docs/manual-2.2/ST_MakePoint.html)|Creates a 2D,3DZ or 4D point geometry.|
|Geometry / PostGIS|ST_MakePointM|geometry ST_MakePointM(float x, float y, float m);|[Example](https://postgis.net/docs/manual-2.2/ST_MakePointM.html)|Creates a point geometry with an x, y, and m coordinate.|
|Geometry / PostGIS|ST_MakePolygon|geometry ST_MakePolygon(geometry outerlinestring, geometry[] interiorlinestrings);|[Example](https://postgis.net/docs/manual-2.2/ST_MakePolygon.html)|Creates a Polygon formed by the given shell. Input geometries must be closed LINESTRINGS.|
|Geometry / PostGIS|ST_MLineFromText|geometry ST_MLineFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_MLineFromText.html)|Return a specified ST_MultiLineString value from WKT representation.|
|Geometry / PostGIS|ST_MPointFromText|geometry ST_MPointFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_MPointFromText.html)|Makes a Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0.|
|Geometry / PostGIS|ST_MPolyFromText|geometry ST_MPolyFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_MPolyFromText.html)|Makes a MultiPolygon Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0.|
|Geometry / PostGIS|ST_Point|geometry ST_Point(float x_lon, float y_lat);|[Example](https://postgis.net/docs/manual-2.2/ST_Point.html)|Returns an ST_Point with the given coordinate values. OGC alias for ST_MakePoint.|
|Geometry / PostGIS|ST_PointFromGeoHash|point ST_PointFromGeoHash(text geohash, integer precision=full_precision_of_geohash);|[Example](https://postgis.net/docs/manual-2.2/ST_PointFromGeoHash.html)|Return a point from a GeoHash string.|
|Geometry / PostGIS|ST_PointFromText|geometry ST_PointFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_PointFromText.html)|Makes a point Geometry from WKT with the given SRID. If SRID is not given, it defaults to unknown.|
|Geometry / PostGIS|ST_PointFromWKB|geometry ST_GeomFromWKB(bytea geom, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_PointFromWKB.html)|Makes a geometry from WKB with the given SRID|
|Geometry / PostGIS|ST_Polygon|geometry ST_Polygon(geometry aLineString, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_Polygon.html)|Returns a polygon built from the specified linestring and SRID.|
|Geometry / PostGIS|ST_PolygonFromText|geometry ST_PolygonFromText(text WKT, integer srid);|[Example](https://postgis.net/docs/manual-2.2/ST_PolygonFromText.html)|Makes a Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0.|
|Geometry / PostGIS|ST_WKBToSQL|geometry ST_WKBToSQL(bytea WKB);|[Example](https://postgis.net/docs/manual-2.2/ST_WKBToSQL.html)|Return a specified ST_Geometry value from Well-Known Binary representation (WKB). This is an alias name for ST_GeomFromWKB that takes no srid|
|Geometry / PostGIS|ST_WKTToSQL|geometry ST_WKTToSQL(text WKT);|[Example](https://postgis.net/docs/manual-2.2/ST_WKTToSQL.html)|Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText|
|Text Expression|ascii|func.ascii(string) returns int|ascii('x')=120<br><br>func.ascii(get_column(table, 'TAX_SEGMENT'))|ASCII code of the first byte of the argument|
|Text Expression|bit_length|func.bit_length(string) returns int|bit_length('jose')=32|Number of bits in string|	
|Text Expression|btrim|func.btrim(string text [, characters text]) returns Text|btrim('xyx johnyyx', 'xy')=john|Remove the longest string consisting only of characters in characters (a space by default) from the start and end of string|
|Text Expression|char_length|func.char_length(string) or func.character_length(string) returns int|char_leng th('jose')=4|Number of characters in string|
|Text Expression|chr|func.chr(int) returns Text|chr(65)=A|Character with the given ASCII code|
|Text Expression|concat|func.concat(string, string) returns Text|concat('Post', 'greSQL')=PostgreSQL<br><br>func.concat(table.YEAR,'_', table.PERIOD)|String concatenation|
|Text Expression|convert|func.convert(string text, [src_encoding name,]dest_encoding name)|convert('text_in_utf8', 'UTF8', 'LATIN1')=text_in_utf8 represented in ISO 8859-1 encoding|Convert string to dest_encoding. The original encoding is specified by src_encoding. If src_encoding is omitted, database encoding is assumed.|
|Text Expression|convert|func.convert(string using conversion_name)|convert('PostgreSQL' using iso_8859_1_to_utf8)|Change encoding using specified conversion name. Conversions can be defined by CREATE CONVERSION. Also there are some pre-defined conversion names. See [here](https://www.postgresql.org/docs/8.2/functions-string.html#CONVERSION-NAMES) for available conversion names.|
|Text Expression|decode|func.decode(string text, type text)||Decode binary data from string previously encoded with encode. Parameter type is same as in encode.		
|Text Expression|initcap|func.initcap(string) returns Text|initcap('hi THOMAS')=Hi Thomas|Convert the first letter of each word to uppercase and the rest to lowercase. Words are sequences of alphanumeric characters separated by non-alphanumeric characters|
|Text Expression|integerize_truncate|func.integerize_truncate(string)|func.integerize_truncate('30.66')=30|Takes a single numeric argument x and returns a numeric vector containing the integers formed by truncating the values in x toward 0|
|Text Expression|integerize_round|func.integerize_round(string)|func.integerize_round('30.66') --> 31|Rounds the values in its first argument to the specified number of decimal places|
|Text Expression|length|func.length(string) returns int|length('jose')=4<br><br>func.length(get_column(table, 'arrival_date_actual'))|Number of characters in string|
|Text Expression|lower|func.lower(string) returns Text|lower('TOM ')=tom|Convert string to lower case|
|Text Expression|lpad|func.lpad(string text, length int [, fill text]) returns Text|lpad('hi', 5, 'xy')=xyxhi<br><br>func.lpad('stringtofillup', 10, 'X')=stringtofi|Fill up the string to length length by prepending the characters fill (a space by default). If the string is already longer than length then it is truncated (on the right)|
|Text Expression|ltrim|func.ltrim(string text [, characters text]) returns Text|ltrim('zzz yjohn', 'xyz')=john<br><br>func.ltrim('texttotrimplaidcloud', 'texttotrim')=plaidcloud<br><br>func.ltrim('plaidcloud')=plaidcloud|Remove the longest string containing only characters from characters (a space by default) from the start of string|
|Text Expression|md5|func.md5(string) returns Text|md5('abc')=900150983cd24fb0d6963f7d28e17f72|Calculates the MD5 hash of string, returning the result in hexadecimal|
|Text Expression|metric_multiply|func.metric_multiply(string)||The Multiply function can take multiple metrics as inputs and multiply the values of the metrics|
|Text Expression|numericize|func.numericize(string)|func.numericize('100')=100|Attempts to coerce a non-numeric R object to natomic_object() or list of {natomic_object}|
|Text Expression|octet_length|func.octet_length(string) returns int|octet_length('jose')=4|Number of bytes in string|
|Text Expression|overlay|func.overlay(string placing string from int [forint]) returns Text|overlay('Txxxxas' placing 'hom' from 2 for 4)=Thomas|Replace a substring (returns: Text)|
|Text Expression|position|func.position(substring in string) returns int|position('om' in 'Thomas')=3|Location of specified substring|
|Text Expression|quote_literal|func.quote_literal(string) returns Text|quote_literal('O\'Reilly')='O''Reilly'<br><br>func.quote_literal('plaidcloud')='plaidcloud'|Return the given string suitably quoted to be used as a string literal in an SQL statement string. Embedded single-quotes and backslashes are properly doubled.|
|Text Expression|regexp_replace|func.regexp_replace(string text, pattern text, replacement text [,flags text]) returns Text|regexp_replace('Thomas', '.[mN]a.', 'M')=ThM<br>[More Examples](#regexp-replace-examples)|Replace substring matching POSIX regular expression.|
|Text Expression|repeat|func.repeat(string text, number int) returns Text|repeat('Pg', 4)=PgPgPgPg|Repeat string the specified number of times|
|Text Expression|replace|func.replace(string text, from text, to text) returns Text|replace('abcdefabc def', 'cd', 'XX')=abXXefabX Xef<br><br>func.replace('string_to_replace_with_spaces','_',' ') --> string to replace with spaces|Replace all occurrences in string of substring from with substring to|
|Text Expression|rpad|func.rpad(string text, length int [, fill text]) returns Text|rpad('hi', 5, 'xy')=hixyx|Fill up the string to length length by appending the characters fill (a space by default). If the string is already longer than length then it is truncated|
|Text Expression|rtrim|func.rtrim(string text [, characters text]) returns Text|rtrim('johnxxxx', 'x')=john|Remove the longest string containing only characters from characters (a space by default) from the end of string|
|Text Expression|split_part|func.split_part(string text, delimiter text, field int) returns Text|split_part('abc~@~def~@~ghi', '~@~', 2)=def<br><br>func.split_part(table.PERIOD, '_', 1)|Split string on delimiter and return the given field (counting from one)|
|Text Expression|strpos|func.strpos(string, substring) returns int|strpos('high', 'ig')=2|Location of specified substring (same as position(subst ring in string), but note the reversed argument order)|
|Text Expression|substr|func.substr(string, from [, count]) returns Text|substr('alphabet', 3, 2)=ph|Extract substring (same as substring(string from from for count))|
|Text Expression|substring|func.substring(string [from int] [for int]) returns Text|substring('Thomas' from 2 for 3)=hom<br><br>func.substring(table.ship_to_postal_code, 1, 5)|Extract substring|
|Text Expression|substring|func.substring(string frompattern) returns Text|substring( 'Thomas' from '…$')=mas|Extract substring matching POSIX regular expression|
|Text Expression|substring|func.substring(string frompatternforescape) returns Text|substring( 'Thomas' from '%#”o_a#” _' for '#')=oma|Extract substring matching SQL regular expression|
|Text Expression|text_to_bigint|func.text_to_bigint(string)||This function allows you to convert a string of character values into a large range integer|
|Text Expression|text_to_bool|func.text_to_bool(string)||Converts the input text or numeric expression to a Boolean value|
|Text Expression|text_to_integer|func.text_to_integer(string)||Convert text to integer|
|Text Expression|text_to_numeric|func.text_to_numeric(string)||This function converts a character string to a numeric value|
|Text Expression|text_to_smallint|func.text_to_smallint(string)||A 2-byte integer data type used in CREATE TABLE and ALTER TABLE statements|
|Text Expression|to_ascii|func.to_ascii(string text [, encoding text]) returns Text|to_ascii('Karel')=Karel|Convert string to ASCII from another encoding (only supports conversion from LATIN1, LATIN2, LATIN9, and WIN1250 encodings)|
|Text Expression|to_hex|func.to_hex(number int or bigint) returns Text|to_hex(2147483647)=7fffffff|Convert number to its equivalent hexadecimal representation|
|Text Expression|translate|func.translate(string text, from text, to text) returns Text|translate( '12345', '14', 'ax')=a23x5|Any character in the string that matches a character in the from set is replaced by the corresponding character in the to set|
|Text Expression|trim|func.trim([leading, trailing, both] [characters] from string) returns Text|trim(both 'x' from 'xTomxx')=Tom|Remove the longest string containing only the characters (a space by default) from the start/end/both ends of the string|
|Text Expression|upper|func.upper(string) returns Text|upper('tom')=TOM|Convert string to uppercase|
|Arrays|string_to_array|func.string_to_array(text, delimiter)|[Examples](#array-examples)|This function is used to split a string into array elements using supplied delimiter and optional null string|
|Arrays|unnest|func.unnest(text)|[Examples](#array-examples)|This function is used to expand an array to a set of rows|
|Grouping / Summarization|first|func.first(field)||This function returns the value of a specified field in the first record of the result set returned by a query|
|Grouping / Summarization|last|func.last(field)||This function returns the value of a specified field in the last record of the result set returned by a query|
|Grouping / Summarization|max|func.max(field)||The MAX function is an aggregate function that returns the maximum value in a set of values|
|Grouping / Summarization|median|func.median(field)||This function will calculate the middle value of a given set of numbers|
|Grouping / Summarization|stdev|func.stdev(field)||The STDEV function calculates the standard deviation for a sample set of data|
|Grouping / Summarization|stdev_pop|func.stdev_pop(field)||STDDEV_POP computes the population standard deviation and returns the square root of the population variance|
|Grouping / Summarization|stdev_samp|func.stdev_samp(field)||STDDEV_SAMP() function returns the sample standard deviation of an expression|
|Grouping / Summarization|var_pop|func.var_pop(field)||VAR_POP returns the population variance of a set of numbers after discarding the nulls in this set|
|Grouping / Summarization|var_samp|func.var_samp(field)||VAR_SAMP returns the sample variance of a set of numbers after discarding the nulls in this set|
|Grouping / Summarization|variance|func.variance(field)||This function is used to determine how far a set of values is spread out based on a sample of the population|
|JSON|array_to_json|func.array_to_json(array)||Returns the array as JSON. A PostgreSQL multidimensional array becomes a JSON array of arrays.|
|JSON|json_array_elements|func.json_array_elements(json)||Expands a JSON array to a set of JSON elements.|
|JSON|json_each|func.json_each(json)||Expands the outermost JSON object into a set of key/value pairs|
|JSON|json_each_text|func.json_each_text(json)||Expands the outermost JSON object into a set of key/value pairs. The returned value will be of type text.|
|JSON|json_extract_path|func.json_extract_path(json, key_1, key_2, ...)||Returns JSON object pointed to by path elements. The return value will be a type of JSON.|
|JSON|json_extract_path_text|func.json_extract_path_text(json, key_1, key_2, ...)||Returns JSON object pointed to by path elements. The return value will be a type of text.|
|JSON|json_object_keys|func.json_object_keys(json)||Returns set of keys in the JSON object. Only the "outer" object will be displayed.|
|Window Functions|avg|func.avg().over(partition_by=field, order_by=field)||This function returns the average of the values in a group. It ignores null values|
|Window Functions|count|func.count().over(partition_by=field, order_by=field)|[See Examples](#count-examples)|An aggregate function that returns the number of rows, or the number of non-NULL rows|
|Window Functions|cume_dist|func.cume_dist().over(partition_by=field, order_by=field)||This function calculates the cumulative distribution of a value within a group of values|
|Window Functions|dense_rank|func.dense_rank().over(partition_by=field, order_by=field)||The DENSE_RANK() is a window function that assigns a rank to each row within a partition of a result set|
|Window Functions|first_value|func.first_value(field).over(partition_by=field, order_by=field)|[See Examples](#first-value-examples)|FIRST_VALUE is a function that returns the first value in an ordered set of values|
|Window Functions|lag|func.lag(field, 1).over(partition_by=field, order_by=field)|[See Examples](#lag-examples)|This function lets you query more than one row in a table at a time without having to join the table to itself|
|Window Functions|last_value|func.last_value(field).over(partition_by=field, order_by=field)|[See Examples](#last-value-examples)|The LAST_VALUE() function is a window function that returns the last value in an ordered partition of a result set|
|Window Functions|lead|func.lead(field, 1).over(partition_by=field, order_by=field)||This function provides access to more than one row of a table at the same time without a self join|
|Window Functions|min|func.min().over(partition_by=field, order_by=field)||The min() function returns the item with the lowest value, or the item with the lowest value in an iterable|
|Window Functions|ntile|func.ntile(4).over(partition_by=field, order_by=field)||This is a function that distributes rows of an ordered partition into a specified number of approximately equal groups, or buckets|
|Window Functions|percent_rank|func.percent_rank().over(partition_by=field, order_by=field)||The PERCENT_RANK() function evaluates the relative standing of a value within a partition of a result set|
|Window Functions|rank|func.rank().over(partition_by=field, order_by=field)||This is a function that assigns a rank to each row within a partition of a result set|
|Window Functions|row_number|func.row_number().over(partition_by=field, order_by=field)||This function is used to provide consecutive numbering of the rows in the result by the order selected in the OVER clause for each partition|
|Window Functions|sum|func.sum().over(partition_by=field, order_by=field)|[See Examples](#sum-examples)|The SUM function adds values. You can add individual values, cell references or ranges or a mix of all three|

## Data Types

There are a wide variety of standard data types (dtypes) to support your requirements. As datasets become larger, determining smaller size dtypes for value storage can shrink the size of the table and improve performance. The following dtypes are available: 


* `Boolean`
* `Text`
* Numbers
	+ `SmallFloat` (6 Digits)
	+ `Float` (15 Digits)
	+ `BigFloat`
	+ `SmallInteger` (16 bit) (-32768 to 32767)
	+ `Integer` (32 bit) (-2147483648 to 2147483647)
	+ `BigInteger` (64 bit) (-9223372036854775808 to 9223372036854775807)
	+ `Numeric`
* Dates and Times
	+ `Date`
	+ `Timestamp`
	+ Time `Interval`

You can convert from one dtype to another using the func.cast() process.

{{< note >}}
Casting to an incompatible dtype may cause errors. For example, casting ‘hello’ to an integer will not work.
{{< /note >}}


## Case Examples
### A simple example
This example returns a person's name. It starts off searching to see if the first name column has a value (the "if"). If there is a value, concatenate the first name with the last name and return it (the "then"). If there isn't a first name, then return the last name only (the "else").

```python
case(
        (table.first_name.isnot(None), func.concat(table.first_name, table.last_name)), 
        else_ = table.last_name
    )
```

### A more complex example with multiple conditions
This example returns a price based on quantity. "If" the quantity in the order is more than 100, then give the customer the special price. If it doesn't satisfy the first condition, go to the second. If the quantity is greater than 10 (11-100), then give the customer the bulk price. Otherwise give the customer the regular price.

```python
case( 
        (order_table.qty > 100, item_table.specialprice), 
        (order_table.qty > 10, item_table.bulkprice) , 
        else_=item_table.regularprice
    )
```

This example returns the first initial of the person's first name. If the user's name is wendy, return W. Otherwise if the user's name is jack, return J. Otherwise return E.

```python
case( 
        (users_table.name == "wendy", "W"), 
        (users_table.name == "jack", "J"), 
        else_='E'
    )
```


The above may also be written in shorthand as:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Other Examples
In this example is from a Table:Lookup step where we are updating the "dock_final" column when the table1. dock_final value is Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
    )
```

This example is from a Table:Lookup step where we are updating the "Marketing Channel" column when "Marketing Channel" in table1 is not 'none' or the "Serial Number" contains a '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel') != Null, get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
    )
```
```python
CASE WHEN "sol_otif_pod_missing" = 1 THEN
'POD is missing.'
ELSE
'POD exists.'
END
```

```python
CASE WHEN
SUM("distance_dc_xd") = 0 THEN 0
ELSE
sum("XD")/sum("distance_dc_xd")
END
```

```python
sum(CASE WHEN "dc" = 'ALAB' THEN
("sol_otif_infull" * "sol_otif_pgi_ontime")
ELSE
0.0
END) / sum(CASE WHEN "dc" = 'ALAB' THEN
1.0
ELSE
0.000001
END)
```




## func.cast() type conversions

| Analyze Expression | Description | Result |
|--------------------|-------------|--------|
| func.cast(123, Text) | Integer to Text | ‘123’ |
| func.cast(‘123’, Integer) | Text to Integer | 123 |
| func.cast(‘78.69’, Float) | Text to Float | 78.69 |
| func.cast(‘78.69’, SmallFloat) | Text to Small Float | 78.69 |
| func.cast(‘78.69’, Integer) | Text to Integer (Truncate decimals) | 78 |
| func.cast(‘78.69’, SmallInteger) | Text to Small Integer (Truncate decimals) | 78 |
| func.cast(‘78.69’, BigInteger) | Text to Big Integer (Truncate decimals) | 78 |
| func.cast(1, Boolean) | Integer to Boolean | True |

**Other Examples**
cast(table.transaction_year, Numeric)
cast(get_column(table, 'End_Date'),Text)


## func.to() Data Type Conversions

| Analyze Expression | Return Type | Description | Example |
|--------------------|-------------|-------------|---------|
| func.to_char(timestamp, text) | text | convert time stamp to text string | to_char(current_timestamp, ‘HH12:MI:S S’) |
| func.to_char(interval, text) | text | convert interval to string | to_char(interval ‘15h 2m 12s’, ‘HH24:MI:S S’) |
| func.to_char(integer, text) | text | convert integer to string | to_char(125, ‘999’) |
| func.to_char(bigfloat, text) | text | convert real/double precision to string | to_char(125.8::real, ‘999D9’) |
| func.to_char(numeric, text) | text | convert numeric to string | to_char(-125.8, ‘999D99S’) |
| func.to_date(text, text) | date | convert string to date | func.to_date(table.Created_on, 'DD-MM-YYYY') |
| func.to_number(text, text) | numeric | convert string to numeric | to_number (‘12,454.8 -‘, ‘99G999D9S ‘) |
| func.to_timestamp(text, text) | timestamp with time zone | convert string to time stamp | to_timestamp(‘05 Dec 2000’, ‘DD Mon YYYY’) |
| func.to_timestamp(bigfloat) | timestamp with time zone | convert UNIX epoch to time stamp | to_timestamp(200120400) |

**Other Examples**
```python
to_char("Sales_Order_w_Status"."WeekName")

func.to_char(func.date_trunc('week', get_column(table, 'date_sol_delivery_required')), 'YYYY-MM-DD')

func.to_date(get_column(table, 'File Creation Date'), 'YYYYMMDD')

result.CreateDate<func.to_date('09022022', 'MMDDYYYY')

to_char("date_delivery", 'YYYY-mm-dd')
```



## Other Date Time Examples
### Date Trunc
```python
func.date_trunc('week', get_column(table, 'Date' ))

func.to_char(func.date_trunc('week', get_column(table, 'date_sol_delivery_required')), 'YYYY-MM-DD')

func.to_char(func.date_trunc('week', ((table.Date) - 6)),'MON-DD')
```

The following patterns can be used to select specific parts of a timestamp or to format date/time as desired.

| Pattern | Description |
|---------|-------------|
| HH | hour of day (01-12) |
| HH12 | hour of day (01-12) |
| HH24 | hour of day (00-23) |
| MI | minute (00-59) |
| SS | second (00-59) |
| MS | millisecond (000-999) |
| US | microsecond (000000-999999 ) |
| SSSS | seconds past midnight (0-86399) |
| AM or A.M. or PM or P.M. | meridian indicator (uppercase) |
| am or a.m. or pm or p.m. | meridian indicator (lowercase) |
| Y,YYY | year (4 and more digits) with comma |
| YYYY | year (4 and more digits) |
| YYY | last 3 digits of year |
| YY | last 2 digits of year |
| Y | last digit of year |
| IYYY | ISO year (4 and more digits) |
| IYY | last 3 digits of ISO year |
| IY | last 2 digits of ISO year |
| I | last digits of ISO year |
| BC or B.C. or AD or A.D. | era indicator (uppercase) |
| bc or b.c. or ad or a.d. | era indicator (lowercase) |
| MONTH | full uppercase month name (blank-padded to 9 chars) |
| Month | full mixed-case month name (blank-padded to 9 chars) |
| month | full lowercase month name (blank-padded to 9 chars) |
| MON | abbreviated uppercase month name (3 chars) |
| Mon | abbreviated mixed-case month name (3 chars) |
| mon | abbreviated lowercase month name (3 chars) |
| MM | month number (01-12) |
| DAY | full uppercase day name (blank-padded to 9 chars) |
| Day | full mixed-case day name (blank-padded to 9 chars) |
| day | full lowercase day name (blank-padded to 9 chars) |
| DY | abbreviated uppercase day name (3 chars) |
| Dy | abbreviated mixed-case day name (3 chars) |
| dy | abbreviated lowercase day name (3 chars) |
| DDD | day of year (001-366) |
| DD | day of month (01-31) |
| D | day of week (1-7; Sunday is 1) |
| W | week in month (1-5) (The first week starts on the first day of the month.) |
| WW | week number in year (1-53) (The first week starts on the first day of the year.) |
| IW | ISO week number of year (The first Thursday of the new year is in week 1.) |
| CC | century (2 digits) |
| J | Julian Day (days since January 1, 4712 BC) |
| Q | quarter |
| RM | month in Roman numerals (I-XII; I=January) (uppercase) |
| rm | month in Roman numerals (i-xii; i=January) (lowercase) |
| TZ | time-zone name (uppercase) |
| tz | time-zone name (lowercase) |


## And Operator
**Example 1**

This example checks if the `period` is any of the three specified dates.

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

**Example 2**

This example is checking if to ensure the `origin_plant` is not one of the values specified. This is using the `!=` expression.

```python
and_(  
    table.origin_plant != '5013',  
    table.origin_plant != '5026',  
    table.origin_plant != '5120',  
    table.origin_plant != '5287',  
    table.origin_plant != '5161',  
    table.origin_plant != '5192'  
)
```

Alternatively, for reference, the above check could be written using the `not_` and `or_` operators like this:

```python
not_(  
    or_(  
        table.origin_plant == '5013',  
        table.origin_plant == '5026',  
        table.origin_plant == '5120',  
        table.origin_plant == '5287',  
        table.origin_plant == '5161',  
        table.origin_plant == '5192'  
    )  
)
```

**Other Examples**
```python
and_(table.origin_plant != '5013',table.origin_plant != '5026')
```


## Not Operator
```python
not_(and_(table.VALUE_FC==0.0, table.VALUE_LC==0.0))

not_(or_(get_column(table, 'GL Account').startswith('7'), get_column(table, 'GL Account').startswith('8')))
```


## Or Operator
**Example 1**
This example checks if the `period` is any of the three specified dates.
```python
or_(  
    table.period == '2020_10',  
    table.period == '2020_11',  
    table.period == '2020_12'  
)
```

**Example 2**
This example is checking if `order_reason_Include` is `null` or has the word `KEEP` as a value.
```python
or_(  
    table.order_reason_Include == 'KEEP',  
    table.order_reason_Include.is_(None)  
)
```


## Coalesce Examples
```python
func.coalesce(table.UOM,  'none', \n)

func.coalesce(get_column(table2, 'TECHNOLOGY_RATE'), 0.0)

func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price) * table_beta.quantity_sold
```

## Regexp Replace Examples
```python
func.regexp_replace('plaidcloud', 'p', 'P') --> Plaidcloud

func.regexp_replace('remove12345alphabets','[[:alpha:]]','','g') --> 12345

func.regexp_replace('remove12345digits','[[:digit:]]','','g') --> removedigits
```

## First Value Examples
This is an example of using the 'first_value()' capability to calculate the running time of the time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
table.timestamp - func.first_value(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp)
```

Adding the expression above to an **Interval** column called 'run_time' would result in an output table like this:

| location   | employee | timestamp           | run_time  |
|------------|----------|---------------------|-----------|
| Building A | John Doe | 2022-01-05 15:34:31 | 00:00:00  |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:10:00  |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:12:10  |



## Lag Examples
This is an example of using the 'lag()' capability to calculate the time interval in time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
table.timestamp - func.lag(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp)
```

Adding the expression above to an **Interval** column called 'delta' would result in an output table like this:

| location   | employee | timestamp           | delta    |
|------------|----------|---------------------|----------|
| Building A | John Doe | 2022-01-05 15:34:31 | *null*   |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:10:00 |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:02:10 |



## Last Value Examples
This is an example of using the 'last_value()' capability to calculate the time remaining in time series data where each event is on a distinct row.

This assumes you have a table of time series data that looks like this:

| location   | employee | timestamp           |
|------------|----------|---------------------|
| Building A | John Doe | 2022-01-05 15:34:31 |
| Building A | John Doe | 2022-01-05 15:44:31 |
| Building A | John Doe | 2022-01-05 15:46:41 |

```python
func.last_value(table.timestamp, 1).over(partition_by=[table.location, table.employee], order_by=table.timestamp) - table.timestamp
```

Adding the expression above to an **Interval** column called 'remaining' would result in an output table like this:

| location   | employee | timestamp           | remaining |
|------------|----------|---------------------|-----------|
| Building A | John Doe | 2022-01-05 15:34:31 | 00:12:10  |
| Building A | John Doe | 2022-01-05 15:44:31 | 00:02:10  |
| Building A | John Doe | 2022-01-05 15:46:41 | 00:00:00  |



## Sum Examples
```python
(sum("sol_otif_infull" * "sol_otif_pgi_ontime")) / (count(*) + 0.000001)

sum("sol_otif_qty_filled") / (sum("sol_otif_qty_requested") + 0.000001)
```



## Count Examples
```python
sum("RW")/COUNT(DISTINCT "ship_to_customer")

(sum("sol_otif_infull" * "sol_otif_pgi_ontime")) / (count(*) + 0.000001)
```



## Array Examples
In the examples below, we will use the following table called contacts with the phones column defined with an array of text.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

The phones column is a one-dimensional array that holds various phone numbers that a contact may have.

To define multiple dimensional array, you add the square brackets.

For example, you can define a two-dimensional array as follows:

```python
column_name data_type [][]
```

An example of inserting data into that table
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
or
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

### Array unnest
The unnest() function expands an array to a list of rows. For example, the following query expands all phone numbers of the phones array.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Output:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |


### STRING_TO_ARRAY() function
This function is used to split a string into array elements using supplied delimiter and optional null string.

Syntax:<br>
string_to_array(text, text [, text])

Return Type:<br>
text[]

Example:<br>
```python
SELECT string_to_array('xx~^~yy~^~zz', '~^~', 'yy');
```

Output:<br>
{xx,NULL,zz}

