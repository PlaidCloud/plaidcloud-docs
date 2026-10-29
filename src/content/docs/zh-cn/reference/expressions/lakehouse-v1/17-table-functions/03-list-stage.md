---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE：列出暂存区中的文件。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

列出暂存区中的文件。借助此函数，可以根据扩展名筛选暂存区中的文件，并获取每个文件的完整详细信息。该函数类似于 DDL 命令 LIST STAGE FILES，但可让您通过 SELECT 语句灵活地检索特定的文件信息，例如文件名、大小、MD5 哈希、最后修改时间戳和创建者，而不是全部文件信息。

## SQL 语法

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

其中：

### 内部暂存区

```sql
internalStage ::= @<internal_stage_name>[/<path>]
```

### 外部暂存区

```sql
externalStage ::= @<external_stage_name>[/<path>]
```

### 用户暂存区

```sql
userStage ::= @~[/<path>]
```

### PATTERN

请参阅 COPY INTO table。


## SQL 示例

```sql
SELECT * FROM list_stage(location => '@my_stage/', pattern => '.*[.]log');
┌────────────────┬──────┬────────────────────────────────────┬───────────────────────────────┬─────────┐
│      name      │ size │                md5                 │         last_modified         │ creator │
├────────────────┼──────┼────────────────────────────────────┼───────────────────────────────┼─────────┤
│ 2023/meta.log  │  475 │ "4208ff530b252236e14b3cd797abdfbd" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
│ 2023/query.log │ 1348 │ "1c6654b207472c277fc8c6207c035e18" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
└────────────────┴──────┴────────────────────────────────────┴───────────────────────────────┴─────────┘

-- Equivalent to the following statement:
LIST @my_stage PATTERN = '.log';
```
