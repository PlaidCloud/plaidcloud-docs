---
title: Document - Remote Delete File
description: Supprimez des fichiers sur des systèmes distants via un agent PlaidLink dans les workflows PlaidCloud pour une gestion de fichiers sécurisée derrière un pare-feu.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Description



Supprime un fichier sur un système de fichiers situé derrière un pare-feu, atteint via un agent PlaidLink. L'agent effectue la suppression localement sur le système de fichiers sur site.

Utilisez cette étape pour le nettoyage après des exportations sur site, ou dans des intégrations par fichiers qui doivent supprimer les fichiers sources traités.


## Exemples


Sélectionnez d'abord une valeur dans la liste déroulante « Agent to Use ». Saisissez ensuite le chemin du fichier ou du dossier sous « File or Folder Path for Delete ». Enfin, sélectionnez « Save and Run Step ».

## Chemin manquant

Avec un agent PlaidLink à jour, un chemin qui n'existe pas sur le système distant termine l'étape avec un avertissement, `Nothing to delete at <path>`, au lieu d'une erreur, et le workflow continue. Les agents qui n'ont pas été mis à jour font toujours échouer l'étape.

Un chemin vide termine l'étape avec l'avertissement `No path to delete; nothing deleted.` et ne supprime rien. Cela inclut un chemin dont le dossier est une variable qui n'a rien donné lors de cette exécution, comme `{folder}/archive`.

Un chemin qui est une racine du système de fichiers ou un dossier parent du répertoire de travail de l'agent PlaidLink (`/`, `C:\`, une racine de partage telle que `\\server\share`, ou `..`) fait échouer l'étape avant toute suppression, avec `Refusing to delete the filesystem root <path>.` ou `Refusing to delete <path>, which contains the agent's working directory.` Les racines et `..` sont refusées par les agents PlaidLink que vous avez déjà déployés ; un agent à jour refuse également tout autre dossier contenant son répertoire de travail, d'après son propre système de fichiers.
