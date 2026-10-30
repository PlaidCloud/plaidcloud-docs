---
title: Charger et décharger des dimensions
description: Chargez et déchargez des données de dimension dans PlaidCloud, y compris les importations en masse, l'actualisation des données et la synchronisation avec des sources de données externes.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

Les dimensions peuvent être maintenues à partir d'opérations de workflow par le chargement de données. De plus, les données dimensionnelles peuvent être aplaties en données tabulaires et stockées dans des tables. C'est souvent utile pour enrichir les données de reporting et d'analyse.


## Charger des dimensions

Les dimensions représentant des structures de données hiérarchiques, le processus de chargement doit transmettre les relations contenues dans les données. PlaidCloud prend en charge deux structures de données différentes pour charger des dimensions :
 * Parent-enfant - Les données sont organisées verticalement, avec une colonne *Parent* et une colonne *Enfant* qui définissent chaque parent d'un enfant dans toute la structure
 * Niveaux - Les données sont organisées horizontalement, chaque colonne représentant un niveau de la hiérarchie, de gauche à droite

 Outre la structure, d'autres informations de dimension peuvent être incluses dans le processus de chargement, comme les valeurs, les alias et les propriétés.

 Un chargement par niveaux (à plat) prend une consolidation par défaut, que reçoit chaque nœud intermédiaire créé par le chargement, et peut désigner une colonne feuille : dans ce cas, cette colonne détermine quel nœud porte les alias, les propriétés et les valeurs de la ligne ; sinon, le dernier niveau renseigné est la feuille.

 Le type de consolidation par défaut d'un chargement parent-enfant s'applique à toute ligne dont la consolidation propre est vide ou non reconnue ; il doit donc être l'un des types valides, même lorsque la table désigne aussi une colonne de consolidation. La hiérarchie ciblée par un chargement ne doit pas porter le même nom qu'une colonne mappée par le chargement : une colonne de ce nom est lue comme la hiérarchie à laquelle appartient chaque ligne, de sorte qu'un chargement qui désigne les deux est refusé plutôt que de suivre une lecture en ignorant l'autre.

 Un chargement d'alias, de propriétés ou de valeurs vérifie le membre de chaque ligne avant d'écrire quoi que ce soit. Si une ligne désigne un membre que la dimension ne contient pas, le chargement échoue et signale ces noms, et rien de ce chargement n'est stocké. Chargez d'abord la structure, ou incluez-y les membres manquants, puis chargez les attributs.

 Consultez l'étape de workflow [Dimension Load](/fr/reference/workflow-steps/dimensions/dimension-load) pour plus d'informations.


## Décharger (exporter) des dimensions

L'exportation de dimensions vers des tables prend en charge deux approches structurelles :
 * Parent-enfant - Les données sont organisées verticalement, avec une colonne *Parent* et une colonne *Enfant* qui définissent chaque parent d'un enfant dans toute la structure
 * Niveaux - Les données sont organisées horizontalement, chaque colonne représentant un niveau de la hiérarchie, de gauche à droite

Les propriétés et les valeurs peuvent aussi être incluses dans les données tabulaires aplaties.

 Consultez l'étape de workflow [Dimension Export](/fr/reference/workflow-steps/dimensions/dimension-export) pour plus d'informations.
