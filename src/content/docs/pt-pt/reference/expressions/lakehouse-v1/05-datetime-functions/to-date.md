---
title: TO_DATE (Lakehouse v1)
description: TO_DATE — converte uma expressão numa data, incluindo os seguintes casos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-date.md
---

Converte uma expressão numa data, incluindo:

- **Converter uma cadeia de caracteres em formato de carimbo de data/hora numa data**: extrai uma data da cadeia indicada.

- **Converter um número inteiro numa data**: interpreta o número inteiro como o número de dias antes (se for negativo) ou depois (se for positivo) da época Unix (meia-noite de 1 de janeiro de 1970). Tenha em atenção que um valor de data varia entre `1000-01-01` e `9999-12-31`. O PlaidCloud Lakehouse devolve um erro se executar "SELECT TO_DATE(9999999999999999999)".

- **Converter uma cadeia de caracteres numa data com o formato especificado**: a função recebe dois argumentos e converte a primeira cadeia numa data com base no formato especificado na segunda cadeia. Para personalizar o formato de data e hora no PlaidCloud Lakehouse, podem ser usados especificadores. Para uma lista completa dos especificadores suportados, consulte Formatação de data e hora.

Os formatos de data são expressos com a especificação `strftime`. Consulte a [referência rápida](https://devhints.io/strftime).

Ver também: [TO_TIMESTAMP](../to-timestamp)

## Parâmetros do strftime

### Referência rápida

#### Data

| Exemplo         | Resultado              |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Hora

| Exemplo         | Resultado              |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Data

| Símbolo | Exemplo                  | Área                 |
| ---    | ---                      | ---                  |
| `%a`   | `Sun`                    | **Dia da semana**    |
| `%A`   | `Sunday`                 |                      |
| `%w`   | `0`..`6` _(o domingo é 0)_ |                    |
| ---    | ---                      | ---                  |
| `%y`   | `13`                     | **Ano**              |
| `%Y`   | `2013`                   |                      |
| ---    | ---                      | ---                  |
| `%b`   | `Jan`                    | **Mês**              |
| `%B`   | `January`                |                      |
| `%m`   | `01`..`12`               |                      |
| ---    | ---                      | ---                  |
| `%d`   | `01`..`31`               | **Dia**              |
| `%e`   | `1`..`31`                |                      |


### Hora

| Símbolo | Exemplo      | Área                    |
| ---    | ---          | ---                     |
| `%l`   | `1`          | Hora                    |
| `%H`   | `00`..`23`   | Hora (formato 24 h)     |
| `%I`   | `01`..`12`   | Hora (formato 12 h)     |
| --     | ---          | ---                     |
| `%M`   | `00`..`59`   | Minuto                  |
| `%S`   | `00`..`60`   | Segundo                 |
| ---    | ---          | ---                     |
| `%p`   | `AM`         | AM ou PM                |
| `%Z`   | `+08`        | Fuso horário            |
| ---    | ---          | ---                     |
| `%j`   | `001`..`366` | Dia do ano              |
| `%%`   | `%`          | Carácter % literal      |


## Sintaxe do Analyze

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Exemplos do Analyze

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
-- Convert a timestamp-format string
TO_DATE('<timestamp_expr>')

-- Convert an integer
TO_DATE(<integer>)

-- Convert a string using the given format
TO_DATE('<string>', '<format>')
```

## Aliases

- [DATE](../date)
- [STR_TO_DATE](../str-to-date)

## Tipo de retorno

A função devolve uma data no formato "YYYY-MM-DD":

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

Para converter a data devolvida novamente numa cadeia de caracteres, utilize a função [DATE_FORMAT](../date-format):

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## Exemplos SQL

### Exemplos SQL 1: conversão de uma cadeia de caracteres em formato de carimbo de data/hora

```sql
SELECT TO_DATE('2022-01-02T01:12:00+07:00'), STR_TO_DATE('2022-01-02T01:12:00+07:00');

┌─────────────────────────────────────────────────────────────────────────────────┐
│ to_date('2022-01-02t01:12:00+07:00') │ str_to_date('2022-01-02t01:12:00+07:00') │
├──────────────────────────────────────┼──────────────────────────────────────────┤
│ 2022-01-01                           │ 2022-01-01                               │
└─────────────────────────────────────────────────────────────────────────────────┘

SELECT TO_DATE('2022-01-02'), STR_TO_DATE('2022-01-02');

┌───────────────────────────────────────────────────┐
│ to_date('2022-01-02') │ str_to_date('2022-01-02') │
├───────────────────────┼───────────────────────────┤
│ 2022-01-02            │ 2022-01-02                │
└───────────────────────────────────────────────────┘
```

### Exemplos SQL 2: conversão de um número inteiro

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### Exemplos SQL 3: conversão de uma cadeia de caracteres com o formato indicado

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```
