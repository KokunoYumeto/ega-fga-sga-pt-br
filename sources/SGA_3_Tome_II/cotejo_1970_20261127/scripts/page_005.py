from audit import *
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
change(f,5,r'''uma
decomposição em soma direta
\[
  \mathscr O_S=\bigoplus_{m\in M}\mathscr L_m.
\]''',r'''uma decomposição de \(\mathscr O_S\) em soma direta de módulos
\(\mathscr L_m\) (\(m\in M\)).''','1970 restored','P. 5, primeira linha: a decomposição é escrita em prosa, sem a fórmula em destaque acrescentada.')
change(f,5,r'Teorema~1.2}. \qed',r'Teorema~1.2}.','typesetting','P. 5: a conclusão da demonstração não tem símbolo de fim de prova.')
f='08_expose_viii/components/02_corolario_1_4_hasta_observacion_1_7_4.tex'
block(f,5,'% Tradução brasileira revista','\\medskip', '% SGA 3, Exposé VIII, tradução brasileira.\n% Autoridade: LNM 152 (1970), pp. 5--6.\n\n','structure','Autoridade e extensão do componente correspondem às páginas 5–6 da impressão de 1970.')
block(f,5,'\\footnote{Nota do editor: a discussão seguinte', '\\medskip\n\\noindent\\SGARefTarget{sga3:viii:corollary:1:5}',r'''\SGARefTarget{sga3:viii:corollary:1:4:discussion:01}
Daí se deduz um isomorfismo de funtores sobre \(S\):
\SGARefTarget{sga3:viii:eq:1:4:1}
\[
  \underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(M_S,N_S)
  \longrightarrow
  \underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(D(N_S),D(M_S)).
\]
Por outro lado, define-se de maneira evidente um homomorfismo
\SGARefTarget{sga3:viii:eq:1:4:2}
\[
  \underline{\operatorname{Hom}}_{\mathrm{gr}}(M,N)_S
  \longrightarrow
  \underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(M_S,N_S),
\]
que é sempre um monomorfismo e que é um isomorfismo desde que \(M\) seja
de tipo finito. Obtém-se assim:

''','re-edition removed','P. 5, depois de 1.4: são impressos somente dois breves parágrafos e dois Hom sem números; não há avaliação em T, aplicação theta, decomposição M_1+M_2, prova para Z/rZ, notas editoriais, itens (a)/(b) anunciados ou remissão a 1.7. As setas não levam sinal de isomorfismo.')
