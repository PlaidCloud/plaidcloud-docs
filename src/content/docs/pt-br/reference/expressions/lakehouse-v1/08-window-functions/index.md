---
title: Funções de janela (Lakehouse v1)
description: "Funções de janela SQL do Lakehouse v1: calculam sobre janelas de linhas — classificação, totais acumulados, valores seguintes e anteriores."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## Visão geral 

Uma função de janela opera sobre um grupo ("janela") de linhas relacionadas.

Para cada linha de entrada, uma função de janela retorna uma linha de saída que depende da linha específica passada à função e dos valores das outras linhas da janela.

Há dois tipos principais de funções de janela sensíveis à ordem:

* `Rank-related functions`: as funções relacionadas a classificação listam informações com base no "ranking" de uma linha. Por exemplo, ao classificar lojas em ordem decrescente de lucro por ano, a loja mais lucrativa recebe a posição 1, a segunda mais lucrativa recebe a posição 2, e assim por diante.

* `Window frame functions`: as funções de quadro de janela permitem executar operações móveis, como calcular um total acumulado ou uma média móvel, sobre um subconjunto das linhas da janela.

## Lista de funções que oferecem suporte a janelas

A lista abaixo mostra todas as funções de janela.

| Nome da função                                                        | Categoria    | Janela | Quadro de janela | Observações |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | Geral        | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | Geral        | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | Geral        | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | Geral        | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | Geral        | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | Geral        | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | Geral        | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | Geral        | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | Geral        | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | Geral        | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | Geral        | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | Geral        | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | Geral        | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | Geral        | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | Geral        | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | Geral        | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | Geral        | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | Geral        | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | Geral        | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | Geral        | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | Classificação | ✔      |              |       |
| [PERCENT_RANK](percent-rank/)                                         | Classificação | ✔      | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | Classificação | ✔      | ✔            |       |
| [RANK](rank)                                                          | Classificação | ✔      | ✔            |       |
| [ROW_NUMBER](row-number)                                              | Classificação | ✔      |              |       |
| [NTILE](ntile)                                                        | Classificação | ✔      |              |       |
| [FIRST_VALUE](first-value)                                            | Classificação | ✔     | ✔            |       |
| [FIRST](first)                                                        | Classificação | ✔     | ✔            |       |
| [LAST_VALUE](last-value)                                              | Classificação | ✔     | ✔            |       |
| [LAST](last)                                                          | Classificação | ✔     | ✔            |       |
| [NTH_VALUE](nth-value)                                                | Classificação | ✔     | ✔            |       |
| [LEAD](lead)                                                          | Classificação | ✔     |              |       |
| [LAG](lag)                                                            | Classificação | ✔     |              |       |

## Sintaxe de janela

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
A `named window` é uma janela definida na cláusula `WINDOW` da instrução `SELECT`, por exemplo: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

A `<function>` é uma entre ([função de agregação](../07-aggregate-functions), função de classificação, função de valor).

A cláusula `OVER` especifica que a função está sendo usada como função de janela.

A subcláusula `PARTITION BY` permite agrupar as linhas em subgrupos, por exemplo por cidade, por ano etc. A cláusula `PARTITION BY` é opcional. Você pode analisar um grupo inteiro de linhas sem dividi-lo em subgrupos.

A cláusula `ORDER BY` ordena as linhas dentro da janela. 

A cláusula `window frame` especifica o tipo e a extensão do quadro da janela. A cláusula `window frame` é opcional. Se você omitir a cláusula `window frame`, o tipo de quadro padrão é `RANGE` e a extensão padrão é `UNBOUNDED PRECEDING AND CURRENT ROW`.


## Sintaxe de quadro de janela

`window frame` pode ser de um dos seguintes tipos:

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


## Exemplos de SQL

**Criar a tabela**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Inserir dados**
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

**Exemplo 1: classificar funcionários por salário**

Neste exemplo, usamos a função RANK() para classificar os funcionários com base nos salários, em ordem decrescente. O maior salário recebe a posição 1, e o menor salário recebe o maior número de posição.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

Resultado:

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



**Exemplo 2: calcular o salário total por departamento**

Neste exemplo, usamos a função SUM() com PARTITION BY para calcular o total de salários pagos por departamento. Cada linha mostra o departamento e o salário total desse departamento.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

Resultado:

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


**Exemplo 3: calcular um total acumulado de salários por departamento**

Neste exemplo, usamos a função SUM() com um quadro de janela cumulativo para calcular um total acumulado de salários dentro de cada departamento. O total acumulado é calculado com base no salário do funcionário, ordenado por employee_id.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

Resultado:

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
