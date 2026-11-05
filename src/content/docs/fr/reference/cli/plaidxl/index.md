---
title: PlaidXL
description: Utilisez le complément Excel PlaidXL pour vous connecter à votre espace de travail PlaidCloud, charger des tables de projet et des hiérarchies de dimension dans des feuilles de calcul, créer des rapports dynamiques, explorer et expliquer les chiffres, lire des métriques gouvernées, planifier en saisissant des valeurs directement dans PlaidCloud et interroger Weave.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL est le complément PlaidCloud pour Microsoft Excel. Il connecte un classeur à votre espace de travail PlaidCloud afin que vos modèles et vos rapports lisent des tables de projet et des dimensions de référence, et non une copie qui devient obsolète à la prochaine exécution d'un workflow.

Vous pouvez travailler avec PlaidXL de trois façons, et la plupart des classeurs les combinent toutes :

- **Le volet des tâches** : parcourez vos projets, choisissez une table ou une dimension, sélectionnez des colonnes et des filtres, puis récupérez les données dans une feuille de calcul. Actualiser les maintient à jour, et **Save to PlaidCloud** réécrit une table modifiée. D'autres onglets créent une formule ou un rapport complet à votre place, expliquent l'origine d'un chiffre et vous permettent de poser vos questions à Weave en langage courant.
- **Les fonctions personnalisées** : des formules comme `=PLAIDXL.TABLE.GET_TABLE("Sales")`, `=PLAIDXL.CELL(...)` et `=PLAIDXL.METRIC("Net Revenue")` qui lisent les données PlaidCloud directement dans les cellules. Utilisez-les pour lister des tables et des dimensions, mettre en page une hiérarchie, calculer des valeurs consolidées pour un rapport et lire des métriques gouvernées.
- **Le ruban et le menu contextuel** : explorez une dimension depuis n'importe quelle cellule, choisissez des membres, actualisez, expliquez un chiffre ou affichez les lignes qui le sous-tendent, avec un raccourci clavier pour chaque action.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel contient le volet des tâches PlaidXL et les fonctions personnalisées PlaidXL. Les deux envoient des requêtes, connectées sous votre identité, à un projet de votre espace de travail PlaidCloud, qui renvoie des lignes de table, des hiérarchies de dimension et des valeurs consolidées dans les cellules de la feuille de calcul." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Classeur Excel</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Volet des tâches PlaidXL</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">parcourir, filtrer, récupérer, actualiser</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Fonctions PLAIDXL.*</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tables, hiérarchies, valeurs dans les cellules</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Espace de travail PlaidCloud</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Projet</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tables</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">dimensions et hiérarchies</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">connecté sous votre identité</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">lignes, nœuds, valeurs</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Le volet des tâches et les fonctions personnalisées lisent tous deux le projet que vous sélectionnez, avec vos propres autorisations PlaidCloud.</figcaption>
</figure>

PlaidXL lit les données de PlaidCloud, et il ne modifie une table de projet que lorsque vous y écrivez vous-même : saisissez un nombre par-dessus une valeur `CELL`, ou enregistrez une feuille récupérée avec **Save to PlaidCloud**. Dans les deux cas, l'écriture est immédiate, et **Undo last write** l'annule. Consultez [Type Values Into PlaidCloud](/fr/reference/cli/plaidxl/write-values/).

## Configuration requise

- Excel pour Microsoft 365, ou Excel 2021 ou version ultérieure, sous Windows ou Mac. L'onglet PlaidCloud du ruban, le menu contextuel et le volet des tâches s'exécutent dans Excel pour ordinateur.
- Un compte PlaidCloud dans au moins un espace de travail, et l'accès aux projets que vous souhaitez lire. PlaidXL n'affiche que les projets, les tables et les dimensions que votre compte peut déjà voir dans PlaidCloud.

## Rubriques

- [Install](/fr/reference/cli/plaidxl/install/) : ajouter PlaidXL à Excel et ouvrir le volet des tâches
- [Sign In](/fr/reference/cli/plaidxl/connect/) : se connecter à votre espace de travail, se déconnecter et changer d'espace de travail
- [Work With Tables and Dimensions](/fr/reference/cli/plaidxl/retrieve/) : choisir un projet, filtrer une table, la récupérer dans une feuille, l'actualiser et la réenregistrer
- [Custom Functions](/fr/reference/cli/plaidxl/functions/) : toutes les fonctions `PLAIDXL`, leurs arguments et ce qu'elles renvoient
- [Build a Report](/fr/reference/cli/plaidxl/build-a-report/) : mettre en page un rapport dynamique depuis le volet des tâches ou avec des formules
- [Drill, Pick Members and Explain Numbers](/fr/reference/cli/plaidxl/drill/) : explorer depuis une cellule, choisir des membres, expliquer un chiffre et afficher ses lignes de détail
- [Type Values Into PlaidCloud](/fr/reference/cli/plaidxl/write-values/) : planifier en saisissant des valeurs par-dessus celles du rapport, et annuler toute écriture
- [Demander à Weave dans Excel](/fr/reference/cli/plaidxl/weave/) : créer, explorer et corriger à partir de demandes en langage courant
- [The PlaidCloud Ribbon](/fr/reference/cli/plaidxl/ribbon/) : toutes les commandes, le menu contextuel et les raccourcis clavier
- [Troubleshooting](/fr/reference/cli/plaidxl/troubleshooting/) : solutions aux problèmes les plus courants

Vous découvrez PlaidXL ? Le tutoriel [Work in Excel With PlaidXL](/fr/get-started/tutorials/excel-with-plaidxl/) vous guide de l'installation du complément jusqu'à un premier rapport en 20 minutes environ.

## Voir aussi

- [Projects](/fr/guides/projects/) : ce que contient un projet et comment en trouver un
- [Tables and Views](/fr/guides/data/tables-views/) : les tables que PlaidXL récupère
- [Using Dimensions](/fr/guides/dimensions/dimensions/) : les hiérarchies que PlaidXL met en page et consolide
