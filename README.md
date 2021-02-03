# Vetor_Palavras

API REST para extração de Vetor de Palavras

## Motivação
Várias aplicações de processamento de linguagem natural necessitam que o texto seja formatado de forma estruturada, diferente da linguagem natural. Uma solução para isso é organizar as palavras do texto em um vetor que represente o documento em termos das palavras que ocorrem no mesmo.

## Solução
Criação de uma API REST que permita a um usuário enviar textos de entrada e que gere como resultado o vocabulário formado pelas palavras dos textos e o vetor de palavras.

## Arquitetura AWS

![alt text](/Imagens/Arquitetura.jpg?raw=true "Arquitetura Vetor Palavras")

## Utilização
### Entrada
O usuário poderá enviar textos via api REST 

### Retorno
1. O vocabulário completo formado pelas palavras isoladas;

2. O vocabulário completo formado por grupos de 2 palavras em sequência (2-gram);

3. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado pelas palavras isoladas;

4. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado por grupos de 2 palavras em sequência (2-gram);