---
title: REPEAT (Lakehouse v1)
description: REPEAT — 문자열 str을 count번 반복한 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

문자열 str을 count번 반복한 문자열을 반환합니다. count가 1보다 작으면 빈 문자열을 반환합니다. str 또는 count가 NULL이면 NULL을 반환합니다.

## Analyze 구문

```python
func.repeat(<str>, <count>)
```

## Analyze 예제

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## SQL 구문

```sql
REPEAT(<str>, <count>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<str>`   | 문자열입니다. |
| `<count>` | 숫자입니다. |

## SQL 예제

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
