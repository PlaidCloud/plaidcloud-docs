---
title: TO_DATE (Lakehouse v1)
description: TO_DATE — convierte una expresión en una fecha, incluyendo las conversiones siguientes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-date.md
---

Convierte una expresión en una fecha, incluyendo:

- **Convertir una cadena con formato de marca de tiempo en una fecha**: extrae una fecha de la cadena dada.

- **Convertir un entero en una fecha**: interpreta el entero como el número de días anteriores (si es negativo) o posteriores (si es positivo) a la época Unix (medianoche del 1 de enero de 1970). Tenga en cuenta que un valor de fecha va de `1000-01-01` a `9999-12-31`. PlaidCloud Lakehouse devolvería un error si ejecuta "SELECT TO_DATE(9999999999999999999)".

- **Convertir una cadena en una fecha con el formato especificado**: la función recibe dos argumentos y convierte la primera cadena en una fecha según el formato indicado en la segunda cadena. Para personalizar el formato de fecha y hora en PlaidCloud Lakehouse se pueden usar especificadores. Para ver una lista completa de los especificadores admitidos, consulte Formateo de fecha y hora.

Los formatos de fecha se expresan con la especificación `strftime`. Consulte la [referencia rápida](https://devhints.io/strftime).

Consulte también: [TO_TIMESTAMP](../to-timestamp)

## Parámetros de strftime

### Referencia rápida

#### Fecha

| Ejemplo         | Resultado              |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Hora

| Ejemplo         | Resultado              |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Fecha

| Símbolo | Ejemplo                  | Área        |
| ---    | ---                      | ---         |
| `%a`   | `Sun`                    | **Día de la semana** |
| `%A`   | `Sunday`                 |             |
| `%w`   | `0`..`6` _(el domingo es 0)_ |             |
| ---    | ---                      | ---         |
| `%y`   | `13`                     | **Año**    |
| `%Y`   | `2013`                   |             |
| ---    | ---                      | ---         |
| `%b`   | `Jan`                    | **Mes**   |
| `%B`   | `January`                |             |
| `%m`   | `01`..`12`               |             |
| ---    | ---                      | ---         |
| `%d`   | `01`..`31`               | **Día**     |
| `%e`   | `1`..`31`                |             |


### Hora

| Símbolo | Ejemplo      | Área                |
| ---    | ---          | ---                 |
| `%l`   | `1`          | Hora                |
| `%H`   | `00`..`23`   | Hora (24 h)         |
| `%I`   | `01`..`12`   | Hora (12 h)         |
| --     | ---          | ---                 |
| `%M`   | `00`..`59`   | Minuto              |
| `%S`   | `00`..`60`   | Segundo             |
| ---    | ---          | ---                 |
| `%p`   | `AM`         | AM o PM             |
| `%Z`   | `+08`        | Zona horaria        |
| ---    | ---          | ---                 |
| `%j`   | `001`..`366` | Día del año         |
| `%%`   | `%`          | Carácter % literal  |


## Sintaxis de Analyze

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Ejemplos de Analyze

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
-- Convert a timestamp-format string
TO_DATE('<timestamp_expr>')

-- Convert an integer
TO_DATE(<integer>)

-- Convert a string using the given format
TO_DATE('<string>', '<format>')
```

## Alias

- [DATE](../date)
- [STR_TO_DATE](../str-to-date)

## Tipo de valor devuelto

La función devuelve una fecha en el formato "YYYY-MM-DD":

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

Para convertir la fecha devuelta de nuevo en una cadena, use la función [DATE_FORMAT](../date-format):

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## Ejemplos de SQL

### Ejemplos de SQL 1: conversión de una cadena con formato de marca de tiempo

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

### Ejemplos de SQL 2: conversión de un entero

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### Ejemplos de SQL 3: conversión de una cadena con el formato dado

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```
