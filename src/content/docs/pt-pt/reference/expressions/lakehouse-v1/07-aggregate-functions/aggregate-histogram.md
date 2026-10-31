---
title: HISTOGRAM (Lakehouse v1)
description: HISTOGRAM — gera um histograma da distribuição dos dados com uma estratégia de agrupamento em intervalos de igual altura.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-histogram.md
---

Gera um histograma da distribuição dos dados com uma estratégia de agrupamento em intervalos de "igual altura".

## Sintaxe do Analyze

```python
func.histogram(<expr>)
```

## Exemplos do Analyze
Consulte o exemplo de SQL para obter mais detalhes

## Sintaxe SQL

```sql
HISTOGRAM(<expr>)

-- The following two forms are equivalent:
HISTOGRAM(<max_num_buckets>)(<expr>)
HISTOGRAM(<expr> [, <max_num_buckets>])
```

| Parâmetro         | Descrição                                                                           |
|-------------------|-------------------------------------------------------------------------------------|
| `expr`            | O tipo de dados de `expr` deve ser ordenável.                                       |
| `max_num_buckets` | Inteiro positivo opcional que especifica o número máximo de intervalos. O valor predefinido é 128. |

## Tipo de retorno

Devolve uma cadeia de caracteres vazia ou um objeto JSON com a seguinte estrutura:

- **buckets**: lista de intervalos com informações detalhadas:
  - **lower**: limite inferior do intervalo.
  - **upper**: limite superior do intervalo.
  - **count**: número de elementos no intervalo.
  - **pre_sum**: contagem acumulada de elementos até ao intervalo atual.
  - **ndv**: número de valores distintos no intervalo.

## Exemplos de SQL

Este exemplo mostra como a função HISTOGRAM analisa a distribuição dos valores de `c_int` na tabela `histagg`, devolvendo os limites dos intervalos, as contagens de valores distintos, as contagens de elementos e as contagens acumuladas:

```sql
CREATE TABLE histagg (
  c_id INT,
  c_tinyint TINYINT,
  c_smallint SMALLINT,
  c_int INT
);

INSERT INTO histagg VALUES
  (1, 10, 20, 30),
  (1, 11, 21, 33),
  (1, 11, 12, 13),
  (2, 21, 22, 23),
  (2, 31, 32, 33),
  (2, 10, 20, 30);

SELECT HISTOGRAM(c_int) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                              histogram(c_int)                                                                                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"13","ndv":1,"count":1,"pre_sum":0},{"lower":"23","upper":"23","ndv":1,"count":1,"pre_sum":1},{"lower":"30","upper":"30","ndv":1,"count":2,"pre_sum":2},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

O resultado é devolvido como uma matriz JSON:

```json
[
  {
    "lower": "13",
    "upper": "13",
    "ndv": 1,
    "count": 1,
    "pre_sum": 0
  },
  {
    "lower": "23",
    "upper": "23",
    "ndv": 1,
    "count": 1,
    "pre_sum": 1
  },
  {
    "lower": "30",
    "upper": "30",
    "ndv": 1,
    "count": 2,
    "pre_sum": 2
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```

Este exemplo mostra como `HISTOGRAM(2)` agrupa os valores de c_int em dois intervalos:

```sql
SELECT HISTOGRAM(2)(c_int) FROM histagg;
-- Or
SELECT HISTOGRAM(c_int, 2) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  histogram(2)(c_int)                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"30","ndv":3,"count":4,"pre_sum":0},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

O resultado é devolvido como uma matriz JSON:

```json
[
  {
    "lower": "13",
    "upper": "30",
    "ndv": 3,
    "count": 4,
    "pre_sum": 0
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```
