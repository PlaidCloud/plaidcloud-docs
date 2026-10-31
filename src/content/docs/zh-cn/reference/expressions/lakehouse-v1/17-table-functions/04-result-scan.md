---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN：将同一会话中先前命令的结果集作为表返回。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

将同一会话中先前命令的结果集作为表返回。


## SQL 语法

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## SQL 示例

创建一个简单的表：

```sql
CREATE TABLE t1(a int);
```

插入一些值；

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
