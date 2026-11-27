from audit import change
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(f,27,r'''\(u:G\to H\) é uma imersão fechada (respectivamente, uma imersão)
equivale então a dizer que \(u\) é um monomorfismo, o que se verifica
por hipótese, e é próprio (respectivamente, próprio em todo ponto de
\(u(G)\)).''',r'''\(u:G\to H\) é uma imersão (resp. uma imersão fechada)
equivale então a dizer que \(u\) é um monomorfismo (o que é verdadeiro
por hipótese) e que \(u\) é próprio em todo ponto de \(u(G)\)
(resp. que \(u\) é próprio).''','1970 restored','The scan first discusses immersion/local properness, then respectively closed immersion/properness. The supplied Portuguese reversed the order.')
change(f,27,'anel de valorização discreta, completo se desejado','anel de valoração discreta, completo se desejado','translation','The valuation-ring reduction uses valuation, standardized as valoração.')
change(f,27,'propriedade local foi omitido em EGA~II, 7.3, e deveria aparecer como errata em\nEGA~IV.','propriedade local foi omitido em EGA~II, 7, e figurará como retificação em\nEGA~IV.','1970 restored','The parenthesis prints EGA II 7 (not 7.3) and the future figurera en remords dans EGA IV.')
change(f,27,r'\footnote[0]{Cf. EGA~IV\(_3\), 15.7.}',r'\footnote[0]{Cf. EGA~IV 15.7.1.}','1970 restored','Original footnote (*): Cf. EGA IV 15.7.1.; no fascicle subscript.')
change(f,27,'um anel de valorização discreta completo, com a ressalva','um anel de valoração discreta completo, com a ressalva','translation','valuation discrète complet: standard valoração.')
change(f,27,'Seja \\(S\\) o espectro de um anel de valorização discreta, com','Seja \\(S\\) o espectro de um anel de valoração discreta, com','translation','Lemma 7.1: valuation discrète; standard valoração.')
change(f,27,r'''um subpré-esquema de \(H\). Existe seu fecho esquemático \(L\) em
\(H\), o menor subpré-esquema fechado de \(H\) que contém \(L'\), cf.
EGA~I, 9.5. É também o único subpré-esquema fechado de \(H\), plano sobre
\(S\), cuja fibra genérica é \(L'\). A formação de \(L\) é funtorial
no par \((H,L')\) e comuta com os produtos fibrados sobre \(S\).''',r'''um subpré-esquema de \(H\). Então o fecho esquemático \(L'\) em
\(H\) (isto é, o menor subpré-esquema fechado de \(H\) que contém
\(L'\), cf. EGA~I 9.5) existe e é também o único subpré-esquema fechado
de \(H\), plano sobre \(S\), cuja fibra genérica é \(L'\). Além disso,
a formação de \(L\) é funtorial em relação a um par \((H,L')\)
variável e comuta com a formação de produtos cartesianos sobre \(S\).''','1970 restored','The scan literally writes l’adhérence schématique L′ dans H, and only later la formation de L. Restored that prime and the original sentence, including variable pair and Cartesian products.')
