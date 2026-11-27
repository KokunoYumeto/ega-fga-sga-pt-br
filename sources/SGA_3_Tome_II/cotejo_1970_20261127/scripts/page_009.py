from audit import *
f='08_expose_viii/components/04_seccion_3.tex'
change(f,9,r'  u^t:\mathcal O_S(M\')',r'  \mathcal O_S(M\')','reading','P. 9: a seta de álgebras não recebe nome u′ ou u^t.') if False else None
change(f,9,"  u^t:\\mathcal O_S(M')\\longrightarrow\\mathcal O_S(M)","  \\mathcal O_S(M')\\longrightarrow\\mathcal O_S(M)",'reading','P. 9: a seta de álgebras O_S(M′) para O_S(M) não recebe nome.')
change(f,9,r'''de \(G''\) para \(\operatorname{Ker}u^t\), e esse núcleo é um grupo
diagonalizável isomorfo a}
\[
  D_S(v(M))=D_S(\operatorname{Coker}u).
\]''',r'''de \(G''\) para \(\operatorname{Ker}u^t\), e este último é um grupo
diagonalizável.}''','re-edition removed','P. 9, 3.3 termina em groupe diagonalisable; a identificação D_S(v(M))=D_S(Coker u) não é impressa.')
s=(ROOT/'sources'/f).read_text();a=s.index('Para demonstrar');b=s.index('\\medskip\n\\noindent\\SGARefTarget{sga3:viii:corollary:3:4}',a);old=s[a:b]
change(f,9,old,old.replace('u^t',"u'").replace('v^t',"v'").replace('quase compacto','quase-compacto'),'reading','P. 9: a prova de 3.2 e o Corolário 3.3 usam u′ e v′. Notação relida na sequência e no núcleo.')
change(f,9,r'''tipo finito sobre \(S\), e ponhamos \(G'=\operatorname{Ker}u\). Então:}''',r'''tipo finito sobre \(S\). Então:}''','structure','P. 9, 3.4: G′=Ker u está definido no item (a), não nas hipóteses.')
change(f,9,r'''\textit{\(G'\) é localmente diagonalizável e, se \(G\) é de tipo''',r'''\textit{\(G'=\operatorname{Ker}u\) é localmente diagonalizável e, se \(G\) é de tipo''','1970 restored','P. 9, início de 3.4(a): G′ = Ker u.')
change(f,9,r'''quase compactos (cf. IV, \SGARefLink{sga3:iv:subsection:3:4}{3.4})''',r'''quase-compactos (cf. Exposé~IV)''','re-edition removed','P. 9, 3.4(b): cf. Exp. IV sem a referência detalhada 3.4 acrescentada.')
