---
title: Workflow Loop
description: Créez une boucle dans une étape de workflow PlaidCloud pour parcourir un ensemble de valeurs et répéter des étapes pour chaque élément de la collection.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## Description

Exécute un workflow cible une fois par ligne d'un jeu de données, en définissant les valeurs des colonnes de chaque ligne comme variables de projet avant chaque itération. Utilisez cette étape lorsque vous avez un processus paramétré qui doit s'exécuter plusieurs fois avec des entrées différentes — par exemple, « exécuter la clôture mensuelle pour chaque unité opérationnelle de cette table » ou « charger ce rapport pour chaque trimestre listé ».

Chaque itération de la boucle voit les variables comme si elles avaient été définies manuellement ; le workflow appelé peut donc les référencer dans des expressions, des filtres, des chemins de fichiers et des noms de tables avec la syntaxe standard `\{variable_name}`. La boucle est séquentielle par défaut ; les itérations ne s'exécutent pas en parallèle.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Une boucle Workflow Loop sur un jeu de données dont les lignes sont T1, T2 et T3. Les valeurs des colonnes de chaque ligne deviennent des variables de projet, puis le workflow cible s'exécute — un passage par ligne, en séquence et non en parallèle." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">jeu de données</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">T1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">T2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">T3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = T1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passage 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = T2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passage 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = T3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">passage 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">séquentiel — un passage à la fois, pas en parallèle</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Les colonnes de chaque ligne deviennent des variables de projet, puis le workflow cible s'exécute — un passage par ligne, en séquence. Pour un déploiement parallèle isolé, utilisez plutôt une <a href="/fr/guides/workflows/create-a-macro/">macro</a>.</figcaption>
</figure>



## Workflow à arrêter


Sélectionnez d'abord le projet qui contient le workflow qui sera exécuté à chaque tour de boucle dans la liste déroulante **Projet**.



Sélectionnez ensuite le workflow à exécuter dans la liste déroulante **Workflow**.

## Si une itération échoue

Par défaut, la boucle s'arrête à la première itération dont le workflow échoue, et l'étape échoue. Sous **Gestion des erreurs**, sélectionnez **Continuer après une itération en échec** pour exécuter chaque itération même si l'une d'elles échoue. Chaque échec est conservé dans le **Statut d'exécution de la boucle**, avec le résultat de chaque itération, et l'étape se termine par un avertissement qui indique combien d'itérations ont échoué. Si l'option est désactivée, la boucle s'arrête au premier échec.

## Exemples

Exemples à venir
