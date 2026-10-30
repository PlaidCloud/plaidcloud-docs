---
title: IGNORE（Lakehouse v1）
description: IGNORE — INSERT IGNORE文を使用すると、エラーの原因となる無効なデータを含む行は無視され、有効なデータを含む行がテーブルに挿入されます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

INSERT IGNORE文を使用すると、エラーの原因となる無効なデータを含む行は無視され、有効なデータを含む行がテーブルに挿入されます。

## SQLの構文

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
