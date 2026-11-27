# Verificação da publicação (27 de novembro de 2026)

Feita por Claude (Claude Opus 5.5, esforço max), ao receber o resultado do cotejo de GPT-6 Astra (OpenAI, modo
ChatGPT Pro), antes da publicação v2026-11-27-sga3-1970.

## Compilação

Os dois mestres, `ptbr_current.tex` e `ptbr_original.tex`, foram compilados com pdfLaTeX (MiKTeX), três passagens
cada, a partir desta pasta.

Na primeira compilação houve 159 erros, todos nos diagramas `tikz-cd`. Aqui o arquivo `brazilian.ldf` existe, e o
babel torna `"` um caractere ativo, o que quebra os rótulos `"..."` das setas. No ambiente do cotejo esse arquivo não
estava instalado (veja `records/BUILD_SETUP.md`), e por isso o problema não apareceu lá. Correção, só na composição:
`\usetikzlibrary{babel}` em `build_support.tex`. O texto não foi alterado.

Depois da correção, para cada mestre:

| | `ptbr_current` | `ptbr_original` |
|---|---:|---:|
| Páginas | 43 | 43 |
| Erros de LaTeX | 0 | 0 |
| Caixas excedentes (overfull) | 0 | 0 |
| Caixas deficientes (underfull) | 0 | 0 |
| Referências indefinidas | 0 | 0 |
| Caracteres ausentes | 0 | 0 |

O texto extraído dos dois PDFs é idêntico. Esta compilação usa a hifenização portuguesa, que faltava no ambiente do
cotejo.

## Páginas olhadas

Páginas do PDF olhadas: 5 (nota desta edição e créditos), 22 (Exposição VIII, §7, com diagrama e nota de rodapé) e
26 (Exposição IX, §1, com o diagrama de implicações). Nada sai da margem, e os rótulos dos diagramas estão no lugar.

## Comparação com o impresso

Duas páginas impressas foram comparadas com o escaneamento de 1970 (LNM 152):

- p. 25: o fim do §6 da Exposição VIII, o Corolário 6.7, a Observação 6.8 e o início do §7. Frase por frase, a
  tradução segue o impresso. O Lema 6.8.1 da reedição não aparece no texto; seus destinos ficam apenas como âncoras
  invisíveis.
- p. 54: a segunda metade da demonstração de IX 4.4 e o enunciado do Lema 4.5. A tradução segue o impresso. A
  desigualdade junto à dobra, $(Z_n^i)_P\ne(Y_n^i)_P$, é a reconstrução assinalada em C0286. É compatível com o
  início visível e com a frase.
