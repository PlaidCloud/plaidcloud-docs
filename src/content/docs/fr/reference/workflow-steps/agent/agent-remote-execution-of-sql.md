---
title: Étape Agent Remote Execution of SQL
description: Exécutez des requêtes SQL à distance via un agent PlaidLink dans les workflows PlaidCloud pour des opérations de base de données sécurisées derrière des pare-feu.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Description

Exécute du SQL sur une base de données que PlaidCloud ne peut atteindre que par l'intermédiaire d'un agent PlaidLink, généralement parce que la base de données se trouve derrière un pare-feu, sur un réseau privé ou dans un centre de données sur site. L'agent exécute le SQL localement et signale à PlaidCloud la réussite ou l'échec.

Utilisez-la pour déclencher des procédures stockées distantes, des routines d'actualisation ou des tâches de maintenance dans le cadre d'un workflow PlaidCloud sans exposer la base de données source à l'Internet public.

## Aperçu de la requête

Dans l'étape **Exécution à distance : SQL**, **Aperçu** dans l'onglet **Source** affiche jusqu'à 100 lignes sans exécuter l'instruction, ce qui vous permet de vérifier un `SELECT` avant de l'exécuter. L'aperçu renseigne les variables de la même manière qu'une exécution, mais ne prend pas en charge les formats de variables comme `{x:>9}`. Il ne fait que lire des données : une instruction qui écrit, ou une fonction que l'aperçu ne peut pas vérifier comme étant en lecture seule, est refusée avec le message *Preview only supports standard SQL functions. Run the step to see results.* L'aperçu n'est pas disponible sur un projet verrouillé, ni pour les instructions qui utilisent des paramètres fictifs `:name` avec une table d'inducteurs. Il n'est pas disponible pour l'étape basée sur un agent que décrit cette page, car seul l'agent peut atteindre ces bases de données.

## Exécuter une instruction une fois par ligne

L'étape **Exécution à distance : SQL**, qui se connecte directement à la base de données plutôt que via un agent, peut exécuter son instruction une fois pour chaque ligne d'une table, par exemple pour appeler une procédure stockée pour chaque ligne d'entrée. Définissez **Exécuter le SQL** sur **Une fois par ligne**, choisissez une **Table d'inducteurs** et renseignez **Paramètres**. Écrivez chaque valeur de l'instruction sous forme de paramètre fictif `:name`, par exemple `CALL load_region(:region, :period)`, et associez chaque paramètre fictif dans **Paramètre** à la **Colonne pilote** qui le fournit. Chaque valeur est envoyée à la base de données comme paramètre lié, jamais collée dans le texte de l'instruction.

Chaque paramètre nécessite à la fois un nom et une colonne pilote, et un paramètre ne peut pas être listé deux fois. Le formulaire avertit lorsqu'un `:name` de l'instruction n'a pas de mappage ou qu'un mappage ne figure pas dans l'instruction. La table pilote doit être une table, et non une vue. Une table pilote sans ligne se termine avec un avertissement et n'exécute rien, et une table de plus de 100 000 lignes fait échouer l'étape sans en exécuter aucune ; filtrez-la donc d'abord.

## Exécuter un script dans une seule transaction

Dans l'étape **Exécution à distance : SQL**, cochez **Exécuter le SQL comme un script d'instructions dans une seule transaction : tout est appliqué ou rien** (`transaction`) pour exécuter le SQL comme un script d'instructions, l'une après l'autre, dans une seule transaction, de sorte que chaque instruction est appliquée ou aucune ne l'est.
