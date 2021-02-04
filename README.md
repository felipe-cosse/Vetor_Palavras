# Vetor_Palavras

API REST para extração de Vetor de Palavras

## Motivação
Várias aplicações de processamento de linguagem natural necessitam que o texto seja formatado de forma estruturada, diferente da linguagem natural. Uma solução para isso é organizar as palavras do texto em um vetor que represente o documento em termos das palavras que ocorrem no mesmo.

## Solução
Criação de uma API REST que permita a um usuário enviar textos de entrada e que gere como resultado o vocabulário formado pelas palavras dos textos e o vetor de palavras.

## Arquitetura AWS

![alt text](/Imagens/Arquitetura.jpg?raw=true "Arquitetura Vetor Palavras")

## Serviços Utilizados
- AWS API Gateway é um serviço da AWS para criação, publicação, manutenção, monitoramento e proteção de APIs REST e WebSocket
- AWS Lambda é um serviço de computação sem servidor que permite executar código sem provisionar ou gerenciar servidores
- AWS DynamoDB é um banco de dados de valores-chave e documentos, totalmente gerenciado, multirregional, multiativo e durável com segurança, backup e restauração integrados e armazenamento em cache na memória para aplicativos em escala de Internet.
- AWS CloudFormation é um serviço para provisionamento de nuvem com infraestrutura como código.
- GitHub é uma plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git.
- GitHub Actions é uma API de causa e efeito no GitHub: orquestrar qualquer fluxo de trabalho, com base em qualquer evento.
- Visual Studio Code é um editor de código-fonte.
- Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
- JSON é um formato compacto, de padrão aberto independente, de troca de dados simples e rápida entre sistemas.

## Utilização
### Entrada
- O usuário poderá enviar textos via api REST 
- O formato do texto é no padrão JSON

Exemplo de entrada:
```json
{
  "gram": 2,
  "texto": [
    "lorem ipsum dolor sit amet consectetur adipiscing elit sagittis",
    "gerador de lorem ipsum, gerar texto aleatório"
  ]
}
```

### Retorno
1. O vocabulário completo formado pelas palavras isoladas;

2. O vocabulário completo formado por grupos de 2 palavras em sequência (2-gram);

3. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado pelas palavras isoladas;

4. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado por grupos de 2 palavras em sequência (2-gram);