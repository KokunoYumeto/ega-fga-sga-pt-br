from audit import *
import re
f='08_expose_viii/components/02_corolario_1_4_hasta_observacion_1_7_4.tex'
block(f,6,'\\begin{enumerate}', 'O Corolário~',r'''\SGARefTarget{sga3:viii:corollary:1:5:item:a}
\textit{Sejam \(M,N\) dois grupos comutativos ordinários, \(M\) de tipo
finito; então \(\underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}
(D(N_S),D(M_S))\) é representável e tem-se um isomorfismo}
\[
  \operatorname{Hom}_{\mathrm{gr}}(M,N)_S
  \xrightarrow{\ \sim\ }
  \underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(D(N_S),D(M_S)).
\]

\SGARefTarget{sga3:viii:corollary:1:5:item:b}
Daí se conclui, mais geralmente, que, se \(G,H\) são localmente
diagonalizáveis, sendo \(H\) de tipo finito, então
\(\underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(G,H)\) é
representável.
''','structure','P. 6: 1.5 não possui itens (a) e (b); a representabilidade precede o isomorfismo. A generalização é um parágrafo após o corolário, não parte de seu enunciado.')
s=(ROOT/'sources'/f).read_text();start=s.index('\\medskip\n\\noindent\\SGAInlineRefTarget{sga3:viii:paragraph:1-7}')
old=s[start:]
anchors=re.findall(r'\\SGA(?:Inline)?RefTarget\{[^{}]+\}',old)
change(f,6,old,'\n'.join(anchors)+'\n','re-edition removed','P. 6: imediatamente após 1.6 começa §2. Retirada integralmente a seção 1.7, Escolio 1.7.1, Lema 1.7.2 e prova, Corolário 1.7.3, Observação 1.7.4, notas e diagramas; preservados somente os alvos invisíveis exigidos pelo roteiro.')
f='08_expose_viii/components/03_seccion_2.tex'
block(f,6,'% Tradução brasileira revista','\\SGARefTarget{sga3:viii:section:2}', '% SGA 3, Exposé VIII, tradução brasileira: §2.\n% Autoridade: LNM 152 (1970), pp. 6--7.\n\n','structure','Comentário de autoridade atualizado para as páginas 6–7 da impressão de 1970.')
change(f,6,'quase compacto sobre','quase-compacto sobre','translation','P. 6, 2.1(a), quasi-compact; grafia prescrita pelo padrão terminológico anexo.')
