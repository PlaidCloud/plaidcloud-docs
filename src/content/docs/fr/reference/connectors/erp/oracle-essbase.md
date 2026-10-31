---
title: Connecteur Oracle Essbase
description: Connectez PlaidCloud à Oracle Essbase 21c ou à Oracle Analytics Cloud avec un compte de service pour exécuter depuis un workflow des requêtes MDX en direct sur des cubes Essbase.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## Documentation de l'API

Ce connecteur communique avec l'[API REST d'Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/) — les mêmes points de terminaison `grid/mdx`, d'application, de base de données et de structure (outline) qu'Oracle documente pour Essbase 21c et Oracle Analytics Cloud (OAC).

## Ce à quoi il se connecte

Oracle Essbase **21c ou version ultérieure**, ainsi qu'Essbase sur Oracle Analytics Cloud (OAC). Ces versions exposent Essbase via une API REST documentée, que PlaidCloud appelle. Les versions d'Essbase sur site antérieures à REST **ne sont pas prises en charge** — il n'existe aucune voie via l'API Java héritée ni via un client de grille.

Une fois la connexion créée, l'étape [Essbase : interroger un cube](/fr/reference/workflow-steps/essbase/essbase-query/) exécute du MDX en direct sur un cube et dépose la grille de résultats dans une table, et l'étape [Essbase : lire une dimension](/fr/reference/workflow-steps/essbase/essbase-dimension-read/) charge la structure d'une dimension dans une dimension PlaidCloud.

## Fonctionnement de l'authentification

La connexion s'authentifie avec le nom d'utilisateur et le mot de passe d'un compte de service via HTTP Basic. Le provisionnement Essbase de ce compte détermine les applications et les cubes qu'il peut voir et interroger : accordez-lui donc un accès en lecture uniquement aux applications que vous comptez interroger, et rien de plus.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| URL de base | Texte | L'origine du serveur Essbase, par exemple `https://your-host:9001`. Saisissez uniquement l'origine, sans chemin `/essbase/...` à la fin. |
| Application par défaut | Texte *(facultatif)* | Présélectionne cette application dans le formulaire de l'étape Essbase : interroger un cube. |
| Nom d'utilisateur | Texte | Utilisateur du compte de service pour l'authentification HTTP Basic. |
| Mot de passe | Texte | Mot de passe du compte de service. Stocké chiffré. |
| Vérifier SSL | Interrupteur | Activé par défaut. Désactivez-le uniquement pour un hôte dont le certificat est auto-signé ou autrement invérifiable. |

## Tester la connexion

Utilisez **Tester la connexion** dans l'éditeur de connexion. Un test réussi atteint le serveur Essbase, liste les applications que le compte de service peut voir et indique combien il en a trouvé — ce qui confirme à la fois l'URL de base et les identifiants avant que vous ne construisiez une requête.

## Voir aussi

- [Essbase : interroger un cube](/fr/reference/workflow-steps/essbase/essbase-query/) — exécuter une requête MDX en direct sur un cube et déposer le résultat dans une table.
- [Essbase : lire une dimension](/fr/reference/workflow-steps/essbase/essbase-dimension-read/) — charger la structure d'une dimension dans une dimension PlaidCloud.
- [Étapes Oracle Essbase](/fr/reference/workflow-steps/essbase/)
- [Connect to Oracle Essbase (guide)](/fr/guides/connections/essbase/)
- [Créer et gérer une connexion](/fr/guides/connections/create-connection/)
