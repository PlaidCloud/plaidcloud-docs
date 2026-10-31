---
title: Allocations récursives et réciproques
description: Modélisez la répartition de coûts en plusieurs passes ou réciproque dans PlaidCloud en enchaînant des étapes d'allocation en passes explicites et échelonnées.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Certains modèles de coûts exigent que la cible d'une allocation devienne la *source* de la suivante, par exemple des services partagés qui se consomment mutuellement (l'informatique sert les RH, mais les RH servent aussi l'informatique). PlaidCloud modélise cela en **enchaînant des étapes d'allocation en passes explicites et échelonnées**, et non au moyen d'un solveur automatique unique.

## Quand plusieurs passes sont nécessaires

- **Services réciproques** : deux pools de coûts qui se consomment mutuellement.
- **Répartitions en cascade** : les coûts divisionnaires descendent dans une hiérarchie, et les niveaux inférieurs doivent absorber les niveaux supérieurs avant de réallouer.
- **Équilibre itératif** : le modèle converge vers un résultat stable au fil de plusieurs passes (le pool A alloue une partie à B, B en réalloue une partie à A, et ainsi de suite).

## Comment le modéliser

PlaidCloud n'a **aucun « mode récursion » intégré ni solveur de convergence automatique**. Vous construisez vous-même la récursion en ajoutant une [étape Allocation Split](/fr/reference/workflow-steps/allocation/allocation-split/) distincte pour chaque passe et en les reliant en séquence :

1. Exécutez la première passe comme une étape Allocation Split normale.
2. Pour la passe suivante, construisez une source qui inclut la sortie de la passe précédente (généralement en réunissant ou en joignant le résultat précédent au pool) et allouez de nouveau.
3. Répétez autant de passes que votre modèle l'exige.

Comme chaque passe est une étape explicite, **vous décidez du nombre de passes exécutées**. Le moteur ne résout pas la relation réciproque comme une équation simultanée unique, et aucun paramètre de tolérance n'arrête automatiquement la boucle. Ajoutez des passes jusqu'à ce que le résidu restant à réallouer soit assez faible pour vos besoins.

## Conseils

- Commencez par une allocation en **une seule passe** et vérifiez que le modèle simple se comporte comme prévu avant d'ajouter des passes.
- Après chaque passe, vérifiez le résidu non alloué restant. S'il ne diminue pas d'une passe à l'autre, revoyez les relations d'inducteur : une véritable dépendance circulaire ne se stabilisera jamais, quel que soit le nombre de passes ajoutées.
- Chaque passe retraite sa source ; la récursion est donc coûteuse sur de grands jeux de données. Testez sur un échantillon avant d'exécuter sur l'ensemble de la source.

## Voir aussi

- [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/) : configuration de base
- [Étape Allocation Split](/fr/reference/workflow-steps/allocation/allocation-split/) : l'étape du workflow que vous enchaînez pour chaque passe
- [Dépannage des allocations](/fr/guides/allocations/results/troubleshooting-allocations/) : lorsque les résidus n'ont pas de sens
