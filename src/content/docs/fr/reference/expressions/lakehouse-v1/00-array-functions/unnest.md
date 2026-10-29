---
title: UNNEST (Lakehouse v1)
description: "UNNEST : déploie le tableau et renvoie l'ensemble de ses éléments."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Déploie le tableau et renvoie l'ensemble de ses éléments.

## Syntaxe Analyze

```python
func.unnest( <array> )
```

## Exemples Analyze

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
UNNEST( <array> )
```

## Exemples SQL

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## Exemple pratique
Dans les exemples ci-dessous, nous utilisons la table suivante, nommée contacts, dont la colonne phones est définie comme un tableau de texte.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

La colonne phones est un tableau à une dimension qui contient les différents numéros de téléphone d'un contact.

Pour définir un tableau à plusieurs dimensions, ajoutez des crochets.

Par exemple, vous pouvez définir un tableau à deux dimensions comme suit :

```python
column_name data_type [][]
```

Exemple d'insertion de données dans cette table
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
ou
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

La fonction unnest() déploie un tableau en une liste de lignes. Par exemple, la requête suivante déploie tous les numéros de téléphone du tableau phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Résultat :
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
