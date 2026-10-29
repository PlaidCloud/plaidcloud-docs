---
title: Créer des applications Panel avec Weave
description: Décrivez l'application souhaitée, laissez Weave l'écrire dans Panel Studio et approuvez la modification exacte avant que quoi que ce soit ne soit enregistré.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave peut écrire et modifier des applications Panel pour vous. Il travaille dans [Panel Studio](/fr/guides/panel-apps/studio/), sur l'application que vous avez ouverte, et rien de ce qu'il propose ne modifie l'application tant que vous ne l'avez pas approuvé.

## Interroger Weave

1. Ouvrez l'application dans Panel Studio.
2. Choisissez **Ask Weave** et décrivez ce que vous souhaitez, par exemple « Ajoute un filtre par région et un graphique du chiffre d'affaires par mois. »

Weave connaît déjà l'application sur laquelle il travaille : ses fichiers, son état de build et les éventuelles erreurs de build, ainsi que la table ou la vue sur laquelle elle repose. Vous n'avez pas besoin de coller du code ou des erreurs dans la conversation. Si un build échoue, demandez à Weave de le corriger.

## Approuver la modification

Lorsque Weave veut modifier le code de l'application, il affiche une carte d'approbation avec la différence complète : chaque ligne ajoutée et supprimée, fichier par fichier.

1. Lisez la différence.
2. Choisissez **Approuver** pour enregistrer la modification dans le brouillon de l'application, ou **Rejeter** pour l'abandonner.

L'approbation enregistre un brouillon. Elle ne publie pas. Prévisualisez le résultat, puis [publiez](/fr/guides/panel-apps/studio/#publier) lorsque vous en êtes satisfait.

### Approbations sur le web uniquement

Vous ne pouvez approuver une modification de code que dans PlaidCloud sur le web. Dans l'application mobile PlaidCloud, vous pouvez rejeter une modification de code proposée, mais pas l'approuver. Les autres modifications de Weave peuvent toujours être approuvées sur votre téléphone. Consultez [Weave sur mobile](/fr/guides/mobile-app/weave-on-mobile/).

## Étapes suivantes

- [Panel Studio](/fr/guides/panel-apps/studio/) : enregistrer, prévisualiser et publier.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) : les composants avec lesquels Weave construit.
