---
title: Alertes et résumés
description: Prévenez les utilisateurs lorsqu'un chiffre d'une application Panel franchit un seuil, ou envoyez un résumé planifié des chiffres clés par notification push, e-mail, Slack ou Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

Une **alerte** surveille un chiffre issu des données d'une application Panel et vous prévient dès qu'il franchit un seuil. Un **résumé** envoie un court récapitulatif de 10 chiffres au maximum, chaque jour ou chaque semaine. Les deux se configurent depuis l'application dans [Panel Studio](/fr/guides/panel-apps/studio/), et les deux vous appartiennent : vous ne voyez et ne modifiez que les vôtres.

## Ouvrir les alertes et les résumés

1. Dans **Mes applications Panel** ou sur le tableau **Accueil** d'un projet, choisissez **Open in Studio** sur l'application.
2. Choisissez **Alerts & Digests**.

La fenêtre comporte un onglet **Alertes** et un onglet **Digests**. L'application doit être affectée à un projet, et ses tables sont celles de ce projet.

## Définir un chiffre à surveiller

Les alertes et les résumés mesurent un **KPI** que vous construisez à partir d'une table du projet de l'application :

| Champ | Ce qu'il définit |
|---|---|
| **Table** | La table à lire. Elle doit être construite. |
| **Measure column** | La colonne à totaliser ou à compter. |
| **Fonction** | `sum`, `avg`, `min`, `max`, `count` ou `count_distinct`. |
| **Ajouter un filtre** | Conditions facultatives qui restreignent les lignes, chacune composée d'une colonne, d'une comparaison et d'une valeur. Pour *is in*, séparez les valeurs par des virgules. **Remove filter** en supprime une. |

Le chiffre est toujours calculé avec votre propre accès à la table, y compris la [sécurité au niveau des lignes](/fr/guides/panel-apps/accessing-data/). Vous ne voyez jamais, et n'envoyez jamais, un chiffre portant sur des lignes que vous ne pouvez pas lire.

## Créer une alerte

1. Dans l'onglet **Alertes**, choisissez **Nouveau**.
2. Saisissez un **Nom**.
3. Construisez le KPI.
4. Sous **Alert when the KPI is**, choisissez `>`, `>=`, `<` ou `<=` et saisissez un **Seuil**.
5. Choisissez le mode de notification dans **Send by** (consultez [Canaux](#canaux)).
6. Laissez **Activé** coché et choisissez **Enregistrer**.

PlaidCloud vérifie chaque alerte activée une fois par heure. Une alerte se déclenche une fois chaque fois que le chiffre franchit le seuil, puis reste silencieuse jusqu'à ce que le chiffre repasse du bon côté et le franchisse de nouveau. La liste indique quand chaque alerte s'est déclenchée pour la dernière fois, et **(off)** après le nom d'une alerte désactivée.

Vous pouvez avoir jusqu'à 20 alertes à vous sur une même application.

## Créer un résumé

1. Dans l'onglet **Digests**, choisissez **Nouveau**.
2. Saisissez un **Nom**.
3. Choisissez **Add KPI**, donnez-lui un **KPI label** et construisez le chiffre. Répétez l'opération pour 10 KPI au maximum. **Remove KPI** en supprime un.
4. À côté de **Envoyer**, choisissez **Chaque jour** ou **Chaque semaine**.
5. Choisissez le mode d'envoi dans **Send by**, puis choisissez **Enregistrer**.

Un résumé est envoyé une fois par jour ou par semaine, lors de la première vérification horaire qui suit le début de la période, la période étant calculée en UTC. La liste indique quand chaque résumé a été envoyé pour la dernière fois. Un KPI pour lequel votre accès à la table ne laisse aucune ligne s'affiche comme sans données, jamais comme un chiffre non filtré.

Vous pouvez avoir jusqu'à 10 résumés à vous sur une même application, et 20 au total toutes applications confondues.

## Canaux

| Send by | Destination |
|---|---|
| **Notification push** | L'application mobile PlaidCloud sur vos appareils. Alertes uniquement. |
| **E-mail** | L'adresse e-mail de votre compte. |
| **Slack** | Un canal Slack, via une connexion Slack. |
| **Microsoft Teams** | Un canal Teams, via une connexion Microsoft Teams. |

Pour **Slack** et **Microsoft Teams**, choisissez la **Connexion** à utiliser pour publier. Un administrateur de l'espace de travail crée la connexion, et l'accès à celle-ci doit vous avoir été accordé. L'adresse de la connexion doit commencer par `https`.

### Ce qu'affiche une carte Slack ou Teams

Une carte n'affiche les chiffres que si votre propre accès à la table n'est pas restreint, c'est-à-dire si aucune sécurité au niveau des lignes ne limite les lignes que vous pouvez lire. Si votre accès est limité à certaines lignes, la carte indique que de nouvelles valeurs sont disponibles et renvoie vers l'application, où chaque lecteur ne voit que les lignes que son propre accès autorise. Chaque carte contient un lien vers l'application. Les membres d'un canal sont gérés en dehors de PlaidCloud, ce qui explique pourquoi les chiffres d'un propriétaire dont l'accès est restreint ne sont pas envoyés vers un canal.

## En cas d'échec de la livraison

Une alerte ou un résumé qui ne peut pas être livré 24 heures de suite, par exemple parce que sa connexion Slack a été supprimée, est désactivé. La liste l'affiche avec **(off)** et le formulaire indique le nombre de livraisons ayant échoué. Corrigez le canal, cochez **Activé** et choisissez **Enregistrer** pour le réactiver.

## Modifier ou supprimer

Choisissez un élément dans la liste pour le modifier, puis **Enregistrer**. Choisissez **Supprimer** pour le retirer. Si vous passez à un autre élément alors que des modifications ne sont pas enregistrées, PlaidCloud vous demande confirmation avant de les abandonner.

## Étapes suivantes

- [Panel Studio](/fr/guides/panel-apps/studio/) : l'endroit où vous accédez à **Alerts & Digests**.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) : créez l'application que les alertes surveillent.
