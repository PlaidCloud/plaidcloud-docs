---
title: Étape Get Workspace Members
description: Écrivez les membres de l'espace de travail dans une table de projet, en choisissant les champs d'identité et d'activité à inclure.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Description

Écrit les membres de l'espace de travail dans une table de projet. Utilisez-la pour établir des rapports sur les accès, rapprocher une liste de membres d'un flux RH ou piloter une étape en aval à partir des personnes qui ont actuellement accès.

## Configuration

### Informations à inclure

Activés par défaut : **Nom de famille**, **Prénom**, **E-mail**, **Nom d'utilisateur**, **Date de création du membre** et **Horodatage de la dernière connexion**.

### Paramètres supplémentaires

Désactivés par défaut :

- **Inclure les membres désactivés** — élargit la sortie au-delà des membres actifs.
- **Mode d'historique des connexions** — renvoie l'historique des connexions plutôt que la seule dernière connexion.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/fr/reference/workflow-steps/general/deactivate-workspace-members/)
- [Gestion des membres](/fr/administration/access/)
