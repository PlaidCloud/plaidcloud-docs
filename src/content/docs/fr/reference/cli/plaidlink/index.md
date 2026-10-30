---
title: PlaidLink
description: Installez et configurez les agents PlaidLink pour accéder en toute sécurité aux systèmes situés derrière un pare-feu, avec requêtes à distance et transferts de fichiers.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink fournit un accès indirect aux systèmes et aux processus des clients protégés par des pare-feu ou soumis à d'autres restrictions qui rendent difficiles les connexions directes depuis PlaidCloud. Grâce à un Agent PlaidCloud installé dans la zone isolée, PlaidCloud peut demander à l'agent d'effectuer des actions telles que l'exécution de requêtes, le téléchargement ou l'envoi de fichiers, la vérification de conditions de capteurs, l'interaction avec SAP, et bien plus encore.

L'agent initiant le contact avec PlaidCloud et communiquant via les protocoles réseau HTTPS standard, il peut normalement fonctionner avec une configuration minimale. De plus, il peut s'exécuter avec un utilisateur non privilégié afin de contrôler les droits d'accès dans un environnement restreint.

## Sujets

- [Installation](/fr/reference/cli/plaidlink/install/) — mise en service de PlaidLink sous Windows, Linux, macOS ou dans un conteneur
- [Configuration](/fr/reference/cli/plaidlink/configure/) — paramètres de connexion, identifiants et options d'exécution
- [Agents](/fr/reference/cli/plaidlink/agents/) — gestion de plusieurs agents et de leurs capacités
- [Mise à niveau](/fr/reference/cli/plaidlink/upgrade/) — passage à une version plus récente de PlaidLink
