---
title: "Essbase : interroger un cube"
description: Exécutez une requête MDX en direct sur un cube Oracle Essbase et placez la grille de résultats dans une table de workflow, avec des colonnes déduites de la grille et l'accès aux lignes appliqué au résultat.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Description

L'étape **Essbase : interroger un cube** exécute un `SELECT` MDX sur un cube Oracle Essbase et écrit la grille renvoyée dans une table cible. C'est une **véritable requête en direct** : l'étape envoie le MDX et lit la grille obtenue de manière synchrone, si bien que chaque exécution reflète les chiffres actuels du cube. Ce n'est ni une extraction ni un sondage : il n'y a aucune tâche intermédiaire à attendre, ni aucun instantané qui devienne obsolète entre deux exécutions.

Utilisez-la pour récupérer une tranche précise d'un cube (un ensemble de comptes par période, une comparaison de scénarios, un jeu d'inducteurs pour une allocation) dans une table PlaidCloud, que vous pouvez ensuite transformer, joindre ou intégrer à vos rapports avec le reste de vos données.

## Prérequis

- Une [connexion Oracle Essbase](/fr/reference/connectors/erp/oracle-essbase/) qui pointe vers Essbase 21c+ ou Oracle Analytics Cloud (OAC), avec un compte de service pouvant lire l'application et le cube que vous voulez interroger.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Flux allant d'une connexion Essbase à une table cible, en passant par l'application et le cube choisis, une requête MDX et la grille renvoyée." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Connexion</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Application</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cube</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Grille</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Table</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Le MDX s'exécute en direct sur le cube ; la grille renvoyée arrive dans la table cible, avec des colonnes déduites de la grille elle-même.</figcaption>
</figure>

## Configuration

- **Connexion** : une connexion Oracle Essbase. Le raccourci de modification à côté du sélecteur ouvre l'éditeur de connexion pour la consulter ou la modifier.
- **Application** : l'application Essbase à interroger. Le sélecteur liste les applications que le compte de service de la connexion peut voir ; si la connexion définit une application par défaut, elle est présélectionnée.
- **Cube (Database)** : le cube de l'application choisie sur lequel exécuter la requête.
- **MDX** : l'instruction `SELECT` MDX à exécuter. Construisez-la avec la sélection guidée des membres ou écrivez-la directement (voir ci-dessous).
- **Table cible** : la table dans laquelle la grille renvoyée est écrite.

## Construire la requête

Vous pouvez produire le MDX de deux manières :

- **Sélection guidée des membres.** Parcourez les dimensions et les membres du cube et choisissez ce qui va en colonnes et en lignes ; l'étape assemble le MDX pour vous. Les membres se chargent un niveau à la fois lorsque vous les développez, ce qui garde un grand plan réactif.
- **MDX brut.** Écrivez ou collez directement un `SELECT` MDX : c'est l'échappatoire pour tout ce que le sélecteur guidé ne couvre pas, comme les membres calculés, les fonctions ou les opérateurs d'ensemble.

Les deux approches produisent la même valeur `MDX` que l'étape exécute ; le sélecteur guidé est un point de départ que vous pouvez toujours modifier à la main.

## Options

| Champ | Par défaut | Remarques |
|---|---|---|
| Supprimer les cellules #Missing | Désactivé | Côté serveur : supprime les cellules `#Missing` et les autres cellules structurellement non pertinentes avant leur transfert sur le réseau. Sans risque : ne supprime jamais un zéro enregistré. |
| Supprimer aussi les cellules à zéro (avec perte) | Désactivé | Un filtre distinct, à activer explicitement, qui écarte aussi toute cellule dont la valeur est déjà exactement `0`, après sa récupération. **Avec perte** : dans un cube de planification, un zéro enregistré est un fait réel, pas une absence de données ; activez cette option uniquement si vous voulez expressément exclure les zéros du résultat. |
| Limite de lignes | 250 000 | Plafonne le nombre de lignes renvoyées. Laissez le champ vide pour utiliser le plafond par défaut de 250 000 ; augmentez-le ou réduisez-le explicitement. Une requête qui dépasse la limite est refusée au lieu d'être tronquée silencieusement : affinez la requête (ajoutez un découpage, `NON EMPTY` ou un ensemble de membres plus restreint) ou augmentez la limite de lignes, puis réessayez. |

## Aperçu

Avant d'enregistrer, **Aperçu** exécute le MDX actuel sur le cube et affiche les colonnes renvoyées et les premières lignes : un contrôle rapide pour vérifier que la requête a la forme attendue, indépendamment de la limite de lignes configurée dans l'étape elle-même.

## Résultats et schéma à la lecture

La grille renvoyée par Essbase est écrite dans la table cible avec des **colonnes déduites de la grille renvoyée** (schéma à la lecture). Vous n'avez pas à déclarer de liste de colonnes à l'avance :

- Les noms de colonnes proviennent des lignes d'en-tête de la grille. Une cellule d'en-tête qui ne couvre rien (le coin au-dessus des libellés de lignes) devient `column_1`, `column_2`, et ainsi de suite ; les noms en double sont rendus uniques par un suffixe numérique.
- Une colonne dont toutes les cellules de données sont numériques est typée comme numérique ; toute autre colonne est typée comme texte. Les cellules Essbase vides arrivent sous forme de valeurs nulles.
- Les libellés de membres et d'alias de la grille proviennent de la table d'alias configurée sur la connexion, appliquée de la même façon à chaque exécution, et non de la valeur par défaut propre à la session d'Essbase, qui pourrait afficher des libellés différents selon la personne connectée au moment de la requête.

Comme la forme du résultat suit la requête, modifier ce que le MDX place en colonnes modifie les colonnes de la table à l'exécution suivante : gardez-le à l'esprit pour les étapes en aval qui référencent des noms de colonnes précis.

## Accès aux lignes

La [sécurité au niveau des lignes](/fr/administration/access/managing-security-groups-and-assignments/#gérer-laccès-aux-lignes) s'applique à la table obtenue exactement comme à toute autre table PlaidCloud. La gouvernance s'applique au résultat que l'étape écrit : un lecteur soumis à une restriction de lignes ne voit que les lignes que son groupe de sécurité autorise. La requête s'exécute avec le compte de service de la connexion, mais la table qu'elle produit est gouvernée comme le reste de vos données.

## Exemple

Ce MDX place deux mesures en colonnes et deux produits en lignes :

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Son exécution sur un cube qui renvoie ces quatre nombres produit une table comme celle-ci :

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

La colonne des libellés de lignes n'a pas d'en-tête dans la grille ; elle devient donc `column_1` (texte). `Sales` et `COGS` sont entièrement numériques et arrivent sous forme de colonnes numériques.

## Voir aussi

- [Se connecter à Oracle Essbase (guide)](/fr/guides/connections/essbase/) : créez la connexion et construisez une requête.
- [Connecteur Oracle Essbase](/fr/reference/connectors/erp/oracle-essbase/) : référence des champs de la connexion.
- [Essbase : lire une dimension](/fr/reference/workflow-steps/essbase/essbase-dimension-read/) : charge le plan d'une dimension Essbase dans une dimension PlaidCloud, en direct depuis le cloud.
- [Étapes Oracle Essbase](/fr/reference/workflow-steps/essbase/)
- [Requête REST](/fr/reference/workflow-steps/general/rest-request/) : l'étape généraliste pour les autres requêtes HTTP en direct.
