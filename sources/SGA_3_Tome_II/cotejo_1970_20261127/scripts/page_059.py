from audit import block
f='09_expose_ix/components/06_seccion_5.tex'
block(f,59,'\\emph{Demonstração.}\nDistinguimos os dois casos.', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:5:2}',r'''Distinguamos os dois casos:
\SGARefTarget{sga3:ix:theorem:5:1:proof:item:a}a) \(S\)
localmente noetheriano. Seja \(K=\operatorname{Ker}(u,v)\),
queremos encontrar \(U\) com \(K_u=H_u\). Essa formulação e
EGA IV 8 nos permitem substituir \(S\) pelo espectro de
\(\mathscr O_{S,s}\), logo supor \(S\) local de ponto fechado
\(s\). Substituindo o anel local \(A\) por seu completamento,
o que introduz uma mudança de base fielmente plana e
quase-compacta, pode-se mesmo supor \(A\) completo. Em virtude
de \SGARefLink{sga3:ix:corollary:3:4}{3.4}, ter-se-á \(u_n=v_n\)
para todo \(n\), onde, como de costume, o índice \(n\) indica
a redução módulo \(\mathfrak m^{n+1}\) (\(\mathfrak m\) sendo
o ideal maximal de \(A\)). Para todo inteiro \(m>0\), denotando
por \({}_mu,{}_mv\) os homomorfismos \({}_mH\to G\) induzidos
por \(u,v\), ter-se-á portanto também
\(({}_mu)_n=({}_mv)_n\). Sendo isso verdadeiro para todo \(n\),
e sendo \({}_mH\) \emph{finito} sobre \(S\) em virtude de
\SGARefLink{sga3:ix:proposition:2:2}{2.2}, segue-se que se terá
\({}_mu={}_mv\). Sendo isso verdadeiro para todo \(m\), ter-se-á
\(u=v\) em virtude de
\SGARefLink{sga3:ix:theorem:4:7:proof:item:a}{4.7 a)}.
\label{fnref:IX-30}

\SGARefTarget{sga3:ix:theorem:5:1:proof:item:b}b) \(G\) de
apresentação finita. Podemos ainda supor \(S\) local de ponto
fechado \(s\), e provar que então \(u=v\). Fazendo uma extensão
fielmente plana e quase-compacta da base, pode-se supor além
disso \(H\) diagonalizável, logo da forma \(D_S(M)\), com
\(M\) um grupo comutativo de tipo finito. Introduzamos, como na
demonstração de \SGARefLink{sga3:ix:corollary:4:6}{4.6}, a
família filtrante crescente das sub-\(\mathbb Z\)-álgebras de
tipo finito \(A_i\) de \(A\). Como \(G\) é de apresentação
finita sobre \(S\), provém de um pré-esquema em grupos de
apresentação finita \(G_i\) sobre um \(S_i\). Aliás, \(H\)
provém de \(H_i=D_{S_i}(M)\). Além disso, para \(j\) grande,
em virtude de EGA IV 8, os homomorfismos \(u,v\) provêm de
homomorfismos de \(S_j\)-grupos \(u_j,v_j:H_j\to G_j\), e
\(u_j\) será central para \(j\) grande. Aliás, se \(s_j\) é
a imagem de \(s\) em \(S_j\), tem-se
\(u_{j\,s_j}=v_{j\,s_j}\). Pode-se então aplicar
\SGARefLink{sga3:ix:theorem:5:1:proof:item:a}{a)} à situação
sobre \(S_j\), donde imediatamente a conclusão enunciada.
''','re-edition removed','Printed59 has two short proof paragraphs, no added heading or editorial notes. Restored original EGA IV8 reductions, lower-case u in K_u=H_u,4.7 a), and the literal claim that u_j is central for large j. Removed the expanded diagonal/kernel/local finiteness proof, added5.0 citation, fpqc descent calculation, rho_i argument, residue-field formulas and detailed references. All original targets and the note label are retained invisibly.')
block(f,59,r'\noindent\SGARefTarget{sga3:ix:corollary:5:2}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:5:3}',r'''\noindent\SGARefTarget{sga3:ix:corollary:5:2}\textbf{Corolário 5.2.}
\textit{Seja \(u:H\to G\) um homomorfismo de \(S\)-pré-esquemas
em grupos, com \(H\) de tipo multiplicativo e de tipo finito,
e \(S\) localmente noetheriano ou \(G\) de apresentação finita
sobre \(S\). Seja \(s\in S\) e suponhamos que \(u_s\) seja o
homomorfismo unidade. Então existe uma vizinhança aberta \(U\)
de \(s\) tal que \(u_U\) seja o homomorfismo unidade.}
''','translation','Original5.2 lists all finiteness hypotheses in the opening sentence, then says Soit s... et supposons..., followed by Alors; restored that sentence structure.')
