---
title: CURRENT_USER（Lakehouse v1）
description: CURRENT_USER — サーバーが現在のクライアントの認証に使用したアカウントの、ユーザー名とホスト名の組み合わせを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

サーバーが現在のクライアントの認証に使用したアカウントの、ユーザー名とホスト名の組み合わせを返します。このアカウントによって、アクセス権限が決まります。戻り値は、文字セットがutf8の文字列です。

## Analyzeの構文

```python
func.current_user()
```

## Analyzeの例

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## SQLの構文

```sql
CURRENT_USER()
```

## SQLの例

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
