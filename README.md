# Introdução


 Análise Exploratória de Dados usando um data set do Kaggle sobre o período inicial de COVID-19. A partir da análise fiz edições na tabela , observei padrões e deduzi resultados no Google Colaboratory.
 
 # Instalação
 
```import pandas as pd```


```import numpy as np```


```import seaborn as sns```


```import matplotlib```


```import matplotlib.pyplot as plt```
 
# Exemplos

O gráfico abaixo monstra a curva de crescimento em relação ao tempo do número de pacientes com covid que faleceram 

 ![](analysis/Histograma.png)
 
Gráfico representando a correlação entre as variáveis, que identificam tendências em variação das variáveis

 ![](analysis/Heatmap.png)
 
Tabela a qual indica valores importantes como média, desvio padrão, máximo, mínimo e os quartis das variáveis 

 ![](analysis/descricao_de_dados.png)
 
# Conclusão

Na condução do projeto optou-se pela adoção da metodologia CRISP-DM composta por suas 6 (seis) etapas. Inicialmente, na etapa de entendimento do negócio, buscou-se definir 5 objetivos a serem alcançados ao fim do projeto como métrica de averificação de sucesso. Na sequência, na fase de entendimento dos dados, houve uma forte preocupacão no estudo dos dados, com especial atenção para conhecermos seu formato, tipos de variáveis,identificação de dados faltantes,bem como uma análise de correlacão entre as variáveis do dataset; houve também a tradução das colunas para português para mais fácil interpretação e a produção de histogramas.

Na etapa posterior, de prepração dos dados,trocamos o nome da coluna de "Mortes a cada 100 recuperados" para "100 Mortes a cada recuperado", vide que os resultados presentes no data frame não estavam condizendo com o nome prévio.
Já na etapa de modelagem foram trabalhadas as 4(quatro) questões de interesse do projeto. Logo em seguida, na avaliação do projeto foi possível constatar o sucesso do mesmo, por meio do alcance dos objetivos previamente definidos e por fim, na fase de implementação foram feitas reflexões sobre a fase de implementação do projeto em produção.

De uma forma geral, valores bastante consistentes com a baseline do projeto.
 
# Fontes

Link do arquivo do Kaggle:https://www.kaggle.com/datasets/imdevskp/corona-virus-report

Data Frame usado : day_wise
 
Google Colaboratory: https://colab.research.google.com/
