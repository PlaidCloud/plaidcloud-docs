---
title: Macro Concurrent
description: Exécutez une invocation de macro isolée par ligne de la table d'inducteurs, avec une limite de simultanéité configurable.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Description

Exécute une [macro](/fr/guides/workflows/create-a-macro/) une fois pour chaque ligne sélectionnée d'une table d'inducteurs côté appelant. Chaque invocation enfant se comporte comme une étape [Macro Run](/fr/reference/workflow-steps/workflow-control/run-macro/) :

- Elle reçoit un nouveau `run_id`.
- Elle s'exécute dans son propre schéma temporaire (`macrorun_<run_id>`).
- Elle reçoit de l'appelant des liaisons de tables, de valeurs scalaires et de dimensions.
- Elle recopie les tables de sortie déclarées vers les destinations côté appelant lorsque l'enfant se termine avec `done` ou `warn`.
- Elle supprime le schéma temporaire lorsque l'enfant se termine, échoue ou est arrêté.

Utilisez l'étape Macro Concurrent lorsque le même processus réutilisable doit s'exécuter pour de nombreuses lignes, par exemple une période, une entité, un client, un lot de fichiers ou une région par ligne de la table d'inducteurs.

## Inducteur

- **Table** — la table côté appelant qui contient une ligne par invocation de macro.
- **Exécutions simultanées** — le nombre maximal d'invocations de macro enfants à maintenir actives en même temps.

## Sélection des données de la table

Sélectionnez les colonnes de la table d'inducteurs dont chaque invocation enfant a besoin. Ces colonnes peuvent être utilisées par les liaisons de la macro et par le filtre d'inducteur.

## Filtre d'inducteur

Ajoutez éventuellement des règles de filtre pour la table d'inducteurs. Seules les lignes correspondantes lancent des invocations de macro enfants.

## Macro

- **Projet** — le projet qui contient la macro. Il doit s'agir du même projet que l'appelant dans la v1.
- **Macro** — le workflow de macro à invoquer pour chaque ligne d'inducteur sélectionnée.

## Liaisons d'entrée

Les liaisons d'entrée relient les données côté appelant aux entrées déclarées de la macro.

**Liaisons d'entrée de tables :**

- **Table source de l'appelant** — la table copiée dans le schéma temporaire de l'invocation enfant.
- **Port cible de la macro** — le nom de la table d'entrée ou le port de la macro qui reçoit la table copiée.
- **Filtre de copie en entrée** — clause `WHERE` facultative appliquée pendant la copie en entrée.
- **JSON des colonnes** — projection JSON facultative des colonnes, lorsque seules certaines colonnes doivent être copiées.

**Liaisons d'entrée de valeurs scalaires et de dimensions :**

- **Variable de la macro** — la variable côté macro à définir pour l'invocation enfant.
- **Valeur** — la valeur littérale, la référence à une variable de l'appelant ou la valeur de colonne d'inducteur à lier.

Les entrées scalaires et de dimensions sont définies avant la copie des tables en entrée, de sorte que les filtres de table peuvent référencer ces variables.

## Liaisons de sortie

Les liaisons de sortie recopient les tables de résultat de la macro vers les destinations côté appelant.

- **Port source de la macro** — le nom de la table de sortie ou le port de la macro à partir duquel copier.
- **Table de destination de l'appelant** — la table côté appelant dans laquelle copier.
- **JSON des colonnes** — projection JSON facultative des colonnes pour la copie en sortie.

Chaque ligne d'inducteur doit aboutir à une table de destination différente : incluez donc une colonne d'inducteur dans le nom de la destination, par exemple `results_{region}`. La copie en sortie remplace la destination au lieu d'y ajouter des données ; deux lignes qui aboutiraient à la même destination ne laisseraient donc que le résultat de la seconde, et l'étape refuse cette configuration avant de lancer quoi que ce soit. Pour combiner les résultats dans une seule table, ajoutez en aval une étape qui réunit les tables de chaque ligne.

La copie en sortie est ignorée pour une invocation enfant arrêtée, afin que des résultats partiels ne soient pas écrits dans les tables durables de l'appelant.

## Lorsqu'une invocation enfant ne répond plus

Une invocation enfant signale son propre résultat lorsqu'elle se termine ; un enfant dont la machine s'arrête sans avertissement ne signale donc jamais rien. Plutôt que de l'attendre indéfiniment, l'étape vérifie que chaque enfant qu'elle attend encore est en vie.

- Un enfant démarré est vérifié environ une fois par minute, et uniquement tant qu'il ne montre aucun signe de progression. Un enfant occupé par une seule étape de longue durée n'affiche aucune progression pendant toute la durée de cette étape, et il est laissé tranquille tant qu'il est réellement en cours d'exécution.
- Un enfant accepté mais qui n'a pas démarré dans les 15 minutes est considéré comme n'ayant jamais démarré. Ce délai couvre la planification et le téléchargement de l'image, pas le travail propre de la macro.

Un enfant traité de l'une ou l'autre manière est arrêté, son schéma temporaire est supprimé et l'étape échoue à la fin en nommant cette invocation, le dernier état qu'elle a signalé et le moment où elle l'a signalé.

**Les autres invocations enfants ne sont pas affectées.** Elles vont jusqu'au bout et leurs tables de sortie sont écrites normalement ; un enfant qui ne répond plus parmi de nombreux autres n'entraîne donc pas l'abandon des autres. Seules les invocations qui n'ont pas pu se terminer sont nommées dans l'échec.

Si la vérification elle-même ne peut pas obtenir de réponse — par exemple lorsque la plateforme est brièvement inaccessible —, l'enfant est considéré comme toujours en cours d'exécution et vérifié de nouveau au passage suivant.

## Comportement à l'arrêt

L'arrêt de l'étape Macro Concurrent parente arrête chaque invocation de macro enfant active et supprime chaque schéma d'exécution actif. Les enfants qui n'ont pas démarré ne sont pas lancés après l'arrêt du parent.

## Voir aussi

- [Créer une macro](/fr/guides/workflows/create-a-macro/) — déclarez un workflow comme macro et définissez son contrat de ports.
- [Macro Run](/fr/reference/workflow-steps/workflow-control/run-macro/) — invoquez une macro une seule fois.
