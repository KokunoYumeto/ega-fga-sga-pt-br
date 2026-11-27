from audit import *
f='08_expose_viii/components/07_seccion_5.tex'
change(f,19,'Como foi observado durante a demonstração, o','Como assinalamos durante a demonstração, o','translation','P. 19, abertura: Comme nous l’avons signalé; conservada a primeira pessoa do plural.')
s=(ROOT/'sources'/f).read_text();a=s.index('\\noindent\\SGARefTarget{sga3:viii:corollary:5:6}');b=s.index('\\medskip',a);old=s[a:b]
change(f,19,old,old.replace('\\sigma','s'),'1970 restored','P. 19, Corolário 5.6: a seção chama-se s e o morfismo é g ↦ s.g, não sigma.')
change(f,19,'(respectivamente, de apresentação finita)','(resp. de apresentação finita)','translation','P. 19, 5.8 conserva resp., conforme o padrão de registro anexo.')
change(f,19,'V, Proposição \\SGARefLink{sga3:v:proposition:9:1}{9.1}','V, \\SGARefLink{sga3:v:proposition:9:1}{9.1}','translation','P. 19, última linha: Exp V 9.1, sem o nome Proposição.')
