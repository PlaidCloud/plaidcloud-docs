---
title: Exécuter l'opération de l'application
description: Appelez une opération d'application enregistrée depuis un workflow, en transmettant éventuellement un chemin de document et des paramètres.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Description

Appelle une opération d'application enregistrée depuis un workflow. Utilisez-la pour déclencher un travail de plateforme qui n'est pas une transformation de données — les opérations qu'une application expose pour l'automatisation.

## Configuration

### Opération d'application à exécuter

L'opération à appeler.

### Chemin du fichier

Pour les opérations qui prennent un fichier :

- **Document directory** — le compte de documents et le chemin à transmettre.
- **File parameter name** — le paramètre sous lequel l'opération attend le chemin. La valeur par défaut est `document_path` ; ne la modifiez que si l'opération le nomme autrement.

### Paramètres facultatifs

Paires nom/valeur transmises à l'opération en plus du chemin du fichier.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [User Defined Transform](/fr/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/fr/reference/workflow-steps/general/run-remote-python/)
