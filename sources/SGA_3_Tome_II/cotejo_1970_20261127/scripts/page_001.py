from audit import *
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
block(f,1,'% Tradução brasileira revista',r'\SGARefTarget{sga3:viii:chapter:viii}', '% SGA 3, Exposé VIII, tradução brasileira.\n% Autoridade: LNM 152 (1970), pp. 1--5.\n\n','structure','Substituição da autoridade editorial pelo escaneamento LNM 152, pp. 1–5; comentários de trabalho alheios ao texto retirados.')
change(f,1,r'\textit{A. Grothendieck}',r'\textit{por A. Grothendieck}','translation','A página imprime «par A. GROTHENDIECK».')
block(f,1,r'Seja \(\mathscr C\)', 'Este corresponde',r'''Seja \(\mathscr C\) uma categoria, que identificamos, como de costume, com uma
subcategoria plena de \(\widehat{\mathscr C}
=\underline{\operatorname{Hom}}(\mathscr C,(\mathrm{Ens}))\)
(cf. Exposé~I). Seja \(I\) um funtor-grupo comutativo, isto é, um objeto de
\(\widehat{\mathscr C}\) munido de uma estrutura de grupo comutativo
(loc. cit.). Para todo grupo \(G\) em \(\widehat{\mathscr C}\), ponhamos
\[
  D(G)=\underline{\operatorname{Hom}}_{\mathrm{gr}}(G,I);
\]
desse modo se obtém um funtor contravariante \(D\) da categoria dos
\(\widehat{\mathscr C}\)-grupos para a categoria dos
\(\widehat{\mathscr C}\)-grupos comutativos. Por definição, para um objeto
variável \(S\) de \(\mathscr C\), tem-se um isomorfismo funtorial:
\SGARefTarget{sga3:viii:eq:1:x}
\begin{equation}
  \tag{x}
  D(G)(S)=\operatorname{Hom}_{S\text{-}\mathrm{gr}}(G_S,I_S),
\end{equation}
onde \(G_S=G\times S\) e \(I_S=I\times S\) são considerados como
\(S\)-grupos, isto é, como grupos em \(\widehat{\mathscr C}_{/S}\).
O segundo membro do isomorfismo anterior também pode ser interpretado como
o subconjunto de \(\operatorname{Hom}(G\times S,I)\) formado pelos morfismos
\(G\times S\to I\) que são «\emph{multiplicativos em relação ao primeiro
argumento} \(G\)». Aliás, as fórmulas anteriores valem mais geralmente
quando \(S\) é um objeto qualquer de \(\widehat{\mathscr C}\), não
necessariamente proveniente de \(\mathscr C\). Se agora tomamos como
\(S\) um grupo em \(\widehat{\mathscr C}\), que denotamos por \(G'\),
então, no primeiro membro \(\operatorname{Hom}(G',D(G))\) de
\(\SGARefLink{sga3:viii:eq:1:x}{(x)}\), podemos distinguir o subconjunto
\(\operatorname{Hom}_{\mathrm{gr}}(G',D(G))\) compatível com as estruturas
de grupo de \(G'\) e \(D(G)\).

''','1970 restored','P. 1, da primeira frase ao fim: Hom(C,(Ens)) não tem C oposta; Hom definidor de D é sublinhado. A definição adicional de Hom(X,I), a explicação de subobjeto/subgrupo e a nota editorial não são impressas; restauradas a ordem das frases e a referência loc. cit.')
