---
title: Étape Get Workspace Members
description: Écrit les membres de l'espace de travail dans une table de projet, en choisissant les champs d'identité et d'activité à inclure.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Description

Écrit les membres de l'espace de travail dans une table de projet. Servez-vous-en pour établir des rapports sur les accès, rapprocher une liste de membres d'un flux RH ou piloter une étape en aval selon les personnes qui ont actuellement accès.

## Configuration

### Informations à inclure

Activés par défaut : **Nom de famille**, **Prénom**, **E-mail**, **Nom d'utilisateur**, **Date de création du membre** et **Horodatage de la dernière connexion**.

### Paramètres supplémentaires

Désactivés par défaut :

- **Inclure les membres désactivés** — élargit la sortie au-delà des membres actifs.
- **Mode d'historique des connexions** — renvoie l'historique des connexions plutôt que seulement la dernière connexion.

## Journal de sécurité

Chaque exécution écrit une entrée dans le Journal de sécurité qui consigne les colonnes écrites, la table cible, le workflow, l'étape et l'exécution.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/fr/reference/workflow-steps/general/deactivate-workspace-members/) (étape)
- [Get Workspace Usage](/fr/reference/workflow-steps/general/get-workspace-usage/) (étape)
- [Gestion des membres](/fr/administration/access/)
