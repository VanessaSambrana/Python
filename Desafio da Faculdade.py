'''O desafio será a criação de um ranking de criticidade de violações/vazamentos “breaches” de dados pessoais em serviços de internet, por meio dos critérios de dados comprometidos como senha, ajuda da senha, número do telefone, nomes, e-mail e data do vazamento. Para resolver o desafio UTILIZE APENAS O CONTEÚDO ESTUDADO DURANTE A FASE.'''

Senha = 6
Ajuda_da_Senha = 5
Número_do_telefone = 4
Nome = 3
E_mail = 2
Data_do_Vazamento = 1

Adobe = [E_mail, Ajuda_da_Senha, Senha, Nome]
Apollo = [Nome, Número_do_telefone]
Canva = [E_mail, Senha, Nome]
Hurb = [Nome, Senha, Número_do_telefone]
ActMobile = [E_mail, Data_do_Vazamento]

Animoto = [Ajuda_da_Senha, Número_do_telefone, Nome]
Chegg = [Senha, Nome, E_mail, Data_do_Vazamento]
Disqus = [Senha]
Evite = [Número_do_telefone, Nome]
HomeChef = [Senha, Data_do_Vazamento]

Ledger = [Senha, Ajuda_da_Senha, Nome, E_mail]
Linkedin = [Nome, E_mail, Data_do_Vazamento]
MangaDex = [Senha, Nome, E_mail]
Quidd = [Ajuda_da_Senha]
Romwe = [Nome, E_mail]

Snail = [Número_do_telefone]
Toondoo = [Nome, Data_do_Vazamento]
Vk = [Ajuda_da_Senha, Nome, E_mail, Data_do_Vazamento]
Weheart = [Nome]
Zomato = [E_mail]

Pesos = [sum(Adobe), sum(Apollo), sum(Canva), sum(Hurb), sum(ActMobile), sum(Animoto), sum(Chegg), sum(Disqus), sum(Evite), sum(HomeChef), sum(Ledger), sum(Linkedin), sum(MangaDex), sum(Quidd), sum(Romwe), sum(Snail), sum(Toondoo), sum(Vk), sum(Weheart), sum(Zomato)]

Pesos.sort(reverse=True)

rank = []

a = sum(Adobe)
b = sum(Apollo)
c = sum(Canva)
d = sum(Hurb)
e = sum(ActMobile) 
f = sum(Animoto)
g = sum(Chegg)
h = sum(Disqus)
i = sum(Evite)
j = sum(HomeChef)
k = sum(Ledger)
l = sum(Linkedin)
m = sum(MangaDex)
n = sum(Quidd)
o = sum(Romwe)
p = sum(Snail)
q = sum(Toondoo)
r = sum(Vk)
s = sum(Weheart)
t = sum(Zomato)


for Peso in Pesos:
    
    if Peso == a:
        if a not in rank:
            rank.append("Adobe")
            a = "Adobe"
    if Peso == b:
        if b not in rank:
            rank.append("Apollo")
            b = "Apollo"
    if Peso == c:
        if c not in rank:
            rank.append("Canva")
            c = "Canva"
    if Peso == d:
        if d not in rank:
            rank.append("Hurb")
            d = "Hurb"
    if Peso == e:
        if e not in rank:
            rank.append("ActMobile")
            e = "ActMobile"
    if Peso == f:
        if f not in rank:
            rank.append("Animoto")
            f = "Animoto"                           
    if Peso == g:
        if g not in rank:
            rank.append("Chegg")
            g = "Chegg" 
    if Peso == h:
        if h not in rank:
            rank.append("Disqus")
            h = "Disqus"
    if Peso == i:
        if i not in rank:
            rank.append("Evite")
            i = "Evite"
    if Peso == j:
        if j not in rank:
            rank.append("HomeChef")
            j = "HomeChef"                        
    if Peso == k:
        if k not in rank:
            rank.append("Ledger")
            k = "Ledger"        
    if Peso == l:
        if l not in rank:
            rank.append("Linkedin")
            l = "Linkedin"
    if Peso == m:
        if m not in rank:
            rank.append("MangaDex")
            m = "MangaDex"
    if Peso == n:
        if n not in rank:
            rank.append("Quidd")
            n = "Quidd"
    if Peso == o:
        if o not in rank:
            rank.append("Romwe")
            o = "Romwe"
    if Peso == p:
        if p not in rank:
            rank.append("Snail")
            p = "Snail"
    if Peso == q:
        if q not in rank:
            rank.append("Toondoo")
            q = "Toondoo"
    if Peso == r:
        if r not in rank:
            rank.append("Vk")
            r = "Vk"
    if Peso == s:
        if s not in rank:
            rank.append("Weheart")
            s = "Weheart"
    if Peso == t:
        if t not in rank:
            rank.append("Zomato")
            t = "Zomato"                                                                        
               
print(rank)
