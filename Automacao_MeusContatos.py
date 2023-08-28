#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# In[7]:


service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")


# In[8]:


from selenium.webdriver.common.keys import Keys
import pyperclip
import time

mensagem = """Falaaa meus amigos!!
Passando para saber como vocês estão?!

Obs¹: Essa mensagem foi programada por mim para ser enviada via WhatssApp por meio da biblioteca Selenium
do Python!!!
"""


# In[12]:


# Lista de contatos

lista_contatos = ["Matheus Cantarutti", 
                  "Big Data Fatec Ipiranga", 
                  "BIG DATA PARA NEGÓCIOS", 
                  "Notícias e coisas import", 
                  "Sopinha de bolacha", 
                  "Alpha 2023",
                  "Irmãos gêmeos e suas esposas",
                  "Iniciação Científica",
                  "Amigos da FATEC"]
# print(len(lista_contatos))

# enviar a mensagem para o Meu Numero para poder depois encaminhar
# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
#Digite o meu nome
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Matheus Cantarutti")
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

# escrever a mensagem para nós mesmos
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(2)


# In[14]:


# encaminhar a mensagem para a lista de contatos
from selenium.webdriver.common.action_chains import ActionChains

qtde_contatos = len(lista_contatos) # 9 contatos

if qtde_contatos % 5 == 0: 
    qtde_blocos = qtde_contatos / 5 # apenas 1 envio com 5 contatos (1 lote de mensagem)
else:
    qtde_blocos = int(qtde_contatos / 5) + 1 # vamos rodar mais um bloco de código (2 lotes de mensagens)

for i in range(qtde_blocos):
    # rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # selecionar a mensagem para enviar e abre a caixa de encaminhar
    lista_elementos = nav.find_elements('class name', '_2AOIt') 
    for item in lista_elementos:
        mensagem = mensagem.replace("\n", "")
        texto = item.text.replace("\n", "")
        if mensagem in texto:
            elemento = item
        
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_3u9t-').click()
    time.sleep(0.5)
    nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(1)

    for nome in lista_enviar:
        # selecionar os 5 conttos para enviar
        # escrever o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1)
        # dar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1)
        # apagar o nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)

