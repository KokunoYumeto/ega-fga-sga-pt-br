from audit import change
f='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(f,32,r'''\(p\operatorname{id}_{G_0}\) \emph{[a fonte imprime
\(p\operatorname{id}_{G}\)]}; por isso se enunciou explicitamente a
condição no Corolário~\SGARefLink{sga3:viii:corollary:7:5}{7.5}.''',r'''que \(p\operatorname{id}_{G}\) seja plano; por isso explicitamos essa
condição na hipótese do Corolário~\SGARefLink{sga3:viii:corollary:7:5}{7.5}.''','1970 restored','The continuation of the unnumbered remark prints p id_G (without 0), followed by soit plat; restored the printed reading and removed the bracketed correction note.')
change(f,32,r'''e ponhamos \(Q=H/G\), um grupo puramente infinitesimal. Existe um inteiro''',r'''e consideremos o grupo (puramente infinitesimal) \(Q=H/G\). Existe um inteiro''','translation','Lemma 7.6: considérons le groupe (purement infinitésimal) Q=H/G.')
change(f,32,r'''de anéis locais nos elementos identidade. Recordemos que \(Q\) tem,
como suporte conjuntista, o único ponto \(e\). Há um homomorfismo natural''',r'''de anéis locais nos elementos neutros. (N.B.: recorde-se que \(Q\)
se reduz ao elemento \(e\) como conjunto.) Ora, há um homomorfismo natural''','1970 restored','The scan keeps the reminder as (N.B. se rappeler que Q est réduit à l’élément e ensemblistement).')
change(f,32,'Frobenius iterado \\(F^\\nu\\).','Frobenius iterado» \\(F^\\nu\\).','typesetting','The expression homomorphisme de Frobénius itéré is in quotation marks in the original.')
change(f,32,'sobre o núcleo do homomorfismo de\nFrobenius','sobre o núcleo do «homomorfismo de\nFrobenius','typesetting','Restored the opening quotation mark of the same printed expression.')
change(f,32,r'''\(\mathscr O_{Q,e}\) é artiniano, enquanto
\(\bigcap_\nu\mathfrak m^{p^\nu}=0\) em \(\mathscr O_{H,e}\), de modo que''',r'''\(\mathscr O_{Q,e}\) é artiniano; por fim, a interseção, em
\(\mathscr O_{H,e}\), dos \(\mathfrak m^p\) se reduz a zero, de modo que''','1970 restored','The last lines print des m^p, not m^{p^ν}; there is no displayed intersection index ν. The apparently erroneous exponent is preserved.')
