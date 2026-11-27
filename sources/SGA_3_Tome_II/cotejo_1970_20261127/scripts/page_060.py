from audit import block
f='09_expose_ix/components/06_seccion_5.tex'
block(f,60,r'\noindent\SGARefTarget{sga3:ix:corollary:5:3}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:5:4}',r'''\noindent\SGARefTarget{sga3:ix:corollary:5:3}\textbf{Corolário 5.3.}
\textit{Sejam \(u,H,G\), como em
\SGARefLink{sga3:ix:corollary:5:2}{5.2}. Suponhamos além disso
\(G\) separado sobre \(S\). Seja \(U\) o conjunto dos
\(s\in S\) tais que \(u_s\) seja o homomorfismo unidade. Então
\(U\) é uma parte ao mesmo tempo aberta e fechada de \(S\),
e \(u_U:H_U\to G_U\) é o homomorfismo unidade.}

Resta provar somente que \(U\) é fechado. Ora, seja
\(K=\operatorname{Ker}u\), como \(H\) é separado sobre \(S\),
é um subpré-esquema \emph{fechado} de \(H\), e \(U\) é o
conjunto dos \(s\in S\) tais que \(K_s=H_s\). Vê-se então
facilmente que \(U\) é fechado, por exemplo como aplicação de
\SGARefLink{sga3:viii:theorem:6:4}{VIII 6.4}, ou notando que
se pode supor \(S\) reduzido e \(U\) denso em \(S\), logo
esquematicamente denso em \(S\), o que implica \(H_U\)
esquematicamente denso em \(H\), pois \(H\) é plano sobre
\(S\), e como \(u\) e o homomorfismo unidade \(e\) coincidem
sobre \(H_U\), coincidem sobre \(H\).
''','1970 restored','Printed60 explicitly says H est séparé in the proof, not G; preserve it. Restored the separate opening sentences of5.3, original e for the unit homomorphism, emphasis on fermé and the continuous proof; removed added VIII6.3/essential-freeness justification, proof heading and square.')
block(f,60,r'\noindent\SGARefTarget{sga3:ix:corollary:5:4}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:corollary:5:4}\textbf{Corolário 5.4.}
\textit{Sejam \(S\) um pré-esquema, \(H\) e \(G\) dois
\(S\)-grupos, com \(H\) de tipo multiplicativo e de tipo finito
e \(G\) separado e de apresentação finita, \(S'\to S\) um
morfismo, de cobertura para a topologia fielmente plana e
quase-compacta (por exemplo fielmente plano e quase-compacto)
e de fibras geometricamente conexas, \(u':H'\to G'\) um
homomorfismo central dos \(S'\)-grupos deduzidos de \(H,G\)
por mudança de base \(S'\to S\). Então existe um único
homomorfismo \(u:H\to G\) de \(S'\)-grupos que define \(u'\).
Quando \(S'/S\) admite uma seção \(g\), então \(u\) é o
morfismo deduzido de \(u'\) pela mudança de base \(g:S\to S'\).}
''','re-edition removed','Original5.4 assumes a covering morphism for the faithfully flat quasi-compact topology, not a universal effective epimorphism. Removed editorial note, added pi, section example and IV1.12 reference. Restored one Soient sentence and the literal S-prime-groupes in the conclusion, with no added base-change equation.')
block(f,60,'\\emph{Demonstração.}\nComo \\(\\pi\\)', 'sobre o qual \\(u_1\'\'\\)',r'''A unicidade de \(u\), e a última asserção relativa a \(g\),
são triviais, tendo em conta o fato de que a topologia fielmente
plana quase-compacta é menos fina que a topologia canônica de
\((\mathrm{Sch})\). Para a existência de \(u\), reduz-se pela
mesma razão a mostrar que os dois homomorfismos
\(u_1'',u_2'':H''\to G''\) de \(S''\)-grupos deduzidos de
\(u'\) pelas duas mudanças de base
\(\operatorname{pr}_1,\operatorname{pr}_2:
S''=S'\times_SS'\to S'\), são idênticos. Ora, coincidem sobre
a diagonal de \(S''\), de modo preciso as imagens inversas
de \(u_1''\) e \(u_2''\) pelo morfismo diagonal \(S'\to S''\)
são idênticas (pois iguais a \(u'\)). Em virtude de
\SGARefLink{sga3:ix:corollary:5:3}{5.3}, existe portanto uma
parte \(U\) de \(S''\), ao mesmo tempo aberta e fechada, e
''','re-edition removed','The proof on printed60 uses the canonical-topology argument, then the two projections inline and the precise diagonal sentence. Removed the epimorphism/descent expansion, pullback calculation, IV2.3 and5.1(b) references, editorial note and u1 times inverse-u2 display. The page ends after et following the open-and-closed subset.')
