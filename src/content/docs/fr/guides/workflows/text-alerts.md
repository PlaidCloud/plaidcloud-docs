---
title: Alertes par SMS
description: Activez la réception des alertes de workflow PlaidCloud sous forme de SMS sur votre numéro de mobile américain, et désactivez-les à nouveau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Les workflows peuvent vous envoyer un SMS lorsqu'ils requièrent votre attention, avec l'étape [Notify Via SMS](/fr/reference/workflow-steps/notifications/notify-via-sms/). Un workflow ne peut vous envoyer de SMS qu'après que vous avez vous-même donné votre accord.

## Activer les alertes par SMS

1. Ouvrez le menu utilisateur dans le coin supérieur droit et choisissez **Alertes par SMS**.
2. Saisissez votre **Numéro de mobile américain**.
3. Cochez **J'accepte de recevoir des alertes SMS de workflow PlaidCloud à ce numéro.** Lisez les mentions d'information au-dessus, ainsi que les liens **SMS Terms** et **SMS Privacy Policy**.
4. Cliquez sur **Envoyer le code**. PlaidCloud envoie par SMS un code à 6 chiffres à votre numéro. L'arrivée des SMS peut prendre une ou deux minutes.
5. Saisissez le **Code de confirmation** dans les 10 minutes et cliquez sur **Confirmer**.

Après l'envoi d'un code, le bouton affiche un compte à rebours de 60 secondes, puis indique **Renvoyer le code**. Renvoyer tant que votre code est encore valide envoie le même code par SMS ; quel que soit le SMS qui arrive, il fonctionne. Vous pouvez demander 3 codes par numéro de téléphone et par jour, et 3 par personne et par heure.

La fenêtre indique alors **Text alerts are on for** suivi de votre numéro masqué. Seuls les numéros de mobile américains sont pris en charge. Des frais de messagerie et de données peuvent s'appliquer, et la fréquence des messages varie.

## Désactiver les alertes par SMS

Ouvrez **Alertes par SMS** et cliquez sur **Arrêter les alertes SMS**, ou répondez **STOP** à n'importe quel SMS. Répondez **HELP** pour obtenir de l'aide.

## Les réactiver après STOP

Répondre STOP bloque tous les SMS vers votre numéro. Envoyez **START** par SMS au numéro d'alerte indiqué dans la fenêtre, puis envoyez un nouveau code et confirmez-le.

## En cas de problème

| Message | Que faire |
|---|---|
| Ce code est incorrect | Vérifiez le SMS et saisissez à nouveau le code. |
| Ce code a expiré | Cliquez sur **Envoyer le code** pour en obtenir un nouveau. |
| Trop de codes incorrects | Après 5 codes incorrects, cliquez sur **Envoyer le code** pour en obtenir un nouveau. |
| Saisissez un numéro de mobile américain valide | Utilisez un numéro de mobile américain à 10 chiffres. |
| Trop de demandes | Vous avez atteint une limite de codes. Attendez quelques minutes et réessayez. |
| Les alertes par SMS ne sont pas disponibles pour votre espace de travail pour le moment | Réessayez plus tard. |

N'utilisez pas les alertes par SMS pour des données personnelles de santé ou financières. Questions : support@plaidcloud.com.
