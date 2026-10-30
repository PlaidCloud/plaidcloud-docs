---
title: Outils CLI
description: "Référence des outils en ligne de commande PlaidCloud : l'agent PlaidLink, le complément Excel PlaidXL et la CLI Jupyter pour l'intégration des notebooks."
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud fournit trois outils en ligne de commande ou installés sur votre machine pour travailler avec les espaces de travail en dehors de l'interface web :

## PlaidLink

[PlaidLink](/fr/reference/cli/plaidlink/) est un agent qui s'exécute dans votre réseau pour relier les workflows PlaidCloud aux ressources protégées par un pare-feu : bases de données, partages de fichiers et autres systèmes que PlaidCloud ne peut pas atteindre directement. Il s'installe en tant que service Windows, démon Unix/Linux/Mac, conteneur ou pod Kubernetes.

- [Installation](/fr/reference/cli/plaidlink/install/)
- [Configuration](/fr/reference/cli/plaidlink/configure/)
- [Agents](/fr/reference/cli/plaidlink/agents/)
- [Mise à niveau](/fr/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/fr/reference/cli/plaidxl/) est le complément PlaidCloud pour Microsoft Excel. Il récupère les tables et les dimensions de projet dans des feuilles de calcul, les actualise à la demande et ajoute des formules `PLAIDXL` qui calculent des valeurs consolidées à partir des données PlaidCloud.

- [Installation](/fr/reference/cli/plaidxl/install/)
- [Connexion](/fr/reference/cli/plaidxl/connect/)
- [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/)
- [Fonctions personnalisées](/fr/reference/cli/plaidxl/functions/)
- [Créer un rapport avec des fonctions personnalisées](/fr/reference/cli/plaidxl/build-a-report/)
- [Le ruban PlaidCloud](/fr/reference/cli/plaidxl/ribbon/)
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/)

## CLI Jupyter

[La CLI Jupyter](/fr/reference/cli/jupyter/) permet aux data scientists de travailler avec les données de projet PlaidCloud depuis des notebooks Jupyter, à l'aide d'une CLI compatible PlaidCloud et d'utilitaires Python.

- [Ligne de commande](/fr/reference/cli/jupyter/command-line/)
- [Notebook Jupyter](/fr/reference/cli/jupyter/jupyter-notebook/)
- [Configuration d'OAuth](/fr/reference/cli/jupyter/oauth-setup/)
