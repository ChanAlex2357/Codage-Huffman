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

## Écrire un programme qui prend en paramètre un mot/texte de S et renvoie le mot/texte codé par le codage de Huffman précédent

- [x] recupere le dicrionnaire
  - [x] lire le ficher dico
  - [x] mettre dans une variable dict
- [x] recupere les donnes a code depuis un fichier
- [x] Compression
  - [x] Encodage
  - [x] sauvegarder en binaire les bit[]

## Stegannographie

- [x] Lecture d'une image avec opencv
<!-- - [ ] Lecture d'une image rgb sans utiliser de librairie -->
- [x] Decoder une image en nuance de gris (N&B)
  - [x]  fonction steg_gray_image_bytes( bitarray[] , bitPostitions[])
  - [x] recuperer les bits sur les positions doneees
  - [x] fonction steg_decode_gray_image(bitarray[],bitposittions[])
    - [x] bytes[] = steg_gray_image_bytes
    - [x] code = ''
    - [x] pour chache byte in bytes recuperer le dernier bit => code.join.each bit
  - [x] fonction steg_decode_gray_image_file(filepath,bitPositions)
    - [x] bytesarray =  Lecture du fichier
    - [x] steg_decode_gray_image
- [ ] Lecture de fichier wave sans librairie
- [ ] Decoder un son wave
  - [ ] steg_decode_wav()