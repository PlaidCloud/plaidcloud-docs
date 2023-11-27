---
title: General Usage PostGIS
slug: general-usage-postgis
weight: 6.0
description: Enhanced 'Analyze' functions for geospatial analysis
date: 2022-01-25T07:39:53
---

Analyze provides access to the powerful PostGIS library of functions for geospatial analysis. The functions available are shown in the following table and link to instructions on the PostGIS site.

{{< note >}}
To specify the use of PostGIS functions in expressions, prefix the name with func. For example, using ST_GeogFromText would use func.ST_GeogFromText()
{{< /note >}}

## Geometry Constructors
| Function | Description |
|----------|-------------|
| [ST_BdPolyFromText](http://postgis.net/docs/manual-2.2/ST_BdPolyFromText.html) | Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString Well-Known text representation. |
| [ST_BdMPolyFromText](http://postgis.net/docs/manual-2.2/ST_BdMPolyFromText.html) | Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString text representation Well-Known text representation. |
| [ST_Box2dFromGeoHash](http://postgis.net/docs/manual-2.2/ST_Box2dFromGeoHash.html)  | Return a BOX2D from a GeoHash string. |
| [ST_GeogFromText](http://postgis.net/docs/manual-2.2/ST_GeogFromText.html) | Return a specified geography value from Well-Known Text representation or extended (WKT). |
| [ST_GeographyFromTex](http://postgis.net/docs/manual-2.2/ST_GeographyFromText.html) | Return a specified geography value from Well-Known Text representation or extended (WKT). |
| [ST_GeogFromWKB](http://postgis.net/docs/manual-2.2/ST_GeogFromWKB.html) | Creates a geography instance from a Well-Known Binary geometry representation (WKB) or extended Well Known Binary (EWKB). |
| [ST_GeomCollFromText](http://postgis.net/docs/manual-2.2/ST_GeomCollFromText.html)  | Makes a collection Geometry from collection WKT with the given SRID. If SRID is not give, it defaults to 0. |
| [ST_GeomFromEWKB](http://postgis.net/docs/manual-2.2/ST_GeomFromEWKB.html) | Return a specified ST_Geometry value from Extended Well-Known Binary representation (EWKB). |
| [ST_GeomFromEWKT](http://postgis.net/docs/manual-2.2/ST_GeomFromEWKT.html) | Return a specified ST_Geometry value from Extended Well-Known Text representation (EWKT). |
| [ST_GeometryFromText](http://postgis.net/docs/manual-2.2/ST_GeometryFromText.html)  | Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText |
| [ST_GeomFromGeoHash](http://postgis.net/docs/manual-2.2/ST_GeomFromGeoHash.html) | Return a geometry from a GeoHash string. |
| [ST_GeomFromGML](http://postgis.net/docs/manual-2.2/ST__GeomFromGML.html) | Takes as input GML representation of geometry and outputs a PostGIS geometry object |
| [ST_GeomFromGeoJSON](http://postgis.net/docs/manual-2.2/ST_GeomFromGeoJSON.html) | Takes as input a geojson representation of a geometry and outputs a PostGIS geometry object |
| [ST_GeomFromKML](http://postgis.net/docs/manual-2.2/ST_GeomFromKML.html) | Takes as input KML representation of geometry and outputs a PostGIS geometry object |
| [ST_GMLToSQL](http://postgis.net/docs/manual-2.2/ST_GMLToSQL.html) | Return a specified ST_Geometry value from GML representation. This is an alias name for ST_GeomFromGML |
| [ST_GeomFromText](http://postgis.net/docs/manual-2.2/ST_GeomFromText.html) | Return a specified ST_Geometry value from Well-Known Text representation (WKT). |
| [ST_GeomFromWKB](http://postgis.net/docs/manual-2.2/ST_GeomFromWKB.html) | Creates a geometry instance from a Well-Known Binary geometry representation (WKB) and optional SRID. |
| [ST_LineFromEncodedPolyline](http://postgis.net/docs/manual-2.2/ST_LineFromEncodedPolyline.html) | Creates a LineString from an Encoded Polyline. |
| [ST_LineFromMultiPoint](http://postgis.net/docs/manual-2.2/ST_LineFromMultiPoint.html) | Creates a LineString from a MultiPoint geometry. |
| [ST_LineFromText](http://postgis.net/docs/manual-2.2/ST_LineFromText.html) | Makes a Geometry from WKT representation with the given SRID. If SRID is not given, it defaults to 0. |
| [ST_LineFromWKB](http://postgis.net/docs/manual-2.2/ST_LineFromWKB.html) | Makes a LINESTRING from WKB with the given SRID |
| [ST_LinestringFromWKB](http://postgis.net/docs/manual-2.2/ST_LinestringFromWKB.html) | Makes a geometry from WKB with the given SRID. |
| [ST_MakeBox2D](http://postgis.net/docs/manual-2.2/ST_MakeBox2D.html) | Creates a BOX2D defined by the given point geometries. |
| [ST_3DMakeBox](http://postgis.net/docs/manual-2.2/ST_3DMakeBox.html) | Creates a BOX3D defined by the given 3d point geometries. |
| [ST_MakeLine](http://postgis.net/docs/manual-2.2/ST__MakeLine.html) | Creates a Linestring from point or line geometries. |
| [ST_MakeEnvelope](http://postgis.net/docs/manual-2.2/ST_MakeEnvelope.html) | Creates a rectangular Polygon formed from the given minimums and maximums. Input values must be in SRS specified by the SRID |
| [ST_MakePolygon](http://postgis.net/docs/manual-2.2/ST_MakePolygon.html) | Creates a Polygon formed by the given shell. Input geometries must be closed LINESTRINGS. |
| [ST_MakePoint](http://postgis.net/docs/manual-2.2/ST_MakePoint.html) | Creates a 2D,3DZ or 4D point geometry. |
| [ST_MakePointM](http://postgis.net/docs/manual-2.2/ST__MakePointM.html) | Creates a point geometry with an x, y, and m coordinate. |
| [ST_MLineFromText](http://postgis.net/docs/manual-2.2/ST_MLineFromText.html) | Return a specified ST_MultiLineString value from WKT representation. |
| [ST_MPointFromText](http://postgis.net/docs/manual-2.2/ST_MPointFromText.html) | Makes a Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0. |
| [ST_MPolyFromText](http://postgis.net/docs/manual-2.2/ST_MPolyFromText.html) | Makes a MultiPolygon Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0. |
| [ST_Point](http://postgis.net/docs/manual-2.2/ST_Point.html) | Returns an ST_Point with the given coordinate values. OGC alias for ST_MakePoint. |
| [ST_PointFromGeoHash](http://postgis.net/docs/manual-2.2/ST_PointFromGeoHash.html)  | Return a point from a GeoHash string. |
| [ST_PointFromText](http://postgis.net/docs/manual-2.2/ST_PointFromText.html) | Makes a point Geometry from WKT with the given SRID. If SRID is not given, it defaults to unknown. |
| [ST_PointFromWKB ](http://postgis.net/docs/manual-2.2/ST_PointFromWKB.html) | Makes a geometry from WKB with the given SRID |
| [ST_Polygon](http://postgis.net/docs/manual-2.2/ST_Polygon.html) | Returns a polygon built from the specified linestring and SRID. |
| [ST_PolygonFromText](http://postgis.net/docs/manual-2.2/ST_PolygonFromText.html) | Makes a Geometry from WKT with the given SRID. If SRID is not give, it defaults to 0. |
| [ST_WKBToSQL](http://postgis.net/docs/manual-2.2/ST_WKBToSQL.html) | Return a specified ST_Geometry value from Well-Known Binary representation (WKB). This is an alias name for ST_GeomFromWKB that takes no srid |
| [ST_WKTToSQL](http://postgis.net/docs/manual-2.2/ST_WKTToSQL.html) | Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText |
