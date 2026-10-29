---
title: FUSE_COLUMN (Lakehouse v1)
description: FUSE_COLUMN — retorna as informações de coluna do instantâneo mais recente ou de um instantâneo especificado de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-column.md
---

Retorna as informações de coluna do instantâneo mais recente ou de um instantâneo especificado de uma tabela. Para mais informações sobre o que é um bloco no PlaidCloud Lakehouse, consulte O que são instantâneo, segmento e bloco?.


Veja também:

- [FUSE_SNAPSHOT](../fuse-snapshot/)
- [FUSE_SEGMENT](../fuse-segment/)
- [FUSE_BLOCK](../fuse-block/)

## Sintaxe SQL

```sql
FUSE_COLUMN('<database_name>', '<table_name>'[, '<snapshot_id>'])
```

## Exemplos de SQL

```sql
CREATE TABLE mytable(c int);
INSERT INTO mytable values(1);
INSERT INTO mytable values(2);

SELECT * FROM FUSE_COLUMN('default', 'mytable');

---
┌──────────────────────────────────┬────────────────────────────┬─────────────────────────────────────────────────────────┬────────────┬───────────┬───────────┬─────────────┬─────────────┬───────────┬──────────────┬──────────────────┐
│ snapshot_id                      │ timestamp                  │ block_location                                          │ block_size │ file_size │ row_count │ column_name │ column_type │ column_id │ block_offset │ bytes_compressed │
├──────────────────────────────────┼────────────────────────────┼─────────────────────────────────────────────────────────┼────────────┼───────────┼───────────┼─────────────┼─────────────┼───────────┼──────────────┼──────────────────┤
│ 3faefc1a9b6a48f388a8b59228dd06c1 │ 2023-07-18 03:06:30.276502 │ 1/118746/_b/44df130c207745cb858928135d39c1c0_v2.parquet │          4 │       196 │         1 │ c           │ Int32       │         0 │            8 │               14 │
│ 3faefc1a9b6a48f388a8b59228dd06c1 │ 2023-07-18 03:06:30.276502 │ 1/118746/_b/b6f8496d7e3f4f62a89c09572840cf70_v2.parquet │          4 │       196 │         1 │ c           │ Int32       │         0 │            8 │               14 │
└──────────────────────────────────┴────────────────────────────┴─────────────────────────────────────────────────────────┴────────────┴───────────┴───────────┴─────────────┴─────────────┴───────────┴──────────────┴──────────────────┘
```
