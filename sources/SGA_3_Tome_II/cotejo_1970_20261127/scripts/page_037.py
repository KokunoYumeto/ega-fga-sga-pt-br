from audit import change,block
f='09_expose_ix/components/01_apertura_y_seccion_1.tex'
change(f,37,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 37--40.','% Autoridade: LNM 152 (1970), pp. 37--40.','structure','The authority is the supplied 1970 scan, printed pages 37–40.')
change(f,37,'% O TeX inglês serve unicamente para o alinhamento estrutural; o PDF francês\n% controla o texto, as fórmulas, a numeração e as notas.\n','','structure','Removed old workflow comments; the explicit LNM 152 authority header remains.')
change(f,37,'EXPOSÉ IX. GRUPOS DE TIPO MULTIPLICATIVO I (HOMOMORFISMOS)','EXPOSÉ IX. GRUPOS DE TIPO MULTIPLICATIVO: HOMOMORFISMOS','re-edition removed','The 1970 title has no added Roman I; removed it from both running-head arguments.',count=2)
change(f,37,r'\textbf{Definição 1.1.} ---',r'\textbf{Definição 1.1.}','structure','The 1970 heading is Définition 1.1. without a following dash.')
block(f,37,r'\textit{Seja \(S\) um pré-esquema e seja \(G\)', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:comments:1:2}',r'''\textit{Seja \(S\) um pré-esquema e seja \(G\) um \(S\)-pré-esquema
em grupos. Diz-se que \(G\) é um grupo \emph{de tipo multiplicativo}
se \(G\) é localmente diagonalizável no sentido da topologia fielmente
plana quase-compacta (cf. \SGARefLink{sga3:iv:subsection:6:3}{IV 6.3}),
isto é, se, para todo \(s\in S\), existe uma vizinhança aberta \(U\)
de \(s\) e um morfismo fielmente plano e quase-compacto \(S'\to S\)
tal que \(G'=G\times_S S'\) seja um \(S'\)-grupo diagonalizável
(\SGARefLink{sga3:i:subsection:4-4}{I 4.4}). Diz-se que \(G\) é de tipo
multiplicativo \emph{quase-isotrivial} se é mesmo localmente
diagonalizável no sentido da topologia étale
(\SGARefLink{sga3:iv:subsection:6:3}{IV 6.3}), isto é, se, na definição
precedente, pode-se mesmo tomar \(S'\to U\) étale sobrejetivo, ou ainda
(o que equivale ao mesmo, como se vê tomando o esquema soma dos \(S'\)
associados aos diversos \(s\in S\)) se existe \(S'\to S\) étale e
sobrejetivo tal que \(G'=G\times_S S'\) seja um \(S'\)-grupo localmente
diagonalizável. Se é possível mesmo escolher \(S'\to S\) étale
sobrejetivo e finito, diz-se que \(G\) é de tipo multiplicativo
\emph{isotrivial}. Por fim, diz-se que \(G\) é um grupo de tipo
multiplicativo \emph{localmente trivial} (resp. \emph{localmente
isotrivial}) se todo \(s\in S\) admite uma vizinhança aberta \(U\)
tal que \(G\times_S U\) seja um \(U\)-grupo diagonalizável (resp. um
grupo de tipo multiplicativo isotrivial, isto é, existe \(S'\to U\)
morfismo étale sobrejetivo finito tal que \(G\times_S S'\) seja um
\(S'\)-grupo diagonalizável).}
''','1970 restored','Definition 1.1 is one continuous paragraph. Restored its first arrow S′→S (not U), the sole reference I 4.4, the parenthetical scheme-sum explanation and resp.; removed the added VIII 1.1 citation and the separate display/paragraph structure. The later arrows S′→U remain as printed.')
change(f,37,r'\textbf{Comentários 1.2.} ---',r'\textbf{Comentários 1.2.}','structure','The heading Commentaires 1.2 has no following dash.')
change(f,37,r'''As cinco noções precedentes são todas obtidas, por localização, a partir
da noção de grupo diagonalizável, com respeito a cinco «topologias»
distintas associadas a \((\mathbf{Sch})\).''',r'''Note-se que as cinco noções precedentes se deduzem todas da noção de
grupo diagonalizável pelo processo de localização, no sentido de cinco
«topologias» diferentes associadas a \((\mathrm{Sch})\).''','translation','Commentaires 1.2 starts On notera que; preserve the impersonal form and the original description of localisation.')
