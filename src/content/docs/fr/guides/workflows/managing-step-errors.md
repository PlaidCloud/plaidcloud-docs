---
title: Gérer les erreurs d'étape
description: Gérez les erreurs d'étape dans les workflows PlaidCloud, y compris les notifications d'erreur, la logique de nouvelle tentative et les options de reprise après échec.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Si un workflow rencontre une erreur pendant son traitement, un indicateur d'erreur s'affiche à la fois sur le workflow et sur l'étape en erreur. PlaidCloud peut réessayer plusieurs fois une étape en échec. C'est souvent utile lorsque l'étape accède à des systèmes distants ou à des données qui ne sont pas hautement disponibles ou qui échouent par intermittence pour des raisons inconnues. La capacité de nouvelle tentative peut être réglée pour réessayer de nombreuses fois, avec un délai entre les tentatives allant de quelques secondes à plusieurs heures.



Une étape dont le serveur est perdu en cours d'exécution est traitée séparément des nouvelles tentatives : une étape qui peut être répétée sans risque est réexécutée automatiquement, et une étape qui ne le peut pas échoue une seule fois avec un message **interrompu**. Consultez [Étapes interrompues](/fr/guides/workflows/run-a-workflow/#étapes-interrompues).

Lorsque PlaidCloud refuse une étape pour une raison que vous pouvez corriger, comme une autorisation manquante ou un paramètre non valide, le journal de l'étape affiche ce message en langage clair plutôt qu'une erreur de serveur avec une trace de pile. Pour une étape Model Loop, Model Run ou Macro Run dont le workflow enfant échoue, le journal affiche le message d'erreur propre à l'enfant, sous la forme « Child workflow run failed: » suivie du message.

Si aucune nouvelle tentative n'est sélectionnée ou si le nombre maximal de nouvelles tentatives est dépassé, l'étape est marquée en erreur. PlaidCloud propose alors trois niveaux de gestion des erreurs :


* Arrêter le workflow lorsqu'une erreur se produit
* Marquer l'étape en erreur mais poursuivre le traitement du workflow
* Marquer l'étape en erreur et déclencher un processus de workflow de remédiation au lieu de poursuivre le workflow actuel

## Arrêter le workflow


Arrêter le workflow lorsqu'une étape échoue est l'approche la plus courante, car les workflows doivent en général s'exécuter sans erreur. Le workflow s'arrête et l'indicateur d'erreur s'affiche sur l'étape et sur le workflow. L'erreur s'affiche également dans le moniteur d'activité, mais aucune autre action n'est entreprise.



## Poursuivre le traitement


Chaque étape peut être réglée pour continuer en cas d'erreur dans le formulaire de l'étape. Si cette case est cochée, toute étape sera marquée en erreur si une erreur se produit, mais le workflow considérera l'erreur comme l'achèvement de l'étape et continuera. C'est souvent utile lorsque des étapes effectuent des tâches qui peuvent échouer en cas de données manquantes, mais sont sans conséquence pour l'ensemble des processus.



Comme le workflow continue malgré l'erreur dans ce scénario, il n'affichera pas d'indicateur d'erreur et continuera d'afficher un indicateur d'exécution.



## Déclencher un workflow de remédiation


Grâce à la possibilité de définir un workflow de remédiation dans la configuration du workflow, une erreur de workflow arrête immédiatement le traitement du workflow actuel et démarre le traitement du workflow de remédiation. Notez que si une étape est marquée pour continuer en cas d'erreur, un échec ne déclenchera pas le workflow de remédiation. Seules les étapes en échec qui entraîneraient aussi l'arrêt de tout le workflow déclenchent le processus de remédiation.



Un workflow de remédiation peut servir simplement à prévenir les personnes concernées qu'un échec s'est produit, ou effectuer d'autres traitements complexes pour tenter de corriger automatiquement les causes sous-jacentes de l'échec du workflow d'origine.
