Fase 7 — expansão do portfólio de obras.

Meu pai executou 7 obras, não 4. As duas obras genéricas atuais
("Obra de Ananás" e "Obra em Andamento") não correspondem à lista real
e devem ser substituídas.

Lista real, agrupada por categoria:

JUDICIÁRIO
- Fórum de Goiatins — Goiatins/TO (já existe, manter)
- Fórum de Natividade — Natividade/TO (já existe, manter)

EDUCAÇÃO
- CEM Félix Camoa — Porto Nacional/TO
- Escola Estadual Henrique Cirqueira Amori — cidade a confirmar
  (o nome pode estar truncado; deixe placeholder para o nome completo)

ILUMINAÇÃO PÚBLICA
- Iluminação Pública de Miranorte — Miranorte/TO
- Iluminação Pública de Monte do Carmo — Monte do Carmo/TO
- Iluminação Pública de Nova Rosalândia — Nova Rosalândia/TO

Tarefas:

1. Reestruture a seção Obras Executadas agrupando por essas 3
   categorias, com subtítulo para cada. Substitua obra-ananas.html e
   obra-em-andamento.html pelas novas páginas.
2. Crie página de detalhe para as 5 obras novas, no mesmo padrão das
   existentes (ficha técnica com os 6 campos de atestado).
3. Não invente NENHUM dado: órgão contratante, objeto, modalidade,
   área, prazo e situação vão como placeholder. Cidade e nome da obra
   são os únicos dados confirmados.
4. As 5 obras novas não têm foto. Use o placeholder "Foto em breve",
   mas diferencie por categoria em vez de repetir o logo 5 vezes —
   proponha algo (ícone de categoria, por exemplo) antes de implementar.
5. Adicione "Iluminação Pública" à lista de Especialidades. É obra
   elétrica em 3 municípios e hoje não aparece no site.
6. Atualize o PENDENCIAS.md com as novas chaves.

Antes de codar, me mostre como pretende resolver o item 4.

Quero uma animação de construção progressiva ligada ao scroll:
um prédio em SVG que se monta por camadas na ordem real de execução
(fundação → estrutura → lajes → fechamento → esquadrias → acabamento).

Restrições:
- HTML/CSS/JS puros, sem biblioteca
- Estética técnica, geométrica, preto e laranja da marca — linguagem
  de planta baixa, não ilustração fofa
- Só transform e opacity; respeitar prefers-reduced-motion
- Deve funcionar bem no celular
- Colocar entre as seções Obras e Especialidades, não no hero

Antes de implementar, descreva 2 abordagens visuais diferentes.