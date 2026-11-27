from audit import change
f='08_expose_viii/components/08_seccion_6_parte_1.tex'
change(f,22,"Seja \\(Z'\\) um subpré-esquema de \\(Z\\). Ele fornece um monomorfismo","Consideremos um subpré-esquema \\(Z'\\) de \\(Z\\), de onde um monomorfismo",'translation','6.5(a): Considérons un sous-pré-schéma Z′ de Z, d’où un monomorphisme.')
change(f,22,"é fechado em \\(Z\\), então o subfuntor \\(X'\\) de \\(X\\) é representável\npor um subpré-esquema fechado de \\(X\\).}","é fechado em \\(Z\\), então o subfuntor \\(X'\\) de \\(X\\) é representável\npor um subpré-esquema fechado.}",'1970 restored','The conclusion of 6.5(a) ends sous-pré-schéma fermé, with no de X.')
change(f,22,'Suponhamos dadas duas ações de \\(X\\) sobre \\(Y\\) com valores em \\(Z\\),','Dêmo-nos duas maneiras de fazer \\(X\\) atuar sobre \\(Y\\) com valores em \\(Z\\),','translation','6.5(b): Donnons nous deux façons de faire opérer X sur Y à valeurs dans Z.')
change(f,22,r'''ou, equivalentemente, um morfismo
\[
  r:X\times_SY\longrightarrow Z\times_SZ.
\]
Ponha-se''','Ponhamos','re-edition removed','The scan passes directly from the displayed q to posons alors U=Z×_S Z; the separate equivalence and display of r are absent.')
change(f,22,r'''\(P=X\times_SY\) e \(P'\) a imagem inversa da diagonal por \(r\), isto
é, o núcleo de''',r'''\(P=X\times_SY\) e \(P'\) a imagem inversa da diagonal por
\(r:X\times_SY\to Z\times_SZ\), deduzido de \(q_1,q_2\), isto
é, o núcleo de''','1970 restored','At the end of page 22 r is specified here, as deduced from q_1,q_2, before the continuation identifying its kernel.')
