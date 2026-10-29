---
title: Explorateur de workflow
description: Utilisez l'Explorateur de workflow PlaidCloud pour consulter les détails d'un workflow, la configuration des étapes, l'historique d'exécution et les informations de dépendance.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Pour consulter les détails d'un workflow, trouvez-le dans le projet, puis double-cliquez dessus pour l'ouvrir dans l'explorateur.

![Explorateur de workflow](/images/workflow_explorer.png)

Vous pouvez ici gérer les étapes du workflow : créer ou modifier des étapes existantes, changer leur ordre, exécuter des étapes, etc.

## Créer une étape

Cliquez sur **Créer une étape** et choisissez un type d'étape. Si une étape est sélectionnée dans la liste, une nouvelle étape Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join ou Table Lookup part de la table que cette étape écrit : celle-ci devient la source de la nouvelle étape (**Table 1** pour une jointure), et les colonnes sont renseignées comme le ferait **Inspecter la source**. Une remarque au bas du formulaire l'indique. Changez la source si la nouvelle étape doit lire autre chose. Rien n'est enregistré tant que vous n'enregistrez pas l'étape.
