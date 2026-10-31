---
title: Étiquetage par règles
description: Configurez l'étiquetage par règles dans les allocations PlaidCloud pour catégoriser et étiqueter automatiquement les enregistrements de données selon des critères définis.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

L'étiquetage par règles vous permet de marquer les lignes sources avec des métadonnées que le moteur d'allocation utilise pour décider *où* ces lignes sont affectées. Utilisez-le lorsque le comportement de l'allocation doit varier selon la ligne — par exemple, lorsque les coûts d'un centre de coûts doivent être répartis selon les effectifs, mais ceux d'un autre selon les revenus.

## Quand l'utiliser

- Une règle d'allocation uniforme ne reflète pas la façon dont le coût doit réellement être réparti (règles différentes selon les types de coûts).
- Vous voulez diriger certaines lignes sources vers des cibles précises tout en laissant les autres se répartir normalement.
- Vous modélisez une allocation à plusieurs pools où chaque pool utilise un inducteur différent.

## Fonctionnement de l'étiquetage

1. **Étiquetez la source.** La table de valeurs reçoit une ou plusieurs colonnes d'étiquettes qui classent chaque ligne.
2. **Référencez les étiquettes dans la règle d'allocation.** Lors de la configuration de l'étape d'allocation, vous exprimez les règles sous la forme *« si l'étiquette source X = valeur Y, allouer avec l'inducteur D et la dimension cible T »*.
3. **Le moteur aiguille les lignes.** Chaque ligne source est comparée aux règles dans l'ordre ; la première règle qui correspond détermine le comportement de l'allocation.

## Modèles de sources adaptés à l'étiquetage

- Une colonne nommée `cost_category` avec des valeurs comme `payroll`, `facilities`, `it`, `marketing`
- Une colonne nommée `pool` qui désigne le pool d'allocation auquel la ligne appartient
- Une colonne booléenne comme `is_overhead` qui déclenche un traitement différent

## Exemple

Une table de coûts avec `cost_center` et `cost_category` :

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Vous pouvez configurer deux règles d'allocation :

- **Les lignes de paie** sont réparties selon l'inducteur des effectifs
- **Les lignes informatiques** sont réparties selon l'inducteur du nombre d'utilisateurs

Les deux règles s'exécutent sur la même table source ; les étiquettes déterminent laquelle s'applique à chaque ligne.

## Voir aussi

- [Démarrage rapide des allocations](/fr/guides/allocations/getting-started/allocations-quick-start/) — flux de base avant d'ajouter l'étiquetage
- [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/) — référence complète des étapes
- [Étape Allocation Rules](/fr/reference/workflow-steps/allocation/allocation-rules/) — étape de workflow qui consomme les données étiquetées
