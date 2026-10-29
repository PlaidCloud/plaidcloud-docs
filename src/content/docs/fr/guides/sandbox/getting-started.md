---
title: Premiers pas avec le bac à sable d'applications personnalisées
description: Commencez à créer et à déployer des applications personnalisées dans l'environnement Sandbox de PlaidCloud grâce aux étapes de mise en place et de configuration.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## Qu'est-ce que le Sandbox
Le Sandbox PlaidCloud permet de déployer vos propres applications personnalisées avec un accès local natif aux données et aux opérations PlaidCloud.  L'environnement Sandbox fournit un environnement de calcul complet pour créer des applications personnalisées qui enrichissent votre utilisation de PlaidCloud.

Toutes les applications personnalisées s'exécutent selon les processus de déploiement Kubernetes ; une compréhension de base des objets Kubernetes est donc nécessaire.  Un [exemple Hello World](https://github.com/PlaidCloud/custom-app-template) est disponible pour vous montrer comment déployer une application simple.

## Ressources disponibles
Les applications du Sandbox sont soumises à une limite de ressources souple, dans l'attente que l'utilisation des ressources ne soit pas abusive.  Nous pouvons prendre en charge de grandes quantités de calcul si nécessaire, mais discutons-en avant toute tentative de déploiement.  Contactez-nous si vous prévoyez d'avoir besoin de ressources importantes.

Les applications exécutées dans le sandbox auront un accès direct au Lakehouse et à autant de bases de données Postgres que vous le souhaitez.  Les bases de données Postgres sont conçues pour gérer des volumes de données modérés ; elles conviennent donc parfaitement au stockage des configurations et d'autres métadonnées.  Pour le stockage principal des données, utilisez le Lakehouse, qui permet de stocker de grandes quantités de données tout en restant performant.

Toutes les API PlaidCloud sont également disponibles directement depuis le Sandbox sans passer par une URL publique, ce qui améliore les vitesses de transfert des données.

## Exigences relatives aux images

Toute image qui prend en charge un déploiement Kubernetes basé sur Docker convient pour une application personnalisée.  Seules les images de type *nix sont actuellement prises en charge.  Si vous avez besoin d'exécuter une image Windows, contactez-nous.

## Intégration à votre pipeline CI/CD

Le déploiement Kubernetes de l'application Sandbox utilise des processus GitOps.  Cela vous permet de mettre en œuvre votre propre processus CI/CD pour les builds d'images et les déploiements.  Le dépôt git de votre application personnalisée est surveillé en permanence ; dès que des mises à jour y sont apportées, votre sandbox est mis à jour.
