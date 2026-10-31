---
title: Créer un workflow (guide)
description: Créez un workflow dans PlaidCloud et choisissez son type (Standard série, Standard parallèle ou Avancé (canevas DAG)) pour charger, transformer et exporter des données.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Pour créer un workflow, vous avez besoin d'un projet existant. Si vous n'en avez pas encore, consultez [Gérer les projets](/fr/guides/projects/managing-projects/).

## Procédure

1. Ouvrez le projet qui doit contenir le workflow.
2. Passez à l'onglet **Workflows**.
3. Cliquez sur **Nouveau workflow** dans la barre d'outils.
4. Renseignez le formulaire :
   - **Nom** : court et descriptif (par exemple, « Clôture mensuelle : chargement des réels »)
   - **Mémo** : description plus longue, facultative, pour donner du contexte
   - **Type de workflow** : Standard série (par défaut), Standard parallèle ou Avancé (canevas DAG). Consultez [Choisir un type de workflow](#choisir-un-type-de-workflow) ci-dessous.
   - **Déclencher un workflow de remédiation en cas d'erreur** : facultatif ; activez-le pour choisir un workflow de remédiation (consultez [À propos des workflows de remédiation](#à-propos-des-workflows-de-remédiation) ci-dessous).
5. Cliquez sur **Créer**.

Le workflow apparaît dans l'onglet Workflows et est prêt à recevoir des étapes. Double-cliquez dessus pour ouvrir l'[explorateur de workflow](/fr/guides/workflows/workflow-explorer/) et commencer à le construire.

## Voir quand une table source a changé pour la dernière fois

Dans le formulaire d'une étape, un sélecteur de table affiche une ligne discrète **Dernière mise à jour** avec la date et l'heure, dans votre heure locale, sous la table que vous avez sélectionnée, afin que vous puissiez voir d'un coup d'œil si les données sont à jour. Survolez la ligne pour afficher le texte complet. La ligne est masquée lorsque la sélection est dynamique ou lorsque la table n'a jamais été mise à jour.

## Choisir un type de workflow

Le **Type de workflow** que vous choisissez à la création d'un workflow détermine la façon dont ses étapes sont organisées et exécutées. Par défaut, il s'agit de **Standard série**, et vous le définissez depuis le sélecteur de type du formulaire Nouveau workflow.

| Type | Organisation et exécution des étapes |
|------|--------------------------------|
| **Standard série** | Les étapes s'exécutent depuis la **liste des étapes**, une à la fois, dans l'ordre. |
| **Standard parallèle** | Les étapes s'exécutent depuis la **liste des étapes**, en parallèle lorsque leurs dépendances le permettent. |
| **Avancé (canevas DAG)** | Les étapes sont disposées sur un **canevas visuel** et s'exécutent dans l'ordre des dépendances, les branches indépendantes s'exécutant en parallèle. Le mode avancé donne aussi accès aux points d'arrêt, aux conteneurs, à l'exécution à partir d'un point, à la simulation et à la collaboration en temps réel. |

Un quatrième type, **Macro** (un workflow réutilisable et appelable, avec des entrées et des sorties déclarées), sera bientôt disponible et apparaît dans le sélecteur comme désactivé.

:::note
Une étape ne peut apparaître qu'une seule fois dans un workflow. L'insertion, la copie, le clonage ou l'importation d'une étape à une position qui la placerait une seconde fois dans un workflow sont refusés, en nommant l'étape ; vous ne pouvez donc plus créer cette situation. Si un workflow antérieur à ce correctif contient encore une étape à deux endroits, son exécution **Standard série** échoue immédiatement avec une erreur nommant l'étape dupliquée, de même qu'une exécution **Standard parallèle** arrêtée à une étape de fin choisie (consultez [Exécuter une plage d'étapes dans un workflow](/fr/guides/workflows/running-a-range-of-steps-in-a-workflow/)), puisque l'exécution jusqu'à un point final est elle aussi séquentielle. Une exécution **Standard parallèle** jusqu'à son terme tolère le doublon et l'exécute simplement une fois. Dans les deux cas, supprimez l'étape dupliquée pour réparer le workflow : la suppression d'étapes n'est jamais restreinte.
:::

Choisissez **Avancé (canevas DAG)** ici si vous voulez le [Concepteur visuel de workflow](/fr/guides/workflows/advanced-workflows/) dès le départ. Ce choix n'est pas définitif : vous pouvez faire passer un workflow standard en mode avancé plus tard avec **Convertir en avancé…** depuis la liste Workflows.

## À propos des workflows de remédiation

Si le nouveau workflow se termine par une erreur, PlaidCloud peut exécuter automatiquement un **workflow de remédiation** en réponse. C'est utile pour :

- Envoyer une notification à un canal Slack, à une liste de diffusion par e-mail ou à un webhook afin que quelqu'un enquête
- Déclencher un workflow de restauration ou de nettoyage qui rétablit un état connu et sain
- Consigner l'échec dans une table d'audit

Un workflow de remédiation est facultatif. Vous pouvez le laisser vide maintenant et le configurer plus tard si nécessaire. Le workflow de remédiation ne se déclenche que sur les échecs terminaux, pas sur les avertissements propres à une étape.

## Étapes suivantes

- [Explorateur de workflow](/fr/guides/workflows/workflow-explorer/) : ajoutez des étapes à votre nouveau workflow
- [Workflows avancés](/fr/guides/workflows/advanced-workflows/) : choisissez un type de workflow et construisez sur le canevas visuel
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/) : exécutez le workflow une fois qu'il contient des étapes
- [Gérer les erreurs d'étape](/fr/guides/workflows/managing-step-errors/) : déboguer les échecs
