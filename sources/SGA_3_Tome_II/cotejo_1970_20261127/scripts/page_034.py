from audit import change
f='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(f,34,'isomorfismo. Provamos:','isomorfismo. Portanto:','translation','The introductory conclusion ends Donc, immediately before Proposition 7.9.')
change(f,34,r'''  \textit{para todo \(s\in S\) cujo corpo residual tenha característica
  \(p>0\), seja \(S'=\operatorname{Spec}(\mathscr O_{S,s})\), e seja
  \(u':G'\to H'\) o morfismo obtido de \(u\) por mudança de base para
  \(S'\). Então \(G'\) é comutativo, a fibra especial
  \(G'_0=G_s\) é liso sobre \(\kappa(s)\), e, para todo \(\nu>0\), o
  grupo \({}_{p^\nu}G'\) é finito sobre \(S'\), enquanto
  \({}_{p^\nu}H'\) é separado sobre \(S'\).}''',r'''  \textit{para todo \(s\in S\) tal que \(k(s)\) seja de característica
  residual \(p>0\), exige-se que as condições seguintes sejam verificadas
  para o homomorfismo \(u':G'\to H'\) de pré-esquemas em grupos sobre
  \(S'=\operatorname{Spec}(\mathscr O_{S,s})\), deduzido de
  \(u:G\to H\) pela mudança de base \(S'\to S\): \(G'\) é comutativo,
  a fibra especial \(G'_0=G_s\) é suave sobre \(k(s)\), e, para todo
  inteiro \(\nu>0\), \({}_{p^\nu}G'\) é finito sobre \(S'\) e
  \({}_{p^\nu}H'\) é separado sobre \(S'\).}''','1970 restored','Condition 7.9(c) explicitly uses k(s), characteristic résiduelle, the homomorphism of group preschemes and the base-change arrow, and every integer ν>0. Restored that wording and standard suave for lisse.')
change(f,34,r'''De fato, a finitude de \({}_pG'\) sobre \(S'\) implica a finitude de sua
fibra especial sobre \(\kappa(s)\). Portanto,
\(G'_0\otimes_{\kappa(s)}\overline{\kappa(s)}\) não contém nenhum
subgrupo isomorfo ao grupo aditivo, e aplicam-se as hipóteses do
Corolário~\SGARefLink{sga3:viii:corollary:7:5}{7.5}.''',r'''Basta observar que, em \SGARefLink{sga3:viii:proposition:7:9:item:c}{(c)},
a condição de que \({}_pG'\) seja finito sobre \(S'\) implica que
\({}_pG'_0\) é finito sobre \(k(s)\), o que já implica que
\(G'_0\otimes_{k(s)}\overline{k(s)}\) não tem subgrupo isomorfo ao
grupo aditivo, de modo que estamos sob as hipóteses de
\SGARefLink{sga3:viii:corollary:7:5}{7.5}.''','1970 restored','The proof explicitly states the finiteness of {}_pG′_0 over k(s), then the base-extended G′_0 and the conclusion under 7.5. It begins Il suffit de remarquer que dans c).')
change(f,34,r'''Exemplos de M. Raynaud (XVI, 1.1(a),
\SGARefLink{sga3:viii:proposition:7:9:item:b}{(b)})''',r'''Exemplos de M. Raynaud (XVI 1.1 a) e
\SGARefLink{sga3:xvi:subsection:1:1:item:b}{b)})''','reading','Remark 7.10 refers to XVI 1.1 a) and b), not to VIII 7.9(b); repaired the hyperlink destination and restored e.')
