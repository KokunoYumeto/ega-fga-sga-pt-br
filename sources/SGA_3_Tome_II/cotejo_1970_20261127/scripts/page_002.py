from audit import *
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
change(f,2,'formado pelos morfismos que são multiplicativos em relação a cada um dos\ndois argumentos, que podemos chamar de \\emph{morfismos bilineares de\n\\(G\\times G\'\\) em \\(I\\)}, ou \\emph{acoplamentos de \\(G\\) e \\(G\'\\) com\nvalores em \\(I\\)}.', 'formado pelos morfismos que são multiplicativos em relação ao primeiro\n\\emph{e} em relação ao segundo argumento, que podemos chamar de morfismos\nbilineares de \\(G\\times G\'\\) em \\(I\\), ou acoplamentos de \\(G\\) e \\(G\'\\)\ncom valores em \\(I\\).','translation','P. 2, primeiro parágrafo: restaurada a distinção primeiro e segundo argumento e a ênfase apenas na conjunção.')
change(f,2,'Obtém-se então um homomorfismo canônico','Obtém-se então um \\emph{homomorfismo canônico}','typesetting','P. 2: homomorphisme canonique está sublinhado.')
block(f,2,'\\medskip\n\\noindent\\SGARefTarget{sga3:viii:definition:1:0}', '\\medskip\n\\noindent\\SGARefTarget{sga3:viii:definition:1:0:2}',r'''\SGARefTarget{sga3:viii:definition:1:0}
Diz-se que \(G\) é \emph{reflexivo} (relativamente a \(I\)) se o
homomorfismo anterior é um isomorfismo. Observe-se que isso implica que
\(G\) é comutativo. \SGARefTarget{sga3:viii:proposition:1:0:1}Vê-se assim
que \emph{o funtor \(D\) induz uma antiequivalência da categoria dos
\(\widehat{\mathscr C}\)-grupos reflexivos consigo mesma}; em particular,
se \(G,H\) são dois grupos reflexivos, \(D\) induz um \emph{isomorfismo}
\[
  \operatorname{Hom}_{\mathrm{gr}}(G,H)
  \xrightarrow{\ \sim\ }
  \operatorname{Hom}_{\mathrm{gr}}(D(H),D(G))
\]
(basta mesmo que \(H\) seja reflexivo, como se vê pela fórmula
\(\SGARefLink{sga3:viii:eq:1:xxx}{(xxx)}\)).

''','re-edition removed','P. 2 termina com parágrafos corridos: não imprime Definição 1.0 nem Proposição 1.0.1. Retirados os cabeçalhos e restaurado o período contínuo; alvos internos preservados sem numeração visível.')
