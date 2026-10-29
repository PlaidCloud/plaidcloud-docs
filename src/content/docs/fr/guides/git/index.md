---
title: PlaidCloud Git
description: Hébergez, versionnez et collaborez sur des dépôts Git dans PlaidCloud, avec tickets, pull requests, tableaux de projet, releases et wikis, et authentification unique intégrée.
sidebar:
  label: Vue d'ensemble
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git est un service Git privé intégré à votre espace de travail. Chaque espace de travail dispose de son propre serveur Git pour stocker du code, de la configuration, des notebooks et tout autre fichier versionné, ainsi que les tickets, pull requests et tableaux de projet que votre équipe utilise pour collaborer dessus.

Vous vous connectez avec votre compte PlaidCloud : il n'y a donc ni nom d'utilisateur ni mot de passe distinct à configurer. Ouvrez **Git** depuis votre espace de travail et vous êtes déjà connecté. Les nouveaux dépôts sont privés par défaut et visibles uniquement des membres auxquels vous accordez l'accès.

## Administrer Git

Tout membre peut créer des dépôts, mais la **création d'organisations** (des espaces partagés qui regroupent des dépôts et des équipes) nécessite l'autorisation **Git Administration**. Accordez-la dans **Identité** en ajoutant l'autorisation à un groupe de sécurité, ou en ajoutant des membres au groupe intégré **Git Administration**. Toute personne appartenant à un groupe disposant de cette autorisation devient administrateur Git à sa prochaine connexion à Git. Le personnel du support PlaidCloud la possède automatiquement.

Si un administrateur nouvellement autorisé n'a jamais ouvert Git, il peut devoir se connecter à Git **deux fois** pour que l'accès administrateur prenne effet : la première connexion crée son compte Git, et l'autorisation est appliquée à la suivante.

## Contenu de cette section

- [Dépôts](/fr/guides/git/repositories/) : créez un dépôt, puis clonez, validez et poussez votre travail
- [Tickets](/fr/guides/git/issues/) : suivez les tâches, les bogues et les idées avec des libellés, des jalons et des personnes assignées
- [Pull requests](/fr/guides/git/pull-requests/) : proposez des modifications sur une branche et faites-les relire avant la fusion
- [Tableaux de projet](/fr/guides/git/projects/) : organisez les tickets et les pull requests sur un tableau Kanban
- [Releases et étiquettes](/fr/guides/git/releases-and-tags/) : marquez et publiez des instantanés versionnés d'un dépôt
- [Wikis](/fr/guides/git/wikis/) : conservez une documentation détaillée à côté de votre code
- [Packages](/fr/guides/git/packages/) : publiez et installez des artefacts de build depuis le registre du dépôt
- [Recherche de code](/fr/guides/git/searching-code/) : retrouvez du code, des tickets et des pull requests dans vos dépôts

## Voir aussi

- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) : servez une application HoloViz Panel directement depuis un dépôt, avec une connexion gérée sans identifiants
- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) : servez de la même manière une application Plotly Dash
- [Gestion des accès](/fr/administration/access/) : comment l'appartenance à l'espace de travail et les groupes de sécurité déterminent qui peut voir et modifier les dépôts
