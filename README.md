# Visão Computacional Aplicada à Análise de Jogos de Futebol

## Introdução
Este projeto utiliza técnicas avançadas de visão computacional para analisar partidas de futebol, com foco em:
- **Detecção de jogadores, árbitros e bola**
- **Cálculo de posse de bola**

## Ferramentas e Tecnologias
- **YOLO (You Only Look Once)**: Modelo rápido e eficiente para detecção de objetos, utilizado para identificar jogadores, árbitros e a bola em tempo real.
- **K-Means**: Técnica de agrupamento usada para identificar cores dos uniformes e classificar jogadores por time.
- **Interpolação**: Método para prever posições ausentes da bola entre frames.
- **Python**: Linguagem principal para desenvolvimento, com bibliotecas como OpenCV e Pandas.

## Metodologias
### Detecção
- Divisão de imagens em grades utilizando o modelo YOLO.
- Aplicação de bounding boxes para delimitar objetos detectados.
- Análise de dificuldade para objetos pequenos ou próximos.

### Treinamento
- Uso de datasets de futebol disponíveis no **Kaggle** e **Roboflow**.
- Modelos baseados no **YOLOv5**, variando entre versões `s` e `m` e entre 10, 50 e 100 épocas.
- Matriz de confusão para avaliar a performance dos modelos.

### Identificação de Times
- Extração de cores de uniformes com o algoritmo **K-Means**.
- Classificação de jogadores detectados com base em cores médias das roupas.

### Interpolação da Bola
- Preenchimento de gaps de detecção com interpolação linear para suavizar trajetórias da bola.

### Posse de Bola
- Associação da bola ao jogador mais próximo em cada frame.
- Acúmulo de dados por frame para análise estatística da posse de bola.

## Referências
- [Football AI Tutorial: From Basics to Advanced Stats with Python (YouTube)](https://www.youtube.com/watch?v=aBVGKoNZQUw)
- [Build an AI/ML Football Analysis System with YOLO, OpenCV, and Python (YouTube)](https://www.youtube.com/watch?v=neBZ6huolkg)
- [Acompanhamento de Cenas com Calibração Automática de Câmeras (PUC-Rio)](https://web.tecgraf.puc-rio.br/~szenberg/doutorado/index.html)
- [Computer Vision for Football Analysis in Python with Yolov8 & OpenCV (YouTube)](https://www.youtube.com/watch?v=yJWAtr3kvPU)

---
**Nota**: Este repositório fornece ferramentas e métodos avançados para análise de futebol, mas não inclui explicações detalhadas de código.



# PDI_PROJECT

- https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true
- https://universe.roboflow.com/roboflow-jvuqo/football-field-detection-f07vi/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true
- https://colab.research.google.com/github/roboflow/sports/blob/main/examples/soccer/notebooks/train_player_detector.ipynb#scrollTo=HI4nADCCj3F5
- https://www.youtube.com/watch?v=aBVGKoNZQUw
- https://www.youtube.com/watch?v=neBZ6huolkg
- https://www.youtube.com/watch?v=L23oIHZE14w
- https://web.tecgraf.puc-rio.br/~szenberg/doutorado/index.html
- https://www.youtube.com/watch?v=yJWAtr3kvPU

# Aleatorios
- https://www.confea.org.br/midias/uploads-imce/Contecc2021/Eletricista/VIS%C3%83O%20COMPUTACIONAL%20APLICADA%20%C3%80%20IDENTIFICA%C3%87%C3%83O%20DE%20%C3%81REAS%20IRRIGADAS%20A%20PIV%C3%94%20CENTRAL%20EM%20GOI%C3%81S.pdf
