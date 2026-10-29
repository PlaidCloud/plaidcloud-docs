---
title: QUERY (Lakehouse v1)
description: QUERY — Recherche les documents satisfaisant une expression de requête donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Recherche les documents satisfaisant une expression de requête donnée. À noter : la fonction QUERY ne peut être utilisée que dans une clause WHERE.

:::info
La fonction QUERY de PlaidCloud Lakehouse s'inspire de la fonction [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) d'Elasticsearch.
:::

## Syntaxe SQL

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

L'expression de requête prend en charge les syntaxes suivantes. À noter : `<keyword>` peut aussi servir à une correspondance par suffixe : un terme de recherche suivi d'un astérisque (*) peut correspondre à un nombre quelconque de caractères ou de mots.

| Syntaxe                                                 | Description                                                                                                                                                                                                                                             | Exemples                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Correspond aux documents dont la colonne spécifiée contient le mot-clé spécifié.                                                                                                                                                                        | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Correspond aux documents dont la colonne spécifiée contient l'un des mots-clés listés entre crochets. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Correspond aux documents dont la colonne spécifiée contient les deux mots-clés spécifiés ou l'un des deux. Dans les requêtes combinant AND et OR, les opérations AND sont prioritaires sur OR : « a AND b OR c » est donc lu comme « (a AND b) OR c ». | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Correspond aux documents dont la colonne spécifiée contient le mot-clé positif spécifié, et exclut les documents contenant le mot-clé négatif spécifié.                                                                                                 | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Correspond aux documents dont la colonne spécifiée contient exactement l'expression spécifiée.                                                                                                                                                          | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Correspond aux documents dont les colonnes spécifiées contiennent le mot-clé spécifié, avec les coefficients d'amplification indiqués pour accroître leur pertinence dans la recherche. Cette syntaxe permet de définir des poids différents pour plusieurs colonnes afin d'influencer la pertinence de la recherche. | `QUERY('title:art^5 body:reading^1.2')` |


| Option    | Description                                                                                                                                                                                         | Exemple                                                                                              | Explication                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Autorise la correspondance de termes dans une distance de Levenshtein donnée. `fuzziness` peut être défini sur 1 ou 2.                                                                              | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | Pour le terme de recherche « box », `fuzziness=1` autorise la correspondance avec des termes comme « fox », car « box » et « fox » ont une distance de Levenshtein de 1.                                             |
| operator  | Indique comment combiner plusieurs termes de recherche. Peut être défini sur OR (par défaut) ou AND. OR renvoie les résultats contenant l'un des termes de recherche, tandis que AND renvoie ceux qui contiennent tous les termes. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | Avec `operator=AND`, la requête exige que « action » et « works » soient tous deux présents dans les résultats. Grâce à `fuzziness=1`, elle correspond à des termes comme « Actions » et « words » : « Actions speak louder than words » est donc renvoyé. |
| lenient   | Détermine si des erreurs sont signalées lorsque le texte de la requête est invalide. La valeur par défaut est `false`. Si elle est définie sur `true`, aucune erreur n'est signalée et un jeu de résultats vide est renvoyé lorsque le texte de la requête est invalide. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | Si le texte de la requête `()` est invalide, définir `lenient=true` évite qu'une erreur soit levée et renvoie à la place un jeu de résultats vide.                                                                   |

## Exemples SQL

```sql
CREATE TABLE test(title STRING, body STRING);

CREATE INVERTED INDEX idx ON test(title, body);

INSERT INTO test VALUES
('The Importance of Reading', 'Reading is a crucial skill that opens up a world of knowledge and imagination.'),
('The Benefits of Exercise', 'Exercise is essential for maintaining a healthy lifestyle.'),
('The Power of Perseverance', 'Perseverance is the key to overcoming obstacles and achieving success.'),
('The Art of Communication', 'Effective communication is crucial in everyday life.'),
('The Impact of Technology on Society', 'Technology has revolutionized our society in countless ways.');

-- Retrieve documents where the 'title' column contains the keyword 'power'
SELECT * FROM test WHERE QUERY('title:power');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains values that start with 'The' followed by any characters
SELECT * FROM test WHERE QUERY('title:The*');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.                     │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success.         │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                           │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains either the keyword 'power' or 'art'
SELECT * FROM test WHERE QUERY('title:power OR art');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT * FROM test WHERE QUERY('title:IN [power, art]')

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
│      Nullable(String)     │                            Nullable(String)                            │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the positive keyword 'the' but not 'reading'
SELECT * FROM test WHERE QUERY('title:+the -reading');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                  body                                  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.             │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                   │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.           │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the exact phrase 'Benefits of Exercise'
SELECT * FROM test WHERE QUERY('title:"Benefits of Exercise"');

┌───────────────────────────────────────────────────────────────────────────────────────┐
│           title          │                            body                            │
├──────────────────────────┼────────────────────────────────────────────────────────────┤
│ The Benefits of Exercise │ Exercise is essential for maintaining a healthy lifestyle. │
└───────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the keyword 'art' with a boost of 5 and the 'body' column contains the keyword 'reading' with a boost of 1.2
SELECT *, score() FROM test WHERE QUERY('title:art^5 body:reading^1.2');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                      body                                      │  score()  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.3860708 │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                           │ 7.1992116 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'body' column contains both "knowledge" and "imagination" (allowing for minor typos).
SELECT * FROM test WHERE QUERY('body:knowledg OR imaginatio', 'fuzziness = 1; operator = AND');

-[ RECORD 1 ]-----------------------------------
title: The Importance of Reading
 body: Reading is a crucial skill that opens up a world of knowledge and imagination.
```
