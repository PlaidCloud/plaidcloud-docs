---
title: Convert Document Encoding to UTF-8
description: "Convertissez l'encodage d'un fichier de document en UTF-8 dans une étape de workflow PlaidCloud pour une large compatibilité avec les systèmes et applications modernes."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## Description

Réécrit un fichier texte en UTF-8. C'est particulièrement utile lorsque la source d'information mélange plusieurs encodages ou que d'autres outils ne prennent pas en charge certains encodages.

## Fonctionnement

- L'encodage de la source est détecté. Un fichier UTF-8 est lu en UTF-8, et les caractères Windows qui y ont été collés (par exemple les guillemets typographiques de Word ou d'Excel) sont conservés intacts, quel qu'en soit le nombre. Un fichier dans un autre encodage est lu dans l'encodage détecté à partir de sa première partie qui n'est pas du UTF-8 valide.
- Le texte est écrit tel quel : les lettres accentuées, les symboles et les autres caractères sont conservés exactement comme ils étaient.
- Un fichier dont l'encodage ne peut pas être détecté fait échouer l'étape, en nommant le fichier.
- Si le chemin d'entrée n'existe pas ou ne contient aucun fichier, l'étape se termine avec un avertissement qui nomme le chemin et ne traite rien, et le workflow se poursuit.
- Pour un dossier, chaque fichier est converti et écrit dans la destination sous son propre nom. Cochez **Conserver les sous-dossiers** pour écrire à la place un fichier d'un sous-dossier dans le sous-dossier correspondant de la destination ; le contenu d'un fichier compressé va alors dans le sous-dossier où se trouvait le fichier compressé.
- Si deux fichiers devaient être écrits au même endroit dans la destination, l'étape échoue avant d'écrire le second, au lieu de laisser celui-ci remplacer le premier. Le message nomme les deux fichiers, ou le fichier compressé dont ils proviennent tous deux, ainsi que l'emplacement ; si cocher **Conserver les sous-dossiers** les écrirait à des endroits distincts, il le précise.

## Exemples

Sélectionnez le fichier d'entrée et parcourez l'emplacement pour le trouver. Sélectionnez l'emplacement de sortie voulu, puis parcourez-le pour choisir l'emplacement du fichier. Enregistrez et exécutez.
