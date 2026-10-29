---
title: FORMAT_BYTES (Lakehouse v2)
description: "PlaidCloud Lakehouse の FORMAT_BYTES 文字列関数の使い方です。バイト数を、適切な単位（B、KB、MB、GB、TB など）を付けた人が読みやすい文字列に変換します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/format-bytes.md
---

バイト数を、適切な単位（B、KB、MB、GB、TB、PB、EB）を付けた人が読みやすい文字列に変換します。1024 を基数とする（バイナリ）計算を使用します。入力が負の値または NULL の場合は NULL を返します。

## Analyze 構文

```python
func.format_bytes(<bytes>)
```

## Analyze の例

```python
func.format_bytes(123456789)

┌──────────────────────────────────┐
│ func.format_bytes(123456789)     │
├──────────────────────────────────┤
│ 117.74 MB                        │
└──────────────────────────────────┘
```

## SQL 構文

```sql
FORMAT_BYTES(<bytes>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<bytes>` | フォーマットするバイト数を表す、非負の BIGINT 整数。 |

## 戻り値の型

VARCHAR

## SQL の例

基本的なフォーマット:

```sql
SELECT format_bytes(0);

┌──────────────────┐
│ format_bytes(0)  │
├──────────────────┤
│ 0 B              │
└──────────────────┘

SELECT format_bytes(123);

┌────────────────────┐
│ format_bytes(123)  │
├────────────────────┤
│ 123 B              │
└────────────────────┘

SELECT format_bytes(1024);

┌─────────────────────┐
│ format_bytes(1024)  │
├─────────────────────┤
│ 1.00 KB             │
└─────────────────────┘

SELECT format_bytes(4096);

┌─────────────────────┐
│ format_bytes(4096)  │
├─────────────────────┤
│ 4.00 KB             │
└─────────────────────┘

SELECT format_bytes(123456789);

┌───��──────────────────────┐
│ format_bytes(123456789)  │
├──────────────────────────┤
│ 117.74 MB                │
└──────────────────────────┘

SELECT format_bytes(10737418240);

┌────────────────────────────┐
│ format_bytes(10737418240)  │
├────────────────────────────┤
│ 10.00 GB                   │
└────────────────────────────┘
```

エッジケース:

```sql
SELECT format_bytes(-1);

┌───────────────────┐
│ format_bytes(-1)  │
├───────────────────┤
│ NULL              │
└───────────────────┘

SELECT format_bytes(NULL);

┌─────────────────────┐
│ format_bytes(NULL)  │
├─────────────────────┤
│ NULL                │
└─────────────────────┘
```

精度と丸め:

```sql
SELECT format_bytes(1536);

┌─────────────────────┐
│ format_bytes(1536)  │
├─────────────────────┤
│ 1.50 KB             │
└─────────────────────┘

SELECT format_bytes(1025);

┌─────────────────────┐
│ format_bytes(1025)  │
├─────────────────────┤
│ 1.00 KB             │
└─────────────────────┘

SELECT format_bytes(1048576 + 52429);

┌──────────────────────────────────┐
│ format_bytes(1048576 + 52429)    │
├──────────────────────────────────┤
│ 1.05 MB                          │
└──────────────────────────────────┘
```

全単位の範囲:

```sql
SELECT format_bytes(512);

┌────────────────────┐
│ format_bytes(512)  │
├────────────────────┤
│ 512 B              │
└────────────────────┘

SELECT format_bytes(2048);

┌─────────────────────┐
│ format_bytes(2048)  │
├─────────────────────┤
│ 2.00 KB             │
└─────────────────────┘

SELECT format_bytes(1572864);

┌──────────────────────────┐
│ format_bytes(1572864)    │
├──────────────────────────┤
│ 1.50 MB                  │
└──────────────────────────┘

SELECT format_bytes(2147483648);

┌────────────────────────────┐
│ format_bytes(2147483648)   │
├────────────────────────────┤
│ 2.00 GB                    │
└────────────────────────────┘

SELECT format_bytes(1099511627776);

┌──────────────────────────────────┐
│ format_bytes(1099511627776)      │
├──────────────────────────────────┤
│ 1.00 TB                          │
└──────────────────────────────────┘

SELECT format_bytes(1125899906842624);

┌─────────────────────────────────────┐
│ format_bytes(1125899906842624)      │
├─────────────────────────────────────┤
│ 1.00 PB                             │
└─────────────────────────────────────┘

SELECT format_bytes(1152921504606846976);

┌────────────────────────────────────────┐
│ format_bytes(1152921504606846976)      │
├────────────────────────────────────────┤
│ 1.00 EB                                │
└────────────────────────────────────────┘
```

実用例（テーブルの監視）:

```sql
CREATE TABLE storage_info (
    table_name VARCHAR(64),
    size_bytes BIGINT
);

INSERT INTO storage_info VALUES
('user_profiles', 1073741824),
('transaction_logs', 5368709120),
('product_catalog', 524288000),
('analytics_data', 2199023255552);

SELECT
    table_name,
    size_bytes,
    format_bytes(size_bytes) AS formatted_size
FROM storage_info
ORDER BY size_bytes DESC;

┌──────────────────┬───────────────┬────────────────┐
│ table_name       │    size_bytes │ formatted_size │
├──────────────────┼───────────────┼────────────────┤
│ analytics_data   │ 2199023255552 │ 2.00 TB        │
│ transaction_logs │    5368709120 │ 5.00 GB        │
│ user_profiles    │    1073741824 │ 1.00 GB        │
│ product_catalog  │     524288000 │ 500.00 MB      │
└──────────────────┴───────────────┴────────────────┘
```
