## Episode 1

Qui l'eu crue que je fasse une suite à cette introduction ! 

Bon, maintenant place au travail.

Je vais littéralement traiter de ton PDF dans l'ordre en essayant de sauter les paragraphes ne concernant pas les maths.

T'auras le droit à des exos perso (normalement).

Bref lançons nous dans la lecture de ce magnifique pdf :

### 1.0 Rappel d'ensembles

Comme prévu nous allons dans un premier temps faire un petit rappel sur les ensembles de nombres vu en seconde (nous sauterons les nombres complexes car ils ne seront pas utilisé dans la vidéo).

On a donc cette chaine d'inclusion suivante : $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{D}\subset\mathbb{Q}\subset\mathbb{R}$
Cette expression mathématique veut dire que chacun de ces ensembles s'inclue dans l'autre; $\mathbb{N}$ est donc dans $\mathbb{Z}$ qui est dans $\mathbb{D}$ qui est dans $\mathbb{Q}$ puis pour finir $\mathbb{R}$. Jusqu'ici tu devrais normalement le savoir.

Définissons maintenant chaque ensemble un par un :

- L'ensemble noté $\mathbb{N}$ contient les entiers naturels, c'est un ensemble constitué de tous les nombres positifs sans virgule (incluant 0), tout va bien pour le moment
- L'ensemble noté $\mathbb{Z}$ enveloppe tous les nombres relatifs, c'est à dire qu'il rajoute les nombres négatifs et contient les entiers naturels.
- C'est ici que l'on commence à corser la notation avec l'ensemble noté $\mathbb{D}$, sa définition mathématique peut sembler dur au premier regard mais devient assez simple quand on se la visualise, on a donc $\mathbb{D} = \{\dfrac{n}{10^p},n\in\mathbb{Z},p\in\mathbb{N} \}$, ce qui veut simplement dire que cet ensemble contient tous les nombres décimaux avec une écriture finie, on nous dit ici qu'un nombre quelconque dans $\mathbb{D}$ peut s'écrire avec la fraction $\dfrac{n}{10^p}$ avec $n$ un entier relatif et $p$ un entier naturel. Pour mieux comprendre cette expression, nous pouvons prendre un exemple simple. On veut vérifier si $1.75$ appartient à $\mathbb{D}$, on sait depuis la 6ème environ que ce nombre correspond à la fraction $\dfrac{175}{100}$, ce qui peut aussi s'écrire sous la forme $\dfrac{175}{10^2}$ avec donc $n=175\in\mathbb{Z}$ et $p=2\in\mathbb{N}$. $1.75$ appartient donc à $\mathbb{D}$.
- Maintenant que l'on a compris comment fonctionnait à peu près la définition $\mathbb{D}$, je vais passer à un niveau supérieur. L'ensemble $\mathbb{Q}$ est assez simple à comprendre sur le papier comme tous ses prédécesseurs. Cependant, sa définition en écriture mathématique est assez bizarre au premier oeil, mais il me semble intéressant de la comprendre pour pouvoir ensuite mieux abordé les expressions mathématiques littérales, il est donc pas essentiel pour toi de retenir ses définitions mais au moins d'en comprendre le sens pour pouvoir utiliser correctement le bonne ensemble dans tes exos. L'ensemble des nombres rationnels se note $\mathbb{Q} =\{\left.{\dfrac {m}{n}}\right|(m,n)\in\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})\}$. Sa définition veut simplement dire qu'un nombre rationnel est un nombre pouvant s'écrire sous la forme de n'importe quelle fraction $\dfrac{m}{n}$ avec $m$ un entier relatif et $n$ un entier relatif non nul, en effet, on annonce $(m,n)$ sous forme d'un couple appartenant à $\mathbb{Z}^2$, car lorsqu'on veut annonce annoncer un couple, un triplet, ou un certains nombres de lettres, on peut élever la puissance de l'ensemble dans lequel on les mets. Imagine que $(m,n)$ serait alors des coordonnées avec $m$ l'axe des abscises et $n$ l'axe des ordonnées, ce qui nous place dans un espace de dimension $2$, d'où le $\mathbb{Z}^2$. Cependant, ici dans notre définition, $n$ ne doit pas être égale à $0$ car on ne divise jamais par $0$, on se place donc dans $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$ (ce qui est exactement la même chose, mais en précisant que la deuxième valeur du couple est différente). Et si je ne t'ai pas perdu avec cette définition je serais extrêmement fier, malheureusement y'a pas mal de chances que ça t'ai confus plus qu'autre chose donc je vais juste me contenter de conclure en disant qu'un nombre dans $\mathbb{Q}$ peut s'écrire sous la forme de n'importe quelle fraction qui ne divise pas par 0 (ce qui est différent du nombre décimal qui doit forcément diviser par une puissance de 10), on peut alors dire que $\dfrac{1}{3}$ ou $\dfrac{25}{7}$ par exemple sont des nombres rationnels.
- Et pour être honnête, après avoir compris cette définition, tu as sûrement fait l'un des trucs les plus durs de cette vidéo, la définition d'un réel $\mathbb{R}$ est en soit trop compliqué et/ou trop longue qu'on ne peut pas la définir direct avec une expression mathématique (en tout cas c'est loin de notre niveau). On va donc ce contenter de dire que $\mathbb{R}$ englobe tous les nombres rationnels et irrationnels, ce qui veut dire que l'on peut ajouter les constantes avec un développement chaotique comme $\pi, e, \ln, \cos(\dfrac{\pi}{4}), \sqrt{2}$, et pleins d'autres. En gros, quand on se place dans les nombres réels, on peut tout utiliser (sauf les complexes et les nombres au dessus encore que tu ne verras surement jamais de ta vie à part si tu t'interesses au maths un peu plus avancé) !

Passons maintenant à ton cours pour de bon.
### 1.1. Définition

On t'introduit principalement l'utilisation de l'analyse mathématiques en ECO. On explique notamment l'importance de l'étude macroscopique et microscopique. C'est alors ici que l'on comprends que le but va être de comprendre des phénomènes d'éco avec des liens de causalités et de corrélations, BREF !

Après le tableau de l'INSEE ; suit directement une formule assez simple permettant de calculer le revenu rapportés grâce à une quantité de biens acheter.

On pose alors $q1$ et $q2$ la quantité de deux types de biens (comme une petite voiture en plastique par exemple), et $p1$, $p2$ leur prix respectif. (préciser les ensembles)

On en conclut alors que le revenu nommé grand $R = q1p1 + q2p2$ (en effet on multiplie chaque biens par leur prix, on les additionne et on obtient directement le total payé)

Jusqu'ici on devrait à peu près se comprendre. On définie ensuite simplement la notion de fonction, j'espère que tu la connais bien parce qu'elle va être utilisé tout le chapitre. Au cas où je vais juste te résumer qu'une fonction exprime une quantité en fonction d'autres quantités mais ça s'est exactement ce que ton cours dit donc passons.

Il est précisé que le premier semestre se contentera des réels, ce qui peut aussi potentiellement dire que les prochains pourront se pencher sur les complexes, ça tombe bien je les travaille en ce moment en maths expertes même si on n'est pas encore aux prochains semestres.

### 1.2. Définitions

C'est en réalité maintenant que l'on se corse un peu. Le vif du chapitre, c'est très peu dur car c'est en soit de la troisième reformulé mais si l'on ne comprends pas instantanément on est très vite laxiste.
On te pose la définition suivante que l'on va décortiquer :

Soient $A$ et $B$ deux ensembles quelconques. On appelle **fonction** $f$ de l'ensemble $A$ vers $B$ toute relation qui à chaque élément de $A$ associe au plus un élément de $B$.
$A$ est donc l'ensemble de départ et $B$ l'ensemble d'arrivée.

Vulgairement, les fonctions que l'on utilise depuis le collège, sont par définition la transformation d'un élément de l'ensemble de départ en celui d'arrivée, concrètement, on a pour tout élément de $A$ au maximum $1$ élément de $B$ associer par la fonction $f$.

