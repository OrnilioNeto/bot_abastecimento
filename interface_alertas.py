from processamento_alerta import ExportReport
from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime, timedelta
import re
from time import sleep
import customtkinter
import datetime
import tkinter as tk
from tkinter import *
import os

class CustomLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#configuracao de cor
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

fechou_janela = False
class gerenciador_alertas():

    def __init__(self):
        self.janela = customtkinter.CTk()
        self.janela.geometry("350x270")
        # self.data_inicial = datetime.datetime.now() - datetime.timedelta(days=1)
        # self.data_final = datetime.datetime.now() - datetime.timedelta(days=1)
        # self.hora_inicial = "23:59"
        self.login= ''
        self.interface()
        
        

    # def show_options(self):  
        
    #     menu = tk.Toplevel()
    #     menu.title("Opções")
    #     menu.geometry("280x200")
    #     menu.configure(bg='light gray') # define a cor de fundo da janela como preto        
    #     # option1 = customtkinter.CTkButton(menu, text="Opção 1")
    #     # option1.pack(pady=10)
        
    #     self.macaiba = customtkinter.CTkCheckBox(menu, text="Unidade Macaiba")
    #     self.macaiba.grid(row=0, column=1, padx=10, pady=10, sticky="W")
    #     menu.grid_rowconfigure(0, weight=1)

    #     self.joao_pessoa = customtkinter.CTkCheckBox(menu, text="Unidade Joao pessoa")
    #     self.joao_pessoa.grid(row=1, column=1, padx=10, pady=10, sticky="W")
    #     menu.grid_rowconfigure(1, weight=1)

    #     self.campina_grande = customtkinter.CTkCheckBox(menu, text="Unidade Campina Grande")
    #     self.campina_grande.grid(row=2, column=1, padx=10, pady=10, sticky="W")
    #     menu.grid_rowconfigure(2, weight=1) 

    #     menu.iconbitmap('alerta.ico')

    #     #setando imagem
    #     self.img = PhotoImage(file="gm.png")
    #     self.label_img = CustomLabel(master=menu, image=self.img)
    #     self.label_img.place(x=5, y=5)

    #     def clique_options():        
    #         und_maca = self.macaiba.get()
    #         und_jpa = self.joao_pessoa.get()
    #         und_cpg = self.campina_grande.get()
    #         #print(und_cpg,und_jpa,und_maca)
    #         email_txt = self.email.get()
    #         senha_txt = self.senha.get()
    #         data_inicio = self.data_inicial_var.get()
    #         data_fim = self.data_final_var.get()


    #         if und_maca == 1:
    #             mac = True
    #         else:
    #             mac = False

    #         if und_jpa == 1:
    #             jpa = True
    #         else:
    #             jpa = False

    #         if und_cpg == 1:
    #             cpg = True
    #         else:
    #             cpg = False

    #         if fechou_janela == False:
    #             if email_txt == '' and senha_txt == '':
    #                 sg.popup_error('Digite seu Email e Senha !')
    #             elif email_txt == '':
    #                 sg.popup_error('Digite seu Email !')
    #             elif senha_txt == '':
    #                 sg.popup_error('Digite sua Senha !')
    #             else:
    #                 ### Para Tratar os Alertas ###
    #                 if (jpa):
    #                     relatorio = ExportReport()
    #                     relatorio.graficos_hora(
    #                         email_txt, senha_txt, data_inicio, data_fim)
                        
    #                     arquivo = jpa
    #                     relatorio.pegar_planilha(arquivo)
    #                     relatorio.horas()
    #                     sg.Popup('Grafico Exportado !')

    #                     ### Faz o tratamento de Alertas - Velocidade - Ociosidade ###
    #                 elif (cpg):
    #                     relatorio = ExportReport()
    #                     relatorio.graficos_hora(
    #                         email_txt, senha_txt, data_inicio, data_fim)

    #                     arquivo = cpg
    #                     relatorio.pegar_planilha(arquivo)
    #                     relatorio.horas()
    #                     sg.Popup('Grafico Exportado !')

    #                     ### Faz o tratamento de Velocidade ###
    #                 elif (mac):
    #                     # chamar grafico de velocidade
    #                     relatorio = ExportReport()
    #                     relatorio.graficos_hora(
    #                         email_txt, senha_txt, data_inicio, data_fim)
                        
    #                     arquivo = mac
    #                     relatorio.pegar_planilha(arquivo)
    #                     relatorio.horas()
    #                     sg.Popup('Grafico Exportado !')
                        
    #                 else:
    #                     sg.popup_error('Selecione ao menos uma opção')

                        

        # # Adicione o botão
        # botao_opitions = customtkinter.CTkButton(menu, text="Logar", command=clique_options)
        # botao_opitions.grid(row=3, columnspan=2, padx=10, pady=10, sticky="WE")
        # menu.grid_rowconfigure(3, weight=1)
        # menu.grid_columnconfigure(0, weight=1)    
        

    def clique(self):
        login_txt = self.login.get()
        senha_txt = self.senha.get()
        # data_inicio = self.data_inicial_var.get()
        # data_fim = self.data_final_var.get()
        garagem_txt = self.garagem.get()
        arla_garagem_txt = self.arla_garagem.get()
        externo_txt = self.externo.get()
        

        if garagem_txt == 1:
            garagem = True
        else:
            garagem = False

        if arla_garagem_txt == 1:
            arla_garagem = True
        else:
            arla_garagem = False

        if externo_txt == 1:
            externo = True
        else:
            externo = False        

        if login_txt == '' and senha_txt == '':
            sg.popup_error('Digite seu Login e Senha !')
        elif login_txt == '':
            sg.popup_error('Digite seu Login !')
        elif senha_txt == '':
            sg.popup_error('Digite sua Senha !')
        else:
            ### lanca abastecimento garagem ###
            if (garagem and arla_garagem == False and externo == False):
                acao = ExportReport()
                acao.evento_logar(login_txt,senha_txt)

                ### lanca todos os abastecimento ###
            elif (garagem and arla_garagem and externo):
                relatorio = ExportReport()
                relatorio.graficos_alertas(
                    login_txt, senha_txt)

                sleep(2)                

                ### lanca abastecimento externo ###
            elif ((externo and arla_garagem == False and garagem == False)):
                # chamar grafico de velocidade
                relatorio = ExportReport()
                relatorio.exportar_graficos(
                    login_txt, senha_txt)           

            else:
                sg.popup_error('Selecione ao menos uma opção')


    def interface(self):
        self.login = customtkinter.CTkEntry(
        self.janela, placeholder_text="Seu Login", width=200)
        self.login.grid(row=0, column=0, padx=0, pady=10)

        self.senha = customtkinter.CTkEntry(self.janela, placeholder_text="Sua senha", show="*", width=200)
        self.senha.grid(row=1, column=0, padx=10, pady=10)

        # self.data_inicial_var = tk.StringVar(value=self.data_inicial.strftime('%d/%m/%Y 00:01'))
        # self.data_inicial = customtkinter.CTkEntry(
        #     self.janela, textvariable=self.data_inicial_var, width=160, justify="center")
        # self.data_inicial.grid(row=2, column=0, padx=10, pady=10)

        # self.data_final_var = tk.StringVar(value=self.data_final.strftime('%d/%m/%Y 23:59'))
        # self.data_final = customtkinter.CTkEntry(
        #     self.janela, textvariable=self.data_final_var, width=160, justify="center")
        # self.data_final.grid(row=3, column=0, padx=10, pady=10)

        # Adicione os checkbox
        self.garagem = customtkinter.CTkCheckBox(self.janela, text="Garagem")
        self.garagem.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.janela.grid_rowconfigure(0, weight=1)

        self.arla_garagem = customtkinter.CTkCheckBox(self.janela, text="Arla Garagem")
        self.arla_garagem.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.janela.grid_rowconfigure(1, weight=1)

        self.externo = customtkinter.CTkCheckBox(self.janela, text="Externo")
        self.externo.grid(row=2, column=1, padx=10, pady=10, sticky="W")
        self.janela.grid_rowconfigure(2, weight=1)

        ### ARLA EXTERNO ###
        # self.arla_externo = customtkinter.CTkCheckBox(self.janela, text="Arla Externo")
        # self.arla_externo.grid(row=3, column=1, padx=10, pady=10, sticky="W")
        # self.janela.grid_rowconfigure(2, weight=1)
        # Adicione o botão
        # self.ociosidade_enradak = customtkinter.CTkButton(self.janela, text="Mostrar Opções", command=self.show_options)
        # self.ociosidade_enradak.grid(row=3, column=1, padx=10, pady=10, sticky="W")
        # self.janela.grid_rowconfigure(3, weight=1)


        self.botao = customtkinter.CTkButton(self.janela, text="Logar", command=self.clique)
        self.botao.grid(row=4, columnspan=2, padx=10, pady=10, sticky="WE")
        self.janela.grid_rowconfigure(4, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)    

        #self.janela.iconbitmap('alerta.ico')

        #setando imagem
        # self.img = PhotoImage(file="gm.png")
        # self.label_img = CustomLabel(master=self.janela, image=self.img)
        # self.label_img.place(x=5, y=5)


        self.janela.title("Abastecimentos")
        

# ini = gerenciador_alertas()
# ini.janela.mainloop()


# janela = customtkinter.CTk()
# janela.geometry("350x270")
# data_inicial = datetime.datetime.now() - datetime.timedelta(days=1)
# data_final = datetime.datetime.now() - datetime.timedelta(days=1)
# hora_inicial = "23:59"

# # classe de inicio


# def clique():
#     email_txt = email.get()
#     senha_txt = senha.get()
#     data_inicio = data_inicial_var.get()
#     data_fim = data_final_var.get()
#     velocidade_txt = velocidade_entrada.get()
#     ociosidade_txt = ociosidade_enrada.get()
#     relatorio_alerta = alertas_entrada.get()

#     if velocidade_txt == 1:
#         velocidade = True
#     else:
#         velocidade = False

#     if ociosidade_txt == 1:
#         ociosidade = True
#     else:
#         ociosidade = False

#     if relatorio_alerta == 1:
#         relatorio_alerta = True
#     else:
#         relatorio_alerta = False

#     if email_txt == '' and senha_txt == '':
#         sg.popup_error('Digite seu Email e Senha !')
#     elif email_txt == '':
#         sg.popup_error('Digite seu Email !')
#     elif senha_txt == '':
#         sg.popup_error('Digite sua Senha !')
#     else:
#         ### Para Tratar os Alertas ###
#         if (relatorio_alerta and ociosidade == False and velocidade == False):
#             relatorio = ExportReport()
#             relatorio.processar(
#                 email_txt, senha_txt)

#             ### Faz o tratamento de Alertas - Velocidade - Ociosidade ###
#         elif (velocidade and ociosidade and relatorio_alerta):
#             relatorio = ExportReport()
#             relatorio.graficos_alertas(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = velocidade
#             relatorio.criar_grafico(arquivo)
#             sg.Popup('Grafico De Velocidade Exportado !')

#             sleep(2)

#             relatorio.criar_grafico_ocioso(arquivo)
#             sg.Popup('Grafico De Ociosidade Exportado !')

#             ### Faz o tratamento de Velocidade ###
#         elif ((velocidade and ociosidade == False and relatorio_alerta == False)):
#             # chamar grafico de velocidade
#             relatorio = ExportReport()
#             relatorio.exportar_graficos(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = velocidade
#             relatorio.criar_grafico(arquivo)
#             sg.Popup('Grafico De Velocidade Exportado !')

#             ### Faz o tratamento de Ociosidade ###
#         elif ((ociosidade and velocidade == False and relatorio_alerta == False)):
#             # chamar grafico de ociosidade
#             relatorio = ExportReport()
#             relatorio.exportar_graficos(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = ociosidade
#             relatorio.criar_grafico_ocioso(arquivo)
#             sg.Popup('Grafico De Ociosidade Exportado !')

#             ### Faz o tratamento de Ociosidade e velocidade ###
#         elif (ociosidade and velocidade and relatorio_alerta == False):
#             relatorio = ExportReport()
#             relatorio.exportar_graficos(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = velocidade
#             relatorio.criar_grafico(arquivo)
#             sg.Popup('Grafico De Velocidade Exportado !')

#             sleep(2)

#             relatorio.criar_grafico_ocioso(arquivo)
#             sg.Popup('Grafico De Ociosidade Exportado !')

#             ### Faz o tratamento de Ociosidade e Alertas ###
#         elif (ociosidade and velocidade == False and relatorio_alerta):
#             relatorio = ExportReport()
#             relatorio.graficos_alertas(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = ociosidade
#             relatorio.criar_grafico_ocioso(arquivo)
#             sg.Popup('Grafico De Ociosidade Exportado !')

#             ### Faz o tratamento de Velocidade e Alertas ###
#         elif (ociosidade == False and velocidade and relatorio_alerta):
#             relatorio = ExportReport()
#             relatorio.graficos_alertas(
#                 email_txt, senha_txt, data_inicio, data_fim)

#             arquivo = velocidade
#             relatorio.criar_grafico(arquivo)
#             sg.Popup('Grafico De Velocidade Exportado !')

#         else:
#             sg.popup_error('Selecione ao menos uma opção')


# email = customtkinter.CTkEntry(
#     janela, placeholder_text="Seu e-mail", width=200)
# email.grid(row=0, column=0, padx=0, pady=10)

# senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*", width=200)
# senha.grid(row=1, column=0, padx=10, pady=10)

# data_inicial_var = tk.StringVar(
#     value=data_inicial.strftime('%d/%m/%Y 00:01'))
# data_inicial = customtkinter.CTkEntry(
#     janela, textvariable=data_inicial_var, width=160, justify="center")
# data_inicial.grid(row=2, column=0, padx=10, pady=10)

# data_final_var = tk.StringVar(value=data_final.strftime('%d/%m/%Y 23:59'))
# data_final = customtkinter.CTkEntry(
#     janela, textvariable=data_final_var, width=160, justify="center")
# data_final.grid(row=3, column=0, padx=10, pady=10)

# # Adicione os checkbox
# alertas_entrada = customtkinter.CTkCheckBox(janela, text="Alertas")
# alertas_entrada.grid(row=0, column=1, padx=10, pady=10, sticky="W")
# janela.grid_rowconfigure(0, weight=1)

# velocidade_entrada = customtkinter.CTkCheckBox(janela, text="Velocidade")
# velocidade_entrada.grid(row=1, column=1, padx=10, pady=10, sticky="W")
# janela.grid_rowconfigure(1, weight=1)

# ociosidade_enrada = customtkinter.CTkCheckBox(janela, text="Ociosidade")
# ociosidade_enrada.grid(row=2, column=1, padx=10, pady=10, sticky="W")
# janela.grid_rowconfigure(2, weight=1)

# # Adicione o botão
# botao = customtkinter.CTkButton(janela, text="Logar", command=clique)
# botao.grid(row=4, columnspan=2, padx=10, pady=10, sticky="WE")
# janela.grid_rowconfigure(4, weight=1)
# janela.grid_columnconfigure(0, weight=1)

# janela.title("Login de Usuário")
# janela.mainloop()

# -----------------
