---
title: Fonctions d'agrégation (Lakehouse v1)
description: "Fonctions d'agrégation SQL de Lakehouse v1 : résumez des lignes avec SUM, AVG, MIN, MAX, COUNT et des agrégats statistiques."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

Les fonctions d'agrégation sont des outils essentiels en SQL : elles permettent d'effectuer des calculs sur un ensemble de valeurs et de renvoyer un seul résultat.

Ces fonctions vous aident à extraire et à synthétiser les données des bases de données pour en tirer des enseignements utiles. 

| Nom de la fonction                                               | Ce qu'elle fait                                                              | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Vérifie si une ligne quelconque remplit la condition spécifiée               | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Estime le nombre de valeurs distinctes avec HyperLogLog                      | 
| [ARG_MAX](aggregate-arg-max)                                     | Trouve la valeur arg correspondant à la valeur val maximale                  | 
| [ARG_MIN](aggregate-arg-min)                                     | Trouve la valeur arg correspondant à la valeur val minimale                  | 
| [AVG_IF](aggregate-avg-if)                                       | Calcule la moyenne des lignes remplissant une condition                      | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Convertit toutes les valeurs d'une colonne en tableau                        |
| [AVG](aggregate-avg)                                             | Calcule la valeur moyenne d'une colonne donnée                               | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Compte le nombre de valeurs distinctes d'une colonne                         | 
| [COUNT_IF](aggregate-count-if)                                   | Compte les lignes remplissant une condition spécifiée                        | 
| [COUNT](aggregate-count)                                         | Compte le nombre de lignes répondant à certains critères                     | 
| [COVAR_POP](aggregate-covar-pop)                                 | Renvoie la covariance de population d'un ensemble de paires de nombres       | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Renvoie la covariance d'échantillon d'un ensemble de paires de nombres       | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Renvoie un tableau dont les éléments sont la moyenne mobile des valeurs d'entrée |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Renvoie un tableau dont les éléments sont la somme mobile des valeurs d'entrée |
| [HISTOGRAM](aggregate-histogram)                                | Génère un histogramme de distribution des données par buckets de hauteur égale |
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | Convertit des valeurs en tableau JSON en ignorant les NULL                  | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | Convertit des paires clé-valeur en objet JSON                               | 
| [KURTOSIS](aggregate-kurtosis)                                   | Calcule le kurtosis en excès d'un ensemble de valeurs                        | 
| [MAX_IF](aggregate-max-if)                                       | Trouve la valeur maximale des lignes remplissant une condition               | 
| [MAX](aggregate-max)                                             | Trouve la plus grande valeur d'une colonne donnée                            | 
| [MEDIAN](aggregate-median)                                       | Calcule la valeur médiane d'une colonne donnée                               | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Calcule la valeur médiane d'une colonne donnée avec l'algorithme t-digest    | 
| [MIN_IF](aggregate-min-if)                                       | Trouve la valeur minimale des lignes remplissant une condition               | 
| [MIN](aggregate-min)                                             | Trouve la plus petite valeur d'une colonne donnée                            | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Calcule le quantile interpolé d'une colonne donnée                           |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Calcule le quantile d'une colonne donnée                                     | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Calcule le quantile avec l'algorithme t-digest                               |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Calcule le quantile pondéré avec l'algorithme t-digest                       |
| [RETENTION](aggregate-retention)                                 | Calcule la rétention pour un ensemble d'événements                           | 
| [SKEWNESS](aggregate-skewness)                                   | Calcule le coefficient d'asymétrie d'un ensemble de valeurs                  | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Calcule l'écart type de population d'une colonne                             | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Calcule l'écart type d'échantillon d'une colonne                             | 
| [STRING_AGG](aggregate-string-agg)                               | Convertit toutes les valeurs non NULL en chaîne, séparées par le délimiteur  |
| [SUM_IF](aggregate-sum-if)                                       | Additionne les valeurs d'une colonne donnée qui remplissent une condition    | 
| [SUM](aggregate-sum)                                             | Additionne les valeurs d'une colonne donnée                                  | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analyse le comportement des utilisateurs dans une séquence d'événements ordonnée dans le temps |
