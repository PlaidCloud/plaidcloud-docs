---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE — 접미사(KiB, MiB 등)가 붙은 읽기 쉬운 크기를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

접미사(KiB, MiB 등)가 붙은 읽기 쉬운 크기를 반환합니다.

## Analyze 구문

```python
func.humanize_size(x);
```

## Analyze 예제

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
HUMANIZE_SIZE(x);
```

## 인수

| 인수 | 설명 |
|-----------|----------------------------|
| x         | 숫자 크기입니다.        |


## 반환 유형

문자열.

## SQL 예제

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
