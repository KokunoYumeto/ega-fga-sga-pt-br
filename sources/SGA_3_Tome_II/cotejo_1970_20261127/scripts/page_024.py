from audit import change
f='08_expose_viii/components/09_seccion_6_parte_2.tex'
change(f,24,'grupos \\(G\\) sobre \\(S\\) atua sobre','grupos \\(G\\) atua sobre','1970 restored','6.5(e) says G is a group prescheme acting on the S-prescheme X; it does not add sobre S after G.')
change(f,24,'subpré-esquema fechado de \\(G\\), desde que \\(X\\)','subesquema fechado de \\(G\\), desde que \\(X\\)','1970 restored','The first conclusion in 6.5(e) prints sous-schéma fermé, without pré-.')
change(f,24,'essencialmente livre sobre \\(S\\) e \\(X\\) seja separado sobre\n\\(S\\), por','essencialmente livre sobre \\(S\\) e \\(X\\) seja separado sobre\n\\(S_X\\), por','1970 restored','The invariants sentence visibly prints S with a subscript X: S_X. The 1970 reading is retained.')
change(f,24,'e tomemos o subfuntor','e consideremos o subfuntor','translation','6.5(e): et considérons le sous-foncteur.')
change(f,24,r'g(Y_T)\subseteq Z_T',r'g(Y_T)\subset Z_T','reading','The transporter condition has the simple inclusion symbol ⊂.')
change(f,24,r'''Consequentemente, se \(Y\) e
\(Z\) são essencialmente livres sobre \(S\) e fechados em \(X\), então
o transportador estrito de \(Y\) para \(Z\) é um subpré-esquema fechado de
\(G\).''',r'''Consequentemente, \textit{se \(Y\) e
\(Z\) são essencialmente livres sobre \(S\) e fechados em \(X\), então
o transportador estrito de \(Y\) para \(Z\) é um subpré-esquema fechado de
\(G\).}''','typesetting','The scan underlines this conclusion about the strict transporter, like the adjacent conclusions.')
change(f,24,r'''\emph{normalizador de \(H\) em \(G\)}, e é denotado por
\(\underline{\operatorname{Norm}}_G H\). Portanto, \textit{se \(H\) é um
subpré-esquema em grupos fechado de \(G\), essencialmente livre sobre \(S\),
então \(\underline{\operatorname{Norm}}_G H\) é representável por um
subpré-esquema em grupos fechado de \(G\).}''',r'''\emph{normalizador de \(H\) em \(G\)}; é, portanto, um subpré-esquema
em grupos fechado de \(G\) quando \(H\) é essencialmente livre sobre
\(S\) e fechado em \(G\).''','re-edition removed','The printed normalizer paragraph has no Norm_G notation and does not strengthen the hypothesis on H to a subgroup prescheme. It is one sentence continuing after the definition, without an emphasized separate assertion.')
