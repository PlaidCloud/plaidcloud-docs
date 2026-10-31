---
title: MATCH (Lakehouse v1)
description: MATCH — Recherche les documents contenant les mots-clés spécifiés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Recherche les documents contenant les mots-clés spécifiés. À noter : la fonction MATCH ne peut être utilisée que dans une clause WHERE.

:::info
La fonction MATCH de PlaidCloud Lakehouse s'inspire de la fonction [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) d'Elasticsearch.
:::

## Syntaxe SQL

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Paramètre    | Description                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | Liste de noms de colonnes de la table, séparés par des virgules, dans lesquelles rechercher les mots-clés spécifiés. Une pondération facultative peut être définie avec la syntaxe (^) : elle permet d'attribuer un poids différent à chaque colonne et d'influencer ainsi son importance dans la recherche. |
| `<keywords>` | Les mots-clés à rechercher dans les colonnes spécifiées de la table. Ce paramètre peut aussi servir à une correspondance par suffixe : un terme de recherche suivi d'un astérisque (*) peut correspondre à un nombre quelconque de caractères ou de mots.                                                                                                                                                                                       |
| `<options>` | Un ensemble d'options de configuration, séparées par des points-virgules `;`, qui personnalisent le comportement de la recherche. Consultez le tableau ci-dessous pour plus de détails. |

| Option    | Description                                                                                                                                                                                         | Exemple                                                                                               | Explication                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Autorise la correspondance de termes dans une distance de Levenshtein donnée. `fuzziness` peut être défini sur 1 ou 2.                                                                                                    | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | Pour le terme de recherche « box », `fuzziness=1` autorise la correspondance avec des termes comme « fox », car « box » et « fox » ont une distance de Levenshtein de 1.                                                                          |
| operator  | Indique comment combiner plusieurs termes de recherche. Peut être défini sur OR (par défaut) ou AND. OR renvoie les résultats contenant l'un des termes de recherche, tandis que AND renvoie ceux qui contiennent tous les termes.     | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Avec `operator=AND`, la requête exige que « action » et « works » soient tous deux présents dans les résultats. Grâce à `fuzziness=1`, elle correspond à des termes comme « Actions » et « words » : « Actions speak louder than words » est donc renvoyé. |
| lenient   | Détermine si des erreurs sont signalées lorsque le texte de la requête est invalide. La valeur par défaut est `false`. Si elle est définie sur `true`, aucune erreur n'est signalée et un jeu de résultats vide est renvoyé lorsque le texte de la requête est invalide. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | Si le texte de la requête `()` est invalide, définir `lenient=true` évite qu'une erreur soit levée et renvoie à la place un jeu de résultats vide.                                                                               |

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

-- Retrieve documents where the 'title' column matches 'art power'
SELECT * FROM test WHERE MATCH('title', 'art power');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains values that start with 'The' followed by any characters
SELECT * FROM test WHERE MATCH('title', 'The*')

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │
│           Nullable(String)          │                                Nullable(String)                                │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.                     │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success.         │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                           │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where either the 'title' or 'body' column matches 'knowledge technology'
SELECT *, score() FROM test WHERE MATCH('title, body', 'knowledge technology');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │  score()  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.1550591 │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │ 2.6830134 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where either the 'title' or 'body' column matches 'knowledge technology', with weighted importance on both columns
SELECT *, score() FROM test WHERE MATCH('title^5, body^1.2', 'knowledge technology');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │  score()  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.3860708 │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │ 7.8053584 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'body' column contains both "knowledge" and "imagination" (allowing for minor typos).
SELECT * FROM test WHERE MATCH('body', 'knowledg imaginatio', 'fuzziness = 1; operator = AND');

-[ RECORD 1 ]-----------------------------------
title: The Importance of Reading
 body: Reading is a crucial skill that opens up a world of knowledge and imagination.
```
