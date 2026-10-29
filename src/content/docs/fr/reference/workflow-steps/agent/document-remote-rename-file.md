---
title: Document - Remote Rename File
description: Renommez des fichiers sur des systèmes distants via un agent PlaidLink dans les workflows PlaidCloud pour une gestion de fichiers sécurisée derrière un pare-feu.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Description



Renomme ou déplace un fichier sur un système de fichiers distant via un agent PlaidLink. Fonctionne entièrement côté site ; aucune donnée n'est transférée vers ou depuis PlaidCloud.

Schéma courant : renommer un fichier source pour le marquer comme « traité » après la réussite d'une étape d'importation à distance, afin que le même workflow ne le réimporte pas à l'exécution suivante.


## Exemples


Sélectionnez d'abord une valeur dans la liste déroulante « Agent to Use ». 



Saisissez ensuite « Source Path » et « Destination Path ». 



Enfin, sélectionnez « Save and Run Step ».

## Source manquante

Avec un agent PlaidLink à jour, une source qui n'existe pas sur le système distant termine l'étape avec un avertissement, `No file or folder found at <path>; nothing renamed`, au lieu d'une erreur, et le workflow continue. Les agents qui n'ont pas été mis à jour font toujours échouer l'étape.

Un chemin source vide termine l'étape avec l'avertissement `No path to rename from; nothing renamed.`, y compris lorsqu'un dossier du chemin est une variable qui n'a rien donné lors de cette exécution.

Une source qui est une racine du système de fichiers ou un dossier parent du répertoire de travail de l'agent PlaidLink (`/`, `C:\`, une racine de partage telle que `\\server\share`, ou `..`) fait échouer l'étape avec `Refusing to rename from the filesystem root <path>.` ou `Refusing to rename from <path>, which contains the agent's working directory.` Un chemin de destination vide fait échouer l'étape avec `No destination path for the rename; it would write into the agent's working directory.` Renommer vers la racine d'un lecteur ou d'un partage, comme `E:\` ou `\\nas\drop`, fonctionne. Les racines et `..` sont refusées par les agents PlaidLink que vous avez déjà déployés ; un agent à jour refuse également tout autre dossier contenant son répertoire de travail, d'après son propre système de fichiers.
