---
title: Parcours d'apprentissage Modélisation
description: Ce qu'il faut lire avant les labs Praticien et Expert Modélisation de PlaidCloud, et ce que chaque lab vous demande de faire.
sidebar:
  label: Modélisation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

Le parcours Modélisation porte sur les dimensions et les allocations : construire des hiérarchies, répartir les coûts selon des inducteurs et prouver que les résultats concordent. Commencez par le parcours [Fondations](/fr/guides/certification/foundations/). Pour savoir comment fonctionnent les labs, consultez [Certification PlaidCloud](/fr/guides/certification/).

## Praticien

### À lire dans cet ordre

1. [Premiers pas avec les dimensions](/fr/guides/dimensions/getting-started/)
2. [Gérer les hiérarchies](/fr/guides/projects/managing-hierarchies/)
3. [Concevoir une hiérarchie de dimension](/fr/get-started/tutorials/design-a-dimension/)
4. [Démarrage rapide des allocations](/fr/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/fr/reference/workflow-steps/allocation/allocation-split/)
6. [Créer un modèle d'allocation](/fr/get-started/tutorials/build-an-allocation/)
7. [Résultats d'allocation](/fr/guides/allocations/results/allocation-results/)
8. [Afficher le journal du workflow](/fr/guides/workflows/viewing-workflow-log/)

### Ce que demande le lab

Le lab s'intitule *Modélisation : répartir le coût informatique partagé*.

Une table liste chaque service et son parent. Vous construisez une dimension dont la hiérarchie principale est exactement cette arborescence. Ensuite, dans le workflow du lab, vous allouez un pool de coûts aux services proportionnellement à leur effectif, avec une ligne de résultat par service. Une seconde table d'inducteurs est également présente, mais ce n'est pas l'inducteur de ce pool.

Le lab vérifie que le workflow s'exécute, que la hiérarchie est correcte, que le total alloué concorde avec la source et que chaque service reçoit le bon montant.

## Expert

Le lab Expert est chronométré : vous disposez de 4 heures à partir du moment où vous le démarrez.

### À lire dans cet ordre

1. [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/)
2. [Dépannage des allocations](/fr/guides/allocations/results/troubleshooting-allocations/)
3. [Suivre les allocations avec un agent IA connecté par MCP](/fr/integrations/ai-coding-agents/tracing-allocations/)
4. [Résultats d'allocation](/fr/guides/allocations/results/allocation-results/)
5. [Essayer une simulation d'inducteur](/fr/guides/allocations/results/driver-what-if/)
6. [Gérer les hiérarchies](/fr/guides/projects/managing-hierarchies/)

### Ce que demande le lab

Le lab s'intitule *Modélisation Expert : réparer le modèle de répartition*.

Un modèle d'allocation en deux étapes ne concorde plus avec le grand livre, et certains services sont manifestement faux. Vous retrouvez la cause et corrigez le modèle : chaque étape alloue exactement son pool, les totaux par service sont corrects et s'additionnent au grand livre, et la dimension des services ne contient que les services qui existent. Aucune ligne d'équilibrage ne doit servir à faire concorder quoi que ce soit. Vous ajoutez ensuite une étape qui montre ce que coûterait l'informatique à chaque service si elle était allouée selon la surface au sol plutôt que selon l'effectif.

Le lab vérifie que le workflow s'exécute, que la hiérarchie est correcte, que chaque étape et les totaux par service concordent avec le grand livre, que chaque service reçoit le bon total et que le scénario de surface au sol est correct.
