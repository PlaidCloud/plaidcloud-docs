---
title: ORD（Lakehouse v1）
description: ORD——返回字符串最左侧字符的字符码（单字节字符为 ASCII 值，多字节字符为计算得出的值）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ord.md
---

如果最左侧的字符不是多字节字符，ORD() 返回与 ASCII() 函数相同的值。

如果字符串 str 最左侧的字符是多字节字符，则返回该字符的字符码，
根据其组成字节的数值按以下公式计算：

```sql
  (1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

## Analyze 语法

```python
func.ord(<str>)
```

## Analyze 示例

```python
func.ord('2')
┌────────────────┐
│ func.ord('2)   │
├────────────────┤
│             50 │
└────────────────┘
```

## SQL 语法

```sql
ORD(<str>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<str>`   | 字符串。 |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT ORD('2')
┌────────┐
│ ORD(2) │
├────────┤
│     50 │
└────────┘
```
