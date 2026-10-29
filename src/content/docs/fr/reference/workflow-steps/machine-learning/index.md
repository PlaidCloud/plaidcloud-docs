---
title: Machine learning
description: Étapes de workflow qui entraînent des modèles scikit-learn et scorent des tables avec ces modèles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/machine-learning/index.md
---

Entraînez un modèle sur n'importe quelle table, transportez-le dans le workflow sous forme de table de modèle, et scorez des tables de données avec lui.

## Étapes

- [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) : ajustez un modèle scikit-learn (classification ou régression) sur une table source et écrivez une table de modèle interrogeable contenant le modèle ajusté, les paramètres, la liste des variables explicatives et les métriques d'entraînement.
- [ML : scorer](/fr/reference/workflow-steps/machine-learning/ml-score/) : scorez une table de données avec une table de modèle entraîné et ajoutez une colonne de prédiction.

Consultez [Migrer des workflows Alteryx](/fr/guides/workflows/migrate-alteryx-workflows/#conversions-dapprentissage-automatique-assisted-modeling) pour savoir comment les pipelines Alteryx Assisted Modeling sont convertis en ces étapes.
