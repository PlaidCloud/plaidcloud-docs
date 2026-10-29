---
title: Expressions Lakehouse v1
description: Expressions Lakehouse v1 fondées sur les fonctions SQL de Databend, avec des références SQLAlchemy utilisant le préfixe func.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1 repose sur le moteur SQL [Databend](https://databend.com/). Pour chaque fonction ci-dessous, ce site fournit une syntaxe et des exemples adaptés à PlaidCloud ; pour la référence canonique en amont (avec tous les cas limites et toutes les variantes d'arguments), consultez la **[référence des fonctions SQL de Databend](https://docs.databend.com/sql/sql-functions/)**.

## Fonctions scalaires

- [Fonctions de tableau](./00-array-functions) — Effectuent des opérations sur les tableaux
- [Fonctions d'expression bit à bit](./01-bitmap-functions) — Effectuent des opérations et des manipulations bit à bit
- [Fonctions d'expression conditionnelle](./03-conditional-functions) — Mettent en œuvre une logique conditionnelle et des instructions CASE
- [Fonctions de contexte](./15-context-functions) — Fournissent des informations sur le contexte d'exécution SQL en cours
- [Fonctions de conversion](./02-conversion-functions) — Convertissent des types de données et transtypent des valeurs
- [Fonctions de date et d'heure](./05-datetime-functions) — Manipulent et formatent les dates et les heures
- [Fonctions géospatiales](./09-geo-functions) — Gèrent et manipulent des données géospatiales
- [Fonctions de géométrie](./09-geometry-functions) — Gèrent et manipulent des données de géométrie géospatiale
- [Fonctions d'intervalle](./05-interval-functions) — Créent et manipulent des intervalles de temps
- [Fonctions de mappage](./10-map-functions) — Créent et manipulent des structures de données de type map
- [Fonctions numériques](./04-numeric-functions) — Effectuent des calculs et des opérations numériques
- [Fonctions de recherche](./10-search-functions) — Recherchent des valeurs à l'aide d'expressions
- [Fonctions pour données semi-structurées et structurées](./10-semi-structured-functions) — Travaillent avec JSON et d'autres formats de données structurées
- [Fonctions de chaîne](./06-string-functions) — Manipulent des chaînes et effectuent des opérations d'expressions régulières

## Fonctions d'agrégation

- [Fonctions d'agrégation](./07-aggregate-functions) — Calculent des synthèses comme la somme, la moyenne, le nombre, etc.
- [Fonctions de fenêtrage](./08-window-functions) — Fournissent des calculs d'agrégation sur une plage de lignes spécifiée

## Fonctions d'IA

- [Fonctions d'IA](./11-ai-functions) — Exploitent les capacités d'IA et d'apprentissage automatique

## Fonctions spécialisées

- [Fonctions de hachage](./12-hash-functions) — Génèrent des valeurs de hachage pour la sécurité et la comparaison des données
- [Fonctions d'adresse IP](./14-ip-address-functions) — Manipulent et analysent des données d'adresse IP
- [Fonctions UUID](./13-uuid-functions) — Génèrent et manipulent des UUID

## Fonctions système et de table

- [Fonctions de séquence](./18-sequence-functions) — Génèrent des valeurs séquentielles
- [Fonctions système](./16-system-functions) — Accèdent aux informations de niveau système et effectuent des opérations de contrôle
- [Fonctions de table](./17-table-functions) — Renvoient des résultats sous forme tabulaire

## Autres fonctions

- [Fonctions de dictionnaire](./19-dictionary-functions) — Travaillent avec des structures de données de type dictionnaire
- [Autres fonctions diverses](./20-other-functions) — Un ensemble de fonctions variées
- [Fonctions de test](./19-test-functions) — Fonctions utilisées à des fins de test
