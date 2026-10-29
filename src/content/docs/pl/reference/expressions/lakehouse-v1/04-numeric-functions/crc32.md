---
title: CRC32 (Lakehouse v1)
description: CRC32 — zwraca sumę kontrolną CRC32 dla x, przy czym 'x' powinno być ciągiem znaków i (jeśli to możliwe) jest tak traktowane.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Zwraca sumę kontrolną CRC32 dla `x`, przy czym 'x' powinno być ciągiem znaków, a jeśli nim nie jest, to (o ile to możliwe) jest tak traktowane.

## Składnia Analyze

```python
func.crc32( '<x>' )
```

## Przykłady Analyze

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## Składnia SQL

```sql
CRC32( '<x>' )
```

## Przykłady SQL

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
