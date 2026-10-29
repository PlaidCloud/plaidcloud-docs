---
title: QUOTE (Lakehouse v1)
description: QUOTE — 文字列を引用符で囲み、SQL ステートメント内で適切にエスケープされたデータ値として使用できる結果を生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

文字列を引用符で囲み、SQL ステートメント内で適切にエスケープされたデータ値として使用できる結果を生成します。 

## Analyze の構文

```python
func.quote(<str>)
```

## Analyze の例

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## SQL構文

```sql
QUOTE(<str>)
```

## SQLの例

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
