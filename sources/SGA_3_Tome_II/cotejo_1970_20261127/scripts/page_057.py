from audit import block
f='09_expose_ix/components/05_seccion_4_parte_2.tex'
block(f,57,'Então,\n\\[\n  M\\simeq', '\n\\smallskip\n\\SGARefTarget{sga3:ix:theorem:4:7:proof:item:b}',r'''Então (M) é da forma (T\times\mathbb Z^r), com (T)
finito, logo (G) é da forma (G_1\times G_2), com
(G_1=D(T)) e (G_2=\mathbf G_m^r), e para (n) grande
multiplicativamente (a saber, (n) múltiplo da ordem de (T))
ter-se-á ({}_nG=G_1\times{}_nG_2), pois ter-se-á
({}_nG_1=G_1). Aplicando ainda
\SGARefLink{sga3:ix:corollary:4:3}{4.3} à projeção
(G\to G_1), reduz-se ao caso de (G_2), i.e. ao caso em que
(G=\mathbf G_m^r). Como então (G) é reduzido, dá no mesmo
dizer que (({}_nG)_{n>0}) é esquematicamente densa em (G),
ou que a união dos ({}_nG) é densa em (G) para a topologia
usual. Como ({}_nG=({}_n\mathbf G_m)^r), reduz-se ao caso de
(G=\mathbf G_m), logo (G) irredutível de dimensão 1. Então
isso resulta do fato de que o conjunto união dos ({}_nG)
(igual ao conjunto das raízes da unidade em (k)) é
\emph{infinito}.
''','1970 restored','Printed p.57 uses T, not Gamma, for the finite group, all formulas inline, original future on aura, impersonal on est ramené, and emphasizes infini. Restored the original paragraph rather than its rearranged displayed expansion.')
block(f,57,'\\smallskip\n\\SGARefTarget{sga3:ix:theorem:4:7:proof:item:b}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:4:8}',r'''\SGARefTarget{sga3:ix:theorem:4:7:proof:item:b}b) Caso geral.
Para todo ponto (s) de (S), existe uma vizinhança aberta
(U) de (s) e um morfismo fielmente plano (S'\to U) tal
que (G'=G_{S'}) seja diagonalizável, i.e. da forma (D_{S'}(M)).
É imediato que se pode reduzir ao caso dos (G'), logo pode-se
supor (G) diagonalizável, logo ele provém do grupo absoluto
(D_{\mathbb Z}(M)) sobre (\operatorname{Spec}(\mathbb Z))
por mudança de base (S\to\operatorname{Spec}(\mathbb Z)).
Basta agora conjugar
\SGARefLink{sga3:ix:theorem:4:7:proof:item:a}{a)} e
\SGARefLink{sga3:ix:lemma:4:4}{4.4}.
''','re-edition removed','Original4.7(b) assumes a faithfully flat map only, says reduction to G prime is immediate, and ends simply by combining(a) and4.4. Removed added quasi-compactness,4.5.0 citation, introduced H and detailed fibre argument; no proof square in1970.')
block(f,57,r'\noindent\SGARefTarget{sga3:ix:corollary:4:8}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:4:9}',r'''\noindent\SGARefTarget{sga3:ix:corollary:4:8}\textbf{Corolário 4.8.}
\begin{enumerate}
  \item[a)]\SGARefTarget{sga3:ix:corollary:4:8:item:a}
  \textit{Sejam (u,v:H\to G) dois homomorfismos de
  (S)-pré-esquemas em grupos, com (H) diagonalizável de tipo
  finito, e suponhamos que para todo inteiro (n>0), as restrições
  de (u) e (v) a ({}_nH) sejam idênticas. Então (u=v).}

  \item[b)]\SGARefTarget{sga3:ix:corollary:4:8:item:b}
  \textit{Sejam (H_1,H_2) dois subgrupos de tipo multiplicativo
  e de tipo finito de um pré-esquema em grupos (G), e suponhamos
  que para todo inteiro (n>0), se tenha ({}_nH_1={}_nH_2),
  então (H_1=H_2).}
\end{enumerate}

A primeira asserção resulta da segunda, pela consideração dos
subgrupos (H_1,H_2) de (H\times G), gráficos de (u) e
(v). Para provar b), seja (H=H_1\cap H_2), é um
subpré-esquema em grupos de (H_i) ((i=1,2)), é preciso
mostrar que é idêntico a (H_i), ora, a hipótese significa que
majora os ({}_nH_i). Reduz-se portanto a provar o
''','1970 restored','Corollary4.8(a) explicitly says H diagonalisable de type fini, not merely multiplicative type. Restored supposition wording in(a)/(b), continuous original proof with inline intersection, no proof heading or square, and its direct lead-in to4.9.')
block(f,57,r'\noindent\SGARefTarget{sga3:ix:corollary:4:9}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:corollary:4:9}\textbf{Corolário 4.9.}
\textit{Sejam (G) um (S)-grupo de tipo multiplicativo e de
tipo finito, e (H) um subpré-esquema em grupos que majora os
({}_nG), (n>0). Então (H=G).}
''','translation','Original4.9 uses a single Soient list and the verb majore with n>0 as an inline qualifier.')
