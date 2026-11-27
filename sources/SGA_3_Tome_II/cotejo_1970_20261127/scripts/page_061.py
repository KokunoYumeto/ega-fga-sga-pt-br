from audit import block
f='09_expose_ix/components/06_seccion_5.tex'
block(f,61,'sobre o qual \\(u_1\'\'\\)', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:5:5}',r'''que contém a diagonal de \(S''\), tal que \(u_1''\) e
\(u_2''\) coincidem acima de \(U\). Ora, sendo as fibras de
\(S'/S\) geometricamente conexas, o mesmo se dá com as de
\(S''/S\), que são portanto a fortiori conexas, donde resulta
que \(U\) (contendo as diagonais das referidas fibras) contém
as referidas fibras, logo é igual a \(S''\), o que conclui
a demonstração.
''','translation','Printed61 continues et contenant la diagonale... and preserves a fortiori plus the parenthetical diagonal clause. Restored the original wording and natural proof ending, without square.')
block(f,61,r'\noindent\SGARefTarget{sga3:ix:corollary:5:5}', 'Indiquemos as variantes',r'''\noindent\SGARefTarget{sga3:ix:corollary:5:5}\textbf{Corolário 5.5.}
\textit{Sejam \(S\) um pré-esquema, \(G\) um \(S\)-pré-esquema
em grupos de fibras conexas, \(H\) um subgrupo invariante de
\(G\), tal que \(H\) seja de tipo multiplicativo e de tipo
finito. Então \(H\) é um subgrupo central de \(G\).}

Aplica-se \SGARefLink{sga3:ix:corollary:5:4}{5.4}, fazendo
\(S'=G\), ao homomorfismo \(H_G\to H_G\) deduzido das ações
de \(G\) sobre \(H\) induzidas pelos automorfismos interiores
de \(G\). (Isso é possível, pois para um esquema em grupos
sobre um corpo, conexo implica geometricamente conexo,
(VI\(_A\) 2.4). A imagem inversa do referido homomorfismo
pela seção unidade de \(S'=G\) sobre \(S\) é o homomorfismo
identidade, logo por \SGARefLink{sga3:ix:corollary:5:4}{5.4}
o mesmo se dá com \(H_G\to H_G\), logo \(H\) é central em \(G\).

''','re-edition removed','Original5.5 uses G, not K, and has no locally-finite-type hypothesis. Restored its short proof with S-prime=G and H_G, removed editorial note, explicit conjugation display, commutativity justification and bracketed correction. The original opens an outer parenthesis at C’est possible and does not close it (4.8x crop); that misprint remains. VI_A2.4 is external, so the wrong IX2.4 hyperlink was removed.')
block(f,61,'Indiquemos as variantes', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:5:1:bis}',r'''Enunciemos as variantes dos resultados precedentes para
subgrupos centrais de tipo multiplicativo. Obtém-se, procedendo
como para os resultados precedentes (e utilizando
\SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis}):
''','translation','The transition explicitly says enonçons and en procédant comme pour les résultats précédents, with3.2bis parenthetical; restored that wording.')
block(f,61,r'\noindent\SGARefTarget{sga3:ix:theorem:5:1:bis}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:5:4:bis}',r'''\noindent\SGARefTarget{sga3:ix:theorem:5:1:bis}\textbf{Teorema 5.1 bis.}
\textit{Sejam \(G\) um \(S\)-pré-esquema em grupos, \(H_1\)
e \(H_2\) dois subpré-esquemas em grupos de tipo multiplicativo
e de tipo finito, com \(H_{1\,s}\) central. Supõe-se \(S\)
localmente noetheriano ou \(G\) de apresentação finita sobre
\(S\). Então para todo \(s\in S\) tal que \(H_{1\,s}=H_{2\,s}\),
existe uma vizinhança aberta \(U\) de \(s\) tal que
\(H_1|U=H_2|U\).}

\medskip
\noindent\SGARefTarget{sga3:ix:corollary:5:3:bis}\textbf{Corolário 5.3 bis.}
\textit{Sob as condições precedentes, suponhamos além disso
\(G\) separado sobre \(S\). Seja \(U\) o conjunto dos
\(s\in S\) tais que \(H_{1\,s}=H_{2\,s}\). Então \(U\)
é uma parte de \(S\) ao mesmo tempo aberta e fechada, e
\(H_1|U=H_2|U\).}
''','1970 restored','Printed5.1bis uses on suppose and the fibres H_{1 s}, H_{2 s};5.3bis repeats those unparenthesized indices. Both use restriction notation H_1|U=H_2|U, not a subscripted U. Restored the sentence order and original notation.')
