---
title: Document - Remote Import File
description: Importez des fichiers depuis des systèmes distants via un agent PlaidLink dans les workflows PlaidCloud pour une récupération de fichiers sécurisée derrière un pare-feu.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Description



Récupère un fichier sur un système de fichiers distant via un agent PlaidLink et le stocke dans un compte de documents PlaidCloud. À utiliser lorsque les fichiers sources proviennent de partages de fichiers internes, de serveurs sur site ou se trouvent derrière un pare-feu.

L'agent lit le fichier localement et le transmet en flux continu à PlaidCloud, où les étapes de workflow suivantes peuvent le traiter.


## Exemples


Sélectionnez d'abord une valeur dans la liste déroulante « Agent to Use ». Saisissez ensuite le chemin du fichier ou du dossier sous « File or Folder Path for Import ». Saisissez alors le dossier de destination sous « Folder Destination ». Vous pouvez aussi choisir une **Compression** pour compresser le fichier à son arrivée : Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib). Enfin, sélectionnez « Save and Run Step ».

## Fichier ou dossier source manquant

Lorsqu'il n'existe rien au chemin indiqué sur le partage distant, l'étape se termine avec un avertissement, `No file or folder found at <path>; nothing imported.`, au lieu d'une erreur. Le workflow passe à l'étape suivante, et les paramètres de nouvelle tentative et de gestion des erreurs de l'étape (aller à une étape, ou continuer) ne s'appliquent pas à une source manquante. Cela fonctionne avec les agents PlaidLink que vous avez déjà déployés.

Un chemin vide se termine de la même façon, avec l'avertissement `No path to import from; nothing imported.`. Cela inclut un chemin dont le dossier est une variable qui n'a rien donné lors de cette exécution, comme `{folder}/archive`.

Un chemin qui est une racine du système de fichiers ou un dossier parent du répertoire de travail de l'agent PlaidLink (`/`, `C:\`, une racine de partage telle que `\\server\share`, ou `..`) fait échouer l'étape avant tout transfert, avec `Refusing to import from the filesystem root <path>.` ou `Refusing to import from <path>, which contains the agent's working directory.` Les racines et `..` sont refusées par les agents PlaidLink que vous avez déjà déployés ; un agent à jour refuse également tout autre dossier contenant son répertoire de travail, d'après son propre système de fichiers.

D'autres échecs font toujours échouer l'étape : autorisation refusée, échec du transfert vers PlaidCloud ou, avec un agent PlaidLink à jour, serveur ou partage injoignable.

Comme rien n'est importé, un document issu d'une exécution précédente reste là où il était. Pour n'exécuter une étape en aval que lorsque le fichier de la période est arrivé, vous pouvez soit :

- Ajouter à l'étape en aval une [condition d'étape](/fr/guides/workflows/step-conditions/#conditions-de-chemin-de-document) **file exists in Document**, avec un chemin de document propre à chaque période, par exemple un chemin dont le nom de fichier inclut la période.
- Supprimer le document importé après son utilisation par le workflow, afin qu'une source manquante ne laisse pas un ancien fichier en place.
