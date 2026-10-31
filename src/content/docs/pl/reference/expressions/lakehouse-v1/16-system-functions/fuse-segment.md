---
title: FUSE_SEGMENT (Lakehouse v1)
description: FUSE_SEGMENT — zwraca informacje o segmentach wskazanej migawki tabeli.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-segment.md
---

Zwraca informacje o segmentach wskazanej migawki tabeli. Więcej informacji o tym, czym jest segment w PlaidCloud Lakehouse, znajdziesz w artykule Czym są migawka, segment i blok?.

Zobacz też:

- [FUSE_SNAPSHOT](../fuse-snapshot/)
- [FUSE_BLOCK](../fuse-block/)

## Składnia SQL

```sql
FUSE_SEGMENT('<database_name>', '<table_name>','<snapshot_id>')
```

## Przykłady SQL

```sql
CREATE TABLE mytable(c int);
INSERT INTO mytable values(1);
INSERT INTO mytable values(2); 

-- Obtain a snapshot ID
SELECT snapshot_id FROM FUSE_SNAPSHOT('default', 'mytable') limit 1;

---
┌──────────────────────────────────┐
│ snapshot_id                      │
├──────────────────────────────────┤
│ 82c572947efa476892bd7c0635158ba2 │
└──────────────────────────────────┘

SELECT * FROM FUSE_SEGMENT('default', 'mytable', '82c572947efa476892bd7c0635158ba2');

---
┌────────────────────────────────────────────────────┬────────────────┬─────────────┬───────────┬────────────────────┬──────────────────┐
│ file_location                                      │ format_version │ block_count │ row_count │ bytes_uncompressed │ bytes_compressed │
├────────────────────────────────────────────────────┼────────────────┼─────────────┼───────────┼────────────────────┼──────────────────┤
│ 1/319/_sg/d35fe7bf99584301b22e8f6a8a9c97f9_v1.json │              1 │           1 │         1 │                  4 │              184 │
│ 1/319/_sg/c261059d47c840e1b749222dabb4b2bb_v1.json │              1 │           1 │         1 │                  4 │              184 │
└────────────────────────────────────────────────────┴────────────────┴─────────────┴───────────┴────────────────────┴──────────────────┘
```
