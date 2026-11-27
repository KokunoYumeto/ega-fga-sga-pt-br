from audit import change,block
f='09_expose_ix/components/01_apertura_y_seccion_1.tex'
block(f,39,r'\noindent\SGARefTarget{sga3:ix:definition:1:3}',r'\medskip\n', '', 'reading','unused') if False else None
block(f,39,r'\noindent\SGARefTarget{sga3:ix:definition:1:3}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:definition:1:4}',r'''\noindent\SGARefTarget{sga3:ix:definition:1:3}\textbf{Definição 1.3.}
\textit{Sejam \(S,G\) como em
\SGARefLink{sga3:ix:definition:1:1}{1.1}. Diz-se que \(G\) é um toro se
for localmente isomorfo, no sentido da topologia fielmente plana e
quase-compacta, a um grupo da forma \(\mathbf G_m^r\) (onde \(r\) é
um inteiro \(>0\)).}

Com as notações de \SGARefLink{sga3:ix:definition:1:1}{1.1}, isso
significa, portanto, que se pode escolher \(S'\) tal que \(G'\) seja
isomorfo a um grupo da forma \((\mathbf G_{m,S'})^r\). Note-se que
o inteiro \(r\) depende de \(s\in S\), é a \emph{dimensão da fibra}
\(G_s=G\otimes_S k(s)\). É uma função localmente constante de \(s\),
como se constata imediatamente. Cabe generalizar essa observação:
''','1970 restored','Page 39 prints the strict inequality r>0, k(s), an inline fibre formula and the parenthesis around the condition on r. Restored On notera and the emphasized phrase dimension de la fibre; removed the added heading dash.')
block(f,39,r'\noindent\SGARefTarget{sga3:ix:definition:1:4}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:remark:1:4:1}',r'''\noindent\SGARefTarget{sga3:ix:definition:1:4}\textbf{Definição 1.4.}
\textit{Seja \(G\) um esquema em grupos diagonalizável sobre um corpo
\(k\), portanto \(G\) é isomorfo a um grupo \(D_k(M)\), onde \(M\)
é um grupo comutativo ordinário, definido a menos de isomorfismo por
essa condição, de modo preciso
\(M\simeq\operatorname{Hom}_{k\text{-}\mathrm{gr}}(G,\mathbf G_m)\)
(\SGARefLink{sga3:viii:corollary:1:3}{VIII 1.3}). A classe de \(M\)
a menos de isomorfismo chama-se o tipo do grupo diagonalizável \(G\);
é evidentemente invariante por extensão do corpo de base. Se agora
\(G\) é um esquema em grupos de tipo multiplicativo sobre um
pré-esquema \(S\) qualquer, então, para todo \(s\in S\), existe uma
extensão \(k\) de \(k(s)\) tal que \(G\times_S\operatorname{Spec}(k)\)
seja um \(k\)-grupo diagonalizável, seu tipo é então independente da
extensão escolhida, pela observação precedente, e será chamado o tipo
de \(G\) em \(s\), ou tipo de \(G_s\). Em particular, se o próprio
\(G\) é diagonalizável, portanto isomorfo a um grupo da forma
\(D_S(M)\), então, para todo \(s\in S\), o tipo de \(G\) em \(s\)
é igual à classe do grupo \(M\). De modo geral, se \(G\) é um grupo
de tipo multiplicativo sobre \(S\), \(M\) um grupo comutativo
ordinário, dir-se-á que \(G\) é de tipo \(M\) se for de tipo \(M\)
em todo ponto \(s\in S\), em outras palavras, se \(G\) for localmente
isomorfo a \(D_S(M)\) no sentido da topologia fielmente plana e
quase-compacta.}
''','1970 restored','Definition 1.4 is one uninterrupted paragraph, with inline Hom(G,G_m) without the added k subscript, k(s), and no nested emphasis of defined terms. Restored its original sentence and paragraph structure.')
change(f,39,r'''\medskip
\noindent\SGARefTarget{sga3:ix:remark:1:4:1}\textbf{Observação 1.4.1.}
\SGARefTarget{sga3:ix:remark:1:4:1:item:a}\textit{a) Para um grupo \(G\)
de tipo multiplicativo sobre \(S\), a função}
\[
  s\longmapsto \text{el tipo de }G_s
\]
\textit{é localmente constante sobre \(S\). Com efeito, com as notações
de \SGARefLink{sga3:ix:definition:1:1}{1.1}, se \(G'\) é de tipo \(M\),
então \(G\) é de tipo \(M\) sobre a vizinhança \(U\) de \(s\). Por
conseguinte, \(S\) possui uma decomposição canônica como união disjunta de
pré-esquemas \(S_i\) tais que, para todo \(i\), \(G_{S_i}\) é de tipo
\(M_i\), onde os grupos comutativos \(M_i\) não são isomorfos dois a dois.}''',r'''\SGARefTarget{sga3:ix:remark:1:4:1}\SGARefTarget{sga3:ix:remark:1:4:1:item:a}
Vê-se imediatamente que, para um dado grupo de tipo multiplicativo
\(G\) sobre \(S\), a função \(s\mapsto\text{tipo de }G_s\) é
localmente constante sobre \(S\): com efeito, com as notações de
\SGARefLink{sga3:ix:definition:1:1}{1.1}, se \(G'\) é de tipo \(M\),
então \(G\) é de tipo \(M\) sobre a vizinhança \(U\) de \(s\).
Segue-se que se tem uma partição canônica como união disjunta de
pré-esquemas \(S_i\) tais que, para todo \(i\), \(G_{S_i}\) é de tipo
\(M_i\), onde os grupos comutativos \(M_i\) não são isomorfos dois a dois.''','re-edition removed','The final paragraph of page 39 is unnumbered prose, not Remark 1.4.1(a); its map is inline and the original begins On voit immédiatement. Removed the extra heading/item and restored Portuguese tipo, preserving invisible targets. Continuation after partition is reviewed on page 40.')
