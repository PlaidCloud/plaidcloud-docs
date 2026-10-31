---
title: Démarrage rapide des allocations
description: Configurez rapidement une allocation de coûts de base dans PlaidCloud avec ce guide pas à pas couvrant les sources, les inducteurs et le mappage des cibles.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Ce pas à pas vous mène des données de coûts brutes à un modèle d'allocation opérationnel en 30 minutes environ.

## Ce dont vous avez besoin

- Un projet contenant au moins deux tables :
  - **Valeurs à allouer** — les coûts (ou les revenus, ou les volumes) que vous voulez répartir. Une ligne par unité source, une colonne contenant le montant.
  - **Données d'inducteur** — la base de répartition. Effectifs, surface en mètres carrés, nombre de transactions, revenus — tout ce selon quoi vous voulez allouer.
- Une dimension qui relie la source et la cible (centres de coûts, services, produits — la taxonomie qui convient à votre modèle).

Si vous ne disposez pas encore de tout cela, les guides [Tables et vues](/fr/guides/data/) et [Dimensions](/fr/guides/dimensions/) expliquent comment charger les données d'entrée.

## Étapes

1. **Ouvrez le projet** qui contient vos tables de valeurs et d'inducteurs.
2. **Créez un nouveau workflow.** Les allocations s'exécutent toujours dans un workflow — elles ne s'appliquent pas directement aux tables en dehors de celui-ci.
3. **Ajoutez une étape d'allocation.** Dans le workflow, ajoutez une étape de la catégorie **Allocation**. Le point de départ le plus courant est **Allocation Rules** pour une répartition simple fondée sur un inducteur.
4. **Configurez la source.** Pointez l'étape vers votre table de valeurs et choisissez la colonne contenant le montant à allouer.
5. **Configurez l'inducteur.** Pointez l'étape vers la table d'inducteurs et choisissez la colonne contenant les valeurs de l'inducteur.
6. **Mappez la dimension.** Identifiez la colonne de chaque table qui représente les membres de la dimension. L'étape d'allocation s'en sert pour faire correspondre les lignes sources aux lignes d'inducteur.
7. **Exécutez l'étape.** Le résultat est une nouvelle table avec une ligne par montant réparti.
8. **Examinez les résultats.** Vérifiez que les totaux correspondent à ce que vous attendiez — la somme des montants alloués doit être égale à la somme des montants sources (dans la limite de la tolérance d'arrondi).

## Suites courantes

- **Répartition récursive** — si une cible contient elle-même des inducteurs pour une allocation ultérieure, consultez [Allocations récursives](/fr/guides/allocations/setup/recursive-allocations/).
- **Étiquetage des lignes pour l'allocation** — pour piloter *quelles* lignes sont allouées à quelles cibles, consultez [Étiquetage par règles](/fr/guides/allocations/getting-started/rule-based-tagging/).
- **Analyse de résultats inattendus** — si les totaux ne concordent pas ou si certaines lignes semblent incorrectes, consultez [Dépannage des allocations](/fr/guides/allocations/results/troubleshooting-allocations/).

## Étapes suivantes

- [Pourquoi les allocations sont-elles utiles ?](/fr/guides/allocations/getting-started/why-are-allocations-useful/) — quand les utiliser
- [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/) — référence de configuration approfondie
- [Types d'étapes d'allocation](/fr/reference/workflow-steps/allocation/) — toutes les étapes de workflow de la catégorie Allocation
