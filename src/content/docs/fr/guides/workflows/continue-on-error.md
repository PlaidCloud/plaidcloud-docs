---
title: Continuer en cas d'erreur
description: Configurez les étapes d'un workflow PlaidCloud pour poursuivre l'exécution en cas d'erreur, afin que les étapes suivantes s'exécutent malgré des échecs antérieurs.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

Les étapes de workflow peuvent être configurées pour poursuivre le traitement même en cas d'erreur. Cela peut être utile pour les conditions de démarrage d'un workflow ou lorsque des données ne sont disponibles que par intermittence. Si l'étape échoue, l'erreur est enregistrée mais le workflow poursuit son traitement.



Pour définir cette option, ouvrez le formulaire de l'étape depuis la table du workflow — cliquez sur son icône d'engrenage, ou faites un clic droit dessus et choisissez **Modifier les détails de l'étape** — puis accédez à l'onglet **Général**. Définissez **Action à effectuer en cas d'erreur** sur **Continuer**. Après l'enregistrement de l'étape mise à jour, les erreurs de cette étape n'arrêteront plus le workflow.



Les étapes configurées pour continuer en cas d'erreur portent un indicateur spécial dans la table de hiérarchie des étapes du workflow.
