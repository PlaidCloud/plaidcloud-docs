---
title: Exécuter une plage d'étapes dans un workflow
description: Exécutez une plage d'étapes précise au sein d'un workflow PlaidCloud pour n'exécuter que certaines parties de votre pipeline de traitement des données.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Exécuter les étapes une à une est utile, mais il peut aussi l'être d'exécuter des sous-ensembles d'un workflow entier pour le développement, les tests ou le dépannage. Pour exécuter un sous-ensemble d'étapes, sélectionnez toutes les étapes que vous souhaitez exécuter, puis choisissez **Exécuter les étapes sélectionnées** dans le menu **Actions** en haut de la hiérarchie des étapes du workflow. Cela déclenche un traitement normal du workflow, mais celui-ci démarre au début des étapes sélectionnées et s'arrête une fois la dernière étape sélectionnée terminée.

Si la dernière étape sélectionnée se trouve dans un groupe défini sur [**Execute in Parallel**](/fr/guides/workflows/controlling-parallel-execution/), l'exécution attend également que toutes les autres étapes sélectionnées de ce groupe soient terminées avant de s'arrêter.
