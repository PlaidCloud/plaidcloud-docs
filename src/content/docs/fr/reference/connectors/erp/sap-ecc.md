---
title: Connecteur SAP ECC et S/4HANA
description: Configurez la connexion SAP ECC / S/4HANA dans PlaidCloud pour intégrer par RFC les données financières, logistiques et opérationnelles de SAP à vos workflows.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Un seul type de connexion couvre à la fois SAP ECC et SAP S/4HANA. Les deux sont atteints de la même manière — des appels de fonction distants (Remote Function Calls) sur le serveur d'applications — si bien que PlaidCloud ne vous demande pas de quelle génération il s'agit. Dans l'écran **Connexions**, choisissez **Nouveau → Instance SAP ECC / S/4HANA**.

Toutes les [étapes de workflow SAP](/fr/reference/workflow-steps/sap/) s'exécutent sur une connexion de ce type. Pour rechercher dans SAP et extraire des tables, des transactions, des rapports et des requêtes SAP Query enregistrées, consultez [Ad-Hoc Extracts from SAP ECC / S/4HANA](/fr/guides/connections/sap-adhoc-extract/).

## Documentation officielle

SAP a supprimé toute la documentation d'ECC et ne fournit plus actuellement que celle de [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). Les interfaces RFC qu'utilise PlaidCloud sont communes aux deux.

## Configuration

Ces champs apparaissent lorsque vous créez ou modifiez la connexion.

### Description du compte

| Champ | Type | Description |
|---|---|---|
| Nom du compte | Texte | Nom d'affichage de cette connexion, affiché partout où une étape choisit une connexion. Obligatoire. |
| Mémo | Texte (multiligne) | Notes facultatives sur la connexion — le système visé, son propriétaire. |

### Environnement SAP

| Champ | Type | Description |
|---|---|---|
| Client | Texte | Numéro du client SAP, par ex. `100`. Obligatoire. |
| Langue | Liste de sélection | Langue de connexion, sous la forme d'un code SAP à deux lettres. `EN` par défaut. Obligatoire. |
| Niveau de trace | Liste de sélection | Niveau de détail de la trace RFC : Désactivée, Succincte, Détaillée ou Complète. Laissez la valeur Désactivée, sauf si vous diagnostiquez un problème de connexion. Obligatoire. |
| Type de connexion | Bouton radio | **Utiliser une connexion directe unique** pour atteindre un seul serveur d'applications, ou **Utiliser une connexion multisystème avec équilibrage de charge** pour passer par un serveur de messages. Les champs ci-dessous s'activent selon ce choix. |

Le choix de **Utiliser une connexion directe unique** active :

| Champ | Type | Description |
|---|---|---|
| Hôte | Texte | Nom d'hôte ou adresse IP du serveur d'applications. |
| Numéro du système | Texte | Numéro de système SAP à deux chiffres, par ex. `00`. |

Le choix de **Utiliser une connexion multisystème avec équilibrage de charge** active :

| Champ | Type | Description |
|---|---|---|
| Hôte MS | Texte | Nom d'hôte ou adresse IP du serveur de messages. |
| Serveur MS | Texte | Port ou nom de service du serveur de messages. |
| ID du système | Texte | ID de système SAP à trois caractères, par ex. `PRD`. |
| Groupe | Texte | Groupe de connexion sur lequel répartir la charge, par ex. `PUBLIC`. |

### Identifiants d'authentification

| Champ | Type | Description |
|---|---|---|
| Utilisateur | Texte | Utilisateur de connexion SAP pour les appels RFC. Obligatoire. |
| Mot de passe | Mot de passe | Mot de passe de cet utilisateur. En écriture seule : laissez le champ vide lors d'une modification pour conserver le mot de passe stocké. |

### Utilisation

| Champ | Type | Description |
|---|---|---|
| Actif (autoriser l'accès) | Interrupteur | Indique si la connexion peut être utilisée. Décochez-le pour mettre la connexion en pause sans la supprimer. |
| Lecture seule | Interrupteur | Limiter la connexion aux opérations de lecture. |

### Modèle de sécurité

| Champ | Type | Description |
|---|---|---|
| Modèle de sécurité | Liste de sélection | Qui peut utiliser cette connexion : Privé (propriétaires uniquement), Membres spécifiques uniquement, Groupes de sécurité spécifiques uniquement ou Tous les membres de l'espace de travail. |

## Tester la connexion

**Tester la connexion**, dans la fenêtre de la connexion, ouvre une session avec les informations ci-dessus et vous renvoie le résultat. Lorsque vous modifiez une connexion existante et changez un paramètre, ressaisissez le mot de passe avant de tester — le mot de passe stocké n'est pas envoyé avec les valeurs modifiées.
