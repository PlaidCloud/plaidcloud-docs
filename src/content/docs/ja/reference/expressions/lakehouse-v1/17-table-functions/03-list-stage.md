---
title: LIST_STAGE（Lakehouse v1）
description: LIST_STAGE — ステージ内のファイルを一覧表示します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

ステージ内のファイルを一覧表示します。拡張子に基づいてステージ内のファイルをフィルターし、各ファイルの詳細情報を取得できます。この関数はDDLコマンドのLIST STAGE FILESに似ていますが、すべてのファイル情報ではなく、ファイル名、サイズ、MD5ハッシュ、最終更新日時、作成者など、必要なファイル情報をSELECT文で柔軟に取得できます。

## SQLの構文

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

各項目の意味は次のとおりです。

### Internalstage

```sql
internalStage ::= @<internal_stage_name>[/<path>]
```

### Externalstage

```sql
externalStage ::= @<external_stage_name>[/<path>]
```

### Userstage

```sql
userStage ::= @~[/<path>]
```

### PATTERN

COPY INTO tableを参照してください。


## SQLの例

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
