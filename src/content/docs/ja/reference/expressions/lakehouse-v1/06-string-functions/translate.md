---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — 指定した文字を、対応する置換文字に置き換えて文字列を変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

指定されたマッピングに従って、特定の文字を対応する置換文字に置き換えることで、与えられた文字列を変換します。

## Analyze の構文

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Analyze の例

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## SQL構文

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| パラメーター                 | 説明                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `<inputString>`           | 変換対象の入力文字列。                                                             |
| `<charactersToReplace>`   | 入力文字列内で置換する文字を含む文字列。                            |
| `<replacementCharacters>` | `<charactersToReplace>` の各文字に対応する置換文字を含む文字列。 |

## SQLの例

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
