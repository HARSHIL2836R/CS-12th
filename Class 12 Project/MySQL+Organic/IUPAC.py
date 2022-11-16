import pickle
f = open('datafiles/IUPAC_A.dat', 'w')
A='''
Prioty order, suffix, prefix for Functional Groups:- 
-----------------------------------------------------------------------------------------------------------------------
S.No.   | Class of Compound         | Functional Group  | Prefix            | Suffix
-----------------------------------------------------------------------------------------------------------------------
1.      | Carboxylic Acid           | -COOH             | carboxy-          | -oic acid
2.      | Sulphonic Acid            | -SO2-OH           | sulpho-           | -sulphonic acid
3.      | Acid Annhydride           | -CO-O-CO-         |         -         | -oic annhydride
4.      | Ester                     | -CO-OR            | alkoxy carbonyl-  | -oate
5.      | Acid Halides              | -CO-X             | haloformyl-       | -oyl halide
6.      | Amides                    | -CO-NH2           | carbamoyl-        | -amide
7.      | Nitriles (Cyanides)       | -CN               | cyano-            | -nitrile
8.      | Isonitriles (Isocyanides) | -NC               | isocyano-         | -isonitrile
9.      | Aldehyde                  | -CO-H (or -CHO)   | oxo-/formyl-      | -al
10.     | Ketone                    | -CO-              | oxo-/keto-        | -one
11.     | Alcohol                   | -OH               | hydroxy-          | -ol
12.     | Thiol                     | -SH               | mercepto-         | -thiol
13.     | Amines                    | -NH2              | amino-            | -amine
-----------------------------------------------------------------------------------------------------------------------
'''
pickle.dump(A, f)
f = open('datafiles/IUPAC_B.dat', 'w')
B='''
Some other Groups:-  
|-OR Alkoxy                     |= Methylidene                              |-CO-OR Alkoxy Carbonyl
|-O-CO-R Alkanoyl Oxy           |-CO-NH-R N-Alkyl Amide (or Carboxamido)    |-NH-CO-R Alkanoyl Amino
|-X Halo                        |-NO->O Nitro                               |-NO Nitroso 
'''
pickle.dump(B,f)