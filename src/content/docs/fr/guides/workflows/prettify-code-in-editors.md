---
title: Mettre en forme le code dans les éditeurs
description: Utilisez le bouton Mettre en forme ou Maj+Alt+F pour formater automatiquement le code SQL, JSON et d'expressions dans les éditeurs d'étapes de workflow PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Mettre en forme le code dans les éditeurs

Plusieurs éditeurs d'étapes de workflow utilisent un éditeur de code : les étapes SQL (Frame Extract SQL, Exécuter SQL à distance, Remote Direct SQL, Remote Export SQL et Importer depuis SQL), le **Result schema** (JSON) de l'étape LLM, et l'Éditeur d'expressions utilisé dans toutes les zones de flux.

Chacun de ces éditeurs dispose d'un bouton **Mettre en forme** qui reformate le code sur place, en l'indentant et en l'organisant de façon cohérente pour faciliter sa lecture et sa relecture. Vous pouvez aussi appuyer sur **Maj+Alt+F** (**Maj+Option+F** sur macOS) lorsque le curseur se trouve dans l'éditeur.

## Ce qui est formaté

- **SQL** : reformaté selon une disposition lisible sur plusieurs lignes, avec une clause par ligne, des `CASE` / `WHEN` alignés et des fonctions imbriquées éclatées. Les variables de projet et les jetons de modèle tels que `{variable}`, `{{ ... }}` et `{% ... %}` sont préservés à l'identique.
- **JSON** : réindenté avec deux espaces (par exemple, le Result schema de l'étape LLM).
- **Expressions** : les expressions PlaidCloud sont formatées selon le formatage Python standard, avec des espaces cohérents autour des opérateurs et des virgules, et des sauts de ligne pour les expressions longues.

## À savoir

- La mise en forme ne change jamais ce que fait votre code, seulement sa disposition. Les mots-clés et identifiants SQL conservent leur casse d'origine.
- Si le code ne peut pas être analysé (erreur de syntaxe), la mise en forme le laisse intact et affiche un bref message, de sorte que vous ne perdez jamais votre travail.
- Le formatage s'applique en une seule opération : appuyez sur **Ctrl+Z** (**Cmd+Z** sur macOS) pour l'annuler.
