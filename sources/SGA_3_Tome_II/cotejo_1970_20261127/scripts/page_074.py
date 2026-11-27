from audit import block,change
f='09_expose_ix/components/09_seccion_8_y_bibliografia.tex'
change(f,74,'% Escopo: §8 integral, bibliografia final e notas editoriais 49--55.\n% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 74--76.','% Escopo: §8 integral.\n% Autoridade: SGA 3, LNM 152 (1970), páginas impressas 74--76.','structure','Pp. 74–76: source authority is the 1970 printing; editorial notes and additional bibliography are not its structure.')
change(f,74,'Este número tardio é independente\ndas Seções','Este número-remorso é independente\ndos números','translation','P. 74, original starred note: Ce numéro-remords est indépendant des nos 3 à ...; the final numeral is hidden by the binding shadow, and 7 is retained contextually as the preceding section endpoint.')
block(f,74,r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:scholium:8:0}',r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:proposition:8:1}',r'\SGARefTarget{sga3:ix:scholium:8:0}%'+'\n\n','re-edition removed','P. 74 proceeds directly from section 8 heading/starred July 1969 note to Proposition 8.1. The entire added Scholium 8.0, editor footnote and character-independence statement are absent; only its invisible target survives.')
block(f,74,r'\textbf{Proposição 8.1.}',r'\SGARefTarget{sga3:ix:eq:8:1:1}',r'''\textbf{Proposição 8.1.}
\textit{Seja \(G\) um grupo algébrico diagonalizável
(resp. de tipo multiplicativo). Então para todo
subesquema em grupos \(H\) de \(G\), \(H\) e \(G/H\)
são diagonalizáveis (resp. de tipo multiplicativo).}

A definição \SGARefLink{sga3:ix:definition:1:1}{1.1}
nos reduz imediatamente ao caso não resp. Uma passagem
ao limite fácil, utilizando VI\(_B\)
\SGARefLink{prop:sga3-VIB-11.13}{11.13} e
\SGARefLink{sga3:viii:theorem:3:1}{VIII 3.1}, nos reduz
ao caso em que \(G\) é de tipo finito sobre \(k\).
Em virtude de VI\(_B\)
\SGARefLink{thm:sga3-VIB-11.16}{11.16}, pode-se
encontrar uma família finita de elementos não nulos
''','1970 restored','P. 74, 8.1: groupe algébrique, no separately supplied base-field hypothesis, resp. abbreviations and original nous ramène wording. VI_B 11.13 and VI_B 11.16 retained.')
change(f,74,r'''f_i=\sum_m a_{im}m,\qquad a_{im}\in k,''',r'''f_i=\sum a_{im}m\qquad a_{im}\in k''','1970 restored','P. 74, (8.1.1): summation sign has no lower index and no comma separates the two parts or follows the formula; enlarged.')
change(f,74,r'''do anel afim \(k(M)\) de \(G=D_k(M)\), tal que os pontos de \(H\),
com valores em uma \(k\)-álgebra arbitrária \(k'\), são precisamente os
pontos \(g\in G(k')\) para os quais''',r'''do anel afim \(k(M)\) de \(G=D_k(M)\), tal que os
pontos de \(H\) (com valores em uma \(k\)-álgebra
arbitrária \(k'\)) são os pontos \(g\in G(k')\) tais
que se tenha''','1970 restored','P. 74: values clause is parenthetical; sont les points ... tels que l’on ait, with no added precisely.')
change(f,74,r'''\qquad \lambda_i(g)\in k',''',r'''\qquad\text{para }\lambda_i(g)\in k',''','1970 restored','P. 74, (8.1.2): prints pour before lambda_i(g) in k prime.')
change(f,74,r'''onde \(\tau_g\) designa a translação por \(g\). Ora,''',r'''onde \(\tau_g\) denota a translação por \(g\). Ora tem-se''','translation','P. 74: où tau_g désigne la translation par g. Or on a.')
change(f,74,r'''\tau_g f_i=\sum_m a_{im}\chi_m(g)m,''',r'''\tau_g f_i=\sum a_{im}\chi_m(g)m,''','1970 restored','P. 74, (8.1.3): summation sign has no lower index.')
change(f,74,r'''onde \(\chi_m:G\to\mathbf G_{m,k}\) é o caráter associado a \(m\).
Portanto, \SGARefLink{sga3:ix:eq:8:1:2}{(8.1.2)} equivale a''',r'''\(\chi_m:G\to\mathbf G_{m,k}\) sendo o caráter associado
a \(m\), de modo que
\SGARefLink{sga3:ix:eq:8:1:2}{(8.1.2)} equivale à relação''','1970 restored','P. 74: participial character clause and de sorte que ... équivaut à la relation.')
block(f,74,r'''onde \(Z_i\) designa''',r'''Seja \(N\) o subgrupo de \(M\)''',r'''\(Z_i\) denotando o conjunto dos \(m\in M\) tais que
\(a_{im}=0\).

''','1970 restored','P. 74 ends with a_im = 0 (equality, enlarged at 5x), not a_im nonzero. The extra equivalent character-difference formula after (8.1.4) is absent and removed.')
