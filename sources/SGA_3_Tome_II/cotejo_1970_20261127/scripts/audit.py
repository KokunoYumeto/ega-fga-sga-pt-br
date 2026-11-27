"""Portable helpers for the sequential, human/model-directed collation.

No automatic claim of reading or verification is made by this module.
Calls to done() and confirm() must follow actual visual inspection.
"""
from pathlib import Path
import csv, json, collections
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['file','printed_page','line','old','new','kind','evidence','confidence']

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def rows():
    p=ROOT/'CORRECTIONS.tsv'
    return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []

def write_rows(rr):
    with (ROOT/'CORRECTIONS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader();w.writerows(rr)

def change(file,page,old,new,kind,evidence,count=1):
    p=ROOT/'sources'/file
    s=p.read_text()
    if old:
        assert s.count(old)==count,(file,s.count(old),old[:100])
        line=s[:s.index(old)].count('\n')+1
        s=s.replace(old,new,count)
    else:
        assert count==1
        line=s.count('\n')+1;s+=new
    p.write_text(s)
    rr=rows()
    rr.append(dict(zip(FIELDS,[f'sources/{file}',str(page),str(line),old,new,kind,evidence,'pending second reading'])))
    write_rows(rr)
    return len(rr)

def block(file,page,start,end,new,kind,evidence):
    s=(ROOT/'sources'/file).read_text();i=s.index(start);j=s.index(end,i)
    return change(file,page,s[i:j],new,kind,evidence)

def confirm(page,detail='confirmed; second visual reading of enlarged scan crop'):
    rr=rows()
    for r in rr:
        if r['printed_page']==str(page) and r['confidence'].startswith('pending'):
            r['confidence']=detail+'; '+utc()
    write_rows(rr)

def done(page,scope,findings,statements=()):
    p=ROOT/'records/pages.json'
    d=json.loads(p.read_text()) if p.exists() else []
    assert page==len(d)+1,(page,len(d))
    d.append({'page':page,'scan_page':page+7,'scope':scope,'findings':findings,'utc':utc()})
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
    eventfile=ROOT/'CHECK_EVENTS.tsv'
    with eventfile.open('a',newline='') as f:
        w=csv.writer(f,delimiter='\t')
        if f.tell()==0:w.writerow(['statement_id','date','who','type','outcome'])
        for st in statements:
            w.writerow([st,utc(),'GPT-6 Astra Pro (OpenAI); reasoning effort not exposed; run 20261127-1970','carried as background without fault found',f'Read in sequential source collation, printed page {page}; no independent re-proof claimed.'])
    report()
    with (ROOT/'progress.log').open('a') as f:f.write(f'page {page} done {utc()}\n')

def report():
    p=ROOT/'records/pages.json'; pp=json.loads(p.read_text()) if p.exists() else []
    rr=rows(); counts=collections.Counter(r['kind'] for r in rr)
    s='# Cotejo com SGA 3, LNM 152 (1970)\n\n'
    s+='Autoridade: escaneamento anexo, páginas impressas 1–76 (páginas 8–83 do PDF). A leitura e as decisões textuais são do agente principal, em uma única sequência.\n\n'
    s+='## Totais por espécie\n\n| Espécie | Alterações |\n|---|---:|\n'
    for k,v in sorted(counts.items()):s+=f'| {k} | {v} |\n'
    s+=f'\nPáginas concluídas: {len(pp)}/76. Linhas de correção: {len(rr)}.\n\n'
    s+='## Passagens da reedição retiradas\n\n'
    for i,r in enumerate(rr,1):
        if r['kind']=='re-edition removed':s+=f'- C{i:04d}, p. {r["printed_page"]}: {r["evidence"]}\n'
    catalog=ROOT/'records/REMOVAL_CATALOG.json'
    if catalog.exists():
        s+='\n### Retiradas incluídas em outras espécies de correção\n\nA espécie principal continua registrada na tabela. A lista abaixo completa o catálogo com acréscimos, remissões e estruturas retirados dentro de restituições mais amplas. Não inclui supressões provisórias posteriormente retiradas.\n\n'
        for item in json.loads(catalog.read_text()):
            s+=f'- {item["correction_id"]}, p. {item["printed_page"]}: {item["description"]}\n'
    s+='\n### Comentários e matéria fora do recorte\n\nOs comentários de autoridade e de trabalho foram depurados nos componentes e nas montagens. Os comentários com leituras corretivas foram retirados junto das respectivas restituições. O índice geral do tomo II e as entradas do sumário para os exposés X–XVIII foram suprimidos por estarem fora das páginas 1–76 solicitadas; isso é uma delimitação de escopo, não uma atribuição desses materiais à reedição (C0377–C0382). Os nomes de arquivo e destinos recebidos permanecem.\n'
    s+='\n## Método e limites dos eventos\n\nCada seção abaixo corresponde à leitura visual da página inteira, à comparação do português e à inspeção ampliada das fórmulas alteradas. As imagens e extrações do escaneamento são material temporário e não integram a entrega. Eventos de simples leitura não são apresentados como demonstrações independentes. A coluna `line` indica a linha do arquivo imediatamente antes da alteração; `old` e `new` permitem localizar o trecho mesmo após outras alterações.\n\n'
    for p in pp:
        s+=f'## Página impressa {p["page"]}\n\n- PDF do escaneamento: página {p["scan_page"]}.\n- Escopo: {p["scope"]}\n- Cotejo: {p["findings"]}\n- Conclusão da leitura sequencial: {p["utc"]}.\n'
        if 'final_review' in p:
            q=p['final_review']
            s+=f'- Revisão dirigida: {q["utc"]}; '+', '.join(q['corrections'])+'. '+q['result']+'\n'
        s+='\n'
    (ROOT/'CHECK_RECORD.md').write_text(s)

if __name__=='__main__':
    report()
