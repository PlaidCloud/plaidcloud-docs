---
title: DICT_GET（Lakehouse v1）
description: DICT_GET — 指定したキー式を使用して、ディクショナリから指定した属性の値を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

指定したキー式を使用して、ディクショナリから指定した属性の値を取得します。

## SQLの構文

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| パラメータ | 説明                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | ディクショナリの名前。                                                                                                                                       |
| attr_name | 値を取得するディクショナリ内の属性の名前。                                                                              |
| key_expr  | ディクショナリ内の特定のエントリを特定するためのキー式。対応するデータを取得するための、ディクショナリの主キーの値を表します。 |

## SQLの例
