from audit import change,block
f='09_expose_ix/components/03_seccion_3.tex'
block(f,49,r'\noindent\SGARefTarget{sga3:ix:theorem:3:6:bis}', '\nIndiquemos como',r'''\noindent\SGARefTarget{sga3:ix:theorem:3:6:bis}\textbf{Teorema 3.6 bis.}
\textit{Sejam \(S\) um esquema afim, \(S_0\) um subesquema definido
por um ideal \(J\) nilpotente, \(G\) um \(S\)-pré-esquema em grupos
suave, \(H_0\) um subpré-esquema em grupos de
\(G_0=G\times_S S_0\), de tipo multiplicativo. Então
\SGARefTarget{sga3:ix:theorem:3:6:bis:item:a:01}existe um
subpré-esquema em grupos \(H\) de \(G\), plano sobre \(S\), tal
que \(H\times_S S_0=H_0\),
\SGAInlineRefTarget{sga3:ix:theorem:3:2:item:b}\SGARefTarget{sga3:ix:theorem:3:6:bis:item:b:01}um
 tal \(H\) é de tipo multiplicativo,
\SGARefTarget{sga3:ix:theorem:3:6:bis:item:c:01}(e dois tais
levantamentos \(H,H'\) de \(H_0\) são conjugados por um elemento
\(g\in G(S)\) que se reduz ao elemento unidade de \(G(S_0)\)).}
''','re-edition removed','Theorem 3.6 bis is one paragraph with no a/b/c subdivision or reference to 3.2 bis. It says un tel H est de type multiplicatif and puts conjugacy in parentheses. All original labels, including the legacy inline b target, are kept invisibly.')
block(f,49,'Indiquemos como', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:proposition:3:8}',r'''Mostremos como se pode provar
\SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis} (do qual
\SGARefLink{sga3:ix:corollary:3:3:bis}{3.3 bis} e
\SGARefLink{sga3:ix:corollary:3:4:bis}{3.4 bis} são uma consequência
imediata) e o resultado de levantamento
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis}. Este último resulta
de \SGARefLink{sga3:ix:theorem:3:1}{3.1} (anulação de
\(\mathrm H^2\)) e de \SGARefLink{sga3:iii:proposition:4-21}{III 4.21}
e \SGARefLink{sga3:iii:proposition:4-22}{4.22},
\SGARefLink{sga3:iii:corollary:4-37:item:ii}{4.37 (ii)}, e do mesmo
modo \SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis} resulta de
\SGARefLink{sga3:ix:theorem:3:1}{3.1} (anulação de \(\mathrm H^1\))
e de \SGARefLink{sga3:iii:corollary:4-37:item:i}{III 4.37 (i)},
ao menos quando \(G,H\) são \emph{suaves} sobre \(S\). Mas,
utilizando os resultados do exposé seguinte, podem-se deduzir muito
simplesmente \SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis} e
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis}, sob a forma geral
aqui enunciada, de \SGARefLink{sga3:ix:theorem:3:2}{3.2} resp.
\SGARefLink{sga3:ix:theorem:3:6}{3.6}. Para
\SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis}, basta com efeito
notar que, em virtude de \SGARefLink{sga3:x:proposition:2:1}{X 2.1},
\(H\) e \(H'\) são isomorfos, o que nos reduz a
\SGARefLink{sga3:ix:theorem:3:2}{3.2}. Para
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis}, nota-se que \(H_0\)
é necessariamente de tipo finito por
\SGARefLink{sga3:ix:proposition:2:1:item:b:01}{2.1 b}, pois suas
fibras o são, portanto por \SGARefLink{sga3:x:corollary:4-5}{X 4.5}
é quase-isotrivial, portanto por
\SGARefLink{sga3:x:proposition:2:1}{X 2.1} provém de um grupo de
tipo multiplicativo \(H\) sobre \(S\), ao qual
\SGARefLink{sga3:ix:theorem:3:6}{3.6} é portanto aplicável. Aliás,
para \emph{todo} levantamento \(H\) de \(H_0\) a um subgrupo plano
de \(G\), \(H\) é necessariamente de tipo multiplicativo
(\SGARefLink{sga3:x:corollary:2:3}{X 2.3}), o que prova também a
segunda afirmação em
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis}. (O leitor verificará
que os resultados \SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis} a
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis} não são utilizados
no Exp. X, portanto que não há círculo vicioso!).
''','re-edition removed','The printed proof is one paragraph. Restored omitted III 4.21 and 4.22 and the original finite-type argument par 2.1 b), car ses fibres le sont. Removed both editorial footnotes and the expanded lifting/immersion proof (topological spaces, local-ring surjectivity and EGA I 4.2.2). Restored the original final parenthesis/exclamation and the second assertion reference without an added item b.')
block(f,49,r'\noindent\SGARefTarget{sga3:ix:proposition:3:8}', '\nA demonstração é',r'''\noindent\SGARefTarget{sga3:ix:proposition:3:8}\textbf{Proposição 3.8.}
\textit{Sejam \(S\) um pré-esquema, \(S_0=V(J)\) um subpré-esquema
definido por um ideal \(J\) localmente nilpotente, \(G\) um
\(S\)-grupo de tipo multiplicativo, \(X\) um \(S\)-pré-esquema
localmente de apresentação finita. Supõe-se que \(G\) atue sobre
\(X\), de tal maneira que \(G_0=G\times_S S_0\) atue trivialmente
sobre \(X_0=X\times_S S_0\). Sob essas condições, \(G\) atua
trivialmente sobre \(X\).}
''','1970 restored','Proposition 3.8 explicitly writes S_0=V(J) and sous-préschéma, without the added fermé; it uses On suppose and Sous ces conditions. Restored those readings and the continuous opening list.')
