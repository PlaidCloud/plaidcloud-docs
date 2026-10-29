---
title: Attendre
description: Ajoutez un délai temporisé dans une étape de workflow PlaidCloud pour suspendre l'exécution pendant une durée donnée avant de passer à l'étape suivante.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Description


La transformation Attendre sert à suspendre le traitement pendant une durée donnée. Elle peut être particulièrement utile pour attendre des opérations d'E/S provenant d'autres systèmes, ou pour déboguer des workflows pendant leur développement.



## Paramètres de durée


Indiquez un nombre entier non négatif à l'aide du champ de saisie numérique **Durée**.



Sélectionnez ensuite l'unité de temps dans la liste déroulante. Les unités suivantes sont disponibles :


* Secondes
* Minutes
* Heures

## Attendre une heure ou un fichier

La section **Autres attentes** comporte les champs suivants. L'étape les attend dans cet ordre, après la durée :

* **Millisecondes** (`milliseconds`) — millisecondes d'attente en plus de la durée.
* **Jusqu'à l'heure de la journée** (`until_time`) — attend ensuite jusqu'à ce que l'horloge indique cette heure de la journée, en UTC, au format `HH:MM:SS`.
* **Attendre un fichier** (`file`) — attend ensuite que ce fichier Document, `{account, path}`, change. **Modification du fichier** (`file_event`) est le changement attendu : `modified` (par défaut), `created` ou `deleted`. L'étape consulte le fichier toutes les **Consulter le fichier toutes les (secondes)** (`poll_seconds`, 5 par défaut) pendant au plus **Attente maximale du fichier (secondes)** (`max_wait_seconds`, 3 600 par défaut, au plus un jour), puis se termine avec un avertissement et le workflow continue. Un fichier déjà présent lorsque l'étape attend `created` met fin à l'attente immédiatement, et un fichier manquant lorsque l'étape attend `modified` ou `deleted` se termine avec un avertissement nommant le chemin, sans attendre.
