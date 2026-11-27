from audit import change
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(f,29,r'''Substituindo \(H\) por \(H'\), podemos reduzir-nos, com a ressalva habitual,
ao caso''',r'''Substituindo \(H\) por \(H'\), podemos, para provar que \(u\) é uma
imersão, reduzir-nos, com a ressalva habitual, ao caso''','1970 restored','The reduction to bijectivity is explicitly qualified pour prouver que u est une immersion.')
change(f,29,r'\kappa(s)',r'k(s)','reading','Both occurrences on page 29 use the Roman residual-field notation k(s), not Greek kappa.',count=2)
change(f,29,r'''reduzido pelo teorema de Cartier (cf.
VI\(_B\), 1.6.1; VII\(_B\), 3.3.1; ou EGA~IV\(_4\), 16.12.2 e 17.12.5).''',r'''reduzido segundo Cartier (VII\(_B\) 3.3.1, ou EGA~IV 16.12.2 e 17.12.5).''','re-edition removed','The scan has only Cartier (VII_B 3.3.1, ou EGA IV 16.12.2 et 17.12.5), without VI_B 1.6.1, cf., or the fascicle subscript.')
change(f,29,r'''apresentação finita sobre \(S\). Se \(u\) é um monomorfismo, \(G\) é
plano sobre \(S\), e todo corpo residual de \(S\) tem característica
zero, então \(u\) é uma imersão.}''',r'''apresentação finita sobre \(S\). Suponhamos que \(u\) seja um monomorfismo,
\(G\) plano sobre \(S\), e os corpos residuais de \(S\) de característica
zero. Então \(u\) é uma imersão.}''','translation','Proposition 7.2: Supposons que ... Alors u est une immersion; preserve the first-person plural formulation.')
change(f,29,r'''Suponhamos agora que \(k(s)\) tenha característica \(p>0\), e
restrinjamo-nos ao caso em que \(G\) é comutativo.''',r'''Quando \(k(s)\) é de característica \(p>0\), vamos nos limitar ao caso
em que \(G\) \emph{é comutativo}.''','translation','The next paragraph begins Lorsque k(s) ... nous allons nous borner; est commutatif is underlined.')
change(f,29,r"esquemático de \(H_{s'}\simeq G_{s'}\).",r"esquemático de \(H_{s'}\simeq G_{s'}\), portanto comutativo.",'1970 restored','The original repeats donc commutatif after the generic-fibre identification.')
change(f,29,'onde \\(V\\) é o anel de valorização que define','onde \\(V\\) é o anel de valoração que define','translation','The ring V is an anneau de valuation; standard valoração.')
change(f,29,'núcleos da multiplicação por \\(m\\) em \\(G\\) e \\(H\\).','núcleos da potência \\(m\\)-ésima em \\(G\\) e \\(H\\).','1970 restored','The text says noyaux de la puissance m-ème, not multiplication by m.')
change(f,29,r'Por VI\(_A\), \SGARefLink{sga3:viii:corollary:3:2}{3.2}',r'Por VI\(_A\), \SGARefLink{sga3:via:3:2}{3.2}','reading','The source citation is VI_A 3.2; the old hyperlink incorrectly pointed to VIII 3.2.')
