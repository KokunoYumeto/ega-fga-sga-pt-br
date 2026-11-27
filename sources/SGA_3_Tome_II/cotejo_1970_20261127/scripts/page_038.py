from audit import change,block
f='09_expose_ix/components/01_apertura_y_seccion_1.tex'
change(f,38,'Subentende-se, em geral, que, quando a palavra','Convenciona-se, em geral, que, quando a palavra','translation','Page 38 begins On convient de façon générale, an explicit convention.')
change(f,38,r'''traduz-se por «diagonalizável». As cinco noções introduzidas se dispõem no
diagrama de implicações seguinte, que resulta das relações correspondentes
entre as topologias consideradas:''',r'''traduz-se por «diagonalizável». Entre as cinco noções introduzidas,
tem-se o diagrama de implicações seguinte, que resulta das relações
correspondentes entre as topologias em questão:''','translation','The original says Entre les cinq notions introduites, on a le diagramme; preserve the impersonal construction.')
change(f,38,r'\node (general) at (0,4.0) {tipo multiplicativo geral};',r'\node (general) at (0,4.0) {t. m. geral};','reading','The top node of the printed implication diagram is abbreviated t. m. général.')
block(f,38,'Para as aplicações, assinalemos', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:definition:1:3}',r'''Do ponto de vista prático, assinalemos desde já que todos os grupos de
tipo multiplicativo que encontraremos serão quase-isotriviais; assim,
veremos no exposé seguinte que, quando \(G\) é de tipo finito sobre
\(S\), então \(G\) é automaticamente quase-isotrivial, mas daremos
exemplos em que não é localmente isotrivial. Veremos ali igualmente que
\(G\) pode ser localmente trivial, sem ser isotrivial nem a fortiori
trivial (o que implica facilmente que as inclusões do
\SGARefLink{sga3:ix:diagram:1:2}{diagrama precedente} são estritas).
Por outro lado, veremos ali igualmente que, quando \(S\) é localmente
noetheriano e normal (mais geralmente, geometricamente unirramoso),
então todo grupo de tipo multiplicativo de tipo finito sobre \(S\)
é necessariamente isotrivial, e além disso trivial desde que seja
localmente trivial (ou somente trivial sobre um aberto denso). Isso
explica que a maioria dos grupos de tipo multiplicativo que se
encontrarão na prática será provavelmente isotrivial, tanto mais que
veremos adiante que os \emph{toros maximais dos esquemas em grupos
semissimples} são automaticamente isotriviais.
''','re-edition removed','The entire lower passage is one paragraph. The scan has no X 4.5 or X 5.16 references; removed both. Restored the parenthesis about strict inclusions, sans doute as probably, and emphasis only on the final phrase about maximal tori.')
