"""One-time assembly of the two identical standalone masters and scope."""
from pathlib import Path
from audit import change,rows,write_rows,confirm,report,utc,FIELDS
root=Path('work/sources')
for f,title in [('08_expose_viii/body.tex','VIII'),('09_expose_ix/body.tex','IX')]:
 old=(root/f).read_text()
 new='\n'.join([f'% SGA 3, LNM 152 (1970), Exposé {title}.', '% Inclusões relativas ao diretório dos dois mestres.']+[line.replace('units/','') for line in old.splitlines() if line.startswith(r'\input')])+'\n'
 change(f,'assembly',old,new,'structure','Standalone build requested: relative component inclusions replace the absent units/ prefix; obsolete working-draft comments removed; input order and filenames preserved.')
f='99_notation_index/components/01_indice_de_notaciones.tex'
change(f,'assembly',(root/f).read_text(),r'''% O índice geral do tomo II está fora das páginas 1--76 deste recorte.
% Mantém-se o identificador recebido, sem acrescentar texto aos exposés.
\SGARefTarget{sga3:tome2:index:notaciones}%
''','structure','The supplied volume-wide terminal index refers to a scan page 663 that is not in the authority supplied for this task. It is outside Exposés VIII–IX, which end on printed p. 76. Suppress its visible material and editorial comments while preserving file and target.')
f='99_notation_index/body.tex'
change(f,'assembly',(root/f).read_text(),r'''% Compatibilidade de estrutura: índice geral fora do recorte VIII--IX.
\input{99_notation_index/components/01_indice_de_notaciones.tex}
''','structure','Do not print a terminal volume-wide index outside the requested p. 1–76 scope; preserve inclusion and label without page break or running header.')
base=(root/'ptbr_current.tex').read_text()
base=base[:base.index('% SGA-SEG BEGIN T2-FM-000005')]
base=base[base.index(r'\hypersetup'):]
base=base.replace('scan_page=1','source_front_cover').replace('scan_page=2','source_rights_notice').replace('scan_page=3','authority_pdf_page=1').replace('scan_page=4','authority_pdf_page=2')
base=base.replace('pré-esquemas de grupos','pré-esquemas em grupos').replace('ESQUEMA DE GRUPOS','ESQUEMA EM GRUPOS')
base=base.replace('Morfismos essencialmente livres e representabilidade','Morfismos essencialmente livres, e representabilidade')
base=base.replace('teorema de levantamento e conjugação','teorema de levantamento e de conjugação')
base=base.replace('Monomorfismos de grupos de tipo multiplicativo e fatoração canônica de um homomorfismo de um desses grupos','Monomorfismos dos grupos de tipo multiplicativo, e fatoração canônica de um homomorfismo de um tal grupo')
base=base.replace('Algebraicidade','Algebricidade')
note=r'''
\clearpage
\chapter*{Nota desta edição}
\thispagestyle{plain}
Esta edição das Exposições VIII e IX de SGA~3 segue o
texto da impressão de 1970, \emph{Lecture Notes in
Mathematics}~152, páginas~1--76. A tradução brasileira
foi feita inicialmente em 2026 a partir dos rascunhos
da reedição e foi trazida ao texto de 1970 em novembro
de 2026. Nada da reedição permanece no texto, nas notas,
na estrutura ou nos comentários desta edição.

A primeira tradução foi realizada com OpenAI Codex
(GPT-5.6 Sol, esforço de raciocínio \emph{ultra}).
Este cotejo foi realizado com GPT-6.0 Astra (OpenAI),
modo ChatGPT Pro. O esforço de raciocínio deste passe
não foi exposto pela interface.

As gralhas da impressão de 1970 foram conservadas.
O sumário acima usa a paginação original e se limita
às duas exposições aqui reunidas; a paginação desta
composição é própria. Os dois arquivos principais,
\texttt{ptbr\_current.tex} e \texttt{ptbr\_original.tex},
têm conteúdo idêntico e compõem a mesma edição.

\mainmatter
\input{08_expose_viii/body}
\input{09_expose_ix/body}
\input{99_notation_index/body}
\end{document}
'''
new='% SGA 3, Exposés VIII--IX: edição portuguesa segundo LNM 152 (1970).\n'+r'\input{build_support}'+'\n'+r'\begin{document}'+'\n'+base+note
for f in ('ptbr_current.tex','ptbr_original.tex'):
 old=(root/f).read_text()
 def rights(s):return s[s.index(r'\SGACopyrightPage'):s.index('% SGA-SEG END T2-FM-000002')]
 assert rights(old)==rights(new),'rights notice changed'
 change(f,'front matter',old,new,'structure','User-requested standalone master, original-1970 note and model/effort credits; identical master bytes. Preserve rights notice verbatim. Keep only the original contents entries for VIII–IX (authority PDF p. 2), adjust their wording against that page and supplied group-scheme terminology; omit unrelated X–XVIII contents. Front source-page metadata corrected to actual supplied PDF mapping.')
rr=rows()
support=(root/'build_support.tex').read_text()
rr.append(dict(zip(FIELDS,['sources/build_support.tex','assembly','1','',support,'typesetting','New composition support required because supplied masters were fragments without their document class or macros. Defines layout and existing macro names; external unavailable references print their text without invented destinations. No mathematical source claim.','confirmed; second inspection against the input macro inventory and build requirements; '+utc()])))
write_rows(rr)
confirm('assembly','confirmed; second technical inspection of inclusions, scope and all preserved targets; p. 76 scan end checked; no scan reading claimed for build-only changes')
confirm('front matter','confirmed; second inspection of note against user instructions, rights block byte equality, original contents crop and identical masters')
report()
