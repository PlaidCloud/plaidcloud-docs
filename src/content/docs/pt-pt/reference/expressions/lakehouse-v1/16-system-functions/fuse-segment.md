---
title: FUSE_SEGMENT (Lakehouse v1)
description: FUSE_SEGMENT — devolve a informação dos segmentos de um instantâneo de tabela especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-segment.md
---

Devolve a informação dos segmentos de um instantâneo de tabela especificado. Para mais informação sobre o que é um segmento no PlaidCloud Lakehouse, consulte O que são instantâneo, segmento e bloco?.

Ver também:

- [FUSE_SNAPSHOT](../fuse-snapshot/)
- [FUSE_BLOCK](../fuse-block/)

## Sintaxe SQL

```sql
FUSE_SEGMENT('<database_name>', '<table_name>','<snapshot_id>')
```

## Exemplos de SQL

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
