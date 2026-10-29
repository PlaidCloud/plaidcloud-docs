---
title: FUSE_BLOCK (Lakehouse v1)
description: FUSE_BLOCK gibt die Blockinformationen des neuesten oder eines angegebenen Snapshots einer Tabelle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-block.md
---

Gibt die Blockinformationen des neuesten oder eines angegebenen Snapshots einer Tabelle zurück. Weitere Informationen dazu, was ein Block in PlaidCloud Lakehouse ist, finden Sie unter "Was sind Snapshot, Segment und Block?".

Der Befehl gibt die Speicherortinformationen jeder Parquet-Datei zurück, auf die ein Snapshot verweist. So können nachgelagerte Anwendungen auf die in den Dateien gespeicherten Daten zugreifen und sie verarbeiten.

Siehe auch:

- [FUSE_SNAPSHOT](../fuse-snapshot/)
- [FUSE_SEGMENT](../fuse-segment/)

## SQL-Syntax

```sql
FUSE_BLOCK('<database_name>', '<table_name>'[, '<snapshot_id>'])
```

## SQL-Beispiele

```sql
CREATE TABLE mytable(c int);
INSERT INTO mytable values(1);
INSERT INTO mytable values(2); 

SELECT * FROM FUSE_BLOCK('default', 'mytable');

---
┌──────────────────────────────────┬────────────────────────────┬────────────────────────────────────────────────────┬────────────┬────────────────────────────────────────────────────┬───────────────────┐
│ snapshot_id                      │ timestamp                  │ block_location                                     │ block_size │ bloom_filter_location                              │ bloom_filter_size │
├──────────────────────────────────┼────────────────────────────┼────────────────────────────────────────────────────┼────────────┼────────────────────────────────────────────────────┼───────────────────┤
│ 51e84b56458f44269b05a059b364a659 │ 2022-09-15 07:14:14.137268 │ 1/7/_b/39a6dbbfd9b44ad5a8ec8ab264c93cf5_v0.parquet │          4 │ 1/7/_i/39a6dbbfd9b44ad5a8ec8ab264c93cf5_v1.parquet │               221 │
│ 51e84b56458f44269b05a059b364a659 │ 2022-09-15 07:14:14.137268 │ 1/7/_b/d0ee9688c4d24d6da86acd8b0d6f4fad_v0.parquet │          4 │ 1/7/_i/d0ee9688c4d24d6da86acd8b0d6f4fad_v1.parquet │               219 │
└──────────────────────────────────┴────────────────────────────┴────────────────────────────────────────────────────┴────────────┴────────────────────────────────────────────────────┴───────────────────┘
```
