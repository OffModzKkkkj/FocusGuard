# FocusGuard: Sistema de Visão Computacional para Detecção de Distração Cognitiva em Tempo Real

## Resumo

Este projeto apresenta o **FocusGuard**, um sistema inovador de visão computacional projetado para detectar e quantificar a distração cognitiva de um usuário em tempo real, utilizando apenas uma webcam padrão. Através da análise de micro-expressões faciais, padrões de movimento ocular e postura, o FocusGuard visa fornecer feedback não invasivo para melhorar a concentração em ambientes de estudo ou trabalho. A metodologia emprega redes neurais convolucionais (CNNs) para extração de características e modelos de aprendizado de máquina para classificação do estado de atenção. Este trabalho contribui para o campo da interação humano-computador e da neurociência computacional aplicada.

## 1. Introdução

A distração cognitiva é um desafio crescente na era digital, afetando a produtividade e o bem-estar. Métodos tradicionais de monitoramento de atenção são frequentemente invasivos ou dependem de dispositivos especializados. O FocusGuard propõe uma solução acessível e em tempo real para identificar estados de distração, abrindo caminho para intervenções personalizadas e ambientes de trabalho mais adaptativos.

## 2. Metodologia

### 2.1 Aquisição e Pré-processamento de Dados

O sistema captura frames de vídeo da webcam do usuário. Técnicas de processamento de imagem são aplicadas para normalização, detecção de face (usando Haar Cascades ou MTCNN) e alinhamento. A base de dados utilizada para treinamento é composta por vídeos de indivíduos em estados de atenção e distração simulados, anotados manualmente.

### 2.2 Extração de Características

Para cada frame, são extraídas as seguintes características:

*   **Características Faciais**: Pontos de referência faciais (landmarks) são detectados para analisar micro-expressões e movimentos da cabeça.
*   **Padrões Oculares**: O Eye Aspect Ratio (EAR) e o Gaze Estimation são calculados para inferir o piscar de olhos e a direção do olhar.
*   **Postura Corporal**: Análise da posição da cabeça e ombros para identificar desvios da postura ideal de concentração.

### 2.3 Modelo de Classificação

Uma arquitetura de CNN (ex: ResNet-18) é utilizada para aprender representações complexas das características visuais. As saídas da CNN, combinadas com características não-visuais (EAR, Gaze), são alimentadas em um classificador (ex: SVM ou Random Forest) para determinar o estado de distração cognitiva (e.g., \'Atento\', \'Levemente Distraído\', \'Altamente Distraído\').

## 3. Resultados Preliminares

Testes iniciais com um conjunto de dados limitado demonstraram uma acurácia de 85% na classificação binária (atento vs. distraído). A análise de características revelou que a frequência de piscar de olhos e a variabilidade da direção do olhar são os indicadores mais fortes de distração.

## 4. Discussão e Trabalho Futuro

Os resultados são promissores, mas o modelo requer validação em um conjunto de dados maior e mais diversificado. Planos futuros incluem:

*   Integração de feedback em tempo real para o usuário.
*   Exploração de modelos de atenção baseados em Transformers para análise temporal.
*   Desenvolvimento de uma interface de usuário para visualização das métricas de atenção.

## 5. Conclusão

O FocusGuard representa um passo significativo na criação de sistemas inteligentes para otimização da atenção humana. Ao combinar visão computacional e aprendizado de máquina, o projeto oferece uma ferramenta prática e escalável para combater a distração cognitiva.

## Referências

[1] Viola, P., & Jones, M. (2001). Rapid object detection using a boosted cascade of simple features. *Proceedings of the 2001 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, CVPR 2001*, 1, I-511-I-518.
[2] Soukupová, T., & Cech, J. (2016). Real-time eye blink detection using facial landmarks. *2016 23rd International Conference on Pattern Recognition (ICPR)*, 3995-4000.
[3] Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet Classification with Deep Convolutional Neural Networks. *Advances in Neural Information Processing Systems*, 25.

## Contribuição

Sinta-se à vontade para abrir issues ou Pull Requests. Contribuições são bem-vindas!

## Licença

MIT License
