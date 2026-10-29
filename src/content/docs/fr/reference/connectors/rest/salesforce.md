---
title: Connecteur REST Salesforce
description: "Configurez une connexion à l'API REST de Salesforce dans PlaidCloud avec le flux d'informations d'identification client OAuth 2.0, testez-la et extrayez des objets CRM dans des tables de projet avec l'étape Salesforce : interroger un objet."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## Documentation de l'API

La [référence de l'API REST de Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) documente les points de terminaison des enregistrements et des métadonnées, et le [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) documente les jobs de requête sur lesquels s'appuie l'étape [Salesforce : interroger un objet](/fr/reference/workflow-steps/salesforce/query-salesforce-object/).

Pour une procédure complète (l'application côté Salesforce, l'utilisateur Run As, la création de la connexion et son test), suivez le guide [Se connecter à Salesforce](/fr/guides/connections/salesforce/). Cette page est la référence des champs qui lui sert de support.

## Fonctionnement de l'authentification

Le connecteur se connecte avec les **informations d'identification client OAuth 2.0** : PlaidCloud échange la clé et le secret consommateur de l'application contre un jeton d'accès auprès du point de terminaison de jeton propre à l'organisation, puis appelle l'API en tant qu'utilisateur désigné par le paramètre **Run As** de l'application. Il n'y a ni connexion interactive, ni jeton d'actualisation, ni certificat à gérer.

Deux propriétés de cet échange comptent en pratique :

- **Un seul jeton couvre toute une extraction.** PlaidCloud met en cache le jeton d'accès par connexion et par environnement jusqu'à peu avant son expiration, de sorte qu'une longue lecture paginée ne se réauthentifie pas à chaque page. Un jeton que Salesforce cesse d'honorer prématurément (révoqué, restriction d'IP, politique de session modifiée) est écarté et remplacé une fois, automatiquement.
- **Les requêtes vont là où Salesforce l'indique.** La réponse du jeton nomme l'instance de l'organisation, et tous les appels suivants sont effectués sur cette instance plutôt que sur l'hôte que vous avez saisi ; une connexion continue donc de fonctionner après un changement de My Domain ou d'instance.

La version de l'API REST est figée par connexion et non flottante, de sorte qu'une mise à niveau de l'organisation ne peut pas modifier silencieusement la forme des réponses sous une étape enregistrée. Les nouvelles connexions utilisent une version actuellement prise en charge ; une connexion peut être figée sur une autre version via l'API de configuration de connexion, et si une version figée arrive en fin de vie, Salesforce répond HTTP 410 et PlaidCloud indique quelle version a été retirée.

## Configuration

Ces champs s'affichent lors de la création ou de la modification d'une connexion Salesforce dans **Tools > Connections**.

### Description du compte

| Champ | Type | Description |
|---|---|---|
| Nom du compte | Texte | Nom d'affichage de cette connexion. |
| Mémo | Texte (multiligne) | Remarques facultatives sur la connexion. |

### Connexion

| Champ | Type | Description |
|---|---|---|
| Hôte ou adresse IP | Texte | L'hôte My Domain de l'organisation : `mycompany.my.salesforce.com` pour la production et Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` pour un bac à sable. PlaidCloud ajoute `https://` si vous l'omettez. |

### Identifiants d'authentification

| Champ | Type | Description |
|---|---|---|
| ID client | Texte | La clé consommateur de l'application. |
| Secret client | Mot de passe | Le secret consommateur de l'application. Enregistré chiffré ; saisissez une nouvelle valeur pour le modifier, laissez le champ vide pour conserver la valeur stockée. |

### Utilisation et sécurité

| Champ | Type | Description |
|---|---|---|
| Actif (autoriser l'accès) | Interrupteur | Indique si la connexion peut être utilisée. Décochez-la pour suspendre l'accès sans supprimer la connexion. |
| Modèle de sécurité | Sélection | Qui peut utiliser la connexion : privée pour ses propriétaires, membres spécifiques, groupes de sécurité spécifiques ou tous les membres de l'espace de travail. |

Chaque connexion conserve un jeu de ces valeurs par environnement, de sorte qu'une même connexion peut pointer vers un bac à sable dans votre environnement de développement et vers la production dans votre environnement de production. Testez et définissez les identifiants pour chaque environnement.

## Tester la connexion

**Tester la connexion** effectue le véritable échange de jeton et indique l'identité avec laquelle les identifiants s'authentifient :

| Élément indiqué | Pourquoi c'est important |
|---|---|
| ID de l'organisation | Confirme l'organisation que les identifiants atteignent, ce qui est le moyen le plus rapide de détecter un identifiant de bac à sable enregistré dans un environnement de production. |
| Version de l'API | La version la plus élevée prise en charge par cette organisation. Les lectures s'exécutent sur la version figée sur la connexion (`v61.0`, sauf si `salesforce_api_version` est défini), et non sur celle-ci. |
| Utilisateur Run As | L'utilisateur auquel est limitée chaque ligne et chaque champ que cette connexion renvoie. Vérifiez-le avant de vous fier au nombre de lignes d'une extraction. |

Un test en échec en indique la cause. Les échecs d'authentification rapportent le statut HTTP et vous invitent à saisir à nouveau l'ID client et le secret, car un secret client ne peut plus être relu une fois enregistré.

## Limitations connues

- **L'utilisateur Run As limite chaque lecture, de deux façons différentes.** Les lignes que cet utilisateur ne peut pas voir sont simplement absentes, sans erreur ni décompte. Un champ que cet utilisateur ne peut pas lire fait échouer toute la requête. Les deux cas sont traités dans [L'utilisateur Run As limite tout](/fr/guides/connections/salesforce/#lutilisateur-run-as-délimite-tout).
- **Lecture seule.** Ce connecteur extrait des données ; il n'écrit pas d'enregistrements dans Salesforce.
- **Certains types de champs ne peuvent pas être extraits** : champs composés d'adresse et de géolocalisation, blobs `base64`, `encryptedstring` et `anyType`. Le sélecteur de champs de l'étape signale chacun d'eux et en indique la raison. Consultez [Champs refusés par l'étape](/fr/reference/workflow-steps/salesforce/query-salesforce-object/#champs-que-létape-refuse).
- **Une extraction n'est pas une synchronisation.** Un enregistrement supprimé dans Salesforce reste dans la table cible.

## Voir aussi

- [Se connecter à Salesforce](/fr/guides/connections/salesforce/) — procédure pas à pas
- [Salesforce : interroger un objet](/fr/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Créer et gérer une connexion](/fr/guides/connections/create-connection/)
