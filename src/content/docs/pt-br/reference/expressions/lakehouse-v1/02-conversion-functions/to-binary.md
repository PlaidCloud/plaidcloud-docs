---
title: TO_BINARY (Lakehouse v1)
description: TO_BINARY converte tipos de dados compatíveis, incluindo string, variant, bitmap, geometry e geography, em sua representação binária (formato hexadecimal).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-binary.md
---

Converte tipos de dados compatíveis, incluindo string, variant, bitmap, geometry e geography, em sua representação binária (formato hexadecimal).

Veja também: [TRY_TO_BINARY](../try-to-binary)

## Sintaxe do Analyze

```python
func.to_binary( <expr> )
```

## Exemplos do Analyze

```python
func.to_binary('Databend')

┌───────────────────────────────┐
│ func.to_binary('Databend')    │
├───────────────────────────────┤
│ 4461746162656E64              │
└───────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_BINARY( <expr> )
```

## Exemplos de SQL

Este exemplo converte uma string em binário:

```sql
SELECT TO_BINARY('Databend');

┌───────────────────────┐
│ to_binary('Databend') │
├───────────────────────┤
│ 4461746162656E64      │
└───────────────────────┘
```

Este exemplo converte dados JSON em binário:

```sql
SELECT TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Este exemplo converte dados de bitmap em binário:

```sql
SELECT TO_BINARY(TO_BITMAP('10,20,30')) AS binary_bitmap;

┌──────────────────────────────────────────────────────────────────────┐
│                             binary_bitmap                            │
├──────────────────────────────────────────────────────────────────────┤
│ 0100000000000000000000003A3000000100000000000200100000000A0014001E00 │
└──────────────────────────────────────────────────────────────────────┘
```

Este exemplo converte dados de geometry (formato WKT) em binário:

```sql
SELECT TO_BINARY(ST_GEOMETRYFROMWKT('SRID=4326;POINT(1.0 2.0)')) AS binary_geometry;

┌────────────────────────────────────────────────────┐
│                   binary_geometry                  │
├────────────────────────────────────────────────────┤
│ 0101000020E6100000000000000000F03F0000000000000040 │
└────────────────────────────────────────────────────┘
```

Este exemplo converte dados de geography (formato EWKT) em binário:

```sql
SELECT TO_BINARY(ST_GEOGRAPHYFROMEWKT('SRID=4326;POINT(-122.35 37.55)')) AS binary_geography;

┌────────────────────────────────────────────────────┐
│                  binary_geography                  │
├────────────────────────────────────────────────────┤
│ 0101000020E61000006666666666965EC06666666666C64240 │
└────────────────────────────────────────────────────┘
```
