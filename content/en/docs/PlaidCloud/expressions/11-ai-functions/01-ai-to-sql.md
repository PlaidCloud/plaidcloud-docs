---
title: 'AI_TO_SQL'
---

Converts natural language instructions into SQL queries with the latest model `text-davinci-003`.

PlaidCloud Lakehouse offers an efficient solution for constructing SQL queries by incorporating OLAP and AI. Through this function, instructions written in a natural language can be converted into SQL query statements that align with the table schema. For example, the function can be provided with a sentence like "Get all items that cost 10 dollars or less" as an input and generate the corresponding SQL query "SELECT * FROM items WHERE price <= 10" as output.

The main code implementation can be found [here](https://github.com/datafuselabs/databend/blob/1e93c5b562bd159ecb0f336bb88fd1b7f9dc4a62/src/query/service/src/table_functions/openai/ai_to_sql.rs).

:::note
The SQL query statements generated adhere to the PostgreSQL standards, so they might require manual revisions to align with the syntax of PlaidCloud Lakehouse.
:::

:::info
Starting from PlaidCloud Lakehouse v1.1.47, PlaidCloud Lakehouse supports the [Azure OpenAI service](https://azure.microsoft.com/en-au/products/cognitive-services/openai-service).

This integration offers improved data privacy.

To use Azure OpenAI, add the following configurations to the `[query]` section:
```sql
# Azure OpenAI
openai_api_chat_base_url = "https://<name>.openai.azure.com/openai/deployments/<name>/"
openai_api_embedding_base_url = "https://<name>.openai.azure.com/openai/deployments/<name>/"
openai_api_version = "2023-03-15-preview"
```
:::

:::caution
PlaidCloud Lakehouse relies on (Azure) OpenAI for `AI_TO_SQL` but only sends the table schema to (Azure) OpenAI, not the data.

They will only work when the PlaidCloud Lakehouse configuration includes the `openai_api_key`, otherwise they will be inactive.

This function is available by default on [PlaidCloud Lakehouse Cloud](https://databend.com) using our Azure OpenAI key. If you use them, you acknowledge that your table schema will be sent to Azure OpenAI by us.
:::

## SQL Syntax

```sql
USE <your-database>;
SELECT * FROM ai_to_sql('<natural-language-instruction>');
```

:::tip Obtain and Config OpenAI API Key
- To obtain your openAI API key, please visit https://platform.openai.com/account/api-keys and generate a new key.
- Configure the **databend-query.toml** file with the openai_api_key setting.

```toml
[query]
... ...
openai_api_key = "<your-key>"
```
:::

## SQL Examples

In this example, an SQL query statement is generated from an instruction with the AI_TO_SQL function, and the resulting statement is executed to obtain the query results.

1. Prepare data.

```sql
CREATE DATABASE IF NOT EXISTS openai;
USE openai;

CREATE TABLE users(
    id INT,
    name VARCHAR,
    age INT,
    country VARCHAR
);

CREATE TABLE orders(
    order_id INT,
    user_id INT,
    product_name VARCHAR,
    price DECIMAL(10,2),
    order_date DATE
);

-- Insert sample data into the users table
INSERT INTO users VALUES (1, 'Alice', 31, 'USA'),
                         (2, 'Bob', 32, 'USA'),
                         (3, 'Charlie', 45, 'USA'),
                         (4, 'Diana', 29, 'USA'),
                         (5, 'Eva', 35, 'Canada');

-- Insert sample data into the orders table
INSERT INTO orders VALUES (1, 1, 'iPhone', 1000.00, '2022-03-05'),
                          (2, 1, 'OpenAI Plus', 20.00, '2022-03-06'),
                          (3, 2, 'OpenAI Plus', 20.00, '2022-03-07'),
                          (4, 2, 'MacBook Pro', 2000.00, '2022-03-10'),
                          (5, 3, 'iPad', 500.00, '2022-03-12'),
                          (6, 3, 'AirPods', 200.00, '2022-03-14');
```

2. Run the AI_TO_SQL function with an instruction written in English as the input.

```sql
SELECT * FROM ai_to_sql(
    'List the total amount spent by users from the USA who are older than 30 years, grouped by their names, along with the number of orders they made in 2022');
```

A SQL statement is generated by the function as the output:

```sql
*************************** 1. row ***************************
     database: openai
generated_sql: SELECT name, SUM(price) AS total_spent, COUNT(order_id) AS total_orders
               FROM users
                        JOIN orders ON users.id = orders.user_id
               WHERE country = 'USA' AND age > 30 AND order_date BETWEEN '2022-01-01' AND '2022-12-31'
               GROUP BY name;
```

3. Run the generated SQL statement to get the query results.

```sql
+---------+-------------+-------------+
| name    | order_count | total_spent |
+---------+-------------+-------------+
| Bob     |           2 |     2020.00 |
| Alice   |           2 |     1020.00 |
| Charlie |           2 |      700.00 |
+---------+-------------+-------------+
```