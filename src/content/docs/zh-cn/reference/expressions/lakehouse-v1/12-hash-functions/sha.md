---
title: SHA (Lakehouse v1)
description: SHA：按 RFC 3174（安全哈希算法）所述，计算字符串的 SHA-1 160 位校验和。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

按 RFC 3174（安全哈希算法）所述，计算字符串的 SHA-1 160 位校验和。返回值为 40 个十六进制数字组成的字符串；如果参数为 NULL，则返回 NULL。

## Analyze 语法

```python
func.sha(<expr>)
```

## Analyze 示例

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
SHA(<expr>)
```

## 别名

- [SHA1](../sha1)

## SQL 示例

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
