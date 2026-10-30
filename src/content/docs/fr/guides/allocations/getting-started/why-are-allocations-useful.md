---
title: Pourquoi utiliser les allocations
description: Découvrez l'intérêt des allocations de coûts dans PlaidCloud pour la comptabilité par activités, la refacturation et l'analyse de rentabilité.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

Les allocations répartissent un ensemble de valeurs (généralement des coûts, mais cela fonctionne pour tout agrégat) entre des consommateurs, selon un inducteur mesurable. Elles répondent à la question suivante : *si nous engageons ce coût, comment l'affecter à ce qui le consomme ?*

## Cas d'usage courants

### Comptabilité par activités

Vous connaissez vos dépenses marketing totales pour un trimestre. Vous voulez les attribuer à des produits précis selon un critère mesurable : heures de campagne, leads générés, opportunités qualifiées. Une allocation répartit l'enveloppe marketing entre les produits à l'aide de l'inducteur de votre choix, ce qui donne à chaque produit un coût complet.

### Refacturation informatique

Vous dépensez X $ pour faire fonctionner une infrastructure partagée (calcul, stockage, licences). Chaque unité opérationnelle en consomme une part différente. Une allocation répartit le coût informatique entre les unités selon des indicateurs d'usage (heures de machine virtuelle, Go de stockage, licences utilisateur), de sorte que le compte de résultat de chaque unité reflète ce qu'elle a réellement consommé.

### Répartition des services partagés

Finance, RH, juridique, services généraux : des fonctions centrales qui servent toute l'entreprise. Les allocations répartissent leur coût entre les divisions desservies, généralement selon l'effectif, le chiffre d'affaires ou une combinaison pondérée.

### Prix de transfert

Pour les organisations multi-entités, les allocations modélisent la tarification des services internes entre entités. Le résultat alimente les écritures intersociétés.

### Analyse de rentabilité

Vous avez le chiffre d'affaires au niveau du produit ou du client. Vous avez des coûts répartis dans différentes enveloppes (ventes, support, infrastructure, coût des marchandises vendues). Les allocations rassemblent le tout à la granularité produit/client pour vous permettre de voir la marge réelle.

### Calcul des coûts par nomenclature

Le coût descend le long d'une hiérarchie de composants. Chaque niveau de la nomenclature est une allocation : les coûts des sous-ensembles se répartissent sur les ensembles, les ensembles sur les produits finis, les produits finis sur les références.

## Ce que les allocations vous épargnent

Sans moteur d'allocation, vous construiriez ces modèles dans des tableurs, fragiles, difficiles à auditer et à reproduire avec des données mises à jour. Les allocations PlaidCloud vous offrent :

- **Des modèles reproductibles** qui s'exécutent de nouveau automatiquement lorsque les données source sont actualisées
- **Une piste d'audit** indiquant quelles lignes source ont contribué à quelles lignes cibles
- **Des allocations en cascade** dont les résultats alimentent d'autres allocations
- **Une intégration dimensionnelle** pour que les allocations respectent vos hiérarchies existantes

## Étapes suivantes

- [Démarrage rapide des allocations](/fr/guides/allocations/getting-started/allocations-quick-start/) : créez une allocation en 30 minutes
- [Étiquetage par règles](/fr/guides/allocations/getting-started/rule-based-tagging/) : contrôlez le comportement de l'allocation ligne par ligne
- [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/) : référence complète de la configuration
