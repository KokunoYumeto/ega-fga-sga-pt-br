from audit import block,change
f='09_expose_ix/components/08_seccion_7.tex'
block(f,72,r'''tal que
\[
  H'=H\times_SS'
''',r'\SGARefTarget{sga3:ix:theorem:7:1:diagram:03}',r'''tal que \(H'=H\times_SS'\) seja diagonalizável.
Utilizaremos somente o fato de que \(S'\to S\) é finito
e de cobertura (para a topologia fielmente plana e
quase-compacta, ou simplesmente para a topologia
canônica de \((\mathrm{Sch})\)) --- assim a hipótese
«étale» poderia ser substituída por «plano». Seja
\(S''=S'\times_SS'\), introduzamos do mesmo modo
\(S'_n\) e \(S''_n=S''\times_SS_n=S'_n\times_{S_n}S'_n\),
e \(H',G',H'',G'',H'_n,G'_n,H''_n,G''_n\) deduzidos de
\(H\) e \(G\) pelas mudanças de base que se adivinham.
Note-se que \(H'\) e \(H''\) são agora diagonalizáveis.
Note-se também que \(S'\), logo \(S''\), é afim, e que
se \(S'=\operatorname{Spec}(A')\),
\(S''=\operatorname{Spec}(A'')\), então \(A'\) e \(A''\)
são separados e completos para a topologia definida por
\(JA'\) resp. por \(JA''\) (resulta do fato de que \(A'\)
e \(A''\) são finitos sobre \(A\)). Como \(S'\to S\) e
\(S'_n\to S_n\) são de cobertura, obtém-se um diagrama
comutativo de aplicações de conjuntos cujas duas
linhas são exatas:
''','1970 restored','P. 72: one continuous paragraph with all preliminary formulas inline; covering parenthesis, quoted hypotheses, Noter que, resp., and JA prime / JA double-prime (J, enlarged at 6x), not I.')
change(f,72,r'''\operatorname{Hom}_{S''_n\text{-}\mathrm{gr}}(H''_n,G''_n).
\end{tikzcd}''',r'''\operatorname{Hom}_{S''_n\text{-}\mathrm{gr}}(H''_n,G''_n)
\end{tikzcd}''','typesetting','P. 72 descent diagram: the terminal entry has no full stop; all six objects and arrow directions compared at enlargement.')
block(f,72,'A segunda linha é exata porque',r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:corollary:7:3}',r'''(NB a segunda linha é exata como limite projetivo de
diagramas exatos, relativos aos diversos \(S'_n\to S_n\)).
Segundo o que já se provou (caso diagonalizável), \(u'\)
e \(u''\) são bijetivos. O mesmo ocorre, portanto, com
\(u\), o que termina a demonstração de
\SGARefLink{sga3:ix:theorem:7:1}{7.1}.

''','1970 restored','P. 72: parenthetical NB, parenthetical diagonalizable case, and original continuous ending without added proof square.')
block(f,72,r'''\textit{Nas condições de
\SGARefLink{sga3:ix:theorem:7:1}{7.1}''','levantamentos '+r"\(u,u'\), constroem-se",r'''\textit{Nas condições de
\SGARefLink{sga3:ix:theorem:7:1}{7.1}, suponhamos além
disso \(G\) suave sobre \(S\), e seja \(u_0:H_0\to G_0\)
um homomorfismo de \(S_0\)-grupos. Então existe um
homomorfismo de \(S\)-grupos \(u:H\to G\) que levanta
\(u_0\). Dois tais levantamentos \(u,u'\) são conjugados
por um elemento \(g\) de \(G(S)\) reduzindo-se segundo
o elemento unidade de \(G_0(S_0)\).}

Resulta da conjunção de
\SGARefLink{sga3:ix:theorem:3:6}{3.6} e de
\SGARefLink{sga3:ix:theorem:7:1}{7.1}. Para construir
um \(u\), constroem-se sucessivamente \(u_n\), o que é
possível por \SGARefLink{sga3:ix:theorem:3:6}{3.6}, e
em virtude de \SGARefLink{sga3:ix:theorem:7:1}{7.1}
o sistema \((u_n)\) provém de um \(u\). Dados dois
''','1970 restored','P. 72, corollary 7.3: lisse translated suave; homomorphisms inline, Deux tels relèvements, original opening Resulta da conjunção with no proof heading or expanded S-homomorphism wording.')
