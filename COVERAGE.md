# Cobertura verificável da prévia inicial

| Corpus | Cobertura admitida | Arquivos | Bytes | Estado |
|---|---:|---:|---:|---|
| EGA III-1 | 11 corpos + controlador + preâmbulo | 13 | 604.467 | PDF determinístico de 149 páginas; build/VQA/controle independente PASS |
| FGA tranche A | 149, 182, 190, 195, e195 | 5 | 279.832 | recibos semânticos dedicados PASS |
| SGA 3 tomo II | preliminares, Exp. VIII, Exp. IX, índice | 26 | 281.524 | quatro recibos de unidade PASS |
| SGA 4½ | componentes 00–04 | 5 | 15.742 | recibo de tranche PASS |
| SGA 5 | preliminares/índices, Exp. III, X, XV | 160 | 429.337 | quatro recibos de revisão manual PASS |
| **Total** |  | **209** | **1.610.902** | prévia-fonte validada |

## Exclusões deliberadas

- FGA `e149`, `e182`, `e190`: têm controles estruturais locais, mas não recibos semânticos dedicados equivalentes aos cinco arquivos admitidos.
- FGA tranche B: nenhum `completed_unit` no cursor vivo; somente fragmentos candidatos.
- SGA 3 tomo II Exposés X–XVIII: não há selos completos de unidade para a totalidade desse intervalo.
- SGA 4½ componentes 05 em diante: incompletos, falhos ou ausentes.
- SGA 5 Exposés V–VI e demais unidades: trabalho parcial sem recibo final de tranche ou ainda não iniciado.
- Traduções vietnamitas: cânone terminológico pronto, mas zero páginas traduzidas.

O PDF aprovado `EGA_III_1_PTBR_FIRST_PUBLIC_CHECKPOINT.pdf` tem 149 páginas. As páginas físicas e os denominadores das demais tarefas são documentados separadamente no relatório de responsabilidade por tarefa; páginas de PDF só são declaradas quando existe uma compilação determinística aprovada.
