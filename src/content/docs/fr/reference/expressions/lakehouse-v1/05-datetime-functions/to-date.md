---
title: TO_DATE (Lakehouse v1)
description: "TO_DATE — convertit une expression en date, notamment :"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-date.md
---

Convertit une expression en date, notamment :

- **Conversion d'une chaîne au format horodatage en date** : extrait une date de la chaîne donnée.

- **Conversion d'un entier en date** : interprète l'entier comme le nombre de jours avant (nombre négatif) ou après (nombre positif) l'époque Unix (minuit le 1er janvier 1970). À noter : une valeur de type Date est comprise entre `1000-01-01` et `9999-12-31`. PlaidCloud Lakehouse renvoie une erreur si vous exécutez « SELECT TO_DATE(9999999999999999999) ».

- **Conversion d'une chaîne en date selon un format donné** : la fonction prend deux arguments et convertit la première chaîne en date d'après le format indiqué dans la seconde. Pour personnaliser le format de date et d'heure dans PlaidCloud Lakehouse, vous pouvez utiliser des spécificateurs. Pour la liste complète des spécificateurs pris en charge, voir Mise en forme de la date et de l'heure.

Les formats de date s'expriment avec la spécification `strftime`. Voir la [référence rapide](https://devhints.io/strftime).

Voir aussi : [TO_TIMESTAMP](../to-timestamp)

## Paramètres strftime

### Référence rapide

#### Date

| Exemple         | Résultat               |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Heure

| Exemple         | Résultat               |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Date

| Symbole | Exemple                  | Domaine                |
| ---    | ---                      | ---                     |
| `%a`   | `Sun`                    | **Jour de la semaine**  |
| `%A`   | `Sunday`                 |                         |
| `%w`   | `0`..`6` _(le dimanche vaut 0)_ |                  |
| ---    | ---                      | ---                     |
| `%y`   | `13`                     | **Année**               |
| `%Y`   | `2013`                   |                         |
| ---    | ---                      | ---                     |
| `%b`   | `Jan`                    | **Mois**                |
| `%B`   | `January`                |                         |
| `%m`   | `01`..`12`               |                         |
| ---    | ---                      | ---                     |
| `%d`   | `01`..`31`               | **Jour**                |
| `%e`   | `1`..`31`                |                         |


### Heure

| Symbole | Exemple      | Domaine                  |
| ---    | ---          | ---                      |
| `%l`   | `1`          | Heure                    |
| `%H`   | `00`..`23`   | Heure sur 24 h           |
| `%I`   | `01`..`12`   | Heure sur 12 h           |
| --     | ---          | ---                      |
| `%M`   | `00`..`59`   | Minute                   |
| `%S`   | `00`..`60`   | Seconde                  |
| ---    | ---          | ---                      |
| `%p`   | `AM`         | AM ou PM                 |
| `%Z`   | `+08`        | Fuseau horaire           |
| ---    | ---          | ---                      |
| `%j`   | `001`..`366` | Jour de l'année          |
| `%%`   | `%`          | Caractère % littéral     |


## Syntaxe Analyze

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Exemples Analyze

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

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

## Type de retour

La fonction renvoie une date au format « YYYY-MM-DD » :

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

Pour reconvertir la date renvoyée en chaîne, utilisez la fonction [DATE_FORMAT](../date-format) :

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## Exemples SQL

### Exemples SQL 1 : conversion d'une chaîne au format horodatage

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

### Exemples SQL 2 : conversion d'un entier

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### Exemples SQL 3 : conversion d'une chaîne selon un format donné

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```
