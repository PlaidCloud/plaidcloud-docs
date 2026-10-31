---
title: REPLACE (Lakehouse v1)
description: REPLACE — 文字列 str に含まれる文字列 from_str をすべて文字列 to_str に置き換えた結果を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

文字列 str に含まれる文字列 from_str をすべて文字列 to_str に置き換えた結果を返します。

## Analyze の構文

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Analyze の例

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## SQL構文

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## 引数

| 引数    | 説明      |
|--------------|------------------|
| `<str>`      | 文字列。      |
| `<from_str>` | 置換前の文字列。 |
| `<to_str>`   | 置換後の文字列。   |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
