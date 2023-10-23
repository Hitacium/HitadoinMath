# Lycée

## Organisation

- Cours "magistraux" (Leçon)
- Cours "interactifs" (Exercices et construction du cours) 

## Première

### Thème 1 : Algèbre

#### Chapitre 1 : Suites numériques, modèle discret

##### Prérequis

- Formalités de calculs (priorités des opérations, factorisation, développement, équations, inéquations)
- Notions de calcul littéral

###### Notions de seconde

- Notion de fonction
- Notion d'objet mathématique (variable, constante, nombre)
- Notion d'entier naturel dans $\mathbb{N}$
- Notion de réel dans $\mathbb{R}$

##### Notion abordées

- Définitions des suites ($u_n = f(n)$)
- Suites définies par récurrence ($u_{n+1} = f(u_n)$)
- Suites arithmétiques ($u_{n+1} = u_n + r$ ou $u_n = u_0 + nr$)
- Suites géométriques ($u_{n+1} = u_n \times q$ ou $u_n = u_0 \times q^n$)
- Variations d'une suite (croissante, décroissante, constante)
- Monotonie d'une suite (croissante, décroissante)
- Sommes des n premiers entiers naturels : $(\sum_{k=0}^n k = \frac{n(n+1)}{2})$
- Sommes de termes consécutifs d'une suite arithmétique ou géométrique : 
$S_n = (n+1)\frac{(u_0 + u_n)}{2}$ ou $S_n = u_0\frac{(1-q^{n+1})}{1-q}$
- Démonstrations des formules de somme
- Remboursement d’un emprunt par annuités constantes

##### Compléments

- Suites arithmético-géométriques
- Suite de Fibonacci
- Tours de Hanoï
- Suite de Syracuse
- Château de cartes
- Sensibilisation à l’idée de limite (sans formalisme)

#### Chapitre 2 : Équations, fonctions polynômes du second degré

##### Prérequis

- Formalités de calculs (priorités des opérations, factorisation, développement, équations du premier degré, inéquations)
- Notions de calcul littéral   

###### Notions de seconde

- Notion de fonction
- Notion d'objet mathématique (variable, constante, nombre)
- Notion d'identités remarquables :
$(a+b)^2 = a^2 + 2ab + b^2$, 
$(a-b)^2 = a^2 - 2ab + b^2$, 
$(a+b)(a-b) = a^2 - b^2$
- Equation du premier degré $(ax + b = 0)$ 
- Système d'équations du premier degré à deux inconnues $\begin{cases} ax + by = c \\ dx + ey = f \end{cases}$

##### Notion abordées

- Équations et inéquations du second degré $(ax^2 + bx + c = 0)$
    - Résolution graphique d'une équation du second degré
    - Résolution algébrique d'une équation du second degré
        - Discriminant d'une équation du second degré $(\Delta = b^2 - 4ac)$
        - Racines d'une équation du second degré 
        $x_1 = \frac{-b - \sqrt{\Delta}}{2a}$ et $x_2 = \frac{-b + \sqrt{\Delta}}{2a}$
        - Racines évidentes d'une équation du second degré
        - Somme et produit des racines d'une équation du second degré 
        $(x_1 + x_2 = -\frac{b}{a}$ et $x_1 \times x_2 = \frac{c}{a})$
- Fonctions polynômes du second degré $(f(x) = ax^2 + bx + c)$
    - Forme canonique d'une fonction polynôme du second degré $(f(x) = a(x - \alpha)^2 + \beta)$
    - Forme factorisée d'une fonction polynôme du second degré $(f(x) = a(x - x_1)(x - x_2))$
    - Sommet d'une fonction polynôme du second degré $(S(\alpha, \beta)$ avec $\alpha = -\frac{b}{2a}$ et $\beta = f(\alpha))$
    - Signe d'une fonction polynôme du second degré
    - Tableau de signe d'une fonction polynôme du second degré
    - Méthode de complétion du carré $(ax^2 + bx + c = a(x + \frac{b}{2a})^2 + c - \frac{b^2}{4a})$
- Démonstrations du discriminant et des racines d'une équation du second degré

##### Compléments

- Équations du quatrième degré avec changement de variable (équations bicarrées)
- Optimisation de fonctions polynômes du second degré (fonction affine)
- Factorisation d’un polynôme du troisième degré admettant une racine et résolution de
l’équation associée $(P(x) = (x - \alpha)(ax^2 + bx + c))$
- Factorisation de $x^n - 1$ par $x - 1$, de $x^n - a^n$ par $x - a$ (avec $a \in \mathbb{R}$)
- Déterminer deux nombres réels dont la somme et le produit sont les racines de la fonction polynôme $f(x) = x^2 - Sx + P$

### Thème 2 : Analyse

#### Chapitre 1 : Dérivation

##### Prérequis

- Formalités de calculs (priorités des opérations, factorisation, développement, équations)
- Notions de calcul littéral

###### Notions de seconde

- Notion de fonction
- Notion d'objet mathématique (variable, constante, nombre)
- Facultatif car vu dans le chapitre : taux de variation d'une fonction $(\frac{f(x_2) - f(x_1)}{x_2 - x_1})$

##### Notions abordées

###### Partie 1 : Dérivation Locale

- Taux d’accroissement moyen : $\frac{f(x_2) - f(x_1)}{x_2 - x_1}$
- Nombre dérivé d'une fonction en un point $a$
    - Notation $f'(a)$
    - $\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$
- Equation de la tangente en un point d'abscisse $a$ : $y = f'(a)(x - a) + f(a)$ 

###### Partie 2 : Dérivation Globale

- Dérivée d'une fonction $f$ sur un intervalle $I$ : $f'(x)$
- Fonctions dérivées usuelles : constantes, puissances, $\sin(x)$ et $\cos(x)$
- Opérations sur les fonctions dérivées : somme, produit, quotient, composition $g(ax + b)$
- Fonction valeur absolue $|x|$ : étude de la dérivée
- Démonstations
    - Equation de la tangente en un point à une courbe représentative
    - La fonction racine carrée n'est pas dérivable en 0
    - Fonction dérivée de la fonction carrée, de la fonction inverse
    - Fonction dérivée d'un produit de fonction

###### Partie 3 : Dérivation et variations

- Lien entre dérivée et variations d'une fonction sur un intervalle $I$
- Tableau de variations d'une fonction $f$ sur un intervalle $I$ à partir de sa dérivée $f'$
- Problèmes d'optimisation : recherche de maximum, minimum $\rightarrow$ extremum local $(f'(x) = 0)$

##### Compléments

- Composition de fonctions $f(g(x))$
- Dérivée d'une fonction composée $(f \circ g)'(x) = f'(g(x)) \times g'(x)$

#### Chapitre 2 : Fonction exponentielle

##### Prérequis

- Formalités de calculs (priorités des opérations, factorisation, développement, équations)
- Notions de calcul littéral
- Propriétés des puissances $(a^x \times a^y = a^{x+y}\text{ , etc.})$
- Dérivation

###### Notions de seconde

- Notion de fonction
- Notion d'objet mathématique (variable, constante, nombre)

##### Notions abordées

- Définition de la fonction exponentielle comme fonction vérifiant $f'(x) = f(x)$ et $f(0) = 1$
    - Existence et unicité de la fonction exponentielle admise
    - Notation $\exp(x)$ et $e^x$
- Dérivée de la fonction exponentielle $(\exp'(x) = \exp(x))$
- Propriété de la fonction exponentielle 
    - $\exp(x+y) = \exp(x) \times \exp(y)$
    - $\exp(x-y) = \frac{\exp(x)}{\exp(y)}$
    - $\exp(x)^y = \exp(xy)$
    - $\exp(x) > 0$
- Pour tout $a$ réel, la suite $(u_n = e^{na})$ est une suite géométrique de raison $e$
- Variation de la fonction exponentielle
- Dérivation de la fonction exponentielle composée $(\exp(ax + b) = a\exp(ax + b))$

##### Compléments

- Démonstration de l'existence et de l'unicité de la fonction exponentielle
- Démonstration des propriétés de la fonction exponentielle
- Monotonie de la fonction exponentielle (équatiosn et inéquations)

#### Chapitre 3 : Fonction trigonométriques

##### Prérequis

- Formalités de calculs (équations)
- Notions de calcul littéral
- Trigonométrie de collège

###### Notions de seconde

- Notion de fonction
- Notion d'objet mathématique (variable, constante, nombre)

##### Notions abordées

- Cercle trigonométrique et angles orientés (radian)
- Valeur remarquable de $\sin(x)$ et $\cos(x)$
- Définition des fonctions trigonométriques $\sin(x)$ et $\cos(x)$, pariété, périodicité
- Démonstration des calculs de $\sin(\frac{\pi}{4})$, $\cos(\frac{\pi}{3})$, $\sin(\frac{\pi}{3})$

##### Compléments

- Démonstration des propriétés de la fonction cosinus et sinus $(\sin^2(x) + \cos^2(x) = 1)$
- Fonction tangente $\tan(x) = \frac{\sin(x)}{\cos(x)}$

### Thème 3 : Géométrie

#### Chapitre 1 : Calcul vectoriel et produit scalaire

##### Prérequis

- Notions de calcul littéral
- Notions de géométrie de collège
- Notions de trigonométrie de collège

###### Notions de seconde

- Notion de vecteur dans un plan (colinéarité, norme, relation de Chasles)
- Plan orthonormé

##### Notions abordées

- Produit scalaire à partir de la projection orthogonale et de la formule avec cosinus
    - Notation $\vec{u} \cdot \vec{v}$
    - $\vec{u} \cdot \vec{v} = ||\vec{u}|| \times ||\vec{v}|| \times \cos(\vec{u}, \vec{v})$
- Bilinearité du produit scalaire et symétrie. Expression du produit scalaire dans une base orthonormée
    - $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$
    - $\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$
    - $(\lambda \vec{u}) \cdot \vec{v} = \lambda (\vec{u} \cdot \vec{v})$
    - $\vec{u} \cdot \vec{u} = ||\vec{u}||^2$
    - $\vec{u} \cdot \vec{v} = u_xv_x + u_yv_y$
- Orthogonalité de deux vecteurs $\vec{u}$ et $\vec{v}$ : $\vec{u} \cdot \vec{v} = 0$
- Développement de $||\vec{u} + \vec{v}||^2$ et $||\vec{u} - \vec{v}||^2$
- Loi des cosinus, formule d'Al-Kashi $a^2 = b^2 + c^2 - 2bc\cos(\alpha)$
- Transformation de l'expression de $\overrightarrow{MA} \cdot \overrightarrow{MB}$

##### Compléments

- Loi des sinus
- Droite d'Euler d'un triangle (médiane, hauteur, bissectrice)
- Les médianes d'un triangle sont concourantes en un point appelé centre de gravité 

#### Chapitre 2 : Géométrie repérée

##### Prérequis

- Notions de calcul littéral
- Notions de géométrie de collège
- Polynomes du second degré

###### Notions de seconde

- Notion de vecteur dans un plan (colinéarité, norme, relation de Chasles)
- Plan orthonormé
- Recommandé : quelques bases sur les équations cartésienne de droite $(ax + by + c = 0)$

##### Notions abordées

- Equation cartésienne d'une droite $(ax + by + c = 0)$
- Equation cartésienne d'un cercle $(x - a)^2 + (y - b)^2 = r^2$
- Symétrie et sommet d'équation cartésienne d'une parabole $(y = ax^2 + bx + c)$
- Vecteur directeur d'une droite $(-b, a)$ et vecteur normal $(a, b)$

##### Compléments

- L’ensemble des points équidistants de l’axe des abscisses et d’un point
donné
- Intersection d’un cercle ou d’une parabole $y = ax^2 + bx + c$ avec une droite parallèle à un axe

### Thème 4 : Probabilités et statistiques

#### Chapitre 1 : Probabilités conditionnelles et indépendance

##### Prérequis

- Notions de calcul littéral
- Notions de probabilités de collège

###### Notions de seconde

- Notion de probabilités et de statistiques (événements, probabilités, fréquences, moyenne, médiane, quartiles, écart-type)

##### Notions abordées

- Probabilité conditionnelle de B sachant A, noté $P(B|A)$ ou $P_B(A)$ : $P(B|A) = \frac{P(A \cap B)}{P(A)}$
- Arbre pondéré, tableau et calcul de probabilités
    - Probabilité de l'événement contraire $\overline{A}$ : $P(\overline{A}) = 1 - P(A)$
    - Probabilité de l'événement intersection/union 
        - $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
        - $P(A \cap B) = P(A) \times P(B|A) = P(B) \times P(A|B)$
- Indépendance de deux événements $A$ et $B$ et succession de deux épreuves indépendantes : $P(A \cap B) = P(A) \times P(B)$
- Partition de l'univers et probabilité totale : $P(A) = \sum_{i=1}^n P(A \cap B_i)$

##### Compléments

- Approximation de $\pi$ ou de l'aire sous la parabole par la méthode de Monte-Carlo
- QCM type bac

#### Chapitre 2 : Variables aléatoires réelles

##### Prérequis similaires à celui du chapitre 1

##### Notions abordées

- Variable aléatoire réelle $X$ : $X(\Omega) = \{x_1, x_2, ..., x_n\}$
- Loi de probabilité d'une variable aléatoire réelle $X$ : $P(X = x_i)$
- Espérance d'une variable aléatoire réelle $X$ : $E(X) = \sum_{i=1}^n x_i \times P(X = x_i)$
- Variance d'une variable aléatoire réelle $X$ : $V(X) = E((X - E(X))^2)$
- Ecart-type d'une variable aléatoire réelle $X$ : $\sigma(X) = \sqrt{V(X)}$

##### Compléments

- Formule de König-Huygens : $V(X) = E(X^2) - E(X)^2$
- Etude de la fonction du second degré $x \mapsto E((X - x)^2)$

## Terminale