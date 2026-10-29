---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — 특정 문자를 해당하는 대체 문자로 바꾸어 지정한 문자열을 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

제공된 매핑에 따라 특정 문자를 해당하는 대체 문자로 바꾸어 지정한 문자열을 변환합니다.

## Analyze 구문

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Analyze 예제

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| 매개변수 | 설명 |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `<inputString>`           | 변환할 입력 문자열입니다.                                                             |
| `<charactersToReplace>`   | 입력 문자열에서 바꿀 문자가 들어 있는 문자열입니다.                            |
| `<replacementCharacters>` | `<charactersToReplace>`의 문자에 대응하는 대체 문자가 들어 있는 문자열입니다. |

## SQL 예제

```sql
-- Replace 'd' with '$' in 'databend'
SELECT TRANSLATE('databend', 'd', '$');

---
$ataben$

-- Replace 'd' with 'D' in 'databend'
SELECT TRANSLATE('databend', 'd', 'D');

---
DatabenD

-- Replace 'd' with 'D' and 'e' with 'E' in 'databend'
SELECT TRANSLATE('databend', 'de', 'DE');

---
DatabEnD

-- Remove 'd' from 'databend'
SELECT TRANSLATE('databend', 'd', '');

---
ataben
```
