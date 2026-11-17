---
title: Convert Document Encoding
description: "Convertissez l'encodage d'un fichier de document d'un jeu de caractères à un autre dans une étape de workflow PlaidCloud pour résoudre les problèmes de compatibilité d'encodage."
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Description



Réencode un fichier texte d'un encodage de caractères à un autre. Utile lorsque les fichiers source arrivent dans des encodages hérités (Windows-1252, ISO-8859-1) alors que les outils en aval ont besoin d'UTF-8, ou inversement.

Lorsque le fichier source n'est pas en UTF-8, son encodage est déduit du contenu du fichier. Un fichier très court ou très répétitif fournit trop peu d'éléments et peut être mal lu ; vérifiez donc la sortie convertie d'un tel fichier.

Un caractère que l'encodage cible ne peut pas représenter fait échouer l'étape par défaut. Sélectionnez **Remplacer par ? les caractères que l'encodage cible ne peut pas représenter** pour écrire un `?` à sa place, comme le fait un writer Java, et l'étape se termine.

Un fichier compressé est d'abord décompressé, et chaque fichier qu'il contient est converti. Pour un dossier, chaque fichier est écrit dans la destination sous son propre nom. Cochez **Conserver les sous-dossiers** pour écrire à la place un fichier d'un sous-dossier dans le sous-dossier correspondant de la destination ; le contenu d'un fichier compressé va alors dans le sous-dossier où se trouvait le fichier compressé. Si deux fichiers devaient être écrits au même endroit, l'étape échoue avant d'écrire le second, au lieu de laisser celui-ci remplacer le premier, et indique si cocher **Conserver les sous-dossiers** permettrait de les séparer.

Choisissez l'encodage cible dans la configuration de l'étape. Pour les raccourcis vers des encodages précis, consultez les variantes [UTF-8](/fr/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/fr/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) et [ASCII](/fr/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Exemples


Créez une entrée source, sélectionnez le fichier d'entrée et parcourez l'emplacement pour le trouver. Sélectionnez l'emplacement de sortie voulu et parcourez-le pour choisir l'emplacement du fichier. Enregistrez et exécutez.
