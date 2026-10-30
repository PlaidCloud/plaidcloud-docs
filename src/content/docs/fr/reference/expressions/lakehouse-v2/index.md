---
title: Expressions Lakehouse v2
description: Expressions Lakehouse v2 fondées sur les fonctions SQL de StarRocks 4.1, avec des références SQLAlchemy.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 repose sur [StarRocks](https://www.starrocks.io/) 4.1. Pour chaque fonction ci-dessous, ce site fournit une syntaxe et des exemples adaptés à PlaidCloud ; pour la référence amont canonique (avec tous les cas limites et toutes les variantes d'arguments), consultez la **[référence des fonctions SQL de StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Fonctions d'agrégation

- [Fonctions d'agrégation](./01-aggregate-functions) — calculent des synthèses comme la somme, la moyenne, le nombre d'occurrences, etc.
- [Fonctions de percentile](./15-percentile-functions) — calculent des valeurs de percentile et gèrent les états de percentile

## Fonctions scalaires

- [Fonctions de tableau](./02-array-functions) — effectuent des opérations sur les tableaux
- [Fonctions binaires](./03-binary-functions) — convertissent entre les formats binaire et chaîne
- [Fonctions sur les bits](./04-bit-functions) — effectuent des opérations bit à bit
- [Fonctions bitmap](./05-bitmap-functions) — effectuent des opérations et des manipulations sur les bitmaps
- [Fonctions conditionnelles](./06-condition-functions) — implémentent une logique conditionnelle et des instructions CASE
- [Fonctions cryptographiques](./07-cryptographic-functions) — chiffrent, déchiffrent et hachent des données
- [Fonctions de date et d'heure](./08-date-time-functions) — manipulent et mettent en forme des dates et des heures
- [Fonctions de dictionnaire](./09-dictionary-functions) — recherchent des valeurs dans des tables de dictionnaire
- [Fonctions de hachage](./10-hash-functions) — génèrent des valeurs de hachage avec MurmurHash et xxHash
- [Fonctions JSON](./11-json-functions) — créent, interrogent et manipulent des données JSON
- [Fonctions de map](./12-map-functions) — créent et manipulent des structures de données de type map
- [Fonctions mathématiques](./13-math-functions) — effectuent des calculs et des opérations numériques
- [Fonctions de recherche de motifs](./14-pattern-matching-functions) — recherchent des correspondances dans des chaînes avec LIKE et des expressions régulières
- [Fonctions scalaires (HLL)](./16-scalar-functions) — fonctions d'estimation de cardinalité HyperLogLog
- [Fonctions spatiales](./17-spatial-functions) — traitent et manipulent des données géospatiales
- [Fonctions de chaîne](./18-string-functions) — manipulent des chaînes et effectuent des opérations sur du texte
- [Fonctions de structure](./19-struct-functions) — créent et utilisent des types de données struct
- [Fonctions variant](./22-variant-functions) — interrogent et inspectent des types de données VARIANT

## Fonctions de table

- [Fonctions de table](./20-table-functions) — renvoient des résultats sous forme tabulaire

## Fonctions utilitaires et méta

- [Fonctions utilitaires](./21-utility-functions) — accèdent aux informations système et aux utilitaires de session
- [Fonctions méta](./23-meta-functions) — inspectent les vues matérialisées, la mémoire et les diagnostics

## Gestion du Lakehouse

- [Gestion de Lakehouse](./lakehouse-management/) — exécutez des requêtes, parcourez le catalogue, gérez les entrepôts et surveillez le calcul
