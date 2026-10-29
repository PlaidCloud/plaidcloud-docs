---
title: PlaidXL
description: Utilisez le complément Excel PlaidXL pour vous connecter à votre espace de travail PlaidCloud, importer des tables de projet et des hiérarchies de dimensions dans des feuilles de calcul, les actualiser à la demande et créer des rapports dynamiques avec les fonctions personnalisées PlaidXL.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL est le complément PlaidCloud pour Microsoft Excel. Il relie un classeur à votre espace de travail PlaidCloud afin que vos modèles et vos rapports lisent les tables et les dimensions de référence des projets, et non une copie qui devient obsolète à la prochaine exécution d'un workflow.

Vous pouvez travailler avec PlaidXL de deux manières, et la plupart des classeurs utilisent les deux :

- **Le volet des tâches** — parcourez vos projets, choisissez une table ou une dimension, sélectionnez des colonnes et des filtres, puis récupérez les données dans une feuille de calcul. **Refresh All Tables** récupère les données actuelles de toutes les tables que vous avez importées.
- **Les fonctions personnalisées** — des formules telles que `=PLAIDXL.TABLE.GET_TABLE("Sales")` et `=PLAIDXL.CELL(...)` qui lisent les données PlaidCloud directement dans les cellules. Utilisez-les pour lister des tables et des dimensions, afficher une hiérarchie et calculer des valeurs consolidées pour un rapport.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel contient le volet des tâches PlaidXL et les fonctions personnalisées PlaidXL. Les deux envoient des requêtes, connectées sous votre identité, à un projet de votre espace de travail PlaidCloud, qui renvoie des lignes de table, des hiérarchies de dimensions et des valeurs consolidées dans les cellules de la feuille de calcul." style="width:100%;max-width:660px;height:auto;">
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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Le volet des tâches et les fonctions personnalisées lisent tous deux le projet que vous sélectionnez, avec vos propres permissions PlaidCloud.</figcaption>
</figure>

PlaidXL lit les données. Il n'écrit rien dans PlaidCloud : modifier une feuille récupérée ne change donc jamais une table de projet.

## Prérequis

- Excel pour Microsoft 365, ou Excel 2021 ou version ultérieure, sous Windows ou Mac. L'onglet PlaidCloud du ruban et le volet des tâches fonctionnent dans Excel pour ordinateur.
- Un compte PlaidCloud dans au moins un espace de travail, et l'accès aux projets que vous souhaitez lire. PlaidXL n'affiche que les projets, les tables et les dimensions que votre compte peut déjà voir dans PlaidCloud.

## Sujets

- [Installation](/fr/reference/cli/plaidxl/install/) — ajouter PlaidXL à Excel et ouvrir le volet des tâches
- [Connexion](/fr/reference/cli/plaidxl/connect/) — se connecter à votre espace de travail, se déconnecter et changer d'espace de travail
- [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/) — choisir un projet, filtrer une table, la récupérer dans une feuille et l'actualiser
- [Fonctions personnalisées](/fr/reference/cli/plaidxl/functions/) — chaque fonction `PLAIDXL`, ses arguments et ce qu'elle renvoie
- [Créer un rapport avec les fonctions personnalisées](/fr/reference/cli/plaidxl/build-a-report/) — afficher une hiérarchie et la remplir avec des valeurs consolidées
- [Le ruban PlaidCloud](/fr/reference/cli/plaidxl/ribbon/) — commandes d'actualisation, d'exploration et de nettoyage
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/) — solutions aux problèmes les plus courants

Vous découvrez PlaidXL ? Le tutoriel [Travailler dans Excel avec PlaidXL](/fr/get-started/tutorials/excel-with-plaidxl/) vous accompagne de l'installation du complément jusqu'à un premier rapport en 20 minutes environ.

## Voir aussi

- [Projets](/fr/guides/projects/) — ce que contient un projet et comment en trouver un
- [Tables et vues](/fr/guides/data/tables-views/) — les tables que PlaidXL récupère
- [Utiliser les dimensions](/fr/guides/dimensions/dimensions/) — les hiérarchies que PlaidXL affiche et consolide
