---
title: Notify Via SMS
description: Envoyez un SMS depuis une étape de workflow aux membres de l'espace de travail inscrits aux alertes par SMS, avec confirmation de remise, repli par e-mail, regroupement des répétitions et heures de silence.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Description

Envoyez un SMS aux membres de l'espace de travail lorsqu'un workflow requiert leur attention. Un SMS n'est envoyé qu'à un membre qui s'est inscrit lui-même, depuis **Alertes par SMS** dans le menu utilisateur, avec un numéro de mobile américain qu'il a confirmé. Vous choisissez des membres ou une liste de distribution ; vous ne saisissez jamais de numéro de téléphone dans l'étape. Pour vous inscrire, consultez [Alertes par SMS](/fr/guides/workflows/text-alerts/).

Les SMS ne sont envoyés qu'à des numéros américains. N'incluez pas de données personnelles de santé ou financières dans un SMS.

Les SMS proviennent d'un numéro d'alerte PlaidCloud unique et commencent par `PlaidCloud [your workspace name]: ` suivi de votre message. Consultez les [Conditions SMS](https://plaidcloud.com/sms-terms/) et la [Politique de confidentialité SMS](https://plaidcloud.com/sms-privacy/).

## Destinataires

Choisissez **Membres** ou **Liste de distribution**.

- **Membres** affiche les membres de votre espace de travail. Chacun affiche **Inscrit**, **Non inscrit** ou **Désinscrit - Envoyez START par SMS au numéro d'alerte**.
- **Liste de distribution** envoie un SMS à chaque membre de la liste qui est inscrit.

Un membre qui ne s'est pas inscrit ne reçoit aucun SMS. Il constitue un problème pour l'étape (consultez **Si un SMS ne peut pas être remis**) et, par défaut, il reçoit le message par e-mail à la place.

## Message

Rédigez le **Message**. Les variables du projet et les variables du workflow fonctionnent, et **Insérer une variable** ajoute l'une des suivantes :

| Variable | Valeur |
|---|---|
| `{workflow_name}` | Le nom du workflow en cours d'exécution |
| `{project_name}` | Le nom du projet |
| `{run_url}` | Un lien vers l'exécution dans PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | Les variables existantes |

Le compteur sous le message indique approximativement le nombre de caractères et de segments que représente le SMS, préfixe `PlaidCloud [workspace]:` et lien d'exécution compris. Un SMS est tronqué au-delà de 3 segments. Les liens issus de raccourcisseurs de liens publics sont rejetés.

## Remise

| Paramètre | Effet |
|---|---|
| **Si un SMS ne peut pas être remis** | **Faire échouer l'étape** (par défaut) ou **Avertir et continuer**. Un SMS non remis n'est jamais silencieux : il est toujours signalé sur l'étape. |
| **Envoyer un e-mail aux destinataires dont le SMS ne peut pas être remis** | Activé par défaut. Un membre dont le SMS échoue, qui ne s'est pas inscrit ou qui s'est désinscrit reçoit le message par e-mail. |
| **Regrouper les répétitions pendant (minutes)** | 60 par défaut. Une répétition du même message au même membre dans ce délai n'est pas envoyée, et le SMS suivant qui part se termine par `(+N similar since HH:MM)`. |
| **Suspendre les SMS pendant les heures de silence** | Choisissez des heures **De** et **à** ainsi qu'un fuseau horaire. Un SMS qui partirait dans cette plage est retenu jusqu'à sa fin. |

Chaque membre reçoit au plus 20 SMS par jour, un espace de travail envoie au plus 500 SMS et e-mails de repli par jour, et une étape envoie des SMS à 50 membres au plus à la fois.

## M'envoyer un test

**M'envoyer un test** envoie un SMS de test à votre propre numéro et affiche le résultat à côté du bouton. Si vous ne vous êtes pas inscrit, la fenêtre **Alertes par SMS** s'ouvre pour que vous puissiez le faire.

## Ce que voient les destinataires

Chaque SMS provient du numéro d'alerte. Répondre **STOP** arrête tous les SMS de PlaidCloud vers ce numéro, et **HELP** renvoie les coordonnées de contact. Après STOP, un membre envoie **START** par SMS au numéro d'alerte pour reprendre, puis réactive les alertes par SMS dans **Alertes par SMS**. Le formulaire de l'étape affiche **Désinscrit - Envoyez START par SMS au numéro d'alerte** à côté de ce membre tant qu'il ne l'a pas fait.

Les administrateurs de l'espace de travail peuvent voir l'état des alertes par SMS de chaque membre, avec le numéro masqué, dans l'onglet **Informations sur le membre** de la fenêtre du membre. Les membres s'inscrivent et se désinscrivent eux-mêmes ; un administrateur ne peut pas le faire à leur place.

## Étapes ayant saisi un numéro

Une version antérieure de cette étape prenait un opérateur mobile et un numéro de téléphone saisi. Une étape toujours enregistrée ainsi ne fait pas échouer le workflow, et elle n'envoie aucun SMS au numéro saisi.

- **Aucun destinataire choisi :** l'étape se termine avec un avertissement, *No text was sent: this step still uses the retired mobile provider and number. Open the step, choose members who've opted in to text alerts, and save it.* Rien n'est envoyé.
- **Membres ou liste de distribution choisis :** l'étape envoie des SMS à ces destinataires et ignore l'opérateur et le numéro résiduels.

Pour corriger une étape, ouvrez-la, choisissez des membres ou une liste de distribution, puis enregistrez-la.

## Exemples

Aucun exemple pour le moment...
