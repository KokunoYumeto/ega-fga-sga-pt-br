from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
change(f,46,r'''\(U'\to U\). Assim, todo ponto \(s\in S\) possui uma vizinhança aberta e fechada
\(U\) tal que \(H_U\) e \(K_U\) são isotriviais. A afirmação''',r'''\(U'\to U\), portanto vê-se que todo ponto \(s\) de \(S\) tem
uma vizinhança \(U\) aberta e fechada tal que \(H_U\) e \(K_U\)
sejam isotriviais. A conclusão''','translation','The continuation of ii says donc on voit que tout point s de S ... and keeps it in the preceding sentence.')
change(f,46,r'''definições. Além disso, o caso quase-isotrivial também se deduzirá do fato
mais geral «tipo finito \(\Longrightarrow\) quase-isotrivial», anunciado
em \SGARefLink{sga3:ix:comments:1:2}{1.2}
(cf. \SGARefLink{sga3:x:corollary:4-5}{X~4.5}).''',r'''definições. Note-se, aliás, que o caso «quase-isotrivial» resultará
também do fato mais geral de que «tipo finito
\(\Longrightarrow\) quase-isotrivial», anunciado em
\SGARefLink{sga3:ix:comments:1:2}{1.2}.''','re-edition removed','The last paragraph of section 2 has no X 4.5 reference; it says Noter d’ailleurs and quotes quasi-isotrivial.')
f='09_expose_ix/components/03_seccion_3.tex'
change(f,46,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 46--50.','% Autoridade: SGA 3, LNM 152 (1970), pp. 46--50.','re-edition removed','Section 3 begins on printed page 46; the 1970 scan is the sole authority.')
change(f,46,r'\SGARefLink{sga3:ix:theorem:3:1}{teorema seguinte}.',r'\SGARefLink{sga3:ix:theorem:3:1}{teorema seguinte}:','reading','The introductory sentence ends in a colon.')
block(f,46,r'\noindent\SGARefTarget{sga3:ix:theorem:3:1}', '\nUtilizando os resultados',r'''\noindent\SGARefTarget{sga3:ix:theorem:3:1}\textbf{Teorema 3.1.}
\textit{Sejam \(S\) um esquema afim, \(H\) um \(S\)-grupo de tipo
multiplicativo, \(F\) um feixe quase-coerente sobre \(S\), sobre o
qual \(G\) atua (\SGARefLink{sga3:i:subsection:4-7}{I 4.7}).
Então tem-se}
\[
  \mathrm H^i(H,F)=0\qquad\text{para }i>0,
\]
\textit{onde \(\mathrm H^i\) é a cohomologia de Hochschild estudada
em Exp. I 5.}

Com efeito, segundo loc.\ cit.,
\SGARefLink{sga3:i:subsection:5-3}{5.3}, a cohomologia de Hochschild
se explicita, em termos dos anéis afins \(A\) de \(S\) e \(B\)
de \(G\), e do módulo \(M\) sobre \(A\) que define \(F\), como
cohomologia de um complexo de \(A\)-módulos \(C^\circ(H,F)\),
\emph{cuja formação comuta com toda mudança de base} \(A\to A'\).
Por conseguinte, para uma mudança de base \(A\to A'\) com \(A'\)
\emph{plano} sobre \(A\), ter-se-á
\[
  \mathrm H^i(H',F')=\mathrm H^i(H,F)\otimes_A A',
\]
e por conseguinte, se se supõe até mesmo \(A'\) fielmente plano
sobre \(A\), para provar que \(\mathrm H^i(H,F)\) é nulo, basta
provar que o mesmo vale para \(\mathrm H^i(H',F')\). Essa observação
nos reduz a verificar \SGARefLink{sga3:ix:theorem:3:1}{3.1} no caso
em que \(G\) é diagonalizável, nesse caso isso foi provado em
\SGARefLink{sga3:i:theorem:5-3-3}{I 5.3.3}.
''','1970 restored','Theorem 3.1 literally introduces H but says G acts; retain this misprint. The scan uses plain F and C°(H,F), not script F or C•(H,M), cites Exp. I 5 and loc. cit. 5.3 in Exposé I, emphasizes base-change commutation and flat, and has no editorial source-error comment. Restored all of these and the continuous proof.')
