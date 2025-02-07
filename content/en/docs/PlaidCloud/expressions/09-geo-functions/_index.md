---
title: Geography Functions
---

This section provides reference information for the geography functions in PlaidCloud Lakehouse.  These functions are based on the very innovate H3 system developed by Uber to better calculate geographic relationships.  The explanation of H3 can be found [here](https://www.uber.com/blog/h3/).

## Coordinate Conversion

- [GEO_TO_H3](geo-to-h3)
- [GEOHASH_DECODE](geohash-decode)
- [GEOHASH_ENCODE](geohash-encode)
- [STRING_TO_H3](string-to-h3)
- [H3_TO_GEO](h3-to-geo)
- [H3_TO_STRING](h3-to-string)

## Hexagon Properties

- [H3_CELL_AREA_M2](h3-cell-area-m2)
- [H3_CELL_AREA_RADS2](h3-cell-area-rads2)
- [H3_HEX_AREA_KM2](h3-hex-area-km2)
- [H3_HEX_AREA_M2](h3-hex-area-m2)
- [H3_GET_BASE_CELL](h3-get-base-cell)
- [H3_GET_FACES](h3-get-faces)
- [H3_GET_RESOLUTION](h3-get-resolution)
- [H3_TO_CENTER_CHILD](h3-to-center-child)
- [H3_TO_CHILDREN](h3-to-children)
- [H3_TO_GEO_BOUNDARY](h3-to-geo-boundary)
- [H3_TO_PARENT](h3-to-parent)
- [H3_NUM_HEXAGONS](h3-num-hexagons)

## Hexagon Relationships

- [H3_HEX_RING](h3-hex-ring)
- [H3_K_RING](h3-k-ring)
- [H3_INDEXES_ARE_NEIGHBORS](h3-indexes-are-neighbors)
- [H3_IS_PENTAGON](h3-is-pentagon)
- [H3_IS_RES_CLASS_III](h3-is-res-class-iii)
- [H3_IS_VALID](h3-is-valid)
- [H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE](h3-get-destination-index-from-unidirectional-edge)
- [H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE](h3-get-indexes-from-unidirectional-edge)
- [H3_GET_ORIGIN_INDEX_FROM_UNIDIRECTIONAL_EDGE](h3-get-origin-index-from-unidirectional-edge)
- [H3_GET_UNIDIRECTIONAL_EDGE_BOUNDARY](h3-get-unidirectional-edge-boundary)
- [H3_GET_UNIDIRECTIONAL_EDGE](h3-get-unidirectional-edge)
- [H3_GET_UNIDIRECTIONAL_EDGES_FROM_HEXAGON](h3-get-unidirectional-edges-from-hexagon)
- [H3_UNIDIRECTIONAL_EDGE_IS_VALID](h3-unidirectional-edge-is-valid)

## Measurement

- [H3_DISTANCE](h3-distance)
- [H3_EDGE_ANGLE](h3-edge-angle)
- [H3_EDGE_LENGTH_KM](h3-edge-length-km)
- [H3_EDGE_LENGTH_M](h3-edge-length-m)
- [H3_EXACT_EDGE_LENGTH_KM](h3-exact-edge-length-km)
- [H3_EXACT_EDGE_LENGTH_M](h3-exact-edge-length-m)
- [H3_EXACT_EDGE_LENGTH_RADS](h3-exact-edge-length-rads)

## General Utility

- [POINT_IN_POLYGON](point-in-polygon)
- [H3_LINE](h3-line)