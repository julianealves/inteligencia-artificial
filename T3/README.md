# Inteligência Artificial
Trabalho 3 da cadeira de IA (INF01048) - 2022/1

Juliane da Rocha Alves - Turma B  
Luiza Martins Spinelli Alves - Turma A  
Maria Eduarda Neves Toneto - Turma A  

**NOTA:** Todas as bibliotecas utilizadas no trabalho são bibliotecas nativas do Python, com exceção do **Numpy**, que pode ser necessário instalar.

**1. Genética da realeza:** Os paramêtros utilizados que resultaram em uma execução bem sucedida, isto é, com zero ataques entre rainhas, são: 
   - ```g```: 200
   - ```n```: 10
   - ```k```: 2
   - ```m```: 0.3
   - ```e```: 1
Obs: foi utilizado o index = 3 para o crossover.

* Para obter gráfico com o maior, o menor e a média do número de conflitos para cada geração foi utilizada a seguinte chamada da função: run_ga(35, 20, 2, 0.3 1)
Obs: foi utilizado o index = 3 para o crossover.

**2. Não me perguntes onde fica o Alegrete...:** Após realizar diversos testes alterando-se o valor de theta_0, theta_1, o número de iterações e o valor de alpha, chegou-se nos seguintes resultados:
   
   - ```theta_0```: -1
   - ```theta_1```: 1
   - ```alpha```: 0.001
   - ```num_iterations```: 10000
   - ```MSE final```: 8.52854301222427
