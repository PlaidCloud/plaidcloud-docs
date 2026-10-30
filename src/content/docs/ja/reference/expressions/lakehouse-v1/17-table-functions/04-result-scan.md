---
title: RESULT_SCAN（Lakehouse v1）
description: RESULT_SCAN — 同じセッション内で以前に実行したコマンドの結果セットを、テーブルであるかのように返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

同じセッション内で以前に実行したコマンドの結果セットを、テーブルであるかのように返します。


## SQLの構文

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## SQLの例

簡単なテーブルを作成します。

```sql
CREATE TABLE t1(a int);
```

値を挿入します。

```sql
INSERT INTO t1(a) VALUES (1), (2), (3);
```

### `result_scan`


```bash
SELECT * FROM t1 ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```


```bash
SELECT * FROM RESULT_SCAN(LAST_QUERY_ID()) ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```
