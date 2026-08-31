# EngPalmas — Site Institucional

Site institucional da EngPalmas, empresa de engenharia civil e elétrica de Palmas (TO),
que executa edificações públicas, subestações abrigadas de 34,5 kV e projetos de
iluminação pública para órgãos contratantes.

Site publicado: https://taw3s.github.io/ENG-PALMAS-SITE/

## O problema que este projeto resolve

A empresa disputa licitações e contratos com órgãos públicos, mas não tinha nenhuma
presença digital. Quando um contratante pesquisava o nome da empresa, não encontrava
comprovação do que ela já havia entregue.

O site resolve isso ao transformar o histórico de obras em material verificável:
cada obra executada tem uma página própria com localização, categoria e escopo, e o
conjunto é apresentado num mapa do Tocantins que mostra a área de atuação real da
empresa. O objetivo não é vender por impulso, e sim dar ao contratante um caminho
rápido entre "quem é essa empresa" e "o que ela já executou".

## Obras documentadas

O site cobre 8 obras do Tocantins, organizadas em quatro categorias filtráveis:

- **Judiciário** — Fórum de Natividade, Fórum de Goiatins
- **Educação** — CEM Félix Camoa (Porto Nacional), Escola Estadual Henrique Cirqueira Amori
- **Iluminação pública** — Miranorte, Monte do Carmo, Nova Rosalândia
- **Outras** — Obra de Ananás

Sete municípios estão confirmados e marcados no mapa; o município da Escola Henrique
Cirqueira ainda não foi informado pela empresa.

## Estado do conteúdo

O front-end está concluído, mas **o conteúdo institucional ainda está em
preenchimento**. Os campos que dependem de dados oficiais da empresa — razão social,
CNPJ, CREA, responsável técnico, e-mail institucional, além dos dados contratuais de
cada obra — aparecem no HTML como marcadores `[[PREENCHER: chave]]`, destacados
visualmente pela classe `.pendente`.

São 133 marcadores, correspondentes a 76 campos distintos. A escolha de usar chaves
nomeadas em vez de texto genérico foi deliberada: cada campo pode ser localizado e
substituído por busca, e o que falta fica explícito na página em vez de virar um dado
inventado. As métricas da home (obras entregues, m² construídos) não animam enquanto
o valor não for numérico.

Enquanto os marcadores existirem, o site deve ser tratado como versão de trabalho.

## Stack

- **HTML5 semântico** — estrutura em seções com landmarks e atributos ARIA
  (`aria-expanded`, `aria-controls`, `aria-labelledby`) para navegação por teclado
  e leitores de tela.
- **CSS3** — layout em Grid e Flexbox, design tokens via variáveis CSS,
  View Transitions para a troca entre páginas de obra, e folha de estilo de
  impressão dedicada (`@media print`), já que propostas costumam ser impressas.
- **JavaScript (sem framework, sem dependências)** — filtro de obras por categoria,
  menu responsivo e animações de entrada com `IntersectionObserver`.
- **SVG inline** — o mapa do Tocantins com os municípios atendidos e a animação da
  ordem de execução de uma obra são desenhados em SVG, com `<title>` em cada
  elemento para descrição acessível.
- **GitHub Pages** — hospedagem.

Não há build, bundler ou dependência externa: o site é HTML, CSS e JS estáticos.

## Decisões técnicas

- **Sem framework.** O site é essencialmente conteúdo institucional. Um framework
  adicionaria etapa de build e peso de runtime sem resolver nenhum problema real aqui.
- **Acessibilidade e movimento.** Todas as animações respeitam
  `prefers-reduced-motion`, e as imagens usam `loading="lazy"`.
- **Sem back-end.** Não há formulário que armazene dados nem qualquer integração que
  exija chave de API — por isso o repositório pode ser público com segurança.

## Como rodar localmente

Clone o repositório:

```bash
git clone https://github.com/Taw3s/ENG-PALMAS-SITE.git
cd ENG-PALMAS-SITE
```

Como o projeto é estático, basta abrir o `index.html` no navegador.

Para servir por HTTP local (recomendado, porque as View Transitions entre páginas e
o carregamento dos SVGs se comportam como em produção):

```bash
# Python 3
python -m http.server 8000
```

Depois acesse `http://localhost:8000`.

## Estrutura

```
index.html          Página principal: empresa, obras, especialidades, mapa, contato
obra-*.html         Uma página por obra executada (8 páginas)
style.css           Folha de estilo única, incluindo estilos de impressão
*.png / *.jpg       Logo e fotos das obras
```

## Autor

Davi Dantas — [github.com/Taw3s](https://github.com/Taw3s)
