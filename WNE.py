#nltk.download()

import nltk
from nltk.corpus import wordnet



class WNE:
    def __init__(self):
        propsFile = "/Users/Public/onto_teste/file_properties.xml"

#---------------------------------------------------------------------------------------   
    def  sinonimos(self,palavra):
        while palavra.find('_')>=0:
            palavra=palavra[0:len(palavra)-1]#retirando caracteres indesejados
        word= wordnet.synsets(palavra)#lista com vários significados para a palavra
        if len(word)>=1:
            resultados=self.auxiliar(word,1)
        return resultados
#---------------------------------------------------------------------------------------
    def auxiliar(self,word,op):
        resultados=[]
        for p in word: #para cada significado p pode haver vários sinônimos
            a=''.join (str(p)) #transformando item da lista em string
            r=a[a.find("'")+1:len(a)-2] #retirando caracteres indesejados
            a=''.join(str(r))
            if op==1:
                s=wordnet.synset(a).lemma_names()#sinômimos para o significado p
            if op==2:
                s=wordnet.synset(a).hyponyms()
                s=self.auxiliar(s,1)
            if op==3:
                s=wordnet.synset(a).hypernyms()
                s=self.auxiliar(s,1)
            if op==4:
                s=wordnet.synset(a).part_holonyms()
                s=self.auxiliar(s,1)
            if op==5:
                s=wordnet.synset(a).part_meronyms()
                s=self.auxiliar(s,1)
            if op==6:
                s=wordnet.synset(a).entailments()
                s=self.auxiliar(s,1)
                
            resultados=resultados+s #juntando resultados anteriores
        resultados=list(set(resultados)) #removendo itens repetidos da lista
        return resultados
#---------------------------------------------------------------------------------------
    def tem_relacao(self,s1,s2): #dadas duas strings s1 e s2, verificando se há relação entre elas
        i=False
        while s1.find('_')>=0:
            s1=s1[0:len(s1)-1] #removendo caracteres indesejados
        while s2.find('_')>=0:
            s2=s2[0:len(s2)-1]
        res=[]  	
        try:
            g1= wordnet.synsets(s1)#obtendo os grupos sysnset de cada string
            g2= wordnet.synsets(s2)
            if len(g1)>=1:
                for j in range(1,7):
                    res=res+self.auxiliar(g1,j) #verificando os relacionamentos
                res=list(set(res))
                if res.count(s2)>0:
                    i=True            #verificando se s2 está contida no grupo de relacionamentos de s1
            #print("\n\n res1 =",res)
            res=[]
            if len(g2)>=1:
                for j in range(1,7):
                    res=res+self.auxiliar(g2,j) #idem comentários referentes a s1
                res=list(set(res))
                if res.count(s1)>0:
                    i=True
            #print("\n\n res2 =",res)
        except:
            print ("Erro")
        return i
       	   
#---------------------------------------------------------------------------------------         
print("CLASSE PYTHON PARA LIDAR COM PROCESSAMENTO DE LINGUAGEM NATURAL - WordNet")
wn=WNE()
print("\nSão os sinônimos de 'funny':\n",wn.sinonimos("funny"))
print ("\nAs palavras 'mouth' and 'face' estão correlacionadas?",wn.tem_relacao("mouth","face"))
print ("\nAs palavras 'mouth' and 'lip' estão correlacionadas?",wn.tem_relacao("mouth","lip"))
print ("\nAs palavras 'mouth' and 'shoes' estão correlacionadas?",wn.tem_relacao("mouth","shoes"))
