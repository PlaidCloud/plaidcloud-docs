---
title: Parcours d'apprentissage Analytique
description: Ce qu'il faut lire avant les labs Praticien et Expert Analytique de PlaidCloud, et ce que chaque lab vous demande de faire.
sidebar:
  label: Analytique
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

Le parcours Analytique porte sur des métriques qui donnent une seule bonne réponse quelle que soit la ventilation, et sur des significations partagées entre les tables. Commencez par le parcours [Fondations](/fr/guides/certification/foundations/). Pour savoir comment fonctionnent les labs, consultez [Certification PlaidCloud](/fr/guides/certification/).

## Praticien

### À lire dans cet ordre

1. [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/)
2. [Afficher le journal du workflow](/fr/guides/workflows/viewing-workflow-log/)
3. [Définitions de métriques](/fr/integrations/ai-coding-agents/metric-definitions/), y compris la façon de dériver une métrique à partir d'autres
4. [Créer un tableau de bord à partir d'une table publiée](/fr/get-started/tutorials/build-a-dashboard/), pour le tableau de bord facultatif

### Ce que demande le lab

Le lab s'intitule *Analytique : définir des indicateurs pour trois questions*.

Vous exécutez un workflow qui prépare une table de ventes, puis vous définissez des métriques sur cette table, chacune avec la région et le canal dans sa granularité : le chiffre d'affaires par région, la valeur moyenne des commandes par canal, dérivée d'un nombre de commandes, et le coût en part du chiffre d'affaires par région, dérivé d'une métrique de coût. Chaque métrique est construite sur la table préparée, et non sur la table brute. Un tableau de bord pour les trois réponses est une bonne étape suivante, mais il n'est pas noté.

Le lab vérifie que le workflow s'exécute et que chacune des trois métriques donne la bonne réponse.

## Expert

Le lab Expert est chronométré : vous disposez de 4 heures à partir du moment où vous le démarrez.

### À lire dans cet ordre

1. [Définitions de métriques](/fr/integrations/ai-coding-agents/metric-definitions/)
2. [Modèle de données et éléments de projet](/fr/guides/projects/data-model/)
3. [Chemins d'analyse](/fr/integrations/ai-coding-agents/analysis-paths/)

### Ce que demande le lab

Le lab s'intitule *Analytique Expert : des indicateurs cohérents*.

Deux métriques donnent des réponses différentes selon la ventilation, et le total du chiffre d'affaires dépasse la somme des commandes. Vous les réparez pour que chacune renvoie une seule réponse correcte par région et par produit, en conservant leurs noms. Vous faites ensuite des colonnes qui ont le même sens un seul élément partagé : un pour la région, à travers les tables qui la contiennent sous des noms de colonne différents, et un pour le produit.

Le lab vérifie que le workflow s'exécute, que le chiffre d'affaires par région et par produit et les unités par produit sont corrects, et que les éléments couvrent les bonnes colonnes.
