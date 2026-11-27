from audit import block
f='09_expose_ix/components/06_seccion_5.tex'
block(f,62,r'\noindent\SGARefTarget{sga3:ix:corollary:5:4:bis}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:5:6}',r'''\noindent\SGARefTarget{sga3:ix:corollary:5:4:bis}\textbf{Corolário 5.4 bis.}
\textit{Sejam \(S\) um pré-esquema, \(G\) um \(S\)-pré-esquema
em grupos separado e de apresentação finita, \(S'\to S\) um
morfismo de cobertura para a topologia fielmente plana
quase-compacta, e de fibras geometricamente conexas, \(H'\)
um subgrupo de tipo multiplicativo e de tipo finito de
\(G'=G\times_SS'\). Então existe um único subgrupo \(H\) de
\(G\) que define \(H'\) por mudança de base \(S'\to S\), (e
\(H'\) é de tipo multiplicativo e de tipo finito sobre \(S\)).
Se \(S'\to S\) admite uma seção \(g\), então \(H\) é a imagem
inversa do subgrupo \(H'\) de \(G'\) por \(g:S\to S'\).}
''','1970 restored','Original5.4bis has one Soient sentence and the parenthetical literal H-prime is of multiplicative type and finite type over S. Restored that misprint, original description of pullback, and covering terminology; removed added1.1/2.1(b) citations and substitute equations.')
block(f,62,r'\noindent\SGARefTarget{sga3:ix:theorem:5:6}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:theorem:5:6}\textbf{Teorema 5.6.}
\textit{Sejam \(S\) um pré-esquema, \(u:H\to G\) um
homomorfismo de \(S\)-pré-esquemas em grupos, com \(H\) de tipo
multiplicativo e de tipo finito, \(G\) de apresentação finita.}
\begin{enumerate}
  \item[a)]\SGARefTarget{sga3:ix:theorem:5:6:item:a}
  \textit{Suponhamos \(G\) de fibras conexas, e seja \(s\in S\)
  tal que \(u_s:H_s\to G_s\) seja um homomorfismo central.
  Então existe uma vizinhança aberta \(U\) de \(s\) tal que
  o homomorfismo \(H|U\to G|U\) induzido por \(u\) seja central.}

  \item[b)]\SGARefTarget{sga3:ix:theorem:5:6:item:b}
  \textit{Suponhamos que para todo \(s\in S\), \(u_s:H_s\to G_s\)
  seja central. Então \(u\) é central.}
\end{enumerate}
''','translation','Original5.6 uses the Soient list, Supposons in both parts, separate Alors sentences, and H|U to G|U with baseline U. Restored its exact structure.')
block(f,62,'\\emph{Demonstração.}\nProvemos primeiro', 'Seja \\(e\\) o elemento unidade',r'''O procedimento padrão nos reduz em
\SGARefLink{sga3:ix:theorem:5:6:item:a}{a)} e
\SGARefLink{sga3:ix:theorem:5:6:item:b}{b)} ao caso em que
\(S\) é localmente noetheriano. Além disso, em a) pode-se
supor \(S\) local, de ponto fechado \(s\), e deve-se então
provar que \(u\) é central. Seja \(K\) o subpré-esquema
\(\operatorname{Ker}(v,w)\), onde
\SGARefTarget{sga3:ix:theorem:5:6:display:01}
\[
  v,w:H\times_SG\rightrightarrows G
\]
são definidos por \(v(h,g)=g\), \(w(h,g)=\operatorname{int}(u(h)).g
=u(h)gu(h)^{-1}\). Então \(K\) é um sub-\(G\)-grupo do
\(G\)-grupo \(H_G=H\times_SG\), quer-se mostrar que é igual
ao próprio \(H_G\). Em virtude de
\SGARefLink{sga3:ix:corollary:4:9}{4.9}, reduz-se a provar que
majora os \({}_n(H_G)=({}_nH)\times_SG\) para todo inteiro
\(n>0\), o que nos reduz ao caso em que \(H={}_nH\), i.e.
\(H\) \emph{finito} sobre \(S\). Pode-se também dizer que
a ação de \(H\)
''','re-edition removed','Printed62 gives one short standard reduction for both(a),(b), not the expanded5.1(b)/finite-type descent proof and editorial note. Restored the single v,w arrow display, inline defining formulas, original n (not m), emphasis on finite, and the final action sentence beginning at the page foot.')
