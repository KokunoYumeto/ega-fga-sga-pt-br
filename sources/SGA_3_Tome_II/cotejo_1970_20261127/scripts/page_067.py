from audit import block
f='09_expose_ix/components/07_seccion_6.tex'
block(f,67,r'\noindent\SGARefTarget{sga3:ix:corollary:6:7}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:6:8}',r'''\noindent\SGARefTarget{sga3:ix:corollary:6:7}\textbf{Corolário 6.7.}
\textit{Seja \(u:H\to G\) um homomorfismo de
\(S\)-pré-esquemas em grupos, com \(H\) de tipo
multiplicativo e de tipo finito; supõe-se \(S\) localmente
noetheriano ou \(G\) localmente de apresentação finita
sobre \(S\). Se todos os homomorfismos induzidos nas fibras
\(u_s:H_s\to G_s\) são monomorfismos, então \(u\) é um
monomorfismo.}

O raciocínio é o mesmo que em
\SGARefLink{sga3:ix:corollary:6:6}{6.6}, sendo aqui inútil
a hipótese de que \(G\) seja separado sobre \(S\) para
assegurar que \(K\) é fechado em \(H\), pois a hipótese
de que os \(u_s\) são monomorfismos implica que \(K\)
é reduzido como conjunto à seção unidade de \(G\).
''','1970 restored','Original6.7 has on suppose after a semicolon, an inline fibre morphism and one proof sentence. It ends literally with the unit section of G; restored G, removed the added redefinition of K, proof heading and square.')
block(f,67,r'\noindent\SGARefTarget{sga3:ix:theorem:6:8}', '\n\\emph{N.B.}',r'''\noindent\SGARefTarget{sga3:ix:theorem:6:8}\textbf{Teorema 6.8.}
\begin{itshape}
Seja \(u:H\to G\) um homomorfismo de \(S\)-pré-esquemas em
grupos, com \(H\) de tipo multiplicativo e de tipo finito,
e \(G\) separado sobre \(S\). Supõe-se além disso \(S\)
localmente noetheriano ou \(G\) de apresentação finita
sobre \(S\). Então \(K=\operatorname{Ker}u\) é um subgrupo
de tipo multiplicativo e de tipo finito de \(H\), e \(u\)
se fatora em
\SGARefTarget{sga3:ix:theorem:6:8:diagram:01}
\[
\begin{tikzcd}[column sep=large]
  H \arrow[r,"u'"] & H/K \arrow[r,"u''"] & G,
\end{tikzcd}
\]
onde \(H/K\) é de tipo multiplicativo e de tipo finito,
\(u'\) é o homomorfismo canônico e é fielmente plano,
enfim \(u''\) um monomorfismo.
\end{itshape}
''','re-edition removed','Original6.8 has inline K=Ker u, on suppose, the displayed factorization and ends enfin u double-prime un monomorphisme. Removed the added parenthetical affine condition and separate K display.')
block(f,67,'\\emph{N.B.}', 'Por construção, \\(v\'_s\\)',r'''(N.B. De fato, \(u''\) é uma imersão fechada se \(G\)
é afim sobre \(S\) ou de apresentação finita sobre \(S\)).
Basta provar que \(K\) é de tipo multiplicativo, o resto
da proposição resulta de
\SGARefLink{sga3:ix:proposition:2:7}{2.7} e
\SGARefLink{sga3:iv:remark:5:2:6}{IV 5.2.6}.
Suponhamos primeiro \(G\) de apresentação finita sobre
\(S\). Sendo essa hipótese estável por mudança de base,
reduz-se, para provar que \(K\) é de tipo multiplicativo,
ao caso em que \(H\) é diagonalizável, i.e. \(H=D_S(M)\),
onde \(M\) é um grupo comutativo de tipo finito. Seja
\(s\in S\), então \(K_s\) é um subgrupo fechado de
\(H_s=D_{k(s)}(M)\), logo em virtude de IV 4.7.5 é da
forma \(D_{k(s)}(N)\), onde \(N\) é um grupo quociente
de \(M\). Ponhamos \(K'=D_S(N)\), então \(K'\) é um
subgrupo de tipo multiplicativo de \(H\), seja
\(v':K'\to G\) induzido por \(G\).
''','1970 restored','Printed67 starts the proof with a parenthetical N.B. and continues in one paragraph. It cites IV4.7.5, not8.1, uses k(s), keeps all these formulas inline, and ends literally v-prime induced by G. Restored those readings and removed the added6.6.1 citation/proof heading.')
