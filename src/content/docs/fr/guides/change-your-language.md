---
title: Changer de langue
description: Affichez PlaidCloud en English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 ou 简体中文, et retrouvez votre choix sur vos autres appareils.
sidebar:
  label: Changer de langue
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/change-your-language.md
---

L'interface de PlaidCloud est disponible en onze langues :

| Langue | Entrée du menu |
|---|---|
| Anglais (États-Unis) | English (US) |
| Anglais (Royaume-Uni) | English (UK) |
| Allemand | Deutsch |
| Espagnol | Español |
| Français | Français |
| Portugais (Portugal) | Português (Portugal) |
| Portugais (Brésil) | Português (Brasil) |
| Polonais | Polski |
| Japonais | 日本語 |
| Coréen | 한국어 |
| Chinois (simplifié) | 简体中文 |

Tout le monde commence en English (US). Rien ne change tant que vous n'avez pas choisi une langue.

## Changer la langue

1. Dans l'en-tête supérieur, cliquez sur le bouton **Langue**, à côté du bouton **Apparence**. Son menu liste chaque langue sous son propre nom : vous pouvez donc trouver la vôtre quelle que soit la langue affichée.
2. Choisissez une langue.
3. Un message confirme que PlaidCloud va se recharger dans cette langue. Les modifications non enregistrées sont perdues ; enregistrez donc d'abord votre travail. Cliquez sur **Recharger** pour continuer, ou annulez pour rester tel quel.

PlaidCloud enregistre votre choix dans votre profil et se recharge dans la nouvelle langue. Pour revenir en arrière, choisissez **English (US)** de la même manière.

## Où votre choix s'applique

- **Autres appareils et navigateurs.** Votre choix vous suit. Si vous vous connectez au même espace de travail depuis un autre appareil ou navigateur, il s'applique dès le prochain chargement de page.
- **Par espace de travail.** Le choix appartient à votre profil dans un seul espace de travail. Si vous utilisez plusieurs espaces de travail, définissez la langue dans chacun.

## Nombres et dates

Les nombres et les dates s'affichent selon le format de la langue que vous choisissez. En allemand, par exemple, mille deux cent trente-quatre et demi s'affiche `1.234,5`. En polonais, 1234567.89 s'affiche `1 234 567,89` et le 12 octobre 2026 s'affiche `12.10.2026`. Le japonais et le chinois affichent cette date sous la forme `2026/10/12`, et le coréen sous la forme `26. 10. 12.`. English (UK) utilise l'orthographe et les formats britanniques.

Seul l'affichage change. Les valeurs que vous enregistrez, exportez ou envoyez à des intégrations conservent leur format habituel.

## Saisie en japonais, en coréen et en chinois

Les méthodes de saisie japonaise, coréenne et chinoise fonctionnent dans les champs numériques et dans les autres champs qui limitent ce que vous pouvez saisir. Les chiffres pleine largeur sont convertis au fur et à mesure de la saisie : `１２３` devient donc `123`.

## Ce qui suit aussi votre langue

Le texte que PlaidCloud vous envoie depuis le serveur suit lui aussi votre langue, dans toutes les langues proposées par PlaidCloud :

- **E-mails.** Les e-mails système tels que les invitations, les réinitialisations de mot de passe, les avis relatifs aux workflows et aux migrations, ainsi que les e-mails d'inscription, de facturation et d'assistance.
- **Écrans de connexion.** Les écrans de connexion, de définition du mot de passe et de déconnexion, ainsi que les e-mails que Keycloak envoie depuis ces écrans.
- **Messages d'erreur.** Les messages que PlaidCloud affiche lorsqu'une requête échoue, dans l'interface, via l'API REST et via JSON-RPC.
- **PDF de documentation du projet.** Le PDF que PlaidCloud génère pour documenter un projet.

## Comment PlaidCloud choisit la langue

| Où | Langue utilisée |
|---|---|
| Dans PlaidCloud | La langue que vous avez choisie avec le bouton **Langue**. Votre page de connexion et vos e-mails suivent le même choix. |
| Connexion et autres écrans avant de vous connecter | La langue de votre navigateur. |
| Inscription | La langue de votre navigateur. PlaidCloud l'enregistre sur votre organisation, et les e-mails de facturation et de compte envoyés à l'organisation l'utilisent. |

Si votre navigateur ou votre profil utilise une langue que PlaidCloud ne propose pas, le texte apparaît en English (US). Les navigateurs configurés en chinois traditionnel (zh-TW ou zh-HK) basculent sur English (US) pour le texte du serveur.

## Ce qui reste en anglais

- Les messages et journaux d'exécution des workflows et des étapes, ainsi que le flux d'activité. Beaucoup de personnes les lisent, et les conserver dans une seule langue les garde consultables et cohérents.
- Le texte de l'assistant IA et des outils MCP.
- Les e-mails que vous rédigez vous-même, y compris les modèles d'e-mail et les e-mails envoyés par les étapes de rapport.
- La documentation OpenAPI.
- Le texte des erreurs des moteurs SQL et d'expressions.
- Les écrans d'inscription.
- Le contenu que vous créez, comme les noms des projets, des tables et des étapes.
