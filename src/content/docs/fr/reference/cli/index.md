---
title: Outils CLI
description: "Référence des outils en ligne de commande de PlaidCloud : l'agent PlaidLink, le complément Excel PlaidXL et la CLI Jupyter pour l'intégration des notebooks."
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

PlaidCloud propose trois outils en ligne de commande et installés sur la machine pour travailler avec les espaces de travail en dehors de l'interface web :

## PlaidLink

[PlaidLink](/fr/reference/cli/plaidlink/) est un agent qui s'exécute dans votre réseau pour relier les workflows PlaidCloud aux ressources protégées par un pare-feu (bases de données, partages de fichiers et autres systèmes que PlaidCloud ne peut pas atteindre directement). Il s'installe comme service Windows, démon Unix/Linux/Mac, conteneur ou pod Kubernetes.

- [Install](/fr/reference/cli/plaidlink/install/)
- [Configure](/fr/reference/cli/plaidlink/configure/)
- [Agents](/fr/reference/cli/plaidlink/agents/)
- [Upgrade](/fr/reference/cli/plaidlink/upgrade/)

## PlaidXL

[PlaidXL](/fr/reference/cli/plaidxl/) est le complément PlaidCloud pour Microsoft Excel. Il récupère les tables et les dimensions de projet dans des feuilles de calcul, les actualise à la demande, ajoute des formules `PLAIDXL` qui calculent des valeurs consolidées et des métriques gouvernées à partir des données PlaidCloud, et réécrit les valeurs planifiées.

- [Install](/fr/reference/cli/plaidxl/install/)
- [Sign In](/fr/reference/cli/plaidxl/connect/)
- [Work With Tables and Dimensions](/fr/reference/cli/plaidxl/retrieve/)
- [Custom Functions](/fr/reference/cli/plaidxl/functions/)
- [Build a Report](/fr/reference/cli/plaidxl/build-a-report/)
- [Drill, Pick Members and Explain Numbers](/fr/reference/cli/plaidxl/drill/)
- [Type Values Into PlaidCloud](/fr/reference/cli/plaidxl/write-values/)
- [Demander à Weave dans Excel](/fr/reference/cli/plaidxl/weave/)
- [The PlaidCloud Ribbon](/fr/reference/cli/plaidxl/ribbon/)
- [Troubleshooting](/fr/reference/cli/plaidxl/troubleshooting/)

## CLI Jupyter

La [CLI Jupyter](/fr/reference/cli/jupyter/) permet aux data scientists de travailler avec les données de projet PlaidCloud depuis des notebooks Jupyter, grâce à une CLI compatible PlaidCloud et à des utilitaires Python.

- [Command line](/fr/reference/cli/jupyter/command-line/)
- [Jupyter notebook](/fr/reference/cli/jupyter/jupyter-notebook/)
- [OAuth setup](/fr/reference/cli/jupyter/oauth-setup/)
