from audit import change,block
f='09_expose_ix/components/04_seccion_4_parte_1.tex'
block(f,53,r'\SGARefTarget{sga3:ix:lemma:4:4:display:01}', '\nNo que segue, limitamo-nos',r'''\SGARefTarget{sga3:ix:lemma:4:4:display:01}
\(S=\operatorname{Spec}(A)\), \(X=\operatorname{Spec}(B)\),
\(S'=\operatorname{Spec}(A')\), \(X'=\operatorname{Spec}(B')\),
onde \(B'=B\otimes_A A'\); \(A\to A'\) é um homomorfismo
\emph{local}. Pode-se também supor \(U'\) afim, da forma
\(X'_{g'}\), com \(g'\in B'\). Para toda sub-\(A\)-álgebra
\(A''\) de \(A'\), considera-se \(S''=\operatorname{Spec}(A'')\)
e \(X'',Z''{}^i\) deduzidos de \(X,Z^i\) pela mudança de base
\(S''\to S\), donde o diagrama:
\SGARefTarget{sga3:ix:lemma:4:4:diagram:01}
\[
\begin{tikzcd}[column sep=large,row sep=large]
  Z^i \arrow[d] & Z''{}^i \arrow[l]\arrow[d]
    & Z'{}^i \arrow[l]\arrow[d] \\
  X \arrow[d] & X'' \arrow[l]\arrow[d] & X' \arrow[l]\arrow[d] \\
  S & S'' \arrow[l] & S' \arrow[l].
\end{tikzcd}
\]
''','1970 restored','Page 53 has inline affine presentations in the order S,X,S′,X′, and no added A,B noetherian sentence. In the diagram, the upper middle and right nodes are Z″^i,Z′^i with no subscript n; removed the contrary source comment. Restored superscript indices and local emphasis.')
block(f,53,'No que segue, limitamo-nos', '\nSeja \\(Y=V(f)\\)',r'''No que segue, nos limitaremos aos \(A''\) que são localizações de
sub-\(A\)-álgebras de tipo finito \(A''_1\) de \(A'\) em
\(\mathfrak m'\cap A''_1\) (onde \(\mathfrak m'\) é o ideal
maximal de \(A'\)), de modo que os homomorfismos
\(A\to A''\to A'\) são locais. Notemos que esses \(A''\) formam
uma família filtrante crescente de subálgebras cuja união é \(A'\),
portanto seu limite indutivo é igualmente \(A'\). Tem-se, portanto,
do mesmo modo \(B'=\varinjlim_{A''}B\otimes_A A''\). Portanto,
existe um \(A''\) e um elemento \(g''\in B''=B\otimes_A A'\),
cuja imagem em \(B'\) é \(g\). Substituindo, se necessário,
\(S\) por \(S''\) (e \(X,Z^i\) por \(X'',Z''{}^i\)), pode-se,
portanto, supor que \(g'\) provém de \(g\in B\). Substituindo,
se necessário, \(X\) pelo aberto \(X_g=U\), pode-se, portanto,
supor que \(U'=X'\). Vê-se do mesmo modo que se pode supor que
\(f'\) provém de uma seção \(f\) de \(\mathscr O_X\) sobre \(X\).
''','re-edition removed','The original paragraph contains neither the forward appeal to Lemma 4.5 nor the editorial note and expanded preservation-of-hypotheses argument. Restored one paragraph, inductive limit, nous/notons versus impersonal on, and the printed misreadings B″=B⊗_A A′ and image g without a prime, both checked enlarged.')
block(f,53,'Seja \\(Y=V(f)\\)', '\nSeja \\(\\mathfrak m\\)',r'''Seja \(Y=V(f)\) o subesquema de \(X\) definido por \(f\), e
\(Y^i=Z^i\times_X Y\) sua interseção com \(Z^i\), que é um
subesquema fechado de \(Z^i\), igual a \(V(f^i)\), onde \(f^i\)
é a seção de \(\mathscr O_{Z^i}\) induzida por \(f\). Denotando
por \(Y',Y'{}^i\) os \(S'\)-esquemas deduzidos dos precedentes
por mudança de base, ter-se-á ainda
\SGARefTarget{sga3:ix:lemma:4:4:display:02}\(Y'=V(f')\),
\(Y'{}^i=V(f'{}^i)\), e têm-se as relações análogas para
\(Y'',Y''{}^i\). A hipótese sobre \(f'\) se exprime pelas
relações \(Y'{}^i=Z'{}^i\) para todo \(i\), ao menos em todo ponto
\(x'\) de \(X'\) sobre \(s'\).
''','1970 restored','The original has superscript i on Y,Z,f and all formulas inline, without the added product identity for Y′^i. Restored the omitted qualification at least at every x′ over s′.')
block(f,53,'Seja \\(\\mathfrak m\\)', 'Mais geralmente,',r'''Para todo inteiro \(n\geq0\), introduzamos o subesquema
\(S_n=\operatorname{Spec}(A/\mathfrak m^{n+1})\) de \(S\), e os
esquemas \(X_n,Y_n,Z_n^i,Y_n^i\) deduzidos de \(X,Y,Z^i,Y^i\)
pela mudança de base \(S_n\to S\).
''','1970 restored','The final paragraph starts directly Pour tout entier n≥0, without a new maximal-ideal definition, calls S_n a subscheme without the added closed adjective, and keeps its formulas inline. Superscript i is maintained; the sentence continues onto page 54.')
