from audit import *
f='08_expose_viii/components/03_seccion_2.tex'
change(f,7,'liso','suave','translation','P. 7: lisse em 2.1(e) e sua demonstração; aplicado o termo suave fixado em STANDARDS_20261119b.',6)
change(f,7,'lisas','suaves','translation','P. 7: fibres géométriques lisses; concordância do termo suave.',1)
change(f,7,'% SGA-SRC-000078, ACEITO: original \\mu_i(k), atual \\mu_{n_i}(k).\n','','structure','P. 7 imprime mu_i(k); a leitura já estava correta no corpo. Retirado comentário que contrapõe uma leitura atual à original.')
change(f,7,r'é primo a \(p\). \hfill\(\square\)',r'é primo a \(p\), c.q.d.','1970 restored','A demonstração termina com cqfd., não com um quadrado.')
f='08_expose_viii/components/04_seccion_3.tex'
block(f,7,'% Tradução brasileira revista','\\SGARefTarget{sga3:viii:section:3}', '% SGA 3, Exposé VIII, tradução brasileira: §3.\n% Autoridade: LNM 152 (1970), pp. 7--10.\n\n','structure','Comentário de autoridade referido às páginas 7–10 de LNM 152.')
