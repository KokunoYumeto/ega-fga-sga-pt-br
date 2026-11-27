from audit import *
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
change(f,4,r'=\operatorname{Hom}_{S\text{-}\mathrm{gr}}(M_S,\mathbf G_m)',r'=\underline{\operatorname{Hom}}_{S\text{-}\mathrm{gr}}(M_S,\mathbf G_m)','reading','Definição 1.1: o Hom interno está sublinhado.')
change(f,4,'é um isomorfismo.\\footnote{Nota do editor: foi acrescentada a frase\nseguinte.} Por conseguinte, o grupo diagonalizável \\(D(M_S)\\) também é\nreflexivo.','é um isomorfismo.','re-edition removed','Teorema 1.2 termina em est un isomorphisme; a nota e a consequência sobre D(M_S) não figuram em 1970.')
change(f,4,'Levando em conta as definições, isso decorre do\n\\SGARefLink{sga3:viii:corollary:1:3}{enunciado seguinte}, aplicado a um\npré-esquema \\(S\'\\) sobre \\(S\\).','Levando em conta as definições, isso equivale ao\n\\SGARefLink{sga3:viii:corollary:1:3}{enunciado seguinte} (que aplicaremos\na um pré-esquema \\(S\'\\) sobre \\(S\\)):','1970 restored','A transição imprime cela équivaut, não apenas uma implicação; restauração da equivalência e do parêntese.')
change(f,4,r'''  \mathbf G_{m,S}
  =\operatorname{GL}(1)_S
  =\operatorname{Aut}_{\mathscr O_S\text{-}\mathrm{mod}}(\mathscr O_S).''',r'''  \mathbf G_m
  =\operatorname{GL}(1)
  =\underline{\operatorname{Aut}}_{\mathscr O_S\text{-}\mathrm{Módulo}}(\mathscr O_S),''','reading','Na demonstração, a identidade definidora imprime G_m = GL(1) = Aut_{O_S-Module}(O_S), sem os dois subscritos S acrescentados; Aut é interno.')
change(f,4,'(cf. I,\n\\SGARefLink{sga3:i:subsection:4-7}{4.7}). Por I,\n\\SGARefLink{sga3:i:proposition:4-7-3}{4.7.3}, isso também equivale a dar\numa graduação de tipo \\(M\\)', '(cf. I). Por loc. cit., isso também equivale a dar\numa \\emph{graduação de tipo} \\(M\\)','re-edition removed','Demonstração de 1.3: a página imprime cf. I e par loc. cit., sem os números 4.7 e 4.7.3; graduation de type recebe ênfase.')
