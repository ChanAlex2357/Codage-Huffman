# Tp - Huffman

## Introduction

Codage d'information en utilisant le codage de Huffman

## 1-a Soit S = (S, P) une source d’information. Écrire un programme permettant d’avoir les codes de chaque si de S selon le codage de Huffman

- [x] creation du dictionnaire
- [x] fichier pour contenir le resultat de codage
- [x] entree de donnee (S,P)
- [x] fichier input
- [x] traitement de l'input
  - [x] premiere ligne le nombre de lettres
  - [x] 2e ligne l'ensemble de lettres (S)
  - [x] 3e ligne les probabilites (P)
- [x] POC process
- [x] Construction de l'arbre
  - [x] buildTree(S,P,m)
    - [x] T = tableau avec valeurs de P
    - [x] mergeTree(T,m)
      - [x] si taille de T == 1 on arrete => T
      - [x] sinon
        - [x] trier par ordre decroissant
        - [x] S_min = somme les 2 dernieres valeurs
        - [x] new_T de taille m-2
        - [x] transferer les valeurs T -> new T
        - [x] rT = mergeTree(new_T,m-2)
        - [x] rT.t1.code = rt.code + 1
        - [x] rT.t2.code = rt.code + 0

##
