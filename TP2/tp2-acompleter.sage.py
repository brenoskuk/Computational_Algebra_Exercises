

# This file was *autogenerated* from the file tp2-acompleter.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_735 = Integer(735); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_397 = Integer(397); _sage_const_1275 = Integer(1275); _sage_const_156 = Integer(156); _sage_const_423 = Integer(423); _sage_const_1485 = Integer(1485); _sage_const_352 = Integer(352); _sage_const_12 = Integer(12); _sage_const_1470 = Integer(1470); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_18 = Integer(18); _sage_const_128 = Integer(128); _sage_const_146 = Integer(146); _sage_const_630 = Integer(630)
print("""\
# *************************************************************************** #
# *************************************************************************** #
# TP2 : ALGEBRE LINEAIRE SUR UN ANNEAU PRINCIPAL                              #
# *************************************************************************** #
# *************************************************************************** #
""")

# CONSIGNES
#
# Les seules lignes a modifier sont annoncee par "Code pour l'exercice"
# indique en commmentaire et son signalees
# Ne changez pas le nom des variables
#
# CONSEILS
#
# Ce modele vous sert a restituer votre travail. Il est deconseille d'ecrire
# une longue suite d'instruction et de debugger ensuite. Il vaut mieux tester
# le code que vous produisez ligne apres ligne, afficher les resultats et
# controler que les objets que vous definissez sont bien ceux que vous attendez.
#
# Vous devez verifier votre code en le testant, y compris par des exemples que
# vous aurez fabrique vous-meme.
#


reset()
print("""\
# ****************************************************************************
# MISE SOUS FORME NORMALE D'HERMITE
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

A = matrix(ZZ,[
        [-_sage_const_2 ,  _sage_const_3 ,  _sage_const_3 ,  _sage_const_1 ],
        [ _sage_const_2 , -_sage_const_1 ,  _sage_const_1 , -_sage_const_3 ],
        [-_sage_const_4 ,  _sage_const_0 , -_sage_const_1 , -_sage_const_4 ]])

A1 = random_matrix(ZZ, _sage_const_7 , _sage_const_8 , algorithm='echelonizable', rank=_sage_const_3 )

# Code pour l'EXERCICE

def MyHNF(A):
    """
    Forme normale d'Hermite selon votre code
    """
    m = A.nrows()
    n = A.ncols()
    H = copy(A)
    U = identity_matrix(n)
    # ECRIVEZ VOTRE CODE ICI
    assert(H-A*U==_sage_const_0 )
    return H,U

def SageHNF(A):
    """
    Forme normale d'Hermite de SAGE avec la convention francaise :
    Les vecteurs sont ecrits en colonne.
    """
    m = A.nrows()
    n = A.ncols()
    Mm = identity_matrix(ZZ,m)[::-_sage_const_1 ,:]
    Mn = identity_matrix(ZZ,n)[::-_sage_const_1 ,:]
    AA = (Mm*A).transpose()
    HH, UU = AA.hermite_form(transformation=True)
    H = (HH*Mm).transpose()*Mn
    U = UU.transpose()*Mn
    assert(H-A*U==_sage_const_0 )
    return H,U

H,  U  = MyHNF(A)
HH, UU = SageHNF(A)

test = False # Test a ecrire

# # Affichage des resultats

print "\n$ Question 4"
print "La matrice A = "
print A
print "a pour forme normale d'Hermite H="
print H
print "et matrice de transformation U="
print U
print "\n$ Question 5"
print "D'apres SageMath, la matrice A a pour forme normale d'Hermite H="
print HH
print "et matrice de transformation U="
print UU
print "\n$ Question 6"
print "Les deux fonctions coincident-elles sur une centaine d'exemples ?"
print test

reset()
print("""\
# ****************************************************************************
# MISE SOUS FORME NORMALE DE SMITH
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

X1 = matrix(ZZ,_sage_const_2 ,_sage_const_3 ,[
        [_sage_const_4 , _sage_const_7 , _sage_const_2 ],
        [_sage_const_2 , _sage_const_4 , _sage_const_6 ]])

X2 = matrix(ZZ,_sage_const_3 ,_sage_const_3 ,[
        [-_sage_const_397 , _sage_const_423 , _sage_const_352 ],
        [   _sage_const_2 ,  -_sage_const_3 ,   _sage_const_1 ],
        [-_sage_const_146 , _sage_const_156 , _sage_const_128 ],
])

PolQ = PolynomialRing(QQ, names=('xQ',)); (xQ,) = PolQ._first_ngens(1)
AQ = matrix(PolQ,_sage_const_3 ,[
            [xQ + _sage_const_1 ,  _sage_const_2 ,     -_sage_const_6 ],
            [     _sage_const_1 , xQ,     -_sage_const_3 ],
            [     _sage_const_1 ,  _sage_const_1 , xQ - _sage_const_4 ]])
Pol2 = PolynomialRing(FiniteField(_sage_const_2 ), names=('x2',)); (x2,) = Pol2._first_ngens(1)
AF2 = matrix(Pol2,_sage_const_3 ,[
            [x2 + _sage_const_1 ,  _sage_const_2 ,     -_sage_const_6 ],
            [     _sage_const_1 , x2,     -_sage_const_3 ],
            [     _sage_const_1 ,  _sage_const_1 , x2 - _sage_const_4 ]])
Pol3 = PolynomialRing(FiniteField(_sage_const_3 ), names=('x3',)); (x3,) = Pol3._first_ngens(1)
AF3 = matrix(Pol3,_sage_const_3 ,[
            [x3 + _sage_const_1 ,  _sage_const_2 ,     -_sage_const_6 ],
            [     _sage_const_1 , x3,     -_sage_const_3 ],
            [     _sage_const_1 ,  _sage_const_1 , x3 - _sage_const_4 ]])
Pol5 = PolynomialRing(FiniteField(_sage_const_5 ), names=('x5',)); (x5,) = Pol5._first_ngens(1)
AF5 = matrix(Pol5,_sage_const_3 ,[
            [x5 + _sage_const_1 ,  _sage_const_2 ,     -_sage_const_6 ],
            [     _sage_const_1 , x5,     -_sage_const_3 ],
            [     _sage_const_1 ,  _sage_const_1 , x5 - _sage_const_4 ]])

# Code pour l'EXERCICE

def MySNF(A):
    """
    Forme normale de Smith selon votre code
    """
    m = A.nrows()
    n = A.ncols()
    H = copy(A)
    L = identity_matrix(m)
    U = identity_matrix(n)
    # ECRIVEZ VOTRE CODE ICI
    assert(H-L*A*U==_sage_const_0 )
    return H,L,U

H1, L1, U1 = MySNF(X1)
H2, L2, U2 = MySNF(X2)

HQ, _, _ = MySNF(AQ)
HF2, _, _ = MySNF(AF2)
HF3, _, _ = MySNF(AF3)
HF5, _, _ = MySNF(AF5)

test = False # Test a ecrire

# # Affichage des resultats

print "\n$ Question 4"
print "La matrice X1 = "
print X1
print "a pour forme normale de Smith H1="
print H1
print "et matrice de transformation L1="
print L1
print "et matrice de transformation U1="
print U1
print "La matrice X2 = "
print X2
print "a pour forme normale de Smith H2="
print H2
print "et matrice de transformation L2="
print L2
print "et matrice de transformation U2="
print U2

print "\n$ Question 5"
print "La forme normale de Smith sur Q est "
print AQ
print "La forme normale de Smith sur F2 est "
print AF2
print "La forme normale de Smith sur F3 est "
print AF3
print "La forme normale de Smith sur F5 est "
print AF5

print "\n$ Question 6"
print "Votre fonction coincide avec celle de Sage ?"
print test


reset()
print("""\
# ****************************************************************************
# RESOLUTION DE SYSTEME LINEAIRE HOMOGENE
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

X = matrix(ZZ,[
      [ -_sage_const_2 ,  _sage_const_3 ,  _sage_const_3 ,  _sage_const_1 ],
      [  _sage_const_2 , -_sage_const_1 ,  _sage_const_1 , -_sage_const_3 ],
      [ -_sage_const_4 ,  _sage_const_0 , -_sage_const_1 , -_sage_const_4 ]])

# Code pour l'EXERCICE

L =[] # liste des vecteurs d'une base

# # Affichage des resultats

print "Le systeme a pour racine le module engendre par"
print L

reset()
print("""\
# ****************************************************************************
# IMAGE D'UNE MATRICE
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

A  = matrix(ZZ, [
           [ _sage_const_15 ,  _sage_const_8 , -_sage_const_9 , _sage_const_23 ,  -_sage_const_9 ],
           [ _sage_const_22 , _sage_const_22 ,  _sage_const_7 , -_sage_const_8 ,  _sage_const_20 ],
           [ _sage_const_21 , _sage_const_18 , -_sage_const_1 , -_sage_const_7 ,  -_sage_const_3 ],
           [  _sage_const_3 , -_sage_const_1 ,  _sage_const_0 , _sage_const_12 , -_sage_const_16 ]])


# Code pour l'EXERCICE

test = false # test a ecrire

# # Affichage des resultats

print "L'image de"
print A
print "est-elle egale a ZZ^4 ?"
print test



reset()
print("""\
# ****************************************************************************
# RESOLUTION DE SYSTEME LINEAIRE NON-HOMOGENE
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

X1 = matrix(ZZ,[
           [ -_sage_const_6 ,  _sage_const_12 ,  _sage_const_6 ],
           [ _sage_const_12 , -_sage_const_16 , -_sage_const_2 ],
           [ _sage_const_12 , -_sage_const_16 , -_sage_const_2 ]])

b1 = vector(ZZ,[ -_sage_const_6 , _sage_const_4 , _sage_const_4 ])

PolF5 = PolynomialRing(GF(_sage_const_5 ), names=('x',)); (x,) = PolF5._first_ngens(1)

X2 = matrix(PolF5,[
           [ x + _sage_const_1 , _sage_const_2 ,     _sage_const_4 ],
           [     _sage_const_1 , x,     _sage_const_2 ],
           [     _sage_const_1 , _sage_const_1 , x + _sage_const_1 ]])

b2 = vector(PolF5,[ _sage_const_3 *x+_sage_const_2 , _sage_const_0 , -_sage_const_1 ])

# Code pour l'EXERCICE

z1 = vector(ZZ,_sage_const_3 )
H1 = []

z2 = vector(PolF5,_sage_const_3 )
H2 = []

z3 = vector(ZZ,_sage_const_3 )
H3 = []

# # Affichage des resultats

print "Une solution particuliere de X1*z1 = b1 est"
print z1
print "les solutions du systeme homogene sont engendres par"
print H1
print "Une solution particuliere de X2*z2 = b2 est"
print z2
print "les solutions du systeme homogene sont engendrees par"
print H2
print "Une solution particuliere du systeme 3 est"
print z3
print "les solutions du systeme homogene sont engendres par"
print H3



reset()
print("""\
# ****************************************************************************
# STRUCTURE DU QUOTIENT
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

A = matrix(ZZ,[
              [ -_sage_const_630 ,   _sage_const_735 ,   _sage_const_0 ,   _sage_const_735 , -_sage_const_630 ],
              [ _sage_const_1275 , -_sage_const_1485 , -_sage_const_15 , -_sage_const_1470 , _sage_const_1275 ],
              [  _sage_const_630 ,  -_sage_const_630 ,   _sage_const_0 ,  -_sage_const_630 ,  _sage_const_630 ]])

# Code pour l'EXERCICE

reponse = "A ecrire"

# # Affichage des resultats

print "La structure de Z^3/N est"
print reponse

reset()
print("""\
# ****************************************************************************
# FACTEURS INVARIANTS
# ****************************************************************************
""")

# Donnees de l'enonce de l'exercice

A = matrix(ZZ,[
              [ -_sage_const_630 ,   _sage_const_735 ,   _sage_const_0 ,   _sage_const_735 , -_sage_const_630 ],
              [ _sage_const_1275 , -_sage_const_1485 , -_sage_const_15 , -_sage_const_1470 , _sage_const_1275 ],
              [  _sage_const_630 ,  -_sage_const_630 ,   _sage_const_0 ,  -_sage_const_630 ,  _sage_const_630 ]])


# Code pour l'EXERCICE

rang = -_sage_const_1  
fact_inv = []
reponse = "A ecrire"

# # Affichage des resultats

print "Le rang de Z^3 / N est"
print rang
print "Les facteurs invariants sont"
print fact_inv
print "Exposants ?"
print reponse


