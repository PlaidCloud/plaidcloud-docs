---
title: Projets
description: Configurez et gérez des projets PlaidCloud pour organiser les workflows, les tables, les importations de données et les autres objets d'analyse selon leur finalité.
sidebar:
  label: Projets
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

Un **projet** est l'unité de travail de PlaidCloud. Chaque projet possède ses propres données, workflows, dimensions et historique d'audit. Les projets ne partagent pas d'état entre eux : ils sont isolés, ce qui en fait la frontière naturelle pour séparer des analyses, des processus métier ou des produits de données distincts.

La plupart des équipes commencent par un projet par domaine d'analyse : un projet pour l'allocation des coûts de masse salariale, un autre pour l'analyse des revenus, un autre pour la clôture mensuelle, selon la façon dont votre équipe conçoit son travail.

## Contenu de cette section

- [Gérer les projets](/fr/guides/projects/managing-projects/) : créez, configurez et organisez les projets de votre espace de travail
- [Data Foundation : le Common Finance Model](/fr/guides/projects/data-foundation/) : réunissez les données ERP de plusieurs systèmes et instances ERP, via leurs connexions directes, dans un seul Common Finance Model que lisent les rapports, les métriques et les assistants IA
- [Démarrer avec Data Foundation](/fr/guides/projects/data-foundation-getting-started/) : la liste de contrôle de configuration, du nouveau projet jusqu'au modèle chargé, vérifié et transmis
- [Cost to Serve](/fr/guides/projects/cost-to-serve/) : répartissez les charges d'exploitation entre les clients par activité et consultez la marge après déduction du coût pour les servir
- [Operational Transfer Pricing](/fr/guides/projects/operational-transfer-pricing/) : comparez le niveau de profit de chaque entité aux fourchettes de votre politique et consultez la régularisation
- [Accueil du projet](/fr/guides/projects/project-home/) : consultez un projet d'un coup d'œil et gérez ses variables, planifications, accès, valeurs par défaut des données et applications
- [Modèle de données et éléments de projet](/fr/guides/projects/data-model/) : décrivez une seule fois une colonne que vos tables partagent, et voyez quelles tables la partagent
- [Consulter les projets](/fr/guides/projects/viewing-projects/) : recherchez et ouvrez des projets existants
- [Gérer les hiérarchies](/fr/guides/projects/managing-hierarchies/) : structure de dossiers pour organiser de nombreux projets
- [Gérer les tables et les vues](/fr/guides/projects/managing-tables-and-views/) : la couche de données au sein d'un projet
- [Gérer les éditeurs de données](/fr/guides/projects/managing-data-editors/) : qui peut modifier les données du projet
- [Consulter le journal du projet](/fr/guides/projects/viewing-the-project-log/) : piste d'audit des modifications
- [Archiver un projet](/fr/guides/projects/archive-a-project/) : conservez le travail terminé sans le supprimer
- [Fils d'Ariane et liens](/fr/guides/projects/breadcrumbs-and-shareable-links/) : remontez depuis n'importe quelle fenêtre et partagez un lien vers ce que vous consultez
- [Comparer et fusionner des projets](/fr/guides/projects/compare-and-merge-projects/) : comparez deux projets et copiez sélectivement les modifications de l'un à l'autre
- [Exporter vers un format portable](/fr/guides/projects/export-to-portable-format/) : empaquetez un projet sous la forme d'un programme Python + DuckDB autonome qui s'exécute hors de la plateforme
- [Gérer le stockage](/fr/guides/projects/managing-storage/) : consultez ce que stocke votre espace de travail et définissez la durée de conservation de l'historique des tables
- [Organiser le travail avec des étiquettes](/fr/guides/projects/organizing-with-labels/) : étiquetez les workflows, étapes, tables et autres objets pour les regrouper et les filtrer
- [Partager des liens](/fr/guides/projects/sharing-links/) : copiez un lien depuis la barre d'adresse qui ouvre directement un projet, un workflow, une table ou une dimension

## Voir aussi

- [Concepts](/fr/get-started/concepts/) : comment les projets s'articulent avec les espaces de travail, les membres et le modèle de données global
- [Workflows](/fr/guides/workflows/) : la primitive d'automatisation qui vit à l'intérieur d'un projet
- [Gestion des accès](/fr/administration/access/) : contrôles au niveau de l'espace de travail qui déterminent qui peut voir et modifier les projets
