"""Additional directed checks after completion of the sequential pages.

Operations are added only after root has visually reread the cited scan crop.
This history file is one-shot, like page_*.py.
"""
from audit import change
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
change(f,1,r'''Se agora tomamos como
\(S\) um grupo em \(\widehat{\mathscr C}\), que denotamos por \(G'\),''',r'''Se agora se toma como
\(S\) um grupo em \(\widehat{\mathscr C}\), que denotaremos por \(G'\),''','translation','P. 1, directed final rereading: Si maintenant on prend ... que nous noterons; preserve impersonal on and future nous noterons.')
change(f,1,r'\), podemos distinguir o subconjunto',r'\), pode-se distinguir o subconjunto','translation','P. 1: on peut distinguer, impersonal formulation confirmed on enlarged scan.')
change(f,2,r'''\operatorname{Hom}_{\mathrm{gr}}(G',D(G))\) compatível com as estruturas
de grupo de \(G'\) e \(D(G)\).''',r'''\operatorname{Hom}_{\mathrm{gr}}(G',D(G))\) formado pelos morfismos
que respeitam as estruturas de grupo de \(G'\) e \(D(G)\).''','1970 restored','P. 2 opening: formé des morphismes qui respectent les structures de groupe, not a subset itself described as compatible.')
change(f,2,'que podemos chamar de morfismos','que se poderão chamar de morfismos','translation','P. 2: qu’on pourra appeler, impersonal future.')
change(f,2,'Em outras palavras, dar um homomorfismo de grupos','Em outras palavras, «é o mesmo» dar um homomorfismo de grupos','1970 restored','P. 2: quoted il revient au même in the paraphrase after (xxx).')
change(f,2,r'''\(G'\to D(G)\) é o mesmo que dar um homomorfismo de grupos \(G\to D(G')\):
ambos equivalem a dar um acoplamento \(G\times G'\to I\).''',r'''\(G'\to D(G)\), ou um homomorfismo de grupos \(G\to D(G')\),
ambos se reduzindo de fato ao dado de um acoplamento \(G\times G'\to I\).''','1970 restored','P. 2: ou ... l’un et l’autre se ramenant en effet à la donnée d’un accouplement.')
f='08_expose_viii/components/03_seccion_2.tex'
change(f,7,'Podemos supor desde o','Pode-se supor desde o','translation','P. 7 proof 2.1(e): Donc on peut supposer déjà, impersonal.')
