---
title: TRIM (Lakehouse v1)
description: TRIM：返回去除开头或末尾指定删除字符串后的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

返回去除开头或末尾指定删除字符串后的字符串。如果省略删除字符串，则删除空格。

Analyze 函数会自动去除开头和末尾的空格。

## Analyze 语法

```python
func.trim(str)
```

## Analyze 示例

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## SQL 语法

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## SQL 示例

请注意，本节中的所有示例都将返回字符串 'databend'。

以下示例从字符串 'xxxdatabendxxx' 中删除开头和末尾的字符串 'xxx'：

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

以下示例从字符串 'xxxdatabend' 中删除开头的字符串 'xxx'：

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
以下示例从字符串 'databendxxx' 中删除末尾的字符串 'xxx'：

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

如果未指定删除字符串，函数会删除开头和末尾的所有空格。以下示例删除开头和/或末尾的空格：

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
