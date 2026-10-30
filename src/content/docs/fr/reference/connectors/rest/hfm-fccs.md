---
title: Connecteur HFM / FCCS
description: Configurez une connexion Oracle FCCS (Financial Consolidation and Close, EPM Cloud) dans PlaidCloud pour obtenir en libre-service une tranche de données ad hoc grâce à un sélecteur de point de vue, avec mise en cache facultative et chargement récurrent planifié.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Connectez PlaidCloud à Oracle **FCCS** (Financial Consolidation and Close, qui fait partie d'Oracle EPM Cloud) afin qu'un utilisateur de la finance puisse obtenir lui-même une tranche de données sans ouvrir de ticket auprès de l'équipe HFM. L'étape [HFM/FCCS : lire les données (ad hoc)](/fr/reference/workflow-steps/oracle-epm/hfm-fccs-read/) donne l'impression d'une requête en direct, mais en réalité il s'agit d'une demande asynchrone, d'une interrogation puis d'une récupération auprès de l'API de jobs d'export de données de FCCS.

Ce type de connexion apparaît dans le sélecteur de connexion sous le nom **REST - HFM/FCCS**.

:::note[Limitez la dimension d'entité]
Gardez chaque point de vue borné : une extraction sans limites peut verrouiller l'application FCCS pendant longtemps, le temps que le job d'export s'exécute.
:::

## Documentation de l'API

Le connecteur utilise l'[API REST](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) d'Oracle EPM Cloud : les points de terminaison de métadonnées de l'application (pour découvrir les dimensions et les membres) et ceux des jobs d'export de données (pour demander, interroger et récupérer une grille).

## Fonctionnement de l'authentification

La connexion utilise l'**authentification HTTP Basic avec un compte de service** sur un pod EPM Cloud classique : il n'y a ni OAuth ni flux de jeton (les pods OCI / Gen 2 à jeton Bearer ne sont pas pris en charge). Lorsqu'un **Domaine d'identité** est défini, PlaidCloud compose l'identifiant de connexion sous la forme `identitydomain.username` (le domaine, un point, puis le nom d'utilisateur). Si vous laissez le domaine d'identité vide, ou si votre nom d'utilisateur contient déjà un point, le nom d'utilisateur est envoyé tel quel. Pointez la connexion vers un compte de service d'intégration dédié, disposant d'un accès en lecture aux applications et aux tranches de point de vue que vos utilisateurs en libre-service extrairont.

## Configuration

| Champ | Obligatoire | Description |
|---|---|---|
| Nom | Oui | Nom d'affichage de cette connexion. |
| URL EPM Cloud | Oui | L'URL du pod/service EPM Cloud, par exemple `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Domaine d'identité | Non | Votre domaine d'identité EPM Cloud. S'il est défini, PlaidCloud le place avant le nom d'utilisateur sous la forme `identitydomain.username` lors de la connexion. |
| Nom d'utilisateur | Oui | Le nom d'utilisateur du compte de service d'intégration. |
| Mot de passe | Oui | Le mot de passe du compte de service. Stocké chiffré. |
| Application par défaut | Non | Une application FCCS par défaut à préremplir dans le sélecteur de point de vue de l'étape. Chaque étape peut la remplacer. |

## Ce que vous pouvez faire avec la connexion

- **Obtenir une tranche ad hoc en libre-service.** Construisez un point de vue (POV), c'est-à-dire l'application plus les dimensions FCCS, dans le formulaire de l'étape, cliquez sur Exécuter, et une table de résultats est alimentée automatiquement. Consultez [HFM/FCCS : lire les données (ad hoc)](/fr/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Se passer du ticket.** La tranche s'exécute sous le compte de service de la connexion : un utilisateur de la finance extrait lui-même les données au lieu d'attendre un administrateur HFM.
- **Mettre en cache les extractions répétées.** Le même POV avec la même date de référence, demandé à nouveau, renvoie instantanément la copie déjà alimentée au lieu de solliciter de nouveau FCCS.
- **Contrôler qui voit quelles entités.** La table alimentée est **compatible avec la sécurité au niveau des lignes** : un administrateur peut déclarer un Accès aux lignes sur la colonne `Entity` afin que les utilisateurs en libre-service ne voient que les entités auxquelles ils ont droit. Ce contrôle relève de l'administrateur et n'est pas automatique ; consultez la référence de l'étape.
- **Planifier un chargement récurrent.** Activez **Cible liée** pour promouvoir une tranche ad hoc en table persistante qui s'enrichit de façon additive et fusionne au lieu d'écraser ; la même étape placée dans un workflow planifié devient alors un chargement récurrent nocturne.

## Découverte des métadonnées

Sur les pods FCCS pris en charge, le formulaire de l'étape découvre en direct la liste des membres de chaque dimension à partir des métadonnées de l'application dès que vous choisissez une connexion et une application, de sorte que le sélecteur de POV propose de vrais membres (la découverte est relancée chaque fois que l'un des deux change). Sur les pods plus anciens qui n'exposent pas le point de terminaison de métadonnées, la découverte ne renvoie rien et le sélecteur bascule en saisie manuelle : vous saisissez les noms de membres à la main, et un point de vue enregistré est toujours restitué à l'identique. L'extraction fonctionne de la même manière dans les deux cas.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Lecture seule | Le connecteur extrait des données de FCCS. Il n'écrit pas de données de consolidation, n'exécute pas de consolidations et ne comptabilise rien en retour. |
| Limiter la dimension d'entité | Une extraction sans limites (sans sélection `Entity`) peut verrouiller l'application FCCS pendant longtemps, le temps que le job d'export s'exécute. Gardez la sélection d'entités bornée. |
| Membres saisis manuellement sur les pods plus anciens | Lorsqu'un pod n'expose pas le point de terminaison de métadonnées, les listes de membres ne se remplissent pas automatiquement : saisissez les noms de membres à la main. |
| La sécurité au niveau des lignes est gérée par l'administrateur, pas automatique | La table alimentée peut être contrôlée par un Accès aux lignes, mais un administrateur doit publier, déclarer la colonne `Entity`, approuver la première écriture contrôlée et réconcilier. Tant qu'il ne l'a pas fait, la table n'est pas filtrée. |

## Voir aussi

- [Extraire depuis HFM / FCCS (guide)](/fr/guides/connections/hfm-fccs/) — créer la connexion, construire un POV, l'exécuter, mettre en cache, contrôler les accès et planifier.
- [HFM/FCCS : lire les données (ad hoc)](/fr/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — la référence des champs de l'étape.
- [Gérer les groupes de sécurité et les affectations](/fr/administration/access/managing-security-groups-and-assignments/) — comment l'Accès aux lignes contrôle la table alimentée.
- [Créer et gérer une connexion](/fr/guides/connections/create-connection/)
