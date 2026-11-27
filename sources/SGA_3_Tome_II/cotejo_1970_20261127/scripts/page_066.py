from audit import block
f='09_expose_ix/components/07_seccion_6.tex'
block(f,66,'\\(\\kappa(t)\\), porque tem essa', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:6:4}',r'''\(k(t)\), isso resulta do fato de que é quase-finito
(resp. não ramificado) sobre \(k(t)\) no elemento neutro,
cf. VI.

Combinando \SGARefLink{sga3:ix:lemma:6:1}{6.1} e
\SGARefLink{sga3:ix:lemma:6:3}{6.3}, encontra-se o
''','1970 restored','Printed66 closes6.3 with k(t), resp., the neutral element and cf.VI only. Removed epsilon(t), added VI_B1.3 reference and square; restored the direct transition to6.4.')
block(f,66,r'\noindent\SGARefTarget{sga3:ix:theorem:6:4}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:6:7}',r'''\noindent\SGARefTarget{sga3:ix:theorem:6:4}\textbf{Teorema 6.4.}
\textit{Sejam \(S\) um pré-esquema, \(H\) um \(S\)-grupo
de tipo multiplicativo e de tipo finito, \(K\) um
subpré-esquema em grupos fechado, de apresentação finita
sobre \(S\). Seja \(s\in S\) tal que \(K_s\) seja finito,
então existe uma vizinhança aberta \(U\) de \(s\) e um
inteiro \(n>0\) tal que \(K|U\) esteja contido em
\({}_nH|U\), e a fortiori (como \({}_nH\) é finito sobre
\(S\)) tal que \(K|U\) seja finito sobre \(U\).}

Utilizando o lema de Nakayama, deduz-se:

\medskip
\noindent\SGARefTarget{sga3:ix:corollary:6:5}\textbf{Corolário 6.5.}
\textit{Com as notações precedentes, suponhamos mesmo que
\(K_s\) seja o grupo unidade. Então existe uma vizinhança
aberta \(U\) de \(s\) tal que \(K|U\) seja o grupo unidade.}

\medskip
\noindent\SGARefTarget{sga3:ix:corollary:6:6}\textbf{Corolário 6.6.}
\textit{Seja \(u:H\to G\) um homomorfismo de
\(S\)-pré-esquemas em grupos, com \(H\) de tipo
multiplicativo e de tipo finito, e \(G\) separado sobre
\(S\). Supõe-se além disso \(S\) localmente noetheriano,
ou \(G\) localmente de apresentação finita sobre \(S\).
Seja \(s\in S\) tal que \(u_s:H_s\to G_s\) seja um
monomorfismo, então existe uma vizinhança aberta \(U\) de
\(s\) tal que \(u\) induza um monomorfismo \(H|U\to G|U\).}

Seja com efeito \(K=\operatorname{Ker}u\), a hipótese
sobre \(u_s\) significa que \(K_s\) é o grupo unidade,
a conclusão que \(K|U\) é o grupo unidade, para \(U\)
conveniente. Ora, sendo \(G\) separado sobre \(S\), \(K\)
é um subgrupo \emph{fechado} de \(H\), e no caso em que
não se supõe \(S\) loc. noeth. mas em compensação \(G\)
localmente de apresentação finita sobre \(S\), \(K\) é
localmente de apresentação finita sobre \(S\), logo de
apresentação finita sobre \(S\), pois é separado sobre
\(S\) (\(H\) o sendo) e quase-compacto sobre \(S\) (sendo
fechado em \(H\), que é quase-compacto sobre \(S\)).
Pode-se portanto aplicar
\SGARefLink{sga3:ix:corollary:6:5}{6.5}, donde
\SGARefLink{sga3:ix:corollary:6:6}{6.6}.
\SGARefTarget{sga3:ix:remark:6:6:1}%
Note-se que quando \(G\) é afim sobre \(S\) ou de
apresentação finita sobre \(S\), \(H|U\to G|U\) é mesmo
uma \emph{imersão fechada}, como se assinalou em
\SGARefLink{sga3:ix:corollary:2:5}{2.5} e
\SGARefLink{sga3:ix:remark:2:6}{2.6}.
''','re-edition removed','Printed66 has inline restrictions and prose containment in6.4, a fortiori and its parenthesis; no added of H. Restored même in6.5, impersonal On suppose in6.6 and the continuous original proof. Removed the added numbered/italic Remark6.6.1 and its resp. structure: the observation is the final sentence of the proof with only immersion fermée emphasized; its anchor remains invisible.')
