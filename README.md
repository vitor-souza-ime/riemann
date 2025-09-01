# Aproximação Numérica da Integral da Função Gaussiana com Somas de Riemann

Este repositório apresenta um exemplo em Python para a aproximação numérica da integral da **Função Gaussiana** no intervalo \[0, 2\], utilizando **Somas de Riemann** (à esquerda, à direita e pelo ponto médio).

## Arquivo principal

- [`main.py`](main.py): Contém a implementação em Python do cálculo das somas de Riemann e a visualização gráfica.

## Funcionalidades

- Cálculo da soma de Riemann à esquerda.  
- Cálculo da soma de Riemann à direita.  
- Cálculo da soma de Riemann pelo ponto médio.  
- Visualização gráfica da função e dos retângulos da soma à esquerda.  

## Dependências

Para rodar o código, é necessário ter instalado:

```bash
pip install numpy matplotlib
````

## Como executar

Clone o repositório e execute o arquivo `main.py`:

```bash
git clone https://github.com/vitor-souza-ime/riemann.git
cd riemann
python main.py
```

## Exemplo de Saída

No console, serão exibidos os valores aproximados:

```
Soma de Riemann (esquerda): 0.723567
Soma de Riemann (direita): 0.477731
Soma de Riemann (ponto médio): 0.599270
```

E uma figura será exibida mostrando a curva da função `f(x) = e^(-x²)` e os retângulos correspondentes à soma de Riemann à esquerda.


Quer que eu também crie um **gráfico ilustrativo gerado pelo próprio código** (como exemplo de imagem pronta) e inclua no `README.md` para deixar mais atrativo?
```
