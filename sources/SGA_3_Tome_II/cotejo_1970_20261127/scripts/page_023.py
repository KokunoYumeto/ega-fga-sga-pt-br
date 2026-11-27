from audit import change
f='08_expose_viii/components/09_seccion_6_parte_2.tex'
change(f,23,'% Tradução brasileira revista a partir do workpass espanhol congelado;\n% a fonte permanece em source_es.\n','','re-edition removed','Translation workflow comments are absent from the 1970 text.')
change(f,23,'% Autoridade: Polo--Gille Exp8-8nov09.pdf; edição original: LNM 152, pp. 23--25.','% Autoridade: LNM 152 (1970), pp. 23--25.','structure','Authority for this component is the scan, printed pages 23–25.')
change(f,23,'Suponhamos dado um morfismo','Dêmo-nos um morfismo','translation','6.5(c): Donnons-nous un morphisme.')
change(f,23,'vê introduzindo um segundo morfismo','vê introduzindo um segundo homomorfismo','1970 restored','6.5(c) prints un deuxième homomorphisme.')
change(f,23,r"tomemos o subfuntor \(Y'\)",r"consideremos o subfuntor \(Y'\)",'translation','6.5(d): considérons le sous-foncteur.')
change(f,23,r'''\SGARefLink{sga3:viii:examples:6:5:item:c:01}{(c)}, e denotando por
\(\bar q\) e \(\bar q'\) os morfismos correspondentes,''',r'''\SGARefLink{sga3:viii:examples:6:5:item:c:01}{(c)}, e os homomorfismos
correspondentes a \(q\) e \(q'\):''','1970 restored','6.5(d) introduces les homomorphismes correspondants à q et q′; the following formula names bar q and bar q′.')
