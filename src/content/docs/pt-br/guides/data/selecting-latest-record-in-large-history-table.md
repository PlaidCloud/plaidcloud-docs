---
title: Selecionando o registro mais recente em uma tabela grande de histórico de versões
description: Saiba como selecionar com eficiência o registro mais recente de tabelas de histórico grandes no PlaidCloud usando técnicas de consulta otimizadas.
sidebar:
  label: Selecionando o registro mais recente em uma tabela grande de histórico de versões
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Desafio

Você tem uma tabela com muitas versões de cada registro, mas precisa usar a versão mais recente.

## Discussão

Esse problema poderia ser resolvido selecionando o ID e a data de atualização MAX em uma tabela temporária.  Em seguida, essa tabela temporária seria unida por INNER JOIN de volta à tabela de histórico para obter o resultado.  Infelizmente, isso exige duas etapas e o armazenamento de uma tabela intermediária que não tem outra função além de encontrar a atualização mais recente.

A solução mais elegante para executar essa operação em uma única consulta usa uma função de janela com ordenação mais um filtro.

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

### Configuração da etapa
Usando uma etapa de extração, crie uma expressão de função de janela em uma coluna chamada `Rank`, como:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

Na guia de filtro da etapa Extract, defina um filtro como:

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

Essa abordagem é altamente eficiente e permite selecionar o registro mais recente em uma tabela de histórico com várias versões em uma única etapa.  Ela funciona classificando cada registro dentro do grupo `employee_id` por `update_date` e escolhendo apenas o primeiro registro.

Se houver várias colunas que compõem a chave exclusiva da linha, você pode adicioná-las ao argumento `partition_by` como uma lista, assim:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Se você precisar aplicar ordenações com várias colunas, também pode fazê-lo com uma lista de colunas, assim:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
