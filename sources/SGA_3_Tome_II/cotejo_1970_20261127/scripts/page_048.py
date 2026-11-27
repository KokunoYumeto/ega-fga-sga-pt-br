from audit import change,block
f='09_expose_ix/components/03_seccion_3.tex'
block(f,48,r'\noindent\SGARefTarget{sga3:ix:theorem:3:6}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:3:2:bis}',r'''\noindent\SGARefTarget{sga3:ix:theorem:3:6}\textbf{Teorema 3.6.}
\textit{Sejam \(S\) um esquema afim, \(S_0\) um subesquema definido
por um ideal \(J\) nilpotente, \(H\) um grupo de tipo multiplicativo
sobre \(S\), \(G\) um pré-esquema em grupos suave sobre \(S\),
\(u_0:H_0\to G_0\) um homomorfismo dos \(S_0\)-grupos deduzidos
pela mudança de base \(S_0\to S\). Então existe um homomorfismo
\(u:H\to G\) de \(S\)-grupos que levanta \(u_0\) (e por
\SGARefLink{sga3:ix:corollary:3:3}{3.3}, dois tais levantamentos
\(u,u'\) são conjugados por um elemento de \(G(S)\) que se reduz
ao elemento unidade de \(G(S_0)\)).}

Isso resulta de \SGARefLink{sga3:iii:theorem:2-1}{III 2.1} e
\SGARefLink{sga3:iii:theorem:2-3}{2.3}, e de
\SGARefLink{sga3:ix:theorem:3:1}{3.1} (anulação de \(\mathrm H^2\)
para a existência do levantamento de \(u_0\), anulação de
\(\mathrm H^1\) para a unicidade a menos de conjugação).

Podem-se provar do mesmo modo as variantes seguintes de
\SGARefLink{sga3:ix:theorem:3:2}{3.2} a
\SGARefLink{sga3:ix:theorem:3:6}{3.6} (que de fato implicam os
enunciados precedentes, aplicando-as aos subgrupos \emph{gráficos}
dos homomorfismos considerados em
\SGARefLink{sga3:ix:theorem:3:2}{3.2} a
\SGARefLink{sga3:ix:theorem:3:6}{3.6}):
''','1970 restored','Theorem 3.6 puts the conjugacy assertion in parentheses and says lisse. Its proof refers to III 2.1 et 2.3, so the second reference is not IX 2.3. The proof explanation and the transition to variants are parenthetical, with graphes emphasized and 3.2 à 3.6 repeated.')
block(f,48,r'\noindent\SGARefTarget{sga3:ix:theorem:3:2:bis}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:3:3:bis}',r'''\noindent\SGARefTarget{sga3:ix:theorem:3:2:bis}\textbf{Teorema 3.2 bis.}
\textit{Sejam \(S\) um esquema afim, \(S_0\) um subesquema definido
por um ideal \(J\), \(G\) um \(S\)-pré-esquema em grupos,
\(H,H'\) subpré-esquemas em grupos, de tipo multiplicativo,
\(G_0,H_0,H'_0\) os grupos sobre \(S_0\) deduzidos por mudança de
base \(S_0\to S\). Se \(J^2=0\) e \(H_0=H'_0\), então existe
\(g\in G(S)\) tal que \(H'=\operatorname{int}(g)H\) e \(g_0=e\).}
''','1970 restored','Theorem 3.2 bis is a continuous Soient list with inline H′=int(g)H and g_0=e; no parentheses around H, no displayed formula and no Spanish y.')
change(f,48,r'''seja liso sobre \(S\) e que \(J\) seja nilpotente (não necessariamente de
quadrado zero). Se \(g_0\in G_0(S_0)\) satisfaz
\(H'_0=\operatorname{int}(g_0)(H_0)\), então \(g_0\) se levanta a um
elemento \(g\in G(S)\) tal que \(H'=\operatorname{int}(g)(H)\).}''',r'''seja suave sobre \(S\) e que \(J\) seja nilpotente (não necessariamente
de quadrado zero). Seja \(g_0\in G_0(S_0)\) tal que
\(H'_0=\operatorname{int}(g_0)H_0\), então \(g_0\) se levanta a
\(g\in G(S)\) tal que \(H'=\operatorname{int}(g)H\).}''','translation','Corollary 3.3 bis uses lisse and Soit g_0 ... tel que, and juxtaposes H_0 and H after int(g), with no added parentheses.')
