---
title: "TM1 : interroger un cube (agent)"
description: "Lisez une tranche de cube depuis un serveur IBM TM1 / Planning Analytics sur site que le cloud ne peut pas atteindre directement — la même requête par vue, MDX ou point de vue que TM1 : interroger un cube, exécutée via un agent PlaidLink installé."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Description

Le jumeau sur site de [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) : la même lecture — une **vue** enregistrée ou une requête **MDX** sur un cube TM1, avec une tranche de point de vue (POV) facultative, déposée dans une table de projet — exécutée via un [agent PlaidLink](/fr/reference/cli/plaidlink/) installé sur votre réseau plutôt qu'appelée en accès direct au cloud. Utilisez cette étape, à la place de TM1 : interroger un cube, lorsque le serveur TM1 n'est accessible que depuis l'intérieur de votre propre réseau.

Cette étape apparaît dans le menu des étapes sous **IBM TM1 / Planning Analytics**.

## Différences avec TM1 : interroger un cube

| | TM1 : interroger un cube | TM1 : interroger un cube (agent) |
|---|---|---|
| Transport | Accès direct au cloud via REST | Envoyé à un agent PlaidLink sur votre réseau |
| Champs de configuration | — | Identiques, plus un **Agent** obligatoire |
| Détection des cubes / vues | En direct, depuis la base de données connectée | Non disponible — saisissez les noms à la main |
| Aperçu avant enregistrement | Oui | Non disponible |

Tout le reste — la connexion, la base de données, le choix vue/MDX, la tranche de point de vue, Supprimer les cellules nulles/vides, Limite de lignes et le schéma d'extraction incrémentale par période — fonctionne exactement comme décrit dans la page [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/). Seules les différences ci-dessous sont propres à cette étape.

## Configuration

### Source et cible

| Champ | Obligatoire | Remarques |
|---|---|---|
| Agent | Oui | L'agent PlaidLink auquel envoyer cette lecture. Sa version doit inclure le gestionnaire TM1 (voir [Prérequis](#prérequis) ci-dessous). |
| Connexion TM1 | Oui | La [connexion TM1](/fr/guides/connections/tm1/) à utiliser pour la lecture. Le sélecteur de connexion n'est pas filtré selon l'agent sélectionné — partagez la connexion avec l'agent séparément (voir ci-dessous). |
| Environnement | Oui | L'environnement de la connexion. |
| Base de données | Oui | La base de données TM1 (instance) à interroger. |
| Cube | Oui | Le cube TM1 à interroger. Saisi à la main — cette étape n'offre aucune détection en direct. |
| Table cible | Oui | La table de projet dans laquelle arrive le jeu de cellules renvoyé. |

### Tranche et options

Les mêmes champs que [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/#tranche) — Mode de source (Par vue / Par MDX), Vue, MDX, Point de vue, Supprimer les cellules nulles/vides et Limite de lignes — tous en saisie manuelle plutôt que détectés, et tous validés à l'exécution de l'étape plutôt que dans un aperçu.

## Aucune détection via un agent

Les sélecteurs Cube, Vue et Dimension de TM1 : interroger un cube interrogent le serveur connecté en direct pendant que vous modifiez l'étape. Cette détection en direct n'existe pas pour cette étape : un agent n'est joignable que pendant une exécution, pas lorsqu'un formulaire est ouvert dans votre navigateur. Le cube, la vue et le MDX sont en saisie manuelle, et un nom non reconnu fait échouer l'exécution avec une erreur claire plutôt que d'échouer silencieusement. Pour la même raison, il n'y a pas de bouton **Aperçu** — un aperçu devrait atteindre TM1, ce que seul l'agent peut faire.

## Prérequis

La lecture d'un serveur TM1 sur site nécessite :

- **Un agent PlaidLink installé** sur une machine ayant un accès réseau au serveur TM1. Consultez [Install PlaidLink](/fr/reference/cli/plaidlink/install/).
- **Une version de cet agent qui inclut le gestionnaire TM1.** PlaidCloud vérifie les capacités annoncées par l'agent avant l'envoi ; un agent dont la version est antérieure à cette capacité ne peut pas traiter la requête. **PlaidLink ne se met pas à jour automatiquement** — un agent existant doit être recompilé ou réinstallé manuellement pour bénéficier de la prise en charge de TM1. Consultez [Upgrade PlaidLink](/fr/reference/cli/plaidlink/upgrade/).
- **La connexion TM1 partagée avec cet agent**, en plus des accès de membre ou de groupe dont elle dispose déjà — accordez-la depuis la liste `Actions > Agents` de la connexion. Consultez [Modèle de sécurité](/fr/guides/connections/create-connection/#modèle-de-sécurité).

## Voir aussi

- [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — le jumeau en accès direct au cloud que cette étape reproduit.
- [TM1 : lire une dimension](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — charge une hiérarchie TM1 dans une dimension PlaidCloud, en accès direct au cloud.
- [Se connecter à TM1 (guide)](/fr/guides/connections/tm1/) — crée la connexion.
- [Connecteur TM1](/fr/reference/connectors/rest/tm1/) — référence des champs de connexion, y compris la voie par agent sur site.
- [PlaidLink](/fr/reference/cli/plaidlink/) — installation et mise à niveau des agents.
- [Étapes IBM TM1 / Planning Analytics](/fr/reference/workflow-steps/ibm-planning-analytics/)
