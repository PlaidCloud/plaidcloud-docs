---
title: TRANSLATE（Lakehouse v1）
description: TRANSLATE——通过按提供的映射将特定字符替换为对应的字符，来转换给定字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

通过按提供的映射将特定字符替换为对应的字符，来转换给定字符串。

## Analyze 语法

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Analyze 示例

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## SQL 语法

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| 参数                 | 说明                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `<inputString>`           | 要转换的输入字符串。                                                             |
| `<charactersToReplace>`   | 包含要在输入字符串中替换的字符的字符串。                            |
| `<replacementCharacters>` | 包含与 `<charactersToReplace>` 中字符一一对应的替换字符的字符串。 |

## SQL 示例

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
