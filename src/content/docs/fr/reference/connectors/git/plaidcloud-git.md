---
title: Connecteur PlaidCloud Git
description: Connectez une application Panel, une application Dash ou un workflow à un dépôt de PlaidCloud Git, le service Git géré et intégré, sans URL de serveur ni identifiants à configurer.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git** est le service Git géré intégré à votre espace de travail. Une connexion PlaidCloud Git relie un déploiement Panel ou Dash, ou un workflow, à l'un de vos dépôts. Le service étant géré, il ne nécessite **aucune URL de serveur, aucun nom d'utilisateur ni aucun jeton** : PlaidCloud fournit l'hôte et s'authentifie pour vous.

Pour la procédure complète de mise en service d'une application à partir d'une de ces connexions, consultez [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) ou [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/). Pour créer des dépôts et y envoyer du code, consultez les [guides PlaidCloud Git](/fr/guides/git/).

## Configuration

Dans **Tools > Connections**, cliquez sur **Nouvelle connexion** et choisissez **PlaidCloud Git**. Le formulaire omet les sections d'authentification, SSL et SSH qu'affichent les fournisseurs Git externes (les identifiants sont dérivés de la plateforme) et ne conserve que l'identité de la connexion, son utilisation et le dépôt cible.

### Identification

| Champ | Type | Description |
|---|---|---|
| Nom du compte | Texte | Nom d'affichage de cette connexion. |
| Mémo | Texte | Remarque facultative sur l'usage de la connexion. |

### Dépôt

| Champ | Type | Description |
|---|---|---|
| Dépôt | Sélecteur | Le dépôt à utiliser. Cliquez sur **Actualiser** pour lister les dépôts de votre espace de travail (par exemple `apps` ou `udfs`) et en choisir un. |
| Branche par défaut | Sélecteur | La branche à lire, choisie parmi les branches du dépôt sélectionné. |
| Chemin de départ | Sélecteur | Facultatif. Parcourez le dépôt sélectionné et choisissez un dossier pour limiter toutes les recherches de fichiers à un sous-répertoire. |

L'**Utilisation** (`Active` / `Read Only`) et le **Modèle de sécurité** (qui, dans l'espace de travail, peut utiliser la connexion) sont les paramètres de connexion standard. Consultez le [guide de la connexion](/fr/guides/connections/plaidcloud-git/) et [Créer et gérer une connexion](/fr/guides/connections/create-connection/).

## Utilisations courantes

- Servir une [application HoloViz Panel](/fr/guides/panel-apps/deploy-from-git/) ou une [application Plotly Dash](/fr/guides/dash-apps/deploy-from-git/) depuis le dépôt `apps` de votre espace de travail.
- Récupérer des fonctions définies par l'utilisateur, de la configuration ou des fichiers modélisés qui résident dans PlaidCloud Git.

## Voir aussi

- [Connexion PlaidCloud Git](/fr/guides/connections/plaidcloud-git/) — guide pratique pour créer la connexion, avec l'utilisation et le modèle de sécurité
- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) — le parcours complet, du dépôt à l'application servie
- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) — le même parcours pour une application Plotly Dash
- [Guides PlaidCloud Git](/fr/guides/git/) — dépôts, tickets, demandes de fusion, etc.
- [Connexions aux dépôts Git](/fr/reference/connectors/git/) — fournisseurs Git externes (GitHub, GitLab, etc.)
