from audit import change
f='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(f,33,'{7.5}, existe um inteiro \\(\\nu_1\\) tal','{7.5}, existe um \\(\\nu_1\\) tal','1970 restored','Lemma 7.7 says il existe un ν_1, without the added word entier.')
change(f,33,r'''\textit{é exata. Mais precisamente, \(w_n\) é fielmente plano e seu
núcleo é \({}_{p^\nu}G_n\).}''',r'''\textit{é exata (mais precisamente, \(w_n\) é fielmente plano e seu
núcleo é \({}_{p^\nu}G\)).}''','1970 restored','The parenthetical clarification in 7.7 has {}_{p^ν}G without n, although the sequence above has G_n.')
change(f,33,r'p^{\nu_0}=\operatorname{rank}Q_0',r'p^{\nu_0}=\operatorname{rang}Q_0','reading','The proof prints the operator rang Q_0.')
change(f,33,r'''\({}_{p^\nu}H_n\) é plano sobre \(S_n\), assim como \(Q_n\);''',r'''\({}_{p^\nu}H\) é plano sobre \(S_n\), assim como \(Q_n\);''','1970 restored','The proof of 7.7 prints {}_{p^ν}H over S_n, with no n on H. The earlier translator’s proposed correction is not followed.')
change(f,33,r'\xrightarrow{\,w\,}Q',r'\longrightarrow Q','re-edition removed','The exact sequence in 7.8 does not name its arrow to Q; there is no w above it.')
change(f,33,r'''planos sobre \(S\), basta prová-lo depois de cada mudança de base para \(S_n\),
onde isso está contido no Corolário~\SGARefLink{sga3:viii:corollary:7:5}{7.5}.
Por fim, a
\SGARefLink{sga3:viii:corollary:7:8:display:exact-sequence:01}{sequência
exata anterior} obtém-se das sequências exatas do
Lema~\SGARefLink{sga3:viii:lemma:7:7}{7.7} ao variar \(n\).''',r'''planos sobre \(S\), basta verificar que isso vale para
\({}_{p^\nu}G_n\) e \({}_{p^\nu}H_n\), para todo \(n\), o que está
contido em \SGARefLink{sga3:viii:corollary:7:5}{7.5}. Por fim, a sequência
exata de \SGARefLink{sga3:viii:corollary:7:8:display:exact-sequence:01}{7.8}
provém das sequências exatas \SGARefLink{sga3:viii:lemma:7:7}{7.7} para
\(n\) variável.''','1970 restored','The last paragraph explicitly writes both base-changed groups and cites the exact sequence of 7.8, followed by the sequences 7.7.')
