from audit import change,block
f='09_expose_ix/components/03_seccion_3.tex'
change(f,47,r'''Utilizando os resultados da Exposição~III, deduziremos de
\SGARefLink{sga3:ix:theorem:3:1}{3.1} várias consequências de natureza
geométrica.''',r'''Utilizando os resultados de Exp. III, vamos deduzir de
\SGARefLink{sga3:ix:theorem:3:1}{3.1} diversas consequências de natureza
geométrica:''','translation','The introductory sentence says Exp. III, nous allons tirer and ends with a colon.')
block(f,47,r'\noindent\SGARefTarget{sga3:ix:theorem:3:2}', '\nIsso se deduz de',r'''\noindent\SGARefTarget{sga3:ix:theorem:3:2}\textbf{Teorema 3.2.}
\textit{Sejam \(S\) um esquema afim, \(S_0\) um subesquema afim
definido por um ideal \(J\), \(H\) um grupo de tipo multiplicativo
sobre \(S\), \(G\) um pré-esquema em grupos qualquer sobre \(S\),
\(u,v:H\to G\) dois homomorfismos de grupos, \(u_0,v_0:H_0\to G_0\)
os homomorfismos deduzidos de \(u,v\) por mudança de base
\(S_0\to S\). Se \(J^2=0\) e \(u_0=v_0\), então existe um
\(g\in G(S)\) tal que \(v=\operatorname{int}(g)\circ u\) e
\(g_0=e\).}
''','1970 restored','Theorem 3.2 has a single opening Soient list and inline final equations, no displayed formula and no Spanish y. Restored the original structure and the conjunction e.')
change(f,47,r'''\SGARefLink{sga3:ix:theorem:3:2}{3.2}, suponhamos ainda que \(G\) seja liso
sobre \(S\), mas suponhamos somente que \(J\) seja nilpotente (não
necessariamente de quadrado zero). Se existe \(g_0\in G_0(S_0)\) tal que
\(v_0=\operatorname{int}(g_0)\circ u_0\), então \(g_0\) se levanta a
um elemento \(g\in G(S)\) tal que
\(v=\operatorname{int}(g)\circ u\).}''',r'''\SGARefLink{sga3:ix:theorem:3:2}{3.2}, suponhamos além disso \(G\)
suave sobre \(S\), mas em contrapartida suponhamos somente \(J\)
nilpotente (não necessariamente de quadrado zero). Seja
\(g_0\in G_0(S_0)\) tal que \(v_0=\operatorname{int}(g_0)u_0\),
então \(g_0\) se levanta a um \(g\in G(S)\) tal que
\(v=\operatorname{int}(g)u\).}''','translation','Corollary 3.3 says lisse (suave), mais en revanche, and Soit g_0 rather than if one exists. Its formulas use juxtaposition after int(g), without added composition circles.')
change(f,47,r'''Por indução sobre um inteiro \(n\) tal que \(J^n=0\), reduz-se ao caso
em que \(J\) é de quadrado zero. Como \(G\) é liso sobre \(S\),
pode-se levantar \(g_0\) a um elemento \(g'\) de \(G(S)\). Substituindo
\(v\) por \(v'=\operatorname{int}(g')\circ u\), reduz-se então à
situação de \SGARefLink{sga3:ix:theorem:3:2}{3.2}.''',r'''Por indução sobre o inteiro \(n\) tal que \(J^n=0\), reduz-se ao
caso em que \(J\) é de quadrado zero. Além disso, sendo \(G\) suave
sobre \(S\), pode-se levantar \(g_0\) a um elemento \(g'\) de
\(G(S)\). Substituindo, se necessário, \(v\) por
\(v'=\operatorname{int}(g')u\), reduz-se então à situação
\SGARefLink{sga3:ix:theorem:3:2}{3.2}.''','translation','The proof says l’entier n, De plus and Quitte à remplacer; the printed replacement is v′=int(g′)u, with juxtaposition.')
change(f,47,r'''\(u_0:H_0\to G_0\) seja o homomorfismo unidade. Então \(u\) é o
homomorfismo unidade.}''',r'''\(u_0:H_0\to G_0\) seja o homomorfismo unidade, então \(u\) é o
homomorfismo unidade.}''','structure','Corollary 3.5 joins its hypothesis and conclusion with a comma, then alors, within one sentence.')
