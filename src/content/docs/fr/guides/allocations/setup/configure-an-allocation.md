---
title: Configurer une allocation
description: "Configurez une allocation PlaidCloud : données sources, données d'inducteur, mappage des cibles, méthodes d'allocation et options de traitement."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Objectif

Les allocations permettent de ventiler des valeurs (généralement des coûts) à un niveau plus granulaire en appliquant un inducteur. Elles servent à de multiples usages, notamment la **comptabilité par activités**, la **refacturation des services informatiques et partagés**, le calcul du coût complet de production et de fourniture d'un bien ou d'un service aux clients, etc. Ce sont un outil fondamental de l'analyse financière et la pierre angulaire d'opérations de reporting de gestion telles que la **rentabilité par client et par produit**. Elles sont aussi un mécanisme utile pour établir et gérer des prix de transfert intersociétés mondiaux pour les biens et services.

## Configurer la transformation d'allocation

En pratique, les allocations se configurent dans PlaidCloud de la même façon que d'autres transformations de données telles que les jointures et les recherches. Quatre paramètres de configuration doivent être définis pour qu'une transformation d'allocation réussisse.

1. **Spécifier les données préallouées** : indiquez la table des données préallouées dans la section **Table des valeurs à allouer** de la transformation d'allocation.
2. **Spécifier les données d'inducteur** : les données d'inducteur servent de base aux ratios utilisés dans l'allocation. Choisissez la table de données d'inducteur dans la section **Table de données de l'inducteur** de la transformation d'allocation.
3. **Spécifier la table de résultat** : les données post-allocation doivent être stockées dans une table. Indiquez cette table dans la section **Table de résultat d'allocation** de la section de résultat d'allocation de la transformation.
4. **Spécifier la dimension d'affectation** : les allocations exigent une dimension d'affectation, dont le rôle est de fournir la règle selon laquelle chaque enregistrement ou ensemble d'enregistrements préalloués sera affecté. Indiquez la dimension d'affectation dans la section **Hiérarchie de la dimension d'affectation** de la transformation d'allocation.

Au-delà de ces quatre paramètres, les deux onglets de mappage exigent que les **Rôles** des colonnes soient définis avant que l'étape puisse être enregistrée : une colonne **Valeur à allouer** dans le **Mappage de la source d'allocation**, et des colonnes **Valeur de fractionnement**, **Relation source (dénominateur)** et **Cible d'allocation (numérateur)** dans le **Mappage des données de l'inducteur**. PlaidCloud vérifie ces éléments à l'enregistrement et nomme ce qui manque ; consultez [Dépannage des allocations](/fr/guides/allocations/results/troubleshooting-allocations/#pourquoi-une-étape-dallocation-ne-senregistre-pas).

## Concepts clés

La somme des valeurs d'un jeu de données alloué doit correspondre à celle des données sources préallouées.

Les allocations sont accessibles dans PlaidCloud en tant qu'option de transformation. Pour configurer une allocation, définissez d'abord des affectations, puis configurez une transformation d'allocation qui utilise ces affectations pour allouer les enregistrements entrants à l'aide d'une table d'inducteurs spécifiée.

Les affectations sont des dimensions particulières. On y accède dans la section Dimensions d'un projet PlaidCloud.

Pour configurer une dimension d'affectation, procédez comme suit :

1. Depuis l'écran du projet, accédez à l'onglet Dimensions
2. Créez une dimension
