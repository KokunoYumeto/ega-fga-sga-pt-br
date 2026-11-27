from pathlib import Path
from audit import change,block
f='09_expose_ix/components/06_seccion_5.tex'
s=(Path('work/sources')/f).read_text();start=s.index(r'Seja \(e\) o elemento unidade')
change(f,63,s[start:],r'''sobre \(G\), via \(u\) e os automorfismos interiores de
\(G\), define um automorfismo \(\theta\) do \(H\)-grupo
\(G_H=G\times_SH\), e queremos provar que esse último
automorfismo é a identidade. Em virtude de
\SGARefLink{sga3:ix:corollary:3:9}{3.9}, é assim em todo caso
se \(S\) é \emph{artiniano} local. No caso de a), conclui-se
que para todo inteiro \(n\), o automorfismo \(\theta_n\) de
\((G_H)_n\) deduzido de \(\theta\) pela mudança de base
\(H_n\to H\) (onde \(H_n=H\times_SS_n\),
\(S_n=\operatorname{Spec}(A/\mathfrak m^{n+1})\)), é a
identidade. Logo se \(K=\operatorname{Ker}(\theta,
\operatorname{id}_{G_H})\), então \(K\) é um subpré-esquema
em grupos de \(G_H\) que majora a seção unidade de \((G_H)_n\)
sobre \(H_n\) para todo \(n\), logo que majora uma vizinhança
aberta induzida \(V\) da seção unidade de \(G_H\) sobre \(H\).
Ora, sendo as fibras de \(G_H\) sobre \(H\) conexas, logo
(sendo pré-esquemas em grupos) tendo um único elemento
associado (VI\(_A\) 1.1.1), segue-se que para todo \(t\in H\),
\(V_t\) é esquematicamente denso em \(G_t\), logo em virtude
de \SGARefLink{sga3:ix:corollary:4:3}{4.3}, \(V\) é
esquematicamente denso em \(G_H\). Além disso, como \(K\) é
um sub-\(H\)-grupo de \(G_H\), induz em cada fibra \(G_h\)
um subgrupo, \(K_h\), e como este último majora uma vizinhança
aberta do elemento neutro e \(G_h\) é conexo, segue-se que
\(K_h=G_h\), donde \(K=G_H\) como conjunto. Assim, \(K\) é
um subpré-esquema \emph{fechado} de \(G_H\) que majora o
subpré-esquema esquematicamente denso \(V\), logo \(K=G_H\),
o que prova a). Quanto a b), é uma consequência direta de
\SGARefLink{sga3:ix:corollary:3:9}{3.9}, tendo em conta que
para verificar que um subpré-esquema \(K\) de \(P=G\times_SH\)
é idêntico a \(P\), basta verificar que para toda mudança
de base \(S'\to S\), onde \(S'\) é um quociente artiniano
de um anel local de \(S\), tem-se \(K'=P'\).
''','re-edition removed','Printed63 continues the theta action argument without the introduced local ring at e, S-zero construction,5.0 application, formal-neighbourhood proof, editorial notes, bracketed correction of B, finite-presentation expansion or Cohen–Macaulay/EGA additions. Restored the literal unit-section claim, the short associated-point argument, and the original wording S-prime is an Artinian quotient (without adding spectrum).')
f='09_expose_ix/components/07_seccion_6.tex'
change(f,63,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 63--68.','% Autoridade: SGA 3, LNM 152 (1970), páginas impressas 63--68.','structure','Section6 begins on printed63; replace re-edition authority comment with the sole1970 authority.')
block(f,63,r'\section*{6. Monomorfismos de grupos', '\n\\medskip',r'''\section*{6. Monomorfismos dos grupos de tipo multiplicativo, e
fatoração canônica de um homomorfismo de um tal grupo}
\addcontentsline{toc}{section}{6. Monomorfismos dos grupos de tipo
multiplicativo, e fatoração canônica de um homomorfismo de um tal grupo}
''','structure','Printed section6 title has des groupes and a comma before et, and ends d’un tel groupe. Restored the full title and corresponding contents entry.')
block(f,63,r'\noindent\SGARefTarget{sga3:ix:lemma:6:1}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:lemma:6:1}\textbf{Lema 6.1.}
\textit{Sejam \(S\) um pré-esquema quase-compacto, \(K\) um
pré-esquema em grupos comutativo sobre \(S\), de apresentação
finita e quase-finito sobre \(S\). Então existe um inteiro
\(n>0\) tal que \(n\operatorname{id}_K=0\), i.e. \(K={}_nK\).}
''','1970 restored','Lemma6.1 explicitly uses K, not G; its conclusion is inline n id_K=0 i.e. K={}_nK. Restored the letter and original single-sentence list.')
