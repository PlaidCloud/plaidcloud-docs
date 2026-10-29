---
title: Agent Remote Execution of SQL
description: Exécutez des requêtes SQL à distance via un agent PlaidLink dans les workflows PlaidCloud pour des opérations de base de données sécurisées derrière un pare-feu.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Description

Exécute du SQL sur une base de données que PlaidCloud ne peut atteindre que par l'intermédiaire d'un agent PlaidLink, généralement parce que la base se trouve derrière un pare-feu, sur un réseau privé ou dans un centre de données sur site. L'agent exécute le SQL localement et signale à PlaidCloud la réussite ou l'échec.

Utilisez cette étape pour déclencher des procédures stockées distantes, des routines d'actualisation ou des tâches de maintenance dans un workflow PlaidCloud, sans exposer la base de données source à l'Internet public.

## Exécuter une instruction une fois par ligne

L'étape **Exécution à distance : SQL**, qui se connecte directement à la base de données plutôt que par un agent, peut exécuter son instruction une fois pour chaque ligne d'une table, par exemple pour appeler une procédure stockée pour chaque ligne en entrée. Définissez **Exécuter le SQL** sur **Une fois par ligne**, choisissez une **Table d'inducteurs** et renseignez les **Paramètres**. Écrivez chaque valeur de l'instruction sous la forme d'un espace réservé `:name`, comme `CALL load_region(:region, :period)`, et associez chaque espace réservé, dans **Paramètre**, à la **Colonne pilote** qui le fournit. Chaque valeur est envoyée à la base de données sous forme de paramètre lié, et jamais collée dans le texte de l'instruction.

Chaque paramètre nécessite à la fois un nom et une colonne pilote, et un paramètre ne peut pas être listé deux fois. Le formulaire vous avertit lorsqu'un `:name` de l'instruction n'a pas d'association, ou lorsqu'une association ne figure pas dans l'instruction. La table d'inducteurs doit être une table, pas une vue. Une table d'inducteurs sans ligne se termine par un avertissement et n'exécute rien ; une table de plus de 100 000 lignes fait échouer l'étape sans en exécuter aucune, filtrez-la donc d'abord.

## Exécuter un script dans une seule transaction

Dans l'étape **Exécution à distance : SQL**, cochez **Exécuter le SQL comme un script d'instructions dans une seule transaction : tout est appliqué ou rien** (`transaction`) pour exécuter le SQL comme un script d'instructions, l'une après l'autre, dans une seule transaction : soit toutes les instructions sont appliquées, soit aucune ne l'est.
