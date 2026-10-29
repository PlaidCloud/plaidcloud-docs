---
title: Fonctions de fenêtre (Lakehouse v1)
description: "Fonctions de fenêtre SQL de Lakehouse v1 : calculs sur des fenêtres de lignes (classement, cumuls, valeurs suivantes et précédentes)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## Vue d'ensemble 

Une fonction de fenêtre opère sur un groupe de lignes liées (une « fenêtre »).

Pour chaque ligne en entrée, une fonction de fenêtre renvoie une ligne en sortie, qui dépend de la ligne précise transmise à la fonction et des valeurs des autres lignes de la fenêtre.

Il existe deux grands types de fonctions de fenêtre sensibles à l'ordre :

* `Rank-related functions` : les fonctions liées au classement fournissent des informations fondées sur le « rang » d'une ligne. Par exemple, si l'on classe des magasins par bénéfice annuel décroissant, le magasin le plus rentable aura le rang 1, le deuxième magasin le plus rentable le rang 2, et ainsi de suite.

* `Window frame functions` : les fonctions à cadre de fenêtre permettent d'effectuer des opérations glissantes, comme le calcul d'un cumul ou d'une moyenne mobile, sur un sous-ensemble des lignes de la fenêtre.

## Liste des fonctions qui prennent en charge les fenêtres

Le tableau ci-dessous présente toutes les fonctions de fenêtre.

| Nom de la fonction                                                    | Catégorie    | Fenêtre | Cadre de fenêtre | Remarques |
|-----------------------------------------------------------------------|--------------|---------|------------------|-----------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | Générale     | ✔       |                  |           |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | Générale     | ✔       | ✔                |           |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | Générale     | ✔       | ✔                |           |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | Générale     | ✔       | ✔                |           |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | Générale     | ✔       | ✔                |           |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | Générale     | ✔       |                  |           |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | Générale     | ✔       |                  |           |
| [MAX](../07-aggregate-functions/aggregate-max)                        | Générale     | ✔       | ✔                |           |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | Générale     | ✔       | ✔                |           |
| [MIN](../07-aggregate-functions/aggregate-min)                        | Générale     | ✔       | ✔                |           |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | Générale     | ✔       | ✔                |           |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | Générale     | ✔       | ✔                |           |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | Générale     | ✔       | ✔                |           |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | Générale     | ✔       | ✔                |           |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | Générale     | ✔       | ✔                |           |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | Générale     | ✔       | ✔                |           |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | Générale     | ✔       | ✔                |           |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | Générale     | ✔       | ✔                |           |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | Générale     | ✔       | ✔                |           |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | Générale     | ✔       | ✔                |           |
| [CUME_DIST](cume-dist)                                                | Liée au classement | ✔ |                  |           |
| [PERCENT_RANK](percent-rank/)                                         | Liée au classement | ✔ | ✔                |           |
| [DENSE_RANK](dense-rank)                                              | Liée au classement | ✔ | ✔                |           |
| [RANK](rank)                                                          | Liée au classement | ✔ | ✔                |           |
| [ROW_NUMBER](row-number)                                              | Liée au classement | ✔ |                  |           |
| [NTILE](ntile)                                                        | Liée au classement | ✔ |                  |           |
| [FIRST_VALUE](first-value)                                            | Liée au classement | ✔ | ✔                |           |
| [FIRST](first)                                                        | Liée au classement | ✔ | ✔                |           |
| [LAST_VALUE](last-value)                                              | Liée au classement | ✔ | ✔                |           |
| [LAST](last)                                                          | Liée au classement | ✔ | ✔                |           |
| [NTH_VALUE](nth-value)                                                | Liée au classement | ✔ | ✔                |           |
| [LEAD](lead)                                                          | Liée au classement | ✔ |                  |           |
| [LAG](lag)                                                            | Liée au classement | ✔ |                  |           |

## Syntaxe des fenêtres

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
La `named window` est une fenêtre définie dans la clause `WINDOW` de l'instruction `SELECT`, par exemple : `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

La `<function>` est l'une des suivantes : ([fonction d'agrégation](../07-aggregate-functions), fonction de classement, fonction de valeur).

La clause `OVER` indique que la fonction est utilisée comme fonction de fenêtre.

La sous-clause `PARTITION BY` permet de regrouper les lignes en sous-groupes, par exemple par ville, par année, etc. La clause `PARTITION BY` est facultative. Vous pouvez analyser un groupe de lignes entier sans le diviser en sous-groupes.

La clause `ORDER BY` ordonne les lignes au sein de la fenêtre. 

La clause `window frame` précise le type et l'étendue du cadre de fenêtre. La clause `window frame` est facultative. Si vous omettez la clause `window frame`, le type de cadre par défaut est `RANGE` et l'étendue par défaut est `UNBOUNDED PRECEDING AND CURRENT ROW`.


## Syntaxe du cadre de fenêtre

`window frame` peut être de l'un des types suivants :

```sql
cumulativeFrame ::=
    {
       { ROWS | RANGE } BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
     | { ROWS | RANGE } BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    }
```

```sql
slidingFrame ::=
    {
       ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN UNBOUNDED PRECEDING AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND UNBOUNDED FOLLOWING
    }
```


## Exemples SQL

**Créer la table**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Insérer les données**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 75000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 90000),
  (4, 'Sara', 'Williams', 'Sales', 60000),
  (5, 'Tom', 'Brown', 'HR', 82000),
  (6, 'Ava', 'Davis', 'Sales', 62000),
  (7, 'Olivia', 'Taylor', 'IT', 72000),
  (8, 'Emily', 'Anderson', 'HR', 77000),
  (9, 'Sophia', 'Lee', 'Sales', 58000),
  (10, 'Ella', 'Thomas', 'IT', 67000);
```

**Exemple 1 : classer les employés par salaire**

Dans cet exemple, nous utilisons la fonction RANK() pour classer les employés selon leur salaire, par ordre décroissant. Le salaire le plus élevé reçoit le rang 1, et le salaire le plus bas reçoit le numéro de rang le plus élevé.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

Résultat :

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 3           | Mike       | Johnson   | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 5           | Tom        | Brown     | HR         | 82000  | 3    |
| 8           | Emily      | Anderson  | HR         | 77000  | 4    |
| 1           | John       | Doe       | IT         | 75000  | 5    |
| 7           | Olivia     | Taylor    | IT         | 72000  | 6    |
| 10          | Ella       | Thomas    | IT         | 67000  | 7    |
| 6           | Ava        | Davis     | Sales      | 62000  | 8    |
| 4           | Sara       | Williams  | Sales      | 60000  | 9    |
| 9           | Sophia     | Lee       | Sales      | 58000  | 10   |



**Exemple 2 : calculer le salaire total par service**

Dans cet exemple, nous utilisons la fonction SUM() avec PARTITION BY pour calculer le total des salaires versés par service. Chaque ligne affichera le service et le salaire total de ce service.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

Résultat :

| department | total_salary |
|------------|--------------|
| HR         | 244000       |
| HR         | 244000       |
| HR         | 244000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| Sales      | 180000       |
| Sales      | 180000       |
| Sales      | 180000       |


**Exemple 3 : calculer un cumul des salaires par service**

Dans cet exemple, nous utilisons la fonction SUM() avec un cadre de fenêtre cumulatif pour calculer un cumul des salaires au sein de chaque service. Le cumul est calculé à partir du salaire de l'employé, ordonné par son employee_id.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

Résultat :

| employee_id | first_name | last_name | department | salary | running_total |
|-------------|------------|-----------|------------|--------|---------------|
| 2           | Jane       | Smith     | HR         | 85000  | 85000         |
| 5           | Tom        | Brown     | HR         | 82000  | 167000        |
| 8           | Emily      | Anderson  | HR         | 77000  | 244000        |
| 1           | John       | Doe       | IT         | 75000  | 75000         |
| 3           | Mike       | Johnson   | IT         | 90000  | 165000        |
| 7           | Olivia     | Taylor    | IT         | 72000  | 237000        |
| 10          | Ella       | Thomas    | IT         | 67000  | 304000        |
| 4           | Sara       | Williams  | Sales      | 60000  | 60000         |
| 6           | Ava        | Davis     | Sales      | 62000  | 122000        |
| 9           | Sophia     | Lee       | Sales      | 58000  | 180000        |
