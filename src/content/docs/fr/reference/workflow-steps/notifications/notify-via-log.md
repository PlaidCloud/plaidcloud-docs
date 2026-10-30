---
title: Notify Via Log
description: Écrivez des entrées de journal depuis une étape de workflow PlaidCloud pour consigner des messages d'état, des informations de débogage et des événements de piste d'audit.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## Description


Écrit un message dans le journal du workflow Analyze.



### Paramètres du message


Saisissez le message à écrire dans le journal. Sélectionnez ensuite l'un des trois niveaux de gravité suivants :


* Information
* Avertissement
* Erreur

À noter : les variables du projet et les variables du workflow sont toutes deux disponibles pour cette transformation.


## Exemples


Dans cet exemple, l'exécution de cette transformation ajoute un élément **Information** au journal, avec le texte *Write a message to the workflow log. I believe you have my stapler, Demo.*
