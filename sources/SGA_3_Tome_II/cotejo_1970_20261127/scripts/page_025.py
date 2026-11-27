import re
from audit import change, block, ROOT
f='08_expose_viii/components/09_seccion_6_parte_2.tex'
change(f,25,r'''Em particular, \textit{se \(G\)
é essencialmente livre e separado sobre \(S\), então o centro \(C\) de
\(G\), que não é outro senão \(\underline{\operatorname{Centr}}_G(G)\), é um
subpré-esquema em grupos fechado de \(G\).}''',r'''Em particular, \(C=\underline{\operatorname{Centr}}_G(G)\) não é outro
senão o \emph{centro} de \(G\); é, portanto, um subpré-esquema em grupos
fechado se \(G\) é essencialmente livre e separado sobre \(S\).''','1970 restored','The sentence spanning pages 24–25 first defines C=Centr_G(G), then identifies the centre and states its closedness; it is not a separate emphasized if-then statement.')
change(f,25,r'''\SGARefLink{sga3:viii:proposition:6:2:item:b:01}{6.2(b)} \emph{[a fonte
imprime 6.3(b)]}''',r'''\SGARefLink{sga3:viii:proposition:6:3}{6.3 b)}''','1970 restored','The printed reference is 6.3 b); no bracketed correction note is printed.')
block(f,25,r'\textit{Seja \(G\) um pré-esquema em grupos sobre um corpo \(k\). Então:}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:viii:remark:6:8}',r'''\textit{Seja \(G\) um pré-esquema em grupos sobre um corpo \(k\).
\SGARefTarget{sga3:viii:corollary:6:7:item:1:01}
Então, para todo subesquema \(Z\) de \(G\), o centralizador de \(Z\)
em \(G\) é um subesquema fechado de \(G\); em particular, o centro de
\(G\) é um subesquema em grupos fechado de \(G\).
\SGARefTarget{sga3:viii:corollary:6:7:item:4:01}
Para todo subesquema em grupos \(H\) de \(G\), o normalizador
\(\underline{\operatorname{Norm}}_G(H)\) é um subesquema em grupos
fechado de \(G\).
\SGARefTarget{sga3:viii:corollary:6:7:item:3:01}
Mais geralmente, para dois subesquemas \(Y,Z\) de \(G\), com \(Z\)
fechado, o transportador \(\underline{\operatorname{Transp}}_G(Y,Z)\)
é um subesquema fechado de \(G\). Se \(Y\) também é fechado,
tem-se a mesma conclusão para
\(\underline{\operatorname{Transp\,str}}_G(Y,Z)\).
\SGARefTarget{sga3:viii:corollary:6:7:item:2:01}
Se \(u,v:X\to G\) são morfismos,
\(\underline{\operatorname{Transp}}_G(u,v)\) é representável por um
subpré-esquema fechado de \(G\).}
''','structure','Corollary 6.7 is one continuous statement: centralizer, centre, normalizer, transporter of Y,Z and finally transporter of u,v. There are no bullet items. The scan prints sous-schéma except in the final conclusion; Transp str is on the baseline. Invisible item targets are retained.')
s=(ROOT/'sources'/f).read_text();i=s.index('\\footnote{Nota do editor: desenvolvemos o original')
old=s[i:]
anchors=re.findall(r'\\(?:SGA(?:Inline)?RefTarget|label)\{[^{}]+\}',old)
new=r'''O Teorema \SGARefLink{sga3:viii:theorem:6:4}{6.4} continua válido
substituindo, no enunciado da definição \SGARefLink{sga3:viii:definition:6:1}{1},
a palavra «livre» por «projetivo». Basta, de fato, uma variante ainda mais
fraca de «livre», a saber, «quase-livre»: um módulo \(M\) sobre um anel
\(A\) diz-se \emph{quase-livre} se a imagem de
\(\check M\otimes_A M\) em \(\operatorname{Hom}_A(M,M)\) contém
\(\operatorname{id}_M\) em seu fecho (e é, portanto, densa em
\(\operatorname{Hom}_A(M,M)\)), quando se mune o módulo Hom da
topologia da convergência pontual discreta (e onde \(\check M\) designa
\(\operatorname{Hom}_A(M,A)\)).

'''+ '\n'.join(anchors)+'\n'
change(f,25,old,new,'re-edition removed','Remark 6.8 is a single paragraph. Removed the editorial note, neighbourhood formula, Θ, equation (*), density proof, base-change proof, projective-module proof, and added Lemma 6.8.1 with its proof. Restored definition 1, check M⊗_A M, Hom_A(M,M), and discrete pointwise convergence. All existing labels/targets retained invisibly.')
g='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(g,25,'% Tradução brasileira revista a partir do workpass espanhol congelado;\n% a fonte permanece em source_es.\n','','re-edition removed','Source workflow comments are not in the 1970 printing.')
change(g,25,'% Autoridade: Polo--Gille Exp8-8nov09.pdf; edição original: LNM 152, pp. 25--31.','% Autoridade: LNM 152 (1970), pp. 25--31.','structure','Authority for this component: printed pages 25–31 of LNM 152.')
change(g,25,r'VI\(_A\).','VI.','1970 restored','The introductory paragraph of §7 refers to Exp VI, without an A subscript.')
