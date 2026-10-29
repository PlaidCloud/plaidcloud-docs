---
title: Macro Run
description: Invoquez un workflow de macro comme sous-invocation isolée avec des liaisons de ports d'entrée et de sortie déclarées — chaque appel s'exécute dans son propre schéma temporaire.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-macro.md
---

## Description

Invoque un workflow de [macro](/fr/guides/workflows/create-a-macro/) comme sous-invocation isolée par exécution. Contrairement à [Exécuter le workflow](/fr/reference/workflow-steps/workflow-control/run-workflow/), chaque appel de l'étape Macro Run :

- Reçoit un `run_id` neuf et unique.
- S'exécute dans son propre schéma temporaire éphémère (`macrorun_<run_id>`) du catalogue du projet.
- Lie les tables et variables côté appelant aux ports d'entrée déclarés de la macro lors de la copie en entrée.
- Recopie en cas de succès les tables de sortie déclarées de la macro vers les destinations côté appelant.
- Supprime toujours le schéma temporaire à la fin de l'appel (succès, erreur ou arrêt).

Cette isolation permet d'appeler la même macro en toute sécurité de façon simultanée — depuis une boucle parente, depuis des workflows indépendants exécutés en même temps ou de façon récursive depuis une autre macro — sans collision de noms de tables intermédiaires entre les exécutions.

Le workflow cible doit être marqué comme macro. Une étape Macro Run qui cible un workflow qui n'est pas une macro échoue avec un message d'erreur explicite ; inversement, une étape [Exécuter le workflow](/fr/reference/workflow-steps/workflow-control/run-workflow/) ou [Workflow Loop](/fr/reference/workflow-steps/workflow-control/workflow-loop/) ne peut pas cibler une macro (ces étapes ne portent pas le cycle de vie d'isolation par exécution).

## Macro à exécuter

- **Projet** — le projet qui contient la macro. Il doit s'agir du même projet que l'appelant dans la v1.
- **Macro** — le workflow de macro à invoquer. Les ports d'entrée et de sortie déclarés de la macro alimentent les listes de liaisons ci-dessous une fois la macro sélectionnée.

## Liaisons des ports d'entrée

Pour chaque port d'entrée déclaré sur la macro, ajoutez une liaison. Les liaisons sont traitées en deux passes — d'abord les entrées scalaires et de dimensions (écrites dans la surcouche de variables de la macro propre à l'exécution), puis les entrées de tables — de sorte qu'un filtre d'entrée de table peut référencer les entrées scalaires.

**Ports d'entrée de tables :**

- **Source** — une table côté appelant (par nom ou identifiant) dont le contenu est copié dans le schéma temporaire de la macro sous le nom du port.
- **Colonnes** — projection facultative des colonnes. Choisissez un sous-ensemble et renommez-le si nécessaire (`source` → `target`) ; les colonnes sont entre guillemets et appliquées lors de la copie en entrée, de sorte que seules les colonnes projetées sont matérialisées.
- **Filtre** — clause `WHERE` facultative appliquée lors de la copie en entrée. Elle peut référencer par leur nom les variables d'entrée de la macro (résolues à partir des liaisons scalaires ci-dessus). Par exemple, `month = {month}` limite la copie en entrée à la tranche d'un mois d'une table pluriannuelle.

**Ports d'entrée scalaires et de dimensions :**

- **Variable** — le nom de la variable côté macro à définir (correspond à un port déclaré sur la macro).
- **Valeur** — la valeur à lier, soit un littéral, soit une référence à une variable côté appelant (résolue par rapport aux variables de l'appelant avant d'être écrite dans la surcouche de la sous-invocation).

## Liaisons des ports de sortie

Pour chaque port de sortie déclaré sur la macro, ajoutez une liaison qui pointe vers une table de destination côté appelant. La destination est créée à la volée si elle n'existe pas déjà. La copie en sortie :

- A lieu une fois la macro terminée avec succès (état `done` ou `warn`).
- Est **ignorée** si la macro est arrêtée manuellement en cours d'exécution (état `stop`) — des sorties partielles atterriraient sinon silencieusement dans le schéma durable de l'appelant.
- Applique la même projection facultative des **colonnes** que pour les liaisons d'entrée.

## Comportement en cas d'échec

| Résultat de la macro    | Effet côté appelant                                                   |
|-------------------------|-----------------------------------------------------------------------|
| `done` / `warn`         | Tables de sortie copiées vers les destinations de l'appelant ; schéma temporaire supprimé. |
| `stop` (arrêt manuel)   | Copie en sortie ignorée ; schéma temporaire supprimé ; avertissement consigné côté appelant. |
| Erreur en cours d'exécution | L'étape Macro Run échoue ; schéma temporaire supprimé ; sorties non écrites. |

Lorsque le workflow de la macro échoue, le journal de l'étape Macro Run affiche le message d'erreur propre à la macro (« Child workflow run failed: » suivi du message), ce qui vous permet de voir ce qu'il faut corriger sans ouvrir l'exécution de la macro.

Le schéma temporaire est toujours récupéré dans un bloc `finally` : une macro en échec ou arrêtée ne laisse donc jamais de tables intermédiaires dans le schéma du projet.

## Exemples

Pas encore d'exemples…

## Voir aussi

- [Créer une macro](/fr/guides/workflows/create-a-macro/) — déclarez un workflow comme macro et définissez son contrat de ports.
- [Exécuter le workflow](/fr/reference/workflow-steps/workflow-control/run-workflow/) — l'appelant de sous-workflow non isolé (ne peut pas cibler une macro).
