---
title: Ignorer des étapes dans un workflow
description: Ignorez des étapes précises d'un workflow PlaidCloud pour contourner des opérations lors des tests, du débogage ou d'exécutions de traitement sélectives.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/skip-steps-in-a-workflow.md
---

Les étapes du workflow peuvent être définies pour être ignorées pendant l'exécution du workflow. Cela peut être utile si certaines étapes servent au débogage ou sont anciennes et que vous n'êtes pas prêt à les supprimer complètement du workflow.

Pour définir cette option, décochez la case **Activé** de l'étape dans la table du workflow. La modification est enregistrée dès que vous cliquez, sans enregistrement séparé. L'étape ne s'exécutera plus dans le cadre du workflow, mais elle peut toujours être exécutée via le processus d'exécution d'une seule étape.



Les étapes qui ont été désactivées affichent un indicateur de désactivation dans la table de la hiérarchie des étapes du workflow.
