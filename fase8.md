Fase 8 — recursos avançados. Continua HTML/CSS/JS puros, sem build,
sem framework, sem npm. Tudo com aprimoramento progressivo: onde o
navegador não suportar, o site funciona igual, só sem o efeito.

CONTEXTO: público são comissões de licitação e construtoras. Priorize
densidade de informação e credibilidade sobre espetáculo visual. Nada
de partícula, cursor customizado ou paralaxe pesada.

1. MAPA DE ATUAÇÃO (prioridade máxima)
   SVG do estado do Tocantins com marcador em cada município onde há
   obra: Goiatins, Natividade, Porto Nacional, Miranorte, Monte do
   Carmo, Nova Rosalândia. Marcador clicável levando à ficha da obra,
   com tooltip no hover mostrando nome da obra e categoria.
   Cor do marcador por categoria. Deve funcionar por teclado e ter
   alternativa textual (lista de municípios) para leitor de tela.
   Coloque como seção nova, antes de Capacidade Técnica.

2. FILTRO DE CATEGORIA no portfólio
   Botões: Todas / Judiciário / Educação / Iluminação Pública.
   JS simples, sem reload. Estado ativo visível. Acessível por teclado.

3. CONTADORES ANIMADOS na Capacidade Técnica
   Números sobem de 0 ao valor final quando a seção entra na viewport.
   Só quando houver número real — placeholder não anima.
   Respeitar prefers-reduced-motion.

4. ANIMAÇÃO DE CONSTRUÇÃO ligada ao scroll
   SVG de edificação que se monta por camadas na ordem real de
   execução (fundação → estrutura → lajes → fechamento → esquadrias).
   Use animation-timeline: view() em CSS puro, sem JS.
   Estética de planta técnica: geométrica, linha fina, preto e laranja.
   NÃO quero ilustração fofa ou infantil.
   Posição: entre Obras e Especialidades. Nunca no hero.

5. VIEW TRANSITIONS entre index e páginas de obra
   view-transition-name na imagem do card e na imagem da página de
   detalhe, para haver continuidade visual na navegação.
   Onde não houver suporte, navegação normal.

6. ESTILO DE IMPRESSÃO (@media print)
   Fundo branco, texto preto, sem menu, sem botão flutuante, sem
   animação. Ficha técnica legível em folha A4. URL da página no
   rodapé impresso. Quebras de página em pontos sensatos.

REGRAS:
- prefers-reduced-motion respeitado em tudo
- só transform e opacity nas animações
- nada pode depender de JS para o conteúdo aparecer
- testar mentalmente o comportamento em tela de 360px

Antes de codar, me apresente sua abordagem para os itens 1 e 4, que
são os que envolvem decisão visual. Não escreva código ainda.