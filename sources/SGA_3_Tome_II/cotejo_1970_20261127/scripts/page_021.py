from audit import change, block
f='08_expose_viii/components/08_seccion_6_parte_1.tex'
change(f,21,'Tomemos\no funtor','Consideremos\no funtor','translation','Theorem 6.4: Considérons le foncteur.')
block(f,21,r'\SGARefTarget{sga3:viii:theorem:6:4:display:functor:01}',r'\smallskip',r'''\SGARefTarget{sga3:viii:theorem:6:4:display:functor:01}
\[
  F=\prod_{Z/S}Y/Z:\;(\mathrm{Sch})_{/S}^{\circ}
    \longrightarrow(\mathrm{Ens})
\]
\textit{definido pela condição: \(F(S')=\varnothing\) quando
\(Z_{S'}\ne Y_{S'}\), e \(F(S')\) se reduz a um elemento no caso
contrário. Esse funtor é representável por um subpré-esquema fechado de \(Z\).}

''','1970 restored','6.4 states the functor through the empty/singleton condition, without Γ or an identity singleton; its last word is Z (not S). The scan category is (Ens).')
block(f,21,'\\smallskip\n\\noindent\\footnote{Nota do editor:', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:viii:examples:6:5}',r'''Notemos primeiro que o funtor considerado é um feixe para a topologia
fielmente plana e quase-compacta, o que nos permite, com as notações de
\SGARefLink{sga3:viii:definition:6:1}{6.1}, limitar-nos ao caso em que
\(S=S_i'\). (Note-se que, em virtude de SGA 1 VIII, os morfismos
fielmente planos e quase-compactos são de descida efetiva para a categoria
fibrada das setas de imersão fechada.) Seja \(Y_j=Y\cap Z_j\), e seja
\(F_j:(\mathrm{Sch})_{/S}^{\circ}\to(\mathrm{Ens})\) o funtor definido
em termos de \((Z_j,Y_j)\) como \(F\) em termos de \((Z,Y)\).
É um subfuntor do funtor final, e temos evidentemente
\(F=\bigcap_i F_j\), o que nos reduz a provar que cada \(F_j\) é
representável por um subesquema fechado \(T_j\) de \(S\) (pois então
\(F\) será representável pelo subesquema fechado \(T\), interseção dos
\(T_j\)). Podemos, portanto, supor \(Z\) também afim,
\(Z=\operatorname{Spec}(B)\), onde \(B\) é um \(A\)-módulo livre.
Seja \(J\) um subconjunto de \(B\) que define o subesquema \(Y\) de
\(Z\), e seja \(K\) o ideal de \(A\) gerado pelos
\(u_i(J)\subset A\), onde os \(u_i:B\to A\) são as formas
coordenadas em relação à base escolhida. Constata-se imediatamente que
\(T=V(K)=\operatorname{Spec}(A/K)\) satisfaz à condição desejada, o
que conclui a demonstração.
''','re-edition removed','The scan gives one short proof: the fpqc sheaf observation, the SGA 1 VIII descent remark, Y_j, F_j and their intersection, and the coordinate ideal K. It has no editorial note, proof of the sheaf assertion, numbered references to SGA 1/EGA, explicit affine cover or definition A=O(S). The printed intersection is indexed i with F_j, and u_i(J)⊂A.')
change(f,21,r'''Daremos alguns exemplos importantes de funtores que se reduzem a funtores
\(\prod_{Z/S}Y/Z\) do tipo considerado em
\SGARefLink{sga3:viii:theorem:6:4}{6.4}, e para os quais serão úteis os
critérios de representabilidade. Aqui \(S\) denota um pré-esquema, e
\(X,Y,Z,\ldots\) denotam pré-esquemas sobre \(S\).''',r'''Demos exemplos importantes de funtores que se reduzem a funtores
\(\prod_{Z/S}Y/S\) do tipo considerado em
\SGARefLink{sga3:viii:definition:6:1}{6.1}, e para os quais é útil,
portanto, ter critérios de representabilidade. Designa-se por \(S\)
um pré-esquema, e por \(X,Y,Z\), etc., pré-esquemas sobre \(S\).''','1970 restored','Examples 6.5 prints ∏_{Z/S}Y/S and the reference 6.1, not Y/Z and 6.4; opening Donnons des exemples.')
change(f,21,'Suponhamos dado um \\(S\\)-morfismo','Dêmo-nos um \\(S\\)-morfismo','translation','6.5(a): Donnons nous un S-morphisme.')
