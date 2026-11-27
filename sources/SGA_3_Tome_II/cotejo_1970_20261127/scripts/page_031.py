from audit import change,block
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(f,31,r'''\textit{Com \(Q\) e os \(Q_n\) como antes, suponhamos que seu grau comum
seja \(p^{\nu_0}\). Então}
\[
  p^{\nu_0}\operatorname{id}_Q=0,
  \qquad
  p^{\nu_0}\operatorname{id}_{Q_n}=0
  \quad\textit{para todo \(n\)}.
\]''',r'''\textit{Sendo \(Q\) e os \(Q_n\) como acima, e sendo seu grau comum
\(p^{\nu_0}\), teremos \(p^{\nu_0}\operatorname{id}_Q=0\) e, por
conseguinte, \(p^{\nu_0}\operatorname{id}_{Q_n}=0\) para todo \(n\).}''','1970 restored','Corollary 7.4 explicitly connects the two identities with et par suite; it is a continuous sentence.')
g='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(g,31,'% Tradução brasileira revista a partir do workpass espanhol congelado;\n% a fonte permanece em source_es.\n','','re-edition removed','Source workflow comments are not part of the 1970 text.')
change(g,31,'% Autoridade: Polo--Gille Exp8-8nov09.pdf; edição original: LNM 152, pp. 31--36.','% Autoridade: LNM 152 (1970), pp. 31--36.','structure','Authority: supplied LNM 152 scan, printed pages 31–36.')
change(g,31,r'''\textit{Suponhamos ainda que \(G_0\) seja liso sobre \(k\) e que
\(p\operatorname{id}_{G_0}\) seja plano. Equivalentemente, pela teoria de
estrutura dos grupos algébricos sobre um corpo algebricamente
fechado \(\overline{k}\), \(G_{\overline{k}}\) não contém nenhum subgrupo
isomorfo ao grupo aditivo. Então,''',r'''\textit{Suponhamos ainda que \(G_0\) seja suave sobre \(k\) e que o
homomorfismo \(p\cdot\operatorname{id}_{G_0}\) seja plano (o que equivale
a dizer, em virtude da estrutura dos grupos algébricos sobre um corpo
algebricamente fechado \(\overline{k}\), que \(G_{\overline{k}}\) não
contém nenhum subgrupo isomorfo ao grupo aditivo). Então,''','1970 restored','7.5 prints the equivalence as a parenthesis within the assumption, names the homomorphism, and uses lisse (standard suave).')
change(g,31,'Afirmamos que \\(v_n\\) é plano.','Afirmo que \\(v_n\\) é plano.','translation','The proof has the first-person singular Je dis que v_n est plat.')
change(g,31,'(SGA~1, IV, 5.9).','(SGA IV 5.9).','1970 restored','The printed reference is SGA IV 5.9, with no 1 between SGA and IV.')
block(g,31,'Consequentemente, \\(v_n\\) é plano e', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:viii:remark:7:5:after:01}',r'''Consequentemente, \(v_n\) é plano e
\(\operatorname{Ker}v_n={}_{p^\nu}H\) é plano sobre \(S\), c.q.d.
''','1970 restored','The end of the proof prints Ker v_n = {}_{p^ν}H, flat over S, without either n subscript. Removed the translator’s note that corrected both readings and replaced the proof square by c.q.d.')
change(g,31,'Não utilizamos explicitamente a hipótese de que \\(G_0\\) seja liso\nsobre \\(k\\). Ela é, contudo, uma consequência fácil da planitude de','Não utilizamos explicitamente o fato de que \\(G_0\\) seja suave\nsobre \\(k\\); mas é fácil ver que isso é uma consequência do fato de','translation','The unnumbered remark starts Nous n’avons pas utilisé explicitement le fait ... mais il est facile de voir que c’est une conséquence du fait que; lisse → suave. The continuation is checked on page 32.')
