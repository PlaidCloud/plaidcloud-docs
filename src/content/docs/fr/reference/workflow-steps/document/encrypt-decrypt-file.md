---
title: Étape Encrypt File and Decrypt File
description: Chiffrez ou déchiffrez un fichier de documents entier avec AES ou Blowfish, ou ajoutez ou retirez le mot de passe d'un classeur Excel, dans une étape de workflow PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Description

**Document : chiffrer un fichier** chiffre un fichier d'un compte de documents et écrit le résultat dans un autre fichier. **Document : déchiffrer un fichier** fait l'inverse. Les deux étapes utilisent les mêmes paramètres. Utilisez-les pour recevoir des fichiers chiffrés d'un partenaire, les déchiffrer avant qu'une importation ne les lise, et chiffrer une exportation avant qu'elle ne parte vers un autre système.

## Fichiers

| Paramètre | Obligatoire | Rôle |
| --- | --- | --- |
| Fichier source | Oui | Le fichier à chiffrer ou à déchiffrer. |
| Fichier cible | Oui | Le fichier à écrire. Il doit être différent du fichier source, afin qu'une réexécution ne travaille jamais sur sa propre sortie. |
| Supprimer le fichier source une fois le fichier cible écrit | Non | Supprime le fichier source une fois le fichier cible écrit en toute sécurité. |

Un fichier source absent n'est pas une erreur : l'étape se termine par un avertissement indiquant le chemin, n'écrit rien, et le workflow continue. Un fichier source vide produit un fichier cible vide avec un avertissement, sauf que le chiffrement d'un fichier vide avec AES ou Blowfish écrit un véritable fichier chiffré. Un compte de documents Smartsheet ne peut pas être utilisé, car les fichiers ne peuvent pas y être relus.

## Paramètres

| Paramètre | Rôle |
| --- | --- |
| Algorithme | Dans le groupe Chiffrement : **AES-128 (clé de 16 octets)**, **AES-192 (clé de 24 octets)**, **AES-256 (clé de 32 octets)**, **Blowfish (clé de 4 à 56 octets)** ou **Mot de passe du classeur Excel**. |
| Mode | **CBC** (valeur par défaut), **ECB** ou **GCM**. Blowfish accepte uniquement CBC ou ECB. |
| Variable de clé | La variable de workflow ou de projet qui contient la clé de chiffrement, par exemple `{aes_key}`. Obligatoire pour AES et Blowfish. |
| Encodage de la clé et de l'IV | La façon dont la clé et l'IV sont écrits : **Texte (UTF-8)**, **Hexadécimal** ou **Base64**. |
| IV fixe | Le vecteur d'initialisation. Laissez-le vide et le chiffrement commence le fichier par un IV aléatoire, que le déchiffrement relit au début du fichier. Le chiffrement GCM utilise toujours un IV aléatoire ; laissez donc ce champ vide pour GCM. |
| Variable du mot de passe du classeur | La variable de workflow ou de projet qui contient le mot de passe à définir sur un classeur Excel, ou à en retirer, par exemple `{xlsx_password}`. Obligatoire pour **Mot de passe du classeur Excel**. |

CBC et ECB utilisent le bourrage PKCS7, et GCM ajoute une balise d'authentification de 16 octets après les données chiffrées. Un fichier GCM peut atteindre 256 Mo. Une clé ou un IV incorrect arrête l'étape avec une erreur et ne laisse aucun fichier partiel.

## Les clés résident dans des variables

**Variable de clé** et **Variable du mot de passe du classeur** n'acceptent qu'une référence de variable, telle que `{aes_key}`, jamais la clé ou le mot de passe lui-même : l'enregistrement d'une étape contenant autre chose est refusé. Placez le secret dans une [variable de workflow](/fr/guides/workflows/manage-workflow-variables/) ou une variable de projet, afin qu'il soit défini à un seul endroit et n'apparaisse jamais dans l'étape, ses versions, ses copies ni ce qu'un assistant IA relit. L'étape lit la valeur de la variable lors de son exécution. **IV fixe** est un champ de mot de passe : sa valeur est donc masquée dans le formulaire.

Pour les étapes qui contenaient une clé ou un mot de passe saisi avant cette règle, celui-ci a été déplacé automatiquement dans une nouvelle variable de projet, visible uniquement des Architectes, et elles font désormais référence à cette variable.

## Voir aussi

- [Étapes Document](/fr/reference/workflow-steps/document/)
- [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
