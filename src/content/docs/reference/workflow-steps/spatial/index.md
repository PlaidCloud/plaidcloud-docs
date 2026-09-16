---
title: Geospatial Steps
description: Every PlaidCloud geospatial workflow step — import spatial files, buffer, match, measure, and build geometry, with full Alteryx spatial-tool coverage.
---

Workflow steps that read, build, transform, and match geometry. Together with the
[geometry expressions](/reference/workflow-steps/spatial/spatial-sql-recipes/) they
cover the whole Alteryx spatial toolset — see the
[Alteryx conversion matrix](/reference/alteryx-conversion-matrix/) for the
tool-by-tool mapping.

## Geometry Is WKT

Every spatial step reads and writes geometry as **WKT** (well-known text) in an
ordinary text column. There is no special geometry type to declare and no
conversion between steps: a geometry column produced by
[Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) is
directly usable by [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/),
[Spatial Match](/reference/workflow-steps/spatial/spatial-match/), or a SQL
expression, in any order.

## Two Execution Routes

Each step runs by the simplest route that gives the right answer.

| Route | What runs there | Why |
|---|---|---|
| **SQL** — in the database | Find Nearest, Match, plus the [geometry expressions](/reference/workflow-steps/spatial/spatial-sql-recipes/) | Predicate joins and column expressions scale with the table; no rows leave the warehouse |
| **Workflow engine** — Shapely and GDAL | Everything that reshapes geometry | Buffering, smoothing, and dissolving are not expressible in database SQL |

You do not choose the route; each step type has one. The distinction matters when
you are sizing a job: SQL-route steps scale with the warehouse, engine-route steps
scale with the workflow pod.

## Load Geometry

- [Spatial File Import](/reference/workflow-steps/spatial/spatial-file-import/) — read a MapInfo `.TAB`, ESRI `.shp`, `.kml`, or `.geojson` file and its sidecars
- [Geometry in SQL](/reference/workflow-steps/spatial/spatial-sql-recipes/) — build points from longitude/latitude columns

## Match and Measure

- [Spatial Find Nearest](/reference/workflow-steps/spatial/spatial-find-nearest/) — the N closest rows of one table to each row of another, with distance
- [Spatial Match](/reference/workflow-steps/spatial/spatial-match/) — pair rows whose geometry intersects, is within, or contains
- [Spatial Match (Intersect / Unmatched)](/reference/workflow-steps/spatial/spatial-match-executor/) — the same match, emitting the overlap geometry or the rows that did not match
- [Spatial Info](/reference/workflow-steps/spatial/spatial-info/) — area, length, centroid, and bounding rectangle, measured geodesically

## Reshape Geometry

- [Spatial Buffer](/reference/workflow-steps/spatial/spatial-buffer/) — grow each geometry by a fixed distance
- [Spatial Trade Area](/reference/workflow-steps/spatial/spatial-trade-area/) — concentric buffers sized in real-world units
- [Spatial Generalize](/reference/workflow-steps/spatial/spatial-generalize/) — simplify to a tolerance
- [Spatial Smooth](/reference/workflow-steps/spatial/spatial-smooth/) — smooth over a number of passes
- [Spatial Process](/reference/workflow-steps/spatial/spatial-process/) — intersect, union, or cut two geometry columns

## Build and Break Apart

- [Spatial Poly-Build](/reference/workflow-steps/spatial/spatial-poly-build/) — build a polygon or convex hull per group of points
- [Spatial Poly-Split](/reference/workflow-steps/spatial/spatial-poly-split/) — one row per vertex, component polygon, or hole
- [Spatial Combine](/reference/workflow-steps/spatial/spatial-combine/) — dissolve each group's geometries into one
- [Spatial Make Grid](/reference/workflow-steps/spatial/spatial-make-grid/) — tile an extent into square cells

## Expression Reference

- [Geometry Functions (Lakehouse v1)](/reference/expressions/lakehouse-v1/09-geometry-functions/) — the `ST_*` family
- [Geography Functions (Lakehouse v1)](/reference/expressions/lakehouse-v1/09-geo-functions/) — H3 hexagonal indexing and geohashes
- [Spatial Functions (Lakehouse v2)](/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Related

- [Geospatial Analytics](/guides/workflows/geospatial-analytics/) — a worked path from source file to published map
- [Migrate Spatial Alteryx Workflows](/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map](/reference/workflow-steps/reports/report-map/) — render geometry into a report
- [Packaged macro steps](/reference/workflow-steps/macros/) — Heat Map and Pie Wedge Trade Area
