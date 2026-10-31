---
title: TO_BINARY (Lakehouse v1)
description: TO_BINARY – wandelt unterstützte Datentypen, darunter String, Variant, Bitmap, Geometry und Geography, in ihre binäre Darstellung um (Hex-Format).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-binary.md
---

Wandelt unterstützte Datentypen, darunter String, Variant, Bitmap, Geometry und Geography, in ihre binäre Darstellung um (Hex-Format).

Siehe auch: [TRY_TO_BINARY](../try-to-binary)

## Analyze-Syntax

```python
func.to_binary( <expr> )
```

## Analyze-Beispiele

```python
func.to_binary('Databend')

┌───────────────────────────────┐
│ func.to_binary('Databend')    │
├───────────────────────────────┤
│ 4461746162656E64              │
└───────────────────────────────┘
```

## SQL-Syntax

```sql
TO_BINARY( <expr> )
```

## SQL-Beispiele

Dieses Beispiel wandelt eine Zeichenfolge in Binärdaten um:

```sql
SELECT TO_BINARY('Databend');

┌───────────────────────┐
│ to_binary('Databend') │
├───────────────────────┤
│ 4461746162656E64      │
└───────────────────────┘
```

Dieses Beispiel wandelt JSON-Daten in Binärdaten um:

```sql
SELECT TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Dieses Beispiel wandelt Bitmap-Daten in Binärdaten um:

```sql
SELECT TO_BINARY(TO_BITMAP('10,20,30')) AS binary_bitmap;

┌──────────────────────────────────────────────────────────────────────┐
│                             binary_bitmap                            │
├──────────────────────────────────────────────────────────────────────┤
│ 0100000000000000000000003A3000000100000000000200100000000A0014001E00 │
└──────────────────────────────────────────────────────────────────────┘
```

Dieses Beispiel wandelt Geometriedaten (WKT-Format) in Binärdaten um:

```sql
SELECT TO_BINARY(ST_GEOMETRYFROMWKT('SRID=4326;POINT(1.0 2.0)')) AS binary_geometry;

┌────────────────────────────────────────────────────┐
│                   binary_geometry                  │
├────────────────────────────────────────────────────┤
│ 0101000020E6100000000000000000F03F0000000000000040 │
└────────────────────────────────────────────────────┘
```

Dieses Beispiel wandelt Geografiedaten (EWKT-Format) in Binärdaten um:

```sql
SELECT TO_BINARY(ST_GEOGRAPHYFROMEWKT('SRID=4326;POINT(-122.35 37.55)')) AS binary_geography;

┌────────────────────────────────────────────────────┐
│                  binary_geography                  │
├────────────────────────────────────────────────────┤
│ 0101000020E61000006666666666965EC06666666666C64240 │
└────────────────────────────────────────────────────┘
```
