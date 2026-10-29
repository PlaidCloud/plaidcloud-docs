---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER — 서버가 현재 클라이언트를 인증하는 데 사용한 계정의 사용자 이름과 호스트 이름 조합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

서버가 현재 클라이언트를 인증하는 데 사용한 계정의 사용자 이름과 호스트 이름 조합을 반환합니다. 이 계정이 사용자의 액세스 권한을 결정합니다. 반환값은 utf8 문자 집합의 문자열입니다.

## Analyze 구문

```python
func.current_user()
```

## Analyze 예제

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## SQL 구문

```sql
CURRENT_USER()
```

## SQL 예제

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
