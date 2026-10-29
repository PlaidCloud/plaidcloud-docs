---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64：生成 64 位 SipHash 哈希值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

生成 64 位 [SipHash](https://en.wikipedia.org/wiki/SipHash) 哈希值。

## Analyze 语法

```python
func.siphash64(<expr>)
```

## Analyze 示例

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## SQL 语法

```sql
SIPHASH64(<expr>)
```

## 别名

- [SIPHASH](../siphash)

## SQL 示例

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
