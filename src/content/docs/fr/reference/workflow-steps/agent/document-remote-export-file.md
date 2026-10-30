---
title: Document - Remote Export File
description: Exportez des fichiers vers des systèmes distants via un agent PlaidLink dans les workflows PlaidCloud pour des transferts de fichiers sécurisés derrière un pare-feu.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Description



Écrit un fichier d'un compte de documents PlaidCloud vers un système de fichiers distant via un agent PlaidLink. Utile pour livrer des rapports, des extractions ou des fichiers traités à des systèmes que PlaidCloud ne peut pas atteindre directement : partages réseau internes, serveurs SFTP sur site ou répertoires d'applications spécialisées.

L'agent reçoit le fichier de PlaidCloud et l'écrit dans la destination locale configurée.


## Exemples


Sélectionnez d'abord une valeur dans la liste déroulante « Agent to Use ». Recherchez ensuite le chemin du fichier ou du dossier sous « File or Folder to Export ». Saisissez alors l'emplacement sous « Export Path Destination ». Enfin, sélectionnez « Save and Run Step ».

## Sécurité des chemins

Un chemin d'exportation vide fait échouer l'étape avec `No destination path for the export; it would write into the agent's working directory.` Cela inclut un chemin qui n'a rien donné parce qu'une variable qu'il contient était vide. Exporter vers la racine d'un lecteur ou d'un partage, comme `E:\` ou `\\nas\drop`, fonctionne.

Lorsque **Décompresser l'archive à l'arrivée** est sélectionné, l'étape décompresse chaque archive du dossier de destination et la supprime. Elle refuse donc une destination qui est une racine du système de fichiers ou un fichier situé directement dans une racine (`Refusing to unpack an export into the filesystem root <path>.`), ou le dossier propre de l'agent PlaidLink (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Choisissez plutôt un sous-dossier dédié.

Les contrôles de chemin vide et de racine fonctionnent avec les agents PlaidLink que vous avez déjà déployés. Le refus du dossier propre de l'agent nécessite un agent PlaidLink à jour.
