#importando a biblioteca tkinter 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry


#cores 
cor_1 = "#F36F20" #laranja
cor_2 = "#00ABCC" #azul 
cor_3 = "#00C2C1" #azul claro 
cor_4 = "#E86B2F" #vermelho 
cor_5 = "#FFFFFF" #branca
cor_6 = "#0B1734" #azul escuro 
cor_7 = "#000000" #preto
cor_8 = "#e9edf5" #verde Claro

#janela Maior
janela = Tk()
janela.title("")
janela.geometry("900x600") #largura x altura
janela.configure(background= cor_3)  # background
janela.resizable(width=False, height=False)

#estilo da janela
style = ttk.Style(janela)
style.theme_use("clam")
#janela maior até aqui





#linha superior 
FrameCima = Frame(janela, width=1043, height=50, bg=cor_5, relief=FLAT) #Largura = width altura= height 
FrameCima.grid(row=0, column=0)
#linha Meio
FrameMeio = Frame(janela, width=1043, height=303, pady=20, bg=cor_5, relief=FLAT)
FrameMeio.grid(row=1, column=0, pady=1 ,padx=0, sticky=NSEW)
#linha Baixo
FrameBaixo = Frame(janela, width=1043, height=300, bg=cor_5,relief=FLAT)
FrameBaixo.grid(row=2, column=0, pady=0 ,padx=1, sticky=NSEW)



#abrindo imagem 
app_img = Image.open("image.png")
app_img = app_img.resize((120,60))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(FrameCima, image=app_img, text= "Controle de Estoque",width=900, compound=LEFT, relief= RAISED, anchor= NW, font=("Helvetica 25 bold"), bg=cor_5, fg= cor_7)
app_logo.place(x=0, y=0)



#frame meio
#criando entradas  nome/ localização/ descrição do item / numero de série/ data de entrada/ data de saída

#nome: 
l_nome = Label(FrameMeio, text= "Nome", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_nome.place(x=10, y=10)

e_nome = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

#localização: 
l_local = Label(FrameMeio, text="Localização", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_local.place(x=10, y=40)

e_local = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)

#descrição do item

#Descrição: 
l_descricao = Label(FrameMeio, text= "Descrição", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_descricao.place(x=10, y=70)

e_descricao = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)

#NÚMERO DE SÉRIE
l_serie = Label(FrameMeio, text= "Número de série", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_serie.place(x=10, y=100)

e_serie = Entry(FrameMeio, width=30, justify="left", relief=SOLID)
e_serie.place(x=130, y=101)

#DATA DE ENTRADA 
l_data_entrada = Label(FrameMeio, text= "Data de Entrada", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_data_entrada.place(x=10, y=130)

e_data_entrada = DateEntry(FrameMeio, width=12, background= "darkblue", bordewidth=2,year=2022, locale='pt_BR')
e_data_entrada.place(x=130, y=131)

#DATA DE SAÍDA
l_data_saida = Label(FrameMeio, text= "Data de Saída", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_data_saida.place(x=10, y=160)

e_data_saida = DateEntry(FrameMeio, width=12,background= "darkblue", bordewidth=2,year=2022, locale='pt_BR')
e_data_saida.place(x=130, y=161)

#Carregar 
l_carregar = Label(FrameMeio, text= "Imagem do Item", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_carregar.place(x=10, y=220)

b_carregar = Button(FrameMeio, width=30, text= "Carregar".upper(),compound=CENTER, anchor=CENTER, overrelief=RIDGE, font= ("Ivy 8"), bg= cor_5, fg=cor_7)
b_carregar.place(x=130, y=221)


#imagem do item
l_data_saida = Label(FrameMeio, text= "Data de Saída", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_data_saida.place(x=10, y=160)

e_data_saida = DateEntry(FrameMeio, width=12,background= "darkblue", bordewidth=2,year=2022, locale='pt_BR')
e_data_saida.place(x=130, y=161)



#----------------------------------------------------------------Criando Botões----------------------------

#Botão carregar

l_carregar = Label(FrameMeio, text= "Imagem do Item", height=1, anchor=NW, font= ("Ivy 10 bold"), bg= cor_5, fg=cor_7)
l_carregar.place(x=10, y=220)

e_carregar = Button(FrameMeio, width=30,text="Carregar".upper(), compound= CENTER, anchor=CENTER, overrelief=RIDGE, font=("Ivy 8"), bg=cor_5, fg=cor_7)
e_carregar.place(x=130, y=221)

#botão inserir 

img_add = Image.open("adc.png")
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(FrameMeio, image= img_add, width=95, text= "  ADICIONAR".upper(), compound=LEFT, overrelief=RIDGE , anchor= NW, font=("Helvetica 9 bold"), bg=cor_5, fg= cor_7)
b_inserir.place(x=330, y=10)



#botão atualizar

img_up = Image.open("atualizar.png")
img_up = img_up.resize((20,20))
img_up = ImageTk.PhotoImage(img_up)

b_inserir = Button(FrameMeio, image= img_up, width=95, text= "  ATUALIZAR".upper(), compound=LEFT, overrelief=RIDGE , anchor= NW, font=("Helvetica 9 bold"), bg=cor_5, fg= cor_7)
b_inserir.place(x=330, y=110)

#botão DELETAR 

img_del = Image.open("deletar.png")
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

b_inserir = Button(FrameMeio, image= img_del, width=95, text= "  DELETAR".upper(), compound=LEFT, overrelief=RIDGE , anchor= NW, font=("Helvetica 9 bold"), bg=cor_5, fg= cor_7)
b_inserir.place(x=330, y=60)

#botão ver arquivo 

img_past = Image.open("pasta.png")
img_past = img_past.resize((20,21))
img_past = ImageTk.PhotoImage(img_past)

b_inserir = Button(FrameMeio, image= img_past, width=95, text= "  DELETAR".upper(), compound=LEFT, overrelief=RIDGE , anchor= NW, font=("Helvetica 9 bold"), bg=cor_5, fg= cor_7)
b_inserir.place(x=330, y=220)


#------------------------------------------------------------Labels Quantidade ---------------------------


l_total = Label(FrameMeio, text= "", height=2, width=35, anchor=CENTER, font= ("Ivy 10 bold"), bg= cor_2, fg=cor_7)
l_total.place(x=540, y=25)

l_total_ = Label(FrameMeio, text= "   Quantidade de itens            ", height=1, anchor=NW, font= ("Ivy 15 bold"), bg= cor_2, fg=cor_5)
l_total_.place(x=540, y=20)


#--------------------------------- criando tabela inferior
# Adicionando Scrollbars

l_total = Label(FrameMeio, text= "", height=2, width=35, anchor=CENTER, font= ("Ivy 10 bold"), bg= cor_2, fg=cor_7)
l_total.place(x=540, y=25)

l_total_ = Label(FrameMeio, text= "   Quantidade de itens            ", height=1, anchor=NW, font= ("Ivy 15 bold"), bg= cor_2, fg=cor_5)
l_total_.place(x=540, y=20)


#---------------------------------                        criando tabela inferior
# Adicionando Scrollbars

# Inicializando a janela
root = Tk()

# Lista de itens e cabeçalhos da tabela
lista_itens = []
tabela_head = ['#Item', 'Nome', 'Localização', 'Descrição', 'Data de entrada', 'Data de saída', 'Número de série']

# Criando a Treeview e os scrollbars
tree = ttk.Treeview(FrameBaixo,selectmode="extended", columns=tabela_head, show="headings")
vsb = ttk.Scrollbar(FrameBaixo,orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(FrameBaixo,orient="horizontal", command=tree.xview)

# Configurando os scrollbars na Treeview
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Posicionando os widgets na tela
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

# Configurando pesos das linhas e colunas no grid
FrameBaixo.grid_rowconfigure(0, weight=1)
FrameBaixo.grid_columnconfigure(0, weight=1)

# Configurando cabeçalhos e largura das colunas
hd = ["center"] * len(tabela_head)
h = [120, 150, 100, 160, 130, 100, 100, 100]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1

# Inserindo os itens na Treeview
def calcular_total():
    for item in lista_itens:
        tree.insert('', 'end', values=item)

# Labels para exibir total de valor e itens
l_total = ttk.Label(root, text="")
l_total.pack()
l_qtd = ttk.Label(root, text="")
l_qtd.pack()

# Calculando e exibindo o total de valor e itens
calcular_total()




janela.mainloop()
