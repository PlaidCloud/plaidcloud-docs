---
title: TO_HEX (Lakehouse v1)
description: TO_HEX：对于字符串参数 str，TO_HEX() 返回 str 的十六进制字符串表示，其中 str 中每个字符的每个字节都会转换为两位十六进制数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-hex.md
---

对于字符串参数 str，TO_HEX() 返回 str 的十六进制字符串表示，其中 str 中每个字符的每个字节都会转换为两位十六进制数字。UNHEX() 函数执行此操作的逆运算。

对于数值参数 N，TO_HEX() 返回将 N 的值视为 longlong (BIGINT) 数字后的十六进制字符串表示。

## Analyze 语法

```python
func.to_hex(<expr>)
```

## Analyze 示例

```python
func.to_hex('abc')

┌────────────────────┐
│ func.to_hex('abc') │
├────────────────────┤
│ 616263             │
└────────────────────┘
```

## SQL 语法

```sql
TO_HEX(<expr>)
```

## 别名

- [HEX](../../06-string-functions/hex)

## SQL 示例

```sql
SELECT HEX('abc'), TO_HEX('abc');

┌────────────────────────────┐
│ hex('abc') │ to_hex('abc') │
├────────────┼───────────────┤
│ 616263     │ 616263        │
└────────────────────────────┘

SELECT HEX(255), TO_HEX(255);

┌────────────────────────┐
│ hex(255) │ to_hex(255) │
├──────────┼─────────────┤
│ ff       │ ff          │
└────────────────────────┘
```
