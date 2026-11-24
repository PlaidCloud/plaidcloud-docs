---
title: Parcours d'apprentissage Ingénierie des données
description: Ce qu'il faut lire avant les labs Praticien et Expert Ingénierie des données de PlaidCloud, et ce que chaque lab vous demande de faire.
sidebar:
  label: Ingénierie des données
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

Le parcours Ingénierie des données porte sur la construction de workflows corrects, pilotés par des variables et rapides. Commencez par le parcours [Fondations](/fr/guides/certification/foundations/). Pour savoir comment fonctionnent les labs, consultez [Certification PlaidCloud](/fr/guides/certification/).

## Praticien

### À lire dans cet ordre

1. [Créer un workflow](/fr/guides/workflows/create-workflow/)
2. [Étapes de workflow](/fr/reference/workflow-steps/), en particulier l'[étape Table Inner Join](/fr/reference/workflow-steps/tables/table-inner-join/) et l'[étape Table Extract](/fr/reference/workflow-steps/tables/table-extract/)
3. [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
4. [Réutiliser votre travail : variables, macros et UDF](/fr/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/)
6. [Afficher le journal du workflow](/fr/guides/workflows/viewing-workflow-log/)

### Ce que demande le lab

Le lab s'intitule *Ingénierie des données : construction mensuelle des ventes*.

Trois tables brutes sont chargées : les lignes de vente, les magasins et les produits. Dans le workflow du lab, vous construisez un récapitulatif mensuel avec une ligne par région et par catégorie de produits, avec les unités et le chiffre d'affaires, pour les lignes vendues d'un mois. Le mois provient d'une variable de projet, et non d'une valeur saisie dans une étape : le lab modifie la variable et exécute à nouveau le workflow. Utilisez uniquement des étapes standard, sans étape SQL ni de code.

Le lab vérifie que le workflow s'exécute, qu'il n'utilise que des étapes standard, et que le récapitulatif est correct pour le mois, puis pour un autre mois.

## Expert

Le lab Expert est chronométré : vous disposez de 4 heures à partir du moment où vous le démarrez.

### À lire dans cet ordre

1. [Déboguer un workflow](/fr/get-started/tutorials/debug-a-workflow/)
2. [Afficher le journal du workflow](/fr/guides/workflows/viewing-workflow-log/)
3. [Gérer les erreurs d'étape](/fr/guides/workflows/managing-step-errors/)
4. [Prévisualiser les données d'une étape](/fr/guides/workflows/preview-step-data/)
5. [Optimiser un workflow](/fr/guides/workflows/optimize-a-workflow/)
6. [Étapes de workflow](/fr/reference/workflow-steps/), en particulier l'[étape Table Inner Join](/fr/reference/workflow-steps/tables/table-inner-join/)

### Ce que demande le lab

Le lab s'intitule *Ingénierie des données Expert : réparer et accélérer la construction nocturne*.

Un workflow nocturne a cessé de s'exécuter, et auparavant il était beaucoup trop lent. Vous lisez le journal d'exécution, trouvez chaque cause et corrigez le workflow pour qu'il réussisse, produise le bon récapitulatif et se termine en une petite fraction de son ancien temps. Les lignes sans compte sont exclues, et les comptes listés deux fois ne doivent pas gonfler les décomptes. Utilisez uniquement des étapes standard et laissez les tables d'entrée telles quelles.

Le lab vérifie que le workflow s'exécute, qu'il n'utilise que des étapes standard, que le récapitulatif est correct, que les tables d'entrée sont inchangées et que le workflow est assez rapide.
