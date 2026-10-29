---
title: Report Single
description: Génère un rapport PDF unique à partir d'une étape de workflow PlaidCloud, avec des modèles, des sources de données et des options de mise en page configurables.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Description



Génère un rapport PDF à partir d'un modèle RML (Report Markup Language), alimenté par les données d'une ou de plusieurs tables PlaidCloud. Utilisez-la pour les rapports formels et mis en forme : factures, états financiers, déclarations réglementaires, synthèses à l'image de la marque.

Le modèle RML définit la mise en page (taille de page, polices, texte fixe, emplacement des tables) ; les tables d'entrée fournissent les données variables. Comparez avec [Reports Batch](/fr/reference/workflow-steps/reports/reports-batch/) (étape) lorsqu'un même modèle doit produire de nombreux rapports (par exemple un par client).


## Noms lus par le modèle

Le modèle lit chaque source de l'onglet **Données du rapport**, et chaque constante sous **Constantes du rapport (valeurs fixes)**, par son nom. Les nouvelles sources se nomment `new_source`, `new_source_2`, etc., et le modèle peut les lire telles quelles ; renommez-les pour indiquer ce qu'elles contiennent.


## Contrôles effectués à l'enregistrement

Le nom de chaque source et de chaque constante doit être :

- **Renseigné** : un nom vide est refusé.
- **Unique** : deux sources, deux constantes, ou une source et une constante ne peuvent pas porter le même nom, car le modèle n'en verrait qu'une : *Source name 'sales' is also a constant name; rename one of them.*
- **Lisible par le modèle** : lettres, chiffres et traits de soulignement, en commençant par une lettre ou un trait de soulignement : *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Différent des mots réservés par le modèle** : `True`, `False`, `None`, `true`, `false`, `none`, `not` et `self` sont interprétés autrement que comme vos données : *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Exemples

Aucun exemple pour le moment...
