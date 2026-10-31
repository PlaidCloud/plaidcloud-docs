---
title: Étape Deactivate Workspace Members
description: Désactivez les membres de l'espace de travail listés dans une table de projet, identifiés par leur adresse e-mail ou leur nom d'utilisateur.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Description

Désactive les membres de l'espace de travail nommés dans une table source. Utilisez-la pour automatiser les départs à partir d'une liste de référence — un extrait RH ou une revue des accès — plutôt que de désactiver les personnes à la main.

Associez-la à [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/) pour construire la liste des personnes qui ne doivent plus avoir accès.

<Aside type="caution" title="Cette action révoque l'accès">
  Chaque membre identifié perd son accès à l'exécution de l'étape. Vérifiez que la table source
  ne contient que les personnes visées avant de planifier cette étape.
</Aside>

## Administrateurs de l'espace de travail dans la liste

[Seul un administrateur de l'espace de travail peut désactiver un administrateur de l'espace de travail](/fr/administration/access/member-management/#modifier-un-administrateur-de-lespace-de-travail). Lorsque l'étape s'exécute sans droits d'administrateur de l'espace de travail et que sa liste contient des administrateurs, elle laisse ces administrateurs actifs, désactive tous les autres, puis se termine en erreur avec un message indiquant combien de membres elle a désactivés et nommant chaque administrateur laissé actif. Les membres qu'elle a désactivés le restent. Pour désactiver un administrateur, demandez à un administrateur de l'espace de travail de le faire dans Identity.

## Configuration

### Paramètre de recherche de membre

La manière dont les lignes de la table source sont associées aux membres. Choisissez l'une des options suivantes :

- **E-mail** (par défaut)
- **Nom d'utilisateur**

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/)
- [Gestion des membres](/fr/administration/access/)
