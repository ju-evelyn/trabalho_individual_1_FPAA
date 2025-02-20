# Projeto Karatsuba
## Sobre o Projeto
O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números
inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a
complexidade da multiplicação em comparação ao método tradicional de
multiplicação direta. Este projeto utiliza a biblioteca padrão do Python, garantindo que seja simples de rodar e entender, mesmo em ambientes isolados.

## Lógica do algoritmo implementado
#### Linha 1
O algoritmo inicia com a função karatsuba recebendo dois números (num1 e num2)
#### Linhas 2 e 3 (base da recursão)
Nesse bloco é feito uma validação se o número possui menos de 2 dígitos, para indicar a base da recursão. Em caso positivo, os dois números recebidos são multiplicados e o resultado é retornado.
#### Linhas 5 e 6
A linha 5 utiliza a função `max()` para atribuir à ***n***  a quantidade de algarismos naturais que o maior número recebido possui. Para isso, os valores recebidos são transformados em *string* e o tamanho de cada um é contado, por meio  das funções `len()` e `str()` aninhadas.

Logo em seguida, é atribuído à ***m*** a metade do resultado de ***n*** para iniciar a organização da divisão do número para a recursividade.
#### Linhas 8 e 9
Nessa parte é feita a organização das variáveis que serão utilizadas no algoritmo. Para dividir os números em duas partes, obtendo a divisão inteira e o resto da divisão, foi utilizada a função `divmod()`, que atribui respectivamente os valores mencionados em 2 variáveis. No algoritmo apresentado são elas:

- variável ***num1***
    - *esq1* para a parte inteira do primeiro número
    - *dir1* para o resto da divisão do primeiro número
- variável ***num2***
    - *esq2* para a parte inteira do segundo número
    - *dir2* para o resto da divisão do segundo número

#### Linhas 12, 13 e 14
Essas linhas iniciam a parte da divisão do algoritmo, implementando 3 recursividades:

- ***rec1*** chama novamente o método para as variáveis da parte inteira (*esq1*, *esq2*)
- ***rec2*** chama novamente o método para as variáveis do resto da divisão (*dir1*, *dir2*)
- ***rec3*** chama novamente o método para as somas das duas variáveis relacionadas ao mesmo número (*esq1* somado a *dir1*, *esq2* somado a *dir2*)

#### Linha 17
Por fim, é feita a conquista com a combinação das 3 recursões por meio da seguinte função:

    (rec1 * 10**(2*m)) + ((rec3 - rec1 - rec2) * 10**m) + rec2

## Como executar o projeto
### Passo 1: Criar e ativar o ambiente virtual
É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1.  Crie um ambiente virtual usando o seguinte comando:
    `python3 -m venv .venv`

2.  Ative o ambiente virtual:
    -   No macOS e Linux
        `source .venv/bin/activate`
    -   No Windows:
        `.venv\Scripts\activate`

### Passo 2: Executar o script
Após ativar o ambiente virtual, execute o script principal:

    python main.py

### Versão do Python
Este projeto foi desenvolvido na versão  **3.13.2**  do Python e  **não exige a instalação de nenhuma dependência adicional**.