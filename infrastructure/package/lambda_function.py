import json
from collections import Counter
import boto3
from datetime import datetime

def ngrams_zip(input_list, n):    
    zip_text =  zip(*(input_list[i:] for i in range(n)))
    l = list(zip_text)
    list_t = []
    for i in l:
        list_t.append(' '.join(i))
    return list_t

def padrao_string(palavra):
    return palavra.lower().replace('.', '').replace(',', '').replace('-', ' ')
    
def stop_words(frase):
    stop_dict = ["a","acerca","adeus","agora","ainda","algmas","algo","algumas","alguns","ali","além","ambos","ano","anos","antes","ao","aos","apenas","apoio","apontar","após","aquela","aquelas","aquele","aqueles","aqui","aquilo","as","assim","através","atrás","até","aí","baixo","bastante","bem","bom","breve","cada","caminho","catorze","cedo","cento","certamente","certeza","cima","cinco","coisa","com","como","comprido","conhecido","conselho","contra","corrente","custa","cá","da","daquela","daquele","dar","das","de","debaixo","demais","dentro","depois","desde","desligado","dessa","desse","desta","deste","deve","devem","deverá","dez","dezanove","dezasseis","dezassete","dezoito","dia","diante","direita","diz","dizem","dizer","do","dois","dos","doze","duas","dá","dão","dúvida","e","ela","elas","ele","eles","em","embora","enquanto","entre","então","era","essa","essas","esse","esses","esta","estado","estar","estará","estas","estava","este","estes","esteve","estive","estivemos","estiveram","estiveste","estivestes","estou","está","estás","estão","eu","exemplo","falta","fará","favor","faz","fazeis","fazem","fazemos","fazer","fazes","fazia","faço","fez","fim","final","foi","fomos","for","fora","foram","forma","foste","fostes","fui","geral","grande","grandes","grupo","hoje","horas","há","iniciar","inicio","ir","irá","isso","ista","iste","isto","já","lado","ligado","local","logo","longe","lugar","lá","maior","maioria","maiorias","mais","mal","mas","me","meio","menor","menos","meses","mesmo","meu","meus","mil","minha","minhas","momento","muito","muitos","máximo","mês","na","nada","naquela","naquele","nas","nem","nenhuma","nessa","nesse","nesta","neste","no","noite","nome","nos","nossa","nossas","nosso","nossos","nova","nove","novo","novos","num","numa","nunca","não","nível","nós","número","o","obra","obrigada","obrigado","oitava","oitavo","oito","onde","ontem","onze","os","ou","outra","outras","outro","outros","para","parece","parte","partir","pegar","pela","pelas","pelo","pelos","perto","pessoas","pode","podem","poder","poderá","podia","ponto","pontos","por","porque","porquê","posição","possivelmente","posso","possível","pouca","pouco","povo","primeira","primeiro","promeiro","próprio","próximo","puderam","pôde","põe","põem","qual","qualquer","quando","quanto","quarta","quarto","quatro","que","quem","quer","quero","questão","quieto","quinta","quinto","quinze","quê","relação","sabe","saber","se","segunda","segundo","sei","seis","sem","sempre","ser","seria","sete","seu","seus","sexta","sexto","sim","sistema","sob","sobre","sois","somente","somos","sou","sua","suas","são","sétima","sétimo","tal","talvez","também","tanto","tarde","te","tem","temos","tempo","tendes","tenho","tens","tentar","tentaram","tente","tentei","ter","terceira","terceiro","teu","teus","teve","tipo","tive","tivemos","tiveram","tiveste","tivestes","toda","todas","todo","todos","trabalhar","trabalho","treze","três","tu","tua","tuas","tudo","tão","têm","um","uma","umas","uns","usa","usar","vai","vais","valor","veja","vem","vens","ver","verdade","verdadeiro","vez","vezes","viagem","vindo","vinte","você","vocês","vos","vossa","vossas","vosso","vossos","vários","vão","vêm","vós","zero","à","às","área","é","és","último", "!","\"","$","%","&","'","(",")","*","+",",","-",".","...","0","1","2","3","4","5","6","7","8","9",";","<","=",">","?","@","\\","^","_","`","|","~","·","—","——","‘","’","“","”","…","、","。","〈","〉","《","》"]
    return [w for w in frase if not w in stop_dict] 
    
def palavra_isolada(frase, ngram):
    texto_padrao = [padrao_string(w) for w in frase.split()]
    texto_stop = stop_words(texto_padrao)
    words = ngrams_zip(texto_stop, ngram) 
    ocorrencias = Counter(words)
    return ocorrencias, list(ocorrencias.keys()), list(ocorrencias.values())
    
def n_gram(textos, ngram):
    lista_frase = []
    for frase in textos:
        lista_frase.append(palavra_isolada(frase, ngram))
    return json.dumps(lista_frase)
    
def salva_dynamo(num_gram, list_texto, result):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    tableVetorPalavras = dynamodb.Table('vetor_palavras_tb')
    
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        tableVetorPalavras.put_item(
               Item={
                    'eventDateTime': eventDateTime,
                    'ngram': num_gram,
                    'list_texto': list_texto,
                    'result': result
                }
            )
    except:
        print('Erro Salvar Dynamo')
    

def lambda_handler(event, context):
    num_gram = event['gram']
    list_texto = event['texto']
    
    result = n_gram(list_texto, num_gram)
    
    salva_dynamo(num_gram, list_texto, result)
    
    try:
        return {
            'statusCode': 200,
            'body': result
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error Vetor Palavras')
        }
