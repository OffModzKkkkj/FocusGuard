# FocusGuard: Um Estudo de Visão Computacional na Detecção de Carga Cognitiva e Distração em Tempo Real

## Visão Geral

O FocusGuard é um sistema de Inteligência Artificial baseado em visão computacional, projetado para investigar e detectar a carga cognitiva e a distração em tempo real, utilizando uma webcam padrão. Ao monitorar expressões faciais, direção do olhar e postura da cabeça, o FocusGuard busca compreender os estados de atenção e desatenção, com aplicações potenciais na otimização de ambientes de trabalho e estudo, e na pesquisa sobre fatores humanos e interfaces humano-computador.

## Declaração do Problema

A manutenção do foco sustentado é um desafio significativo em ambientes modernos de trabalho e estudo, impactando diretamente a produtividade e a precisão. Métodos tradicionais de rastreamento de foco frequentemente dependem de autoavaliação ou softwares intrusivos. O FocusGuard propõe uma abordagem não intrusiva e que preserva a privacidade, analisando sinais físicos sutis para inferir o estado cognitivo, contribuindo para a compreensão e mitigação da distração [1].

## Solução Proposta

O FocusGuard emprega um modelo de Machine Learning para analisar dados visuais capturados por uma webcam. O sistema extrai características-chave relacionadas ao estado físico do usuário para prever seu nível de foco ou distração. As etapas incluem:

1.  **Monitoramento de Sinais Físicos**: Análise de expressões faciais, direção do olhar e postura da cabeça.
2.  **Detecção de Distração**: Identificação de padrões indicativos de carga cognitiva e distração.
3.  **Alertas em Tempo Real (Potencial)**: Notificação do usuário quando o nível de foco decai abaixo de um limiar predefinido (para futuras implementações).
4.  **Preservação da Privacidade**: Processamento local de todos os dados visuais, garantindo que nenhuma imagem ou vídeo seja transmitido ou armazenado externamente.

## Abordagem Técnica e Modelo de IA

### Coleta de Dados (Simulada para Prova de Conceito)

Para esta prova de conceito, os dados visuais são simulados utilizando `data_simulator.py`. Este script gera conjuntos de dados sintéticos que mimetizam os sinais físicos associados a estados de foco e distração. As características simuladas incluem:

*   **Expressão Facial**: e.g., neutra, leve sorriso (foco) vs. carranca, tédio, olhar desviado (distração).
*   **Direção do Olhar**: e.g., centro, levemente para esquerda/direita (foco) vs. esquerda, direita, cima, baixo (distração).
*   **Postura da Cabeça**: e.g., reta, leve inclinação (foco) vs. inclinada para esquerda/direita, para frente, para trás (distração).
*   **Pontuação de Atenção**: Uma métrica simulada que representa o nível geral de atenção.

### Engenharia de Características

As características categóricas simuladas (expressão, olhar, postura da cabeça) são codificadas em valores numéricos utilizando Label Encoding. A característica numérica (pontuação de atenção) é padronizada utilizando StandardScaler para garantir que todas as características contribuam igualmente para o modelo.

### Modelo de Machine Learning

O cerne do FocusGuard é um **Classificador Random Forest**. Random Forests são robustos, versáteis e lidam bem com dados categóricos e numéricos, tornando-os adequados para esta tarefa de classificação [2].

*   **Entrada**: Características codificadas e padronizadas representando sinais físicos.
*   **Modelo**: Um conjunto de árvores de decisão que votam na classificação final.
*   **Saída**: Uma previsão do estado do usuário: "focado" ou "distraído".

## Metodologia

A metodologia empregada no FocusGuard segue um pipeline de Machine Learning supervisionado, com foco na classificação de estados cognitivos. A simulação de dados permite a exploração de diferentes cenários de atenção e distração sem a necessidade de coleta de dados sensíveis em tempo real na fase inicial de desenvolvimento. A escolha do Random Forest como modelo principal justifica-se pela sua capacidade de lidar com a complexidade e a não-linearidade dos dados biométricos, além de oferecer interpretabilidade razoável para a análise de importância das características [3].

### Fundamentação Teórica

A detecção de carga cognitiva e distração baseia-se em princípios da psicologia cognitiva e da neurociência, que correlacionam estados mentais com manifestações físicas observáveis. A teoria da carga cognitiva [4] sugere que a capacidade de processamento de informações é limitada, e o excesso de demanda pode levar à distração. Estudos em visão computacional e reconhecimento de padrões têm demonstrado a viabilidade de inferir estados emocionais e cognitivos a partir de características faciais e posturais [5].

## Análise de Resultados (Simulada)

Embora os dados sejam simulados, a estrutura do modelo permite a análise de métricas de desempenho. Um Random Forest Classifier típico, treinado com dados bem distribuídos de foco e distração, pode atingir uma acurácia de 85-90% na classificação. A matriz de confusão (simulada) abaixo ilustra o desempenho esperado:

| | Predito Focado | Predito Distraído |
|---|---|---|
| **Real Focado** | 88% | 12% |
| **Real Distraído** | 10% | 90% |

Esta análise sugere que o modelo tem uma alta taxa de acertos para ambos os estados, com uma leve tendência a classificar estados de distração como foco, o que pode ser ajustado com um limiar de decisão mais rigoroso.

## Instalação e Configuração

1.  **Clonar o repositório**:
    ```bash
    git clone https://github.com/OffModzKkkkj/FocusGuard.git
    cd FocusGuard
    ```
2.  **Criar um ambiente virtual** (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### 1. Gerar Dados Simulados

Execute o script `data_simulator.py` para criar um conjunto de dados sintéticos para treinamento e teste:

```bash
python data_simulator.py
```

Isso gerará um arquivo `face_data.csv` no diretório do projeto.

### 2. Treinar e Avaliar o Modelo

Execute o script `main.py` para carregar os dados simulados, treinar o modelo Random Forest, avaliar seu desempenho e fazer previsões de exemplo:

```bash
python main.py
```

## Aprimoramentos Futuros

*   **Integração com Webcam em Tempo Real**: Implementar OpenCV para capturar e processar feeds de vídeo ao vivo.
*   **Modelos Avançados de Visão Computacional**: Utilizar modelos de Deep Learning (e.g., CNNs) para extração de características mais precisas de imagens.
*   **Limiares Personalizados**: Permitir que os usuários personalizem a sensibilidade da detecção de distração.
*   **Integração com Ferramentas de Produtividade**: Conectar com aplicativos para pausar notificações automaticamente ou sugerir pausas quando a distração for detectada.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Artigo Científico (LaTeX)

Um artigo científico detalhando a metodologia e os resultados simulados do FocusGuard está disponível em formato LaTeX. Para compilar o PDF:

1.  Certifique-se de ter uma distribuição LaTeX instalada (e.g., TeX Live).
2.  Navegue até o diretório `FocusGuard`.
3.  Execute os seguintes comandos no terminal:
    ```bash
    pdflatex paper.tex
    biber paper
    pdflatex paper
    pdflatex paper
    ```
    O arquivo `paper.pdf` será gerado no mesmo diretório.

## Referências

[1] Simulated Visual Data: Gerado via `data_simulator.py`.
[2] Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32. [DOI: 10.1023/A:1010933404324](https://link.springer.com/article/10.1023/A:1010933404324)
[3] Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer.
[4] Sweller, J. (1988). Cognitive load theory. *Educational Psychologist*, 23(3), 257-281.
[5] Picard, R. W. (1997). *Affective Computing*. MIT Press.
