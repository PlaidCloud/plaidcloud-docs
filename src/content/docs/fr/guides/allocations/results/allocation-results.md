---
title: Résultats d'allocation
description: "Analysez les résultats d'allocation PlaidCloud : examen des données de sortie, vérification des répartitions et validation de l'exactitude des allocations."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Après l'exécution d'une étape d'allocation, le résultat est une table de résultat que vous pouvez inspecter, vérifier et transmettre aux étapes suivantes.

## Contenu de la table de résultat

Une ligne de résultat d'allocation typique comprend :

- **Identifiant de la source** : la ligne de la table source dont provient cette allocation
- **Identifiant de la cible** : la ligne de la dimension ou de la table cible qui a reçu la répartition
- **Montant alloué** : la part du montant source affectée à cette cible
- **Valeur de l'inducteur** : le chiffre d'inducteur qui a justifié la répartition (par exemple l'effectif, le chiffre d'affaires, les heures)
- **Taux d'allocation** : la part de l'inducteur en proportion du total
- **Montant source** : le total d'origine réparti (conservé pour l'auditabilité)
- **Référence d'enveloppe / d'étiquette / de règle** : si l'étiquetage par règles a été utilisé, la règle qui a produit cette ligne

Les colonnes exactes dépendent du type d'étape d'allocation et de votre configuration.

## Liste de contrôle de vérification

Avant de vous fier aux résultats :

1. **Rapprochement** : la somme des montants alloués est égale à la somme des montants source (à la tolérance près des nombres à virgule flottante). Sinon, une partie n'a pas été répartie.
2. **Aucune ligne source orpheline** : chaque ligne source a produit au moins une ligne d'allocation. Des lignes orphelines signifient généralement qu'aucune donnée d'inducteur ne correspondait à l'étiquette ou au membre de dimension de la source.
3. **Aucune cible orpheline** : si vous vous attendiez à ce que chaque cible reçoive quelque chose, vérifiez que chaque membre de la dimension cible apparaît dans les résultats.
4. **Taux raisonnables** : les taux d'allocation doivent totaliser 1,0 (100 %) par enveloppe source. Des taux nettement éloignés de la cible indiquent des problèmes dans les données d'inducteurs.
5. **Contrôle ponctuel des totaux** : choisissez une ligne source de forte valeur et vérifiez que son allocation correspond à ce que vous calculeriez à la main.

## Schémas courants à repérer

- **Allocations nulles** : une cible qui n'a rien reçu signifie généralement que la ligne d'inducteur était absente ou avait une valeur nulle
- **Forte concentration** : si l'essentiel de la répartition se concentre sur une seule cible, c'est généralement que la colonne d'inducteur contient une valeur très élevée (souvent un problème de qualité des données en amont)
- **Inducteurs négatifs** : selon l'étape d'allocation, des valeurs d'inducteur négatives peuvent produire des répartitions inversées. Vérifiez que c'est voulu.

## Étapes suivantes

- [Analyser les allocations avec un agent IA](/fr/guides/allocations/results/analyzing-allocations-with-ai/) : demandez, via MCP, pourquoi un résultat a changé, ce qui le détermine et quel serait l'effet d'une modification
- [Dépannage des allocations](/fr/guides/allocations/results/troubleshooting-allocations/) : que faire lorsque le rapprochement échoue
- [Publication de données](/fr/guides/data/publish/) : une fois les résultats validés, publiez-les pour les tableaux de bord et les consommateurs en aval
