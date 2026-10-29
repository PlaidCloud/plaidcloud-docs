---
title: Set Project Variable
description: Définissez des variables au niveau du projet à partir d'une étape de workflow PlaidCloud pour stocker des valeurs accessibles à tous les workflows du projet.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## Description


L'étape « Set Project Variable » définit des variables de projet utilisables pendant le workflow. Le nom et la valeur d'une variable peuvent contenir n'importe quelle combinaison de caractères valides, y compris des espaces. Les variables sont référencées dans le workflow en les plaçant entre accolades. Par exemple, *a_variable* est référencée dans une transformation sous la forme *\{a_variable}*, ce qui permet de l'utiliser dans une formule ou une valeur de champ (par exemple, \{a_variable} * 2).



## Liste des variables


Le tableau liste toutes les variables enregistrées dans le projet, chacune avec sa **Valeur actuelle** et son **Mémo**, relus à chaque ouverture de l'étape — vous pouvez ainsi voir ce que contient une variable avant de décider de la valeur à lui donner.

Pour en définir une, cochez **Définir** sur sa ligne et saisissez la nouvelle valeur sous **Définir la valeur**. Seules les lignes cochées sont écrites à l'exécution de l'étape : une valeur saisie sans cocher **Définir** est donc ignorée. Il est aussi possible de définir une variable qui n'a pas encore été enregistrée : ajoutez une ligne et définissez-la de la même manière — l'exécution de l'étape la crée.







## Exemples


Pas encore d'exemples…
