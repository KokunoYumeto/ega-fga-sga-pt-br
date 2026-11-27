from audit import change,block
f='09_expose_ix/components/04_seccion_4_parte_1.tex'
block(f,52,'Por hipótese, todos os', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:4:3}',r'''Por hipótese, os \(f_i\) são nulos. Aliás, \(\mathscr E\) é
localmente livre por hipótese, portanto o mesmo vale para
\(\mathscr F=\mathscr E\otimes_{\mathscr O_{S_0}}\mathscr O_{X_0}\).
Portanto \(f\) é uma seção do módulo \emph{localmente livre}
\(\mathscr F\) sobre \(X_0\), tal que, para todo \(i\), sua
restrição a \(S^i_0\) seja nula. Como \((Z^i_0)_{i\in I}\) é
esquematicamente densa em \(X_0\), segue-se imediatamente que
\(f\) é nula, cqfd.
''','1970 restored','The end of 4.2 puts F=E⊗O inline, emphasizes locally free, and literally says restriction to S^i_0 (not Z^i_0), before using the family (Z^i_0). It ends cqfd, not a square.')
block(f,52,r'\noindent\SGARefTarget{sga3:ix:corollary:4:3}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:4:4}',r'''\noindent\SGARefTarget{sga3:ix:corollary:4:3}\textbf{Corolário 4.3.}
\textit{Sejam \(X\) um \(S\)-pré-esquema plano, com \(X\)
localmente noetheriano, \((Z^i)_{i\in I}\) uma família de
subpré-esquemas de \(X\) planos sobre \(S\). Supõe-se que, para
todo \(s\in S\), a família \((Z^i_s)_{i\in I}\) das fibras em
\(s\) seja esquematicamente densa em \(X_s\). Então a família
\((Z^i)_{i\in I}\) é esquematicamente densa em \(X\).}

Substituindo, se necessário, \(X\) por um aberto induzido, reduz-se
a provar que toda seção \(f\) de \(\mathscr O_X\) cuja restrição
aos \(Z^i\) é nula é nula. Para isso, basta provar que, para todo
\(s\in S\) e todo inteiro \(n\), a seção induzida sobre
\(X\times_S\operatorname{Spec}(\mathscr O_{S,s}/\mathfrak m_s^{n+1})\)
é nula, onde \(\mathfrak m_s\) é o ideal maximal de
\(\mathscr O_{S,s}\) (é aqui que serve a hipótese localmente
noetheriana sobre \(X\)). Isso nos reduz, portanto, ao caso em que
\(S\) é o espectro de um anel local cujo ideal maximal \(J\) é
nilpotente. Está-se então sob as condições de aplicação de
\SGARefLink{sga3:ix:lemma:4:2}{4.2}, donde a conclusão.
''','re-edition removed','Restored the original short proof of 4.3 and its hypothesis order. Removed the editorial note, added proof heading, maximal ideals at x, intersection formulas, extra fibre/base-change displays, S_0=Spec κ(s) and final square. The original keeps its sole formula inline and explains parenthetically where local noetherianity is used.')
block(f,52,r'\noindent\SGARefTarget{sga3:ix:lemma:4:4}', '\n\\SGARefTarget{sga3:ix:lemma:4:4:display:01}',r'''\noindent\SGARefTarget{sga3:ix:lemma:4:4}\textbf{Lema 4.4.}
\textit{Sob as hipóteses de
\SGARefLink{sga3:ix:corollary:4:3}{4.3} e supondo \(S\)
localmente noetheriano, para toda mudança de base \(S'\to S\)
(\(S'\) não necessariamente localmente noetheriano), a família
\((Z'{}^i)_{i\in I}\) é esquematicamente densa em \(X'\).}

É preciso mostrar que toda seção \(f'\) de \(\mathscr O_{X'}\)
sobre um aberto \(U'\) de \(X'\), que se anula sobre os \(Z'{}^i\),
é nula. Seja \(s'\in S'\), basta provar que \(f'\) \emph{é nula
em todos os pontos de} \(U'\) \emph{sobre} \(s'\). Seja \(s\)
a imagem de \(s'\) em \(S\), substituindo, se necessário,
\(S,S'\) pelos espectros dos anéis locais em \(s,s'\), pode-se
supor \(S,S'\) locais, e que \(s,s'\) são seus pontos fechados.
Pode-se além disso supor \(X\) afim, portanto''','re-edition removed','Lemma 4.4 begins Under the hypotheses of 4.3, without restating them, and has no added universal-density reformulation or EGA IV_3 11.10.8 reference. Removed the proof heading; restored its impersonal wording, emphasized nullity over s′, and superscript i.')
