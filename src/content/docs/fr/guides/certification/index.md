---
title: Certification PlaidCloud
description: "Obtenez des badges PlaidCloud en réussissant des labs pratiques notés automatiquement : Fondations, puis Praticien et Expert sur chaque parcours, et Master sur examen."
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/index.md
---

La certification PlaidCloud prouve ce que vous savez faire grâce à des labs pratiques. Chaque lab vous donne un projet dans lequel travailler et une tâche, et note automatiquement votre travail lorsque vous le soumettez. Il n'y a aucun examen à réserver ni aucun cours auquel s'inscrire : vous vous préparez en lisant, dans l'ordre, les guides que liste chaque [parcours d'apprentissage](#parcours-dapprentissage).

## Niveaux et parcours

| Niveau | Parcours | Comment l'obtenir |
|---|---|---|
| **Fondations** | Aucun parcours | Réussir le lab Fondations |
| **Praticien** | **Ingénierie des données**, **Modélisation** ou **Analytique** | Réussir le lab Praticien du parcours |
| **Expert** | **Ingénierie des données**, **Modélisation** ou **Analytique** | Réussir le lab Expert du parcours, qui est chronométré |
| **Principal** | Aucun parcours | Détenir trois badges Expert et réussir un examen par PlaidCloud d'une implémentation en production |

Les parcours **Opérations financières** et **Administration et sécurité** sont indiqués comme **Bientôt disponible**. Ils n'ont pas encore de labs.

Sur chaque parcours, votre badge Expert s'affiche à la place de votre badge Praticien.

## Ouvrir Certifications

Ouvrez le menu utilisateur dans le coin supérieur droit et choisissez **Certifications**. Le volet s'ouvre sur votre onglet Accueil avec :

- une bannière avec votre objectif, lorsqu'un administrateur de l'espace de travail en a défini un, indiquant si vous détenez déjà ce badge ;
- **Vos badges**, avec la date d'obtention de chaque badge et sa date d'expiration ;
- **Labs**, une grille de chaque parcours croisé avec **Fondations**, **Praticien** et **Expert**. Chaque cellule affiche **Démarrer le lab**, **Obtenu** pour un badge que vous détenez, ou, dans l'espace de travail de certification, la date à laquelle le lab est de nouveau disponible après une [attente](#lattente-de-7-jours). La ligne de votre objectif est marquée **votre objectif**, et un objectif Fondations ou Principal marque **Tous les parcours** ;
- **Principal**, avec le nombre de badges Expert, sur trois, que vous détenez.

**Retour à l'accueil** ferme le volet.

## L'espace de travail de certification

Les labs s'exécutent uniquement dans l'espace de travail de certification de PlaidCloud. Dans tout autre espace de travail, **Démarrer le lab** vous ajoute à l'espace de travail de certification en tant que membre pouvant construire, avec la même adresse e-mail, et l'ouvre dans un nouvel onglet sur son propre volet **Certifications**. Choisissez de nouveau **Démarrer le lab** à cet endroit pour démarrer le lab.

La première fois, PlaidCloud vous envoie un e-mail pour définir un mot de passe pour l'espace de travail de certification. Vérifiez votre boîte de réception.

Si vous n'appartenez à aucun espace de travail PlaidCloud, contactez PlaidCloud, et nous vous invitons dans l'espace de travail de certification.

Démarrer un lab, en abandonner un et obtenir un badge nécessitent tous une adresse e-mail vérifiée, car vos badges lui sont rattachés.

## Fonctionnement d'un lab

1. Choisissez **Démarrer le lab** dans l'espace de travail de certification. PlaidCloud crée le projet du lab pour vous ; vous seul pouvez l'ouvrir.
2. Le volet affiche le lab : son titre, l'heure à laquelle vous l'avez démarré, **Votre tâche**, ainsi que **Soumettre pour notation**, **Ouvrir le projet** et **Abandonner**. Tant qu'un lab est ouvert, le volet l'affiche à la place de vos badges et de la grille.
3. Choisissez **Ouvrir le projet** et réalisez la tâche.
4. Choisissez **Soumettre pour notation**. La notation exécute le workflow du lab, puis vérifie ce que cette exécution a produit ; elle peut donc durer aussi longtemps que l'exécution.
   - Si tous les contrôles réussissent, le badge est à vous, et le projet du lab est supprimé.
   - Si un contrôle échoue, **Dernier résultat** liste chaque contrôle comme **Réussi** ou **Échec**. Un contrôle échoué indique ce qui n'allait pas et comporte un lien **Guide ›** vers le guide qui traite du sujet. Corrigez votre projet et soumettez à nouveau.

Vous pouvez soumettre autant de fois que vous le souhaitez tant que le lab est ouvert. Soumettre alors que le workflow du lab est déjà en cours d'exécution ne note rien ; attendez la fin de l'exécution, puis soumettez à nouveau.

Si tous les contrôles réussissent mais que votre adresse e-mail n'est pas vérifiée, aucun badge n'est attribué. Vérifiez votre adresse e-mail, puis soumettez à nouveau.

### Limites de temps

Les labs Expert sont chronométrés : la grille **Labs** affiche **Chronométré · 4 h**, et un lab Expert ouvert indique combien de minutes il reste. Le chronomètre démarre lorsque vous démarrez le lab et continue de tourner que vous y travailliez ou non.

Une fois le temps écoulé, le lab ne peut plus être réussi. Votre prochaine soumission met fin à la tentative, supprime le projet du lab et démarre l'attente de 7 jours.

Les labs Fondations et Praticien n'ont pas de limite de temps.

### L'attente de 7 jours

**Abandonner** supprime le projet de votre lab et met fin à la tentative. Vous le confirmez d'abord. Abandonner un lab, ou manquer de temps sur un lab Expert, démarre une attente de 7 jours avant de pouvoir démarrer de nouveau ce lab ; la grille **Labs** affiche la date à laquelle il est de nouveau disponible. Soumettre un lab dont certains contrôles échouent ne démarre pas d'attente.

## Expiration

Les badges expirent deux ans après leur obtention. Un badge expiré n'apparaît plus dans **Vos badges** ni pour les administrateurs, et son lab peut être démarré de nouveau, sauf si vous détenez encore un badge supérieur sur le même parcours.

## Master

Master est le seul badge qui ne s'obtient pas dans un lab. Il nécessite trois badges Expert non expirés et une implémentation en production, examinée par PlaidCloud.

**Demander l'examen Master**, sur la carte **Principal**, devient disponible dès que vous détenez trois badges Expert. Il ouvre **Aide et support** avec un nouveau ticket qui nomme déjà vos badges Expert. Ajoutez les détails de votre implémentation et envoyez-le. L'examen vérifie :

- qu'il s'agit d'une implémentation en production chez un client ou un partenaire nommé ;
- que vous l'avez construite ou dirigée ;
- qu'elle utilise les capacités d'au moins deux parcours ;
- qu'un contact nommé la confirme.

Le badge Master expire lui aussi deux ans après son attribution.

## Partager un badge

Chaque badge a sa propre page de vérification publique, qui affiche le badge, votre nom, sa date d'émission, sa date d'expiration et s'il est toujours valide. Le nom est celui de votre profil dans l'espace de travail de certification au moment où vous rendez le badge public ; si PlaidCloud y a créé votre compte lorsque vous avez démarré un lab, il s'agit de la partie de votre adresse e-mail située avant le @. Pour afficher un nom modifié, rendez le badge privé puis de nouveau public. La page n'affiche jamais votre adresse e-mail complète. La page n'existe que tant que le badge est public.

Dans l'espace de travail de certification, sous chaque badge de **Vos badges** :

- **Rendre public** publie la page de vérification du badge. Décochez-le pour retirer la page.
- **Copier le lien** copie l'adresse de la page.
- **Ajouter à LinkedIn** ouvre le formulaire de LinkedIn pour ajouter une certification, rempli à partir du badge.

**Copier le lien** et **Ajouter à LinkedIn** ne fonctionnent que tant que le badge est public. Dans tout autre espace de travail, un badge public conserve **Copier le lien** et **Ajouter à LinkedIn**, et un badge qui n'est pas public propose **Partager depuis l'espace de travail de certification**, qui ouvre l'espace de travail de certification sur son volet **Certifications**.

Le partage nécessite une adresse e-mail vérifiée. Tant que la vôtre n'est pas vérifiée, **Vos badges** n'en liste aucun.

## Ce que voient les administrateurs

Les badges sont rattachés à votre adresse e-mail, ils apparaissent donc dans chaque espace de travail dont vous êtes membre avec cette adresse. Dans la liste **Membres** d'un espace de travail, les administrateurs voient les badges et l'objectif de chaque membre, et peuvent attribuer un parcours cible. Ils voient les badges, pas les tentatives ni les résultats des labs. Consultez [Badges et objectifs de certification](/fr/administration/access/member-management/#badges-et-objectifs-de-certification).

## Parcours d'apprentissage

- [Fondations](/fr/guides/certification/foundations/)
- [Ingénierie des données](/fr/guides/certification/data-engineering/)
- [Modélisation](/fr/guides/certification/modeling/)
- [Analytique](/fr/guides/certification/analytics/)
