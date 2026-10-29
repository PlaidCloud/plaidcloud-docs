---
title: FUSE_SEGMENT (Lakehouse v1)
description: FUSE_SEGMENT — 지정한 테이블 스냅샷의 세그먼트 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-segment.md
---

지정한 테이블 스냅샷의 세그먼트 정보를 반환합니다. PlaidCloud Lakehouse의 세그먼트에 대한 자세한 내용은 스냅샷, 세그먼트, 블록이란 무엇입니까?를 참조하십시오.

참고 항목:

- [FUSE_SNAPSHOT](../fuse-snapshot/)
- [FUSE_BLOCK](../fuse-block/)

## SQL 구문

```sql
FUSE_SEGMENT('<database_name>', '<table_name>','<snapshot_id>')
```

## SQL 예제

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
