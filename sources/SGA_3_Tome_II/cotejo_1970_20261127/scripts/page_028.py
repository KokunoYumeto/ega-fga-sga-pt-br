from audit import change
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(f,28,r'''\renewcommand{\thefootnote}{(\(\ast\ast\))}%
\footnote[0]{Cf. EGA~IV\(_2\), 2.8.}''',r'''\renewcommand{\thefootnote}{(\(\ast\))}%
\footnote[0]{Cf. EGA~IV 2.8.}''','1970 restored','Footnote on page 28 uses one asterisk and cites EGA IV 2.8, with no fascicle subscript.')
change(f,28,r"G\xrightarrow{\,u'\,}L\longrightarrow H",r'G\longrightarrow L\longrightarrow H','1970 restored','The first factorization prints G→L→H without u′ on the arrow; u′ is introduced in the next assertion.')
change(f,28,r"\(S\), e \(u':G\to L\) induz",r'\(S\), e \(G\to L\) induz','1970 restored','The explanatory clause still says G→L, without u′.')
change(f,28,r'é uma imersão, sua imagem \(u(G)\) é um subpré-esquema de \(H\)',r'é uma imersão, sua imagem \(u(G)\) é um subpré-esquema fechado de \(H\)','1970 restored','The scan explicitly prints sous-pré-schéma fermé de H at this point, despite then deriving openness.')
change(f,28,r'''respectivamente isomorfismos (cf. SGA~1, I,
\SGARefLink{sga3:viii:corollary:5:7}{5.7}).''',r'''resp. isomorfismos (cf. SGA~1 I
\SGARefLink{sga1:i:5:7}{5.7}).''','reading','Printed citation is SGA 1 I 5.7; it must not hyperlink to SGA 3 VIII 5.7. The target is kept external to the present volume.')
change(f,28,r'''Como \(G\) e \(H\) são planos sobre \(S\), as dimensões de suas fibras
são constantes (VI\(_B\),
\SGARefLink{sga3:viii:corollary:4:3}{4.3}).''',r'''Notemos primeiro que, como \(G\) e \(H\) são planos sobre \(S\), as
dimensões de suas fibras são constantes (VI\(_B\)
\SGARefLink{sga3:vib:4:3}{4.3}).''','reading','The paragraph begins Notons d’abord. Its reference is VI_B 4.3, not VIII 4.3; repaired the link destination without altering the printed citation.')
change(f,28,r'''De fato, após passar a um
corpo-base algebricamente fechado e reduzir \(G\) e \(H\), ambos são
lisos sobre o corpo e a afirmação é imediata.''',r'''(Reduzimo-nos ao caso em que o corpo-base é algebricamente fechado, e
\(G\) e \(H\) reduzidos, portanto suaves sobre \(k\), onde isso é
imediato\ldots)''','1970 restored','The scan gives this as a parenthesis, explicitly lisses sur k, ending in an ellipsis. Standard lisse → suave.')
