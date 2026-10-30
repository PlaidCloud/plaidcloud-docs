---
title: Selecionar o registo mais recente numa tabela de histórico de versões grande
description: Saiba como selecionar de forma eficiente o registo mais recente em tabelas de histórico grandes no PlaidCloud, com técnicas de consulta otimizadas.
sidebar:
  label: Selecionar o registo mais recente numa tabela de histórico de versões grande
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Desafio

Dispõe de uma tabela com muitas versões de cada registo, mas tem de utilizar a versão mais recente.

## Discussão

Este problema poderia ser resolvido selecionando o ID e a data de atualização máxima (MAX) para uma tabela temporária. Essa tabela temporária seria depois associada por INNER JOIN à tabela de histórico para obter o resultado. Infelizmente, isto requer dois passos e o armazenamento de uma tabela intermédia que não tem outra função senão encontrar a atualização mais recente.

A solução mais elegante, que realiza esta operação numa única consulta, usa uma função de janela com ordenação mais um filtro.

## Solução

### A tabela de histórico de versões

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Configuração do passo
Com um passo de extração, crie uma expressão de função de janela numa coluna chamada `Rank`, como:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

No separador de filtro do passo Extract, defina um filtro como:

```python
table.Rank == 1
```

### O resultado

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

Esta abordagem é muito eficiente e permite selecionar o registo mais recente numa tabela de histórico com várias versões num único passo. Funciona classificando cada registo dentro do grupo `employee_id` pelo `update_date` e escolhendo depois apenas o primeiro registo.

Se a chave única da linha for composta por várias colunas, pode adicioná-las ao argumento `partition_by` sob a forma de lista, como:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Se precisar de ordenações por várias colunas, também pode aplicá-las com uma lista de colunas, como:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
