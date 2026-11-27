from audit import change,block
f='09_expose_ix/components/03_seccion_3.tex'
change(f,50,r'''\SGARefLink{sga3:iii:corollary:2-4:item:b}{III~2.4(b)}. Também se pode
reduzir a loc.\ cit. observando que''',r'''\SGARefLink{sga3:iii:corollary:2-4:item:b}{III 2.4 b}; também se pode
reduzir a loc.\ cit. notando que''','structure','The proof of 3.8 joins its two statements with a semicolon and cites III 2.4 b).')
change(f,50,r'''apresentação finita sobre \(S\). Suponhamos que o homomorfismo
\(u_0:G_0\to H_0\), obtido pela mudança de base \(S_0\to S\), seja
central.''',r'''apresentação finita sobre \(S\). Supõe-se que o homomorfismo
\(u_0:G_0\to H_0\) deduzido por mudança de base \(S_0\to S\) seja
central.''','translation','Corollary 3.9 says On suppose; restore impersonal Portuguese.')
s=open('work/sources/'+f).read();i=s.index('Com efeito, basta aplicar \\SGARefLink{sga3:ix:proposition:3:8}')
change(f,50,s[i:],r'''Com efeito, basta aplicar \SGARefLink{sga3:ix:proposition:3:8}{3.8}
fazendo \(X=G\), e fazendo \(H\) atuar sobre \(G\) por
\((h,g)\mapsto\operatorname{int}(u(h)).g=u(h)gu(h)^{-1}\).

''','1970 restored','The printed proof of 3.9 literally uses X=G, lets H act on G, and writes (h,g)↦int(u(h)).g=u(h)gu(h)^−1, despite the opposite direction in the statement. Restore this printed error, inline, instead of the corrected X=H and G-action.')
f='09_expose_ix/components/04_seccion_4_parte_1.tex'
change(f,50,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 50--54.','% Autoridade: SGA 3, LNM 152 (1970), pp. 50--54.','re-edition removed','Section 4 begins on printed page 50; its authority is LNM152 (1970).')
block(f,50,r'\SGARefTarget{sga3:ix:section:4}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:definition:4:1}',r'''\SGARefTarget{sga3:ix:section:4}
\begingroup
\renewcommand{\thefootnote}{\(\ast\)}
\section*{4. O teorema de densidade\protect\footnotemark}
\footnotetext{Todos os resultados de
\SGARefLink{sga3:ix:definition:4:1}{4.1} a
\SGARefLink{sga3:ix:corollary:4:6}{4.6} estão contidos em EGA IV 11.10,
ao qual remetemos o leitor para uma exposição em forma da noção de
densidade esquemática.}
\addtocounter{footnote}{-1}
\endgroup
\addcontentsline{toc}{section}{4. O teorema de densidade}

Este teorema (cf. \SGARefLink{sga3:ix:theorem:4:7}{4.7 abaixo}),
juntamente com o teorema do
\SGARefLink{sga3:ix:section:7}{n.º 7}, será a ferramenta essencial
no presente exposé e nos dois seguintes, para passar das propriedades
infinitesimais dos grupos de tipo multiplicativo, que se acaba de
desenvolver, às propriedades «finitas».
''','1970 restored','The original star footnote belongs to the section heading, and cites EGA IV 11.10 without subscript 3. Restored its placement, exposition en forme and the introductory reference to n°7 and impersonal qu’on vient de développer.')
block(f,50,r'\noindent\SGARefTarget{sga3:ix:definition:4:1}', '\nÉ imediato',r'''\noindent\SGARefTarget{sga3:ix:definition:4:1}\textbf{Definição 4.1.}
\textit{Sejam \(X\) um pré-esquema, \((Z^i)_{i\in I}\) uma família
de subpré-esquemas de \(X\). Diz-se que essa família é esquematicamente
densa se, para todo aberto \(U\) de \(X\), e todo subpré-esquema
fechado \(U'\) de \(U\) que majora os \(Z^i\cap U\), tem-se
\(U'=U\). Diz-se que um subpré-esquema \(Z\) de \(X\) é
esquematicamente denso em \(X\), se o mesmo vale para a família
reduzida a \(Z\).}
''','1970 restored','Definition 4.1 uses superscript Z^i, U′ (not U_0), qui majore, and one continuous paragraph for both definitions.')
block(f,50,'É imediato', '\nCom efeito, \\(u=v\\)',r'''Vê-se imediatamente que a definição equivale também a dizer que,
para todo aberto \(U\) de \(X\), toda seção \(f\) de
\(\mathscr O_U\) que é nula sobre os \(Z^i\cap U\) é nula.
\SGARefTarget{sga3:ix:definition:4:1:display:01}Ou ainda (quando
\(X\) está sobre um pré-esquema \(S\)) que, para todo aberto \(U\)
de \(X\) e todo par \((u,v)\) de morfismos de \(U\) para um
\(S\)-pré-esquema \(Y\) \emph{separado} sobre \(S\), que
coincidem sobre os \(Z^i\cap U\), tem-se \(u=v\).''','re-edition removed','The original has no EGA IV_3 11.10.1 citation and no additional kernel/intersection criterion or displayed maps u_i to pushforward sheaves. Removed that whole addition, retaining its invisible target; restored Z^i and the emphasis of separated.')
change(f,50,r'''Com efeito, \(u=v\) equivale a \(U_0=U\), onde \(U_0\) é a imagem''',r'''(Com efeito, a relação \(u=v\) equivale à relação \(U'=U\), onde
\(U'\) é a imagem''','1970 restored','The explanatory proof begins a parenthesis and uses U′; the continuation is read on page 51.')
