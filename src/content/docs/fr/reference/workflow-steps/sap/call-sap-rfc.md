---
title: Étape Call SAP RFC
description: Appelez des modules fonction RFC SAP depuis une étape de workflow PlaidCloud pour une intégration directe avec les systèmes SAP ECC et S/4HANA.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Description


Appelle un Remote Function Call (RFC) SAP ECC / S/4HANA et en récupère les données sous forme de tableau. Ces données sont ensuite disponibles pour les processus de transformation dans PlaidCloud.


## Destination des données

Enregistrez le résultat du RFC dans un fichier ou dans une table.

**Fichier** écrit le résultat au format **JSON**, **Séparé par des virgules**, **Séparé par des tabulations**, **Séparé par des barres verticales** ou **Parquet**. Un fichier Parquet conserve les mêmes types de colonnes qu'une table.

**Table** enregistre le résultat dans une **Table cible**, typée d'après les définitions de champs propres à la fonction RFC :

| Type de champ SAP | Enregistré comme |
|---|---|
| Date | Date. Une date vide ou initiale est enregistrée vide. Une date non valide est enregistrée vide, et l'étape se termine par un avertissement indiquant la colonne. |
| Décimal compressé | Décimal exact. Au-delà de 10 décimales ou de 28 chiffres entiers, la valeur est enregistrée sous forme de texte, et l'étape se termine par un avertissement indiquant la colonne. |
| Entier | Entier. |
| `FLOAT` | Double. |
| Flottant décimal | Texte exact. |
| `NUMC`, `CHAR` | Texte, zéros de tête conservés. |
| Heure | Texte, au format `HH:MM:SS`. |
| Octets bruts | Texte hexadécimal. |
| `UTCLONG` | Texte. |

Si SAP ne peut pas décrire les champs de la fonction, les décimaux sont enregistrés sous forme de texte exact.

Lorsque SAP décrit la fonction, chaque paramètre est converti dans le type attendu : dates en `YYYYMMDD`, heures en `HHMMSS`, entiers et décimaux en nombres, champs de texte en texte, et paramètres de structure et de table champ par champ. Une valeur qui ne peut pas être convertie en paramètre entier ou décimal fait échouer l'étape.

## Exemples


### Paramètres RFC


Sélectionnez l'agent dans Agent à utiliser. Sélectionnez le Répertoire cible dans la liste déroulante, puis parcourez l'arborescence ci-dessous pour trouver le sous-dossier de destination du fichier. Nommez ensuite correctement le « Target File Name ». Sous « Function Call Information », saisissez la fonction et le Paramètre de valeur de retour, puis sélectionnez les paramètres.

Vous pouvez choisir Insérer une ligne ou Ajouter une ligne dans la section Paramètres, nommer les paramètres et leur attribuer des valeurs. Choisissez le Nombre max. de requêtes simultanées, puis sélectionnez Wait for RFC to Complete. Enregistrez et exécutez l'étape (Enregistrer et exécuter).



### Itération avancée de valeurs


Vous pouvez sélectionner « No Iterators » en haut de cet onglet, puis Enregistrer et exécuter si vous le souhaitez, ou bien définir des itérateurs.


Ici, vous pouvez sélectionner « Specify Argument Values » pour Itérer sur des arguments, puis créer des arguments à renseigner dans Valeur d'itération.


À côté de Sélectionner l'argument d'itération dont modifier les valeurs, vous pouvez insérer une ligne, ajouter une ligne, Supprimer la ligne, la Descendre ou la Déplacer en bas.
En dessous, vous pouvez choisir des Itérateurs de plage à l'aide du même menu déroulant. La dernière section s'intitule « Exclusions for Selected Range Iteration »,
avec les mêmes options par ligne pour ajouter, supprimer, etc. Les valeurs exclues peuvent être saisies en dessous. Enregistrez et exécutez l'étape.
