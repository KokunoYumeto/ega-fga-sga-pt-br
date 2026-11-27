from audit import *
f='08_expose_viii/components/07_seccion_5.tex'
change(f,18,r'\(p_i\in M-\{0\}\)',r'\(p_i\in M-0\)','reading','P. 18, 5.3 imprime M-0, sem chaves.')
change(f,18,r'''livremente sobre \(P\) \emph{[a fonte imprime \(P'\)]}''',r'''livremente sobre \(P'\)''','1970 restored','P. 18, prova de 5.4: a impressão traz P′. Retirada a correção para P e o comentário entre colchetes.')
change(f,18,r"m_i'\in M'-\{0\}",r"m_i'\in M'-0",'reading','P. 18, após 1=Σ f_i g_i, imprime M′-0 sem chaves.')
change(f,18,r'''  J_pJ_q\subseteq J_{p+q}
  \qquad\text{y}\qquad''',r'''  J_pJ_q\subset J_{p+q}
  \qquad\text{e}\qquad''','reading','P. 18: inclusão simples e conjunção portuguesa e em lugar do espanhol residual y.')
change(f,18,r'''\(J_m=A_0\)
\emph{[a fonte imprime \(J_p=A_0\)]}''',r'''\(J_p=A_0\)''','1970 restored','P. 18: no conjunto dos m em M, a impressão usa J_p=A_0; restaurado p e retirado o comentário corretivo.')
change(f,18,r'''Isto conclui a demonstração do
\SGARefLink{sga3:viii:theorem:5:1}{Teorema 5.1}.''',r'''Isto conclui a demonstração.''','translation','P. 18 termina Cela achève la démonstration, sem repetição do número 5.1.')
