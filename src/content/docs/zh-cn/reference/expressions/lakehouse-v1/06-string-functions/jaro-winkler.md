---
title: JARO_WINKLER（Lakehouse v1）
description: JARO_WINKLER——计算两个字符串之间的 Jaro-Winkler 距离。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

计算两个字符串之间的 [Jaro-Winkler 距离](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)。它常用于衡量字符串之间的相似度，取值范围为 0.0（完全不相似）到 1.0（字符串完全相同）。

## Analyze 语法

```python
func.jaro_winkler(<string1>, <string2>)
```

## Analyze 示例

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## SQL 语法

```sql
JARO_WINKLER(<string1>, <string2>)
```

## SQL 示例

JARO_WINKLER 函数返回一个 FLOAT64 值，表示两个输入字符串之间的相似度。返回值遵循以下规则：

- 相似度范围：结果范围为 0.0（完全不相似）到 1.0（完全相同）。

    ```sql
    SELECT JARO_WINKLER('databend', 'Databend') AS similarity;

    ┌────────────────────┐
    │     similarity     │
    ├────────────────────┤
    │ 0.9166666666666666 │
    └────────────────────┘

    SELECT JARO_WINKLER('databend', 'database') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │        0.9 │
    └────────────┘
    ```
- NULL 处理：如果 string1 或 string2 为 NULL，则结果为 NULL。

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- 空字符串：
    - 比较两个空字符串返回 1.0。

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - 比较空字符串与非空字符串返回 0.0。

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
