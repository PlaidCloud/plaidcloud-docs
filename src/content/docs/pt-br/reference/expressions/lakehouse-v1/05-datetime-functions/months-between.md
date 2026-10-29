---
title: MONTHS_BETWEEN (Lakehouse v1)
description: MONTHS_BETWEEN — retorna o número de meses entre date1 e date2.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/months-between.md
---

Retorna o número de meses entre *date1* e *date2*.

## Sintaxe do Analyze

```python
func.months_between(<date1>, <date2>)
```

## Exemplos do Analyze

```python
func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ 1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

```python
func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ -1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
MONTHS_BETWEEN( <date1>, <date2> )
```

## Argumentos

*date1* e *date2* podem ser do tipo DATE, do tipo TIMESTAMP ou uma combinação dos dois.

## Tipo de retorno

A função retorna um valor FLOAT de acordo com as seguintes regras:

- Se *date1* for anterior a *date2*, a função retorna um valor negativo; caso contrário, retorna um valor positivo.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-03-15'::DATE,
                    '2024-02-15'::DATE),
        MONTHS_BETWEEN('2024-02-15'::DATE,
                    '2024-03-15'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-03-15'::date, '2024-02-15'::date): 1
    months_between('2024-02-15'::date, '2024-03-15'::date): -1
    ```

- Se *date1* e *date2* caírem no mesmo dia de seus respectivos meses, ou se ambas forem o último dia de seus respectivos meses, o resultado é um inteiro. Caso contrário, a função calcula a parte fracionária do resultado com base em um mês de 31 dias.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-29'::DATE),
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-31'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-02-29'::date, '2024-01-29'::date): 1
    months_between('2024-02-29'::date, '2024-01-31'::date): 1

    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-01-01'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-08-05'::date, '2024-01-01'::date): 7.129032258064516
    ```

- Se *date1* e *date2* forem a mesma data, a função ignora quaisquer componentes de hora e retorna 0.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-08-05'::DATE),
        MONTHS_BETWEEN('2024-08-05 02:00:00'::TIMESTAMP,
                    '2024-08-05 01:00:00'::TIMESTAMP);

    -[ RECORD 1 ]-----------------------------------
                                months_between('2024-08-05'::date, '2024-08-05'::date): 0
    months_between('2024-08-05 02:00:00'::timestamp, '2024-08-05 01:00:00'::timestamp): 0
    ```
