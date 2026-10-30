---
title: Connecteur TM1
description: Connectez PlaidCloud à un serveur IBM TM1 / Planning Analytics via son API REST (authentification Basic native ou par espace de noms CAM), en accès direct depuis le cloud ou via un agent PlaidLink local pour un serveur que le cloud ne peut pas atteindre directement.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Connectez PlaidCloud à un serveur IBM **TM1 / Planning Analytics** via son API REST OData v4 publiée, sans pont JVM ni pilote PAOlap. Lisez les données d'un cube avec [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) ou la hiérarchie d'une dimension TM1 avec [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/), toutes deux en accès direct depuis le cloud. Pour un serveur TM1 accessible uniquement depuis votre propre réseau, l'étape [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) envoie la même lecture via un agent PlaidLink installé.

Le type de connexion apparaît dans le sélecteur de connexion sous le nom **IBM Planning Analytics (TM1)**.

## Fonctionnement de l'authentification

Deux modes d'authentification, correspondant aux schémas de connexion REST propres à TM1 :

- **Native** : authentification HTTP Basic avec un nom d'utilisateur et un mot de passe TM1.
- **CAM** : authentification unique (SSO) IBM Cognos Access Manager, limitée à un espace de noms. La requête transporte un en-tête `Authorization: CAMNamespace` construit à partir du nom d'utilisateur, du mot de passe et de l'espace de noms, distinct d'une authentification Basic classique.

La connexion par jeton porteur PlanningAnalytics-as-a-Service (PAaaS) n'est pas encore disponible : seuls les deux schémas de connexion REST ci-dessus sont pris en charge.

## Configuration

| Champ | Obligatoire | Description |
|---|---|---|
| Nom | Oui | Nom d'affichage de cette connexion. |
| Hôte | Oui | L'hôte de l'API REST TM1, par exemple `https://tm1-prod.example.com:8010` ou une URL PAaaS. |
| Base de données par défaut | Non | Valeur de préremplissage pour le champ Base de données d'une étape TM1 : interroger un cube. Chaque étape peut la remplacer. |
| Mode d'authentification | Oui | `Native` (utilisateur/mot de passe TM1) ou `CAM` (SSO Cognos Access Manager). Native par défaut. |
| Nom d'utilisateur | Oui | Le compte TM1 avec lequel s'authentifier. |
| Mot de passe | Oui | Stocké chiffré. |
| Espace de noms CAM | Uniquement avec CAM | L'espace de noms Cognos Access Manager auprès duquel s'authentifier. Inutilisé en mode Native. |
| Vérifier le certificat SSL | Non | Activé par défaut. Ne le désactivez que pour un certificat auto-signé connu sur un serveur de test. |
| Délai d'expiration (secondes) | Non | 30 par défaut. |

## Test de la connexion

**Tester la connexion** interroge le singleton `Configuration` du serveur (`GET {host}/api/v1/Configuration`), l'appel authentifié le moins coûteux exposé par TM1, qui ne nécessite aucun contexte de base de données ni de cube. Un test réussi indique la **`ProductVersion`** du serveur, ce qui confirme à la fois que l'hôte est joignable et que les identifiants s'authentifient.

## Lecture seule

Ce connecteur est en lecture seule. Il lit les données de cubes et les hiérarchies de dimensions dans TM1 ; il n'écrit rien, ne comptabilise rien et n'exécute aucun processus TI dans TM1.

## Ce que vous pouvez faire avec la connexion

- **Lire les données d'un cube par vue enregistrée ou MDX.** L'étape [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) exécute une vue de cube nommée ou une requête MDX brute, applique une tranche de point de vue facultative et dépose le résultat dans une table.
- **Charger une hiérarchie TM1 comme dimension PlaidCloud.** L'étape [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) lit les éléments d'une dimension, les liens parent/enfant et les attributs, puis construit à partir d'eux une dimension PlaidCloud.
- **Découper par période pour une extraction incrémentale.** TM1 n'offre aucun suivi des modifications intégré ; un workflow qui n'a besoin que des nouvelles données restreint donc la requête par période ou par version. Consultez la référence de l'étape pour le modèle à suivre.
- **Découvrir en direct les cubes, les vues et les dimensions**, en accès direct depuis le cloud. Les sélecteurs Cube, Vue et Dimension du formulaire de l'étape interrogent directement le serveur connecté, ce qui vous permet de choisir de vrais noms au lieu de les saisir à l'aveugle.
- **Lire un serveur TM1 que le cloud ne peut pas atteindre, via un agent local.** Consultez [Lire TM1 derrière un pare-feu](#lire-tm1-derrière-un-pare-feu) ci-dessous.

## Lire TM1 derrière un pare-feu

Un serveur TM1 accessible uniquement depuis votre propre réseau (sans point d'accès public, sans IP autorisée, sans VPN vers PlaidCloud) est atteint via un **agent PlaidLink** installé, et non en accès direct depuis le cloud. L'étape de workflow [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) exécute la même requête de vue, MDX ou point de vue que TM1 : interroger un cube, mais l'envoie à l'agent, qui joint TM1 sur votre réseau et renvoie le résultat.

Ce mode nécessite :

- **Un agent PlaidLink installé** sur une machine ayant un accès réseau au serveur TM1. Consultez [Installer PlaidLink](/fr/reference/cli/plaidlink/install/).
- **Une version de cet agent qui inclut le gestionnaire TM1.** PlaidCloud vérifie les capacités annoncées par un agent avant de lui envoyer une requête ; une ancienne version de l'agent ne peut donc pas traiter les requêtes TM1 tant qu'elle n'a pas été reconstruite et réinstallée, car PlaidLink ne se met pas à jour automatiquement. Consultez [Mettre à niveau PlaidLink](/fr/reference/cli/plaidlink/upgrade/).
- **Cette connexion TM1 partagée avec cet agent**, en plus de l'accès par membre ou par groupe dont elle dispose déjà, depuis la liste `Actions > Agents` de la connexion. Consultez [Modèle de sécurité](/fr/guides/connections/create-connection/#modèle-de-sécurité).

TM1 : interroger un cube (agent) n'offre aucune découverte en direct : un agent n'est joignable que pendant une exécution, et non lorsque le formulaire de l'étape est ouvert. Le cube, la vue et le MDX se saisissent donc à la main et sont validés à l'exécution de l'étape. TM1 : lire une dimension fonctionne uniquement en accès direct depuis le cloud ; elle n'a pas encore de mode local.

## Limitations connues

| Limitation | Signification |
|---|---|
| Lecture seule | Aucune réécriture, aucune exécution de processus TI. |
| La portée locale se limite aux requêtes | Le mode agent PlaidLink local couvre les lectures de cubes (TM1 : interroger un cube (agent)). TM1 : lire une dimension n'a pas encore de mode local : elle nécessite un chemin réseau que PlaidCloud peut joindre directement. |
| La lecture de dimension gère une seule hiérarchie et un seul parent | Une hiérarchie TM1 dont un élément a plusieurs parents ne peut pas être chargée comme dimension PlaidCloud, et l'amplitude du poids d'une consolidation (0,5 ; 2,0) n'est pas représentable, seul son signe l'est. Consultez [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#ce-que-cette-étape-ne-peut-pas-représenter). |
| Pas d'authentification par jeton porteur PAaaS | Seules les authentifications Native (Basic) et CAM sont prises en charge. |

## Voir aussi

- [Se connecter à TM1 (guide)](/fr/guides/connections/tm1/) : créez la connexion et construisez une requête.
- [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) : lectures de cubes, en accès direct depuis le cloud.
- [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) : lectures de cubes via un agent local.
- [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) : chargez une hiérarchie TM1 comme dimension PlaidCloud.
- [Créer et gérer une connexion](/fr/guides/connections/create-connection/)
