"""One-shot historical audit-indexing pass; no source edits.

Do not rerun on the final tree: later catalog and page-record additions are
already saved in the delivered JSON records and CHECK_RECORD.md.
"""
import json
from audit import ROOT,rows,report,utc

extra = {
58:"Nota corretiva e argumento ampliado pelos abertos auxiliares na prova de VIII 4.7.",
68:"Notação phi, bar-phi e K′, discussão acrescida dos núcleos, nota de mudança de notação e comentário entre colchetes.",
75:"Correção de P′ para P e comentário corretivo na prova de VIII 5.4.",
78:"Comentário corretivo sobre o índice de J na prova de VIII 5.4.",
96:"Descrição acrescida por Γ e pelo singleton da identidade no enunciado de VIII 6.4.",
120:"Divisão de VIII 6.7 em itens, ausente no enunciado contínuo de 1970.",
167:"Parêntese acrescentado que identificava VIII 7.3 com VII_A 8.5.",
174:"Nota que corrigia os índices de H e S no final da prova de VIII 7.5.",
176:"Correção entre colchetes do índice de G na observação após VIII 7.5.",
182:"Palavra «inteiro» acrescida à existência de ν_1 em VIII 7.7.",
201:"Palavra «diretamente» acrescida à aplicação de VIII 7.12.",
210:"Citação acrescida a VIII 1.1 e divisão em parágrafos/fórmulas destacadas de IX 1.1.",
218:"Travessão e apresentação destacada acrescidos ao enunciado de IX 1.3.",
219:"Índice k acrescido a Hom(G,G_m), subdivisões e ênfases internas de IX 1.4.",
227:"Expansões verbais das setas de equivalência nos itens de IX 2.1.",
229:"Igualdade adicional com ker(...) em IX 2.2.",
240:"Remissão à observação acrescentada 1.4.1(a), substituída pelas considerações após 1.4.",
242:"Alternativas resp. e linguagem adicional de subfuntores na prova de IX 2.10.",
248:"Remissões substitutas VIII 3.1, IX 8.1, VIII 1.5 e VIII 3.2(b) na prova de IX 2.11.",
257:"Círculos de composição acrescentados às fórmulas de IX 3.3.",
262:"Parênteses acrescentados às fórmulas de IX 3.3 bis.",
265:"Adjetivo «fechado» acrescido a S_0=V(J) em IX 3.8.",
275:"Título de prova, igualdade adicional O_X/J^nO_X e premissa de planura repetida em IX 4.2.",
282:"Frase adicional sobre A e B noetherianos e comentário contrário aos índices do diagrama de IX 4.3.",
284:"Identidade adicional de produto para Y′^i na prova de IX 4.3.",
285:"Definição repetida do ideal maximal e adjetivo «fechado» acrescido a S_n.",
295:"Apresentação ampliada por fórmulas destacadas na prova de IX 4.7.",
297:"Título de prova e apresentação destacada acrescidos à prova de IX 4.8.",
318:"Justificação adicional por VIII 6.3 e liberdade essencial, título de prova e quadrado final em IX 5.3.",
325:"Citações adicionais 1.1/2.1(b) e equações substitutas em IX 5.4 bis.",
333:"Construção por chave, notação S_{s,n} e equações tensoriais substitutas em IX 6.2.",
335:"Reestruturação em fórmulas destacadas da prova de IX 6.2.",
337:"Título de prova e condição de isolamento repetida/ampliada em IX 6.3.",
339:"Notação epsilon(t), citação VI_B 1.3 e quadrado final no encerramento de IX 6.3.",
341:"Redefinição adicional de K, título de prova e quadrado final em IX 6.7.",
343:"Citação à numeração acrescida 6.6.1 e título de prova em IX 6.8.",
349:"Redação introdutória ampliada de IX 7.2.",
354:"Quadrado final acrescentado à prova de IX 7.2.",
355:"Título de prova e explicitação adicional de S-homomorfismos em IX 7.3.",
356:"Fórmulas destacadas e quadrado final acrescentados ao encerramento de IX 7.3.",
363:"Palavra «precisamente» acrescida à condição sobre os pontos de IX 8.1.",
369:"Remissão eletrônica a um exposé diferente, incompatível com a referência impressa IV_B 11.16.",
374:"Fórmula substituta étale/Gamma/Hom topológico, retirada na restauração da prova iniciada na p.75.",
375:"Redação adicional sobre descida na observação IX 8.3.",
391:"Desdobramento da prova de VIII 2.1(e) em várias fórmulas destacadas; o impresso tem um parágrafo e uma fórmula destacada.",
396:"Redação independente acrescentada à transição entre VIII 4.6 e 4.7."
}
rr=rows()
catalog=[]
for n,desc in sorted(extra.items()):
 r=rr[n-1]
 assert r['kind']!='re-edition removed'
 catalog.append({'correction_id':f'C{n:04d}','printed_page':r['printed_page'],'description':desc})
(ROOT/'records/REMOVAL_CATALOG.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
p=ROOT/'records/pages.json';pages=json.loads(p.read_text())
for page in pages:
 n=page['page']
 follow=[f'C{i:04d}' for i,r in enumerate(rr,1) if i>=384 and r['printed_page']==str(n)]
 if follow:
  page['final_review']={'utc':utc(),'corrections':follow,'result':'Revisão dirigida posterior à sequência; segunda leitura concluída, com emendas e retiradas explícitas na coluna confidence.'}
p.write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
report()
