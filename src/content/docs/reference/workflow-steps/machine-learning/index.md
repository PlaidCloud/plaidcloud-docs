---
title: Machine Learning
description: Workflow steps that train scikit-learn models and score tables with them.
---

Train a model on any table, carry it through the workflow as a model table, and score data tables with it.

## Steps

- [ML: Train Model](/reference/workflow-steps/machine-learning/ml-train/) — fit a scikit-learn model (classification or regression) on a source table and write a queryable model table with the fitted model, parameters, feature list, and training metrics.
- [ML: Score](/reference/workflow-steps/machine-learning/ml-score/) — score a data table with a trained model table and append a prediction column.

See [Migrate Alteryx Workflows](/guides/workflows/migrate-alteryx-workflows/#machine-learning-assisted-modeling-conversions) for how Alteryx Assisted Modeling pipelines convert to these steps.
