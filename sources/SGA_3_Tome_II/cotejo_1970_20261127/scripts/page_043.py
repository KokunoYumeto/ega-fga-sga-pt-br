from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
block(f,43,r'\noindent\SGARefTarget{sga3:ix:proposition:2:7}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:proposition:2:7}\textbf{Proposição 2.7.}
\textit{Seja \(u:G\to H\) um homomorfismo de \(S\)-grupos de tipo
multiplicativo, com \(H\) de tipo finito sobre \(S\). Então:}
\begin{enumerate}
  \item[(i)]\SGARefTarget{sga3:ix:proposition:2:7:item:i:01}
  \textit{\(G'=\operatorname{Ker}u\) é um \(S\)-grupo de tipo
  multiplicativo, a relação de equivalência definida por \(G'\) em
  \(G\) é \(\mathcal M\)-efetiva, onde \(\mathcal M\) é o
  conjunto dos morfismos fielmente planos e quase-compactos, portanto
  (\SGARefLink{sga3:iv:subsection:3:4}{IV 3.4}) \(u\) se fatora em
  \SGARefTarget{sga3:ix:proposition:2:7:diagram:01}
  \(G\to G/G'=I\to H\), onde \(I\to H\) é um monomorfismo de
  \(S\)-grupos; \(I\) é de tipo multiplicativo, a relação de
  equivalência em \(H\) definida por \(I\) é \(\mathcal M\)-efetiva,
  por conseguinte \(H'=H/I\) existe, e além disso \(H'\) é de tipo
  multiplicativo.}

  \item[(ii)]\SGARefTarget{sga3:ix:proposition:2:7:item:ii:01}
  \textit{\(H'\) e \(I\) são de tipo finito, o mesmo vale para
  \(G'\) se \(G\) o é.}
\end{enumerate}
''','1970 restored','The printed variables throughout 2.7 are G′ and H′, not G_0,H_0. The original defines M again in item i and puts the factorization inline; restored all of these, retaining the diagram target.')
change(f,43,r'''\SGARefLink{sga3:viii:corollary:3:4}{VIII~3.4}.

Registremos os corolários seguintes.''',r'''\SGARefLink{sga3:viii:corollary:3:4}{VIII 3.4}.
Notemos os corolários seguintes:''','structure','The proof ends with Notons les corollaires suivants: in the same paragraph, not a separate sentence ending in a full stop.')
block(f,43,r'\noindent\SGARefTarget{sga3:ix:corollary:2:8}', '\nBasta observar',r'''\noindent\SGARefTarget{sga3:ix:corollary:2:8}\textbf{Corolário 2.8.}
\SGARefTarget{sga3:ix:corollary:2:8:item:a:01}\textit{Seja \(S\)
um pré-esquema. Então a categoria dos \(S\)-grupos de tipo
multiplicativo e de tipo finito é uma categoria abeliana.
\SGARefTarget{sga3:ix:corollary:2:8:item:b:01}Seja \(u:G\to H\) um
homomorfismo nessa categoria, para que ele seja um monomorfismo (resp.
um epimorfismo, resp. um isomorfismo) nessa categoria, é necessário e
suficiente que \(u\) seja um monomorfismo de pré-esquemas (resp. que
\(u\) seja fielmente plano, resp. que \(u\) seja um isomorfismo de
pré-esquemas).}
''','re-edition removed','Corollary 2.8 is one paragraph with no a/b items; it repeats resp. and the conditional pour que ... il faut et il suffit. Removed the added subdivision while keeping its targets.')
change(f,43,r'''para os quais \(u_s:G_s\to H_s\) é um monomorfismo (respectivamente,
fielmente plano, respectivamente, um isomorfismo).''',r'''tais que \(u_s:G_s\to H_s\) seja um monomorfismo (resp.
fielmente plano, resp. um isomorfismo).''','translation','The beginning of 2.9 prints tels que ... soit and the abbreviations resp. twice.')
