import pyautogui
import os
from time import sleep

from drivers_alertas import *
from datetime import datetime
from PIL import Image
import logging
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')
# importar as blibiotecas


agora = datetime.now()
data_atual = agora.strftime("%Y-%m-%d")
hora_atual = agora.strftime("%H:%M")


class ExportReport:
    # def __init__(self):
    #     self.__driver = iniciar_driver_solar()

    def evento_garagem(self, email, pwd, data_ini, data_fim):
        self.__driver.get('http://tracking.systemsatx.com.br/')

        try:
            # Realiza o login
            self.__login(email, pwd)
            sleep(2.3)

            # Download do relatorio
            self.__gerar_relatorio(data_ini, data_fim)

            # Exportando relatório
            self.__exportar()

        except:
            logging.info("Erro na geracao dos graficos !") 

    # def __gerar_relatorio_hora(self, dt_ini, dt_fim):
    #     # Carregando elementos da página
    #     menu_relatorio_geral = WebDriverWait(self.__driver, 5).until(
    #         EC.element_to_be_clickable((By.ID, 'Menu_4')))
    #     menu_relatorio_especifico = self.__driver.find_element(
    #         By.ID, 'Menu_21')

    #     # Clique nos botões para geração do relatório
    #     sleep(1.5)
    #     menu_relatorio_geral.click()
    #     sleep(1.5)
    #     menu_relatorio_especifico.click()
    #     logging.info("Filtrando o relatorio !")

    #     # Preenchendo data final
    #     self.__limpar_campo(data_fim)
    #     self.__preencher_campo(data_fim, dt_fim)

    #     # Preenchendo data inicial
    #     self.__limpar_campo(data_inicio)
    #     self.__preencher_campo(data_inicio, dt_ini)

    #     # Gerando relatório
    #     sleep(1)
    #     consultar.click()           

    def evento_arla_garagem(self, email, pwd, data_ini, data_fim):
        self.__driver.get('http://tracking.systemsatx.com.br/')

        try:
            self.__login(email, pwd)
            sleep(2.3)

            self.__gerar_relatorio(data_ini, data_fim)

            # Exportando relatório
            self.__exportar()
            return True

            # self.__driver.close()
        except Exception as e:
            return False
            print(e)

    def evento_externo(self, email, pwd, data_ini, data_fim):
        self.__driver.get('http://tracking.systemsatx.com.br/')

        try:
            self.__login(email, pwd)
            sleep(2.3)

            # confere as notificaçoes
            self.notificacao()

            # clica na seta para subir a pagina
            self.botao_subir()

            # clica no ok dos alertas
            self.seta_ciente()

            self.__gerar_relatorio(data_ini, data_fim)

            # Exportando relatório
            self.__exportar()
            return True

            # self.__driver.close()
        except Exception as e:
            return False
            print(e)

    # Função que realiza o processamento do sistema
    def evento_logar(self,login, senha):
       pyautogui.moveTo(32,125, duration=2)
       pyautogui.doubleClick()
       sleep(9)
       pyautogui.moveTo(1323,10, duration=2)
       pyautogui.click()
       pyautogui.moveTo(646,441, duration=2)
       sleep(0.5)
       pyautogui.click()
       pyautogui.doubleClick()
       for i in login:
           pyautogui.typewrite(i)
           sleep(0.5)        
       pyautogui.moveTo(645,463, duration=2)
       pyautogui.doubleClick()
       for i in senha:
           pyautogui.typewrite(i)
           sleep(0.5)
       pyautogui.moveTo(580,485, duration=1) 
       pyautogui.doubleClick()

        
      


  

    

    #     # Preenchendo campos
    #     self.__preencher_campo(input_email, email)
    #     self.__preencher_campo(input_senha, pwd)

    
    # # Preenchendo data final
    #     self.__limpar_campo(data_fim)
    #     self.__preencher_campo(data_fim, dt_fim)

    #     # Preenchendo data inicial
    #     self.__limpar_campo(data_inicio)
    #     self.__preencher_campo(data_inicio, dt_ini)      

    

    # Limpa o campo de texto

    def __limpar_campo(self, input):
        sleep(1.5)
        input.click()
        sleep(0.5)
        input.send_keys(Keys.CONTROL, 'a')
        sleep(0.25)
        input.send_keys(Keys.DELETE)

    # Preenche o elemento indicado com o texto informado
    def __preencher_campo(self, input, text):
        sleep(1)
        input.click()
        sleep(0.5)
        for l in text:
            input.send_keys(l)
            sleep(0.075)


    def pegar_planilha(self, arquivo):
        prosseguir = arquivo
        if prosseguir:
            caminho = "C:\\relatorios"
            lista_arquivo = os.listdir(caminho)

            lista_data = []
            # itera sobre a lista de arquivos, atribuindo cada arquivo a variável arquivo.
            for arquivo in lista_arquivo:
                # utiliza a função os.path.getmtime() para obter a data da última modificação do arquivo. O caminho do arquivo é construído concatenando a variável caminho (que deve conter o caminho para a pasta que contém os arquivos) com a variável arquivo.
                data = os.path.getmtime(f"{caminho}\\{arquivo}")
                # adiciona uma tupla contendo a data de modificação do arquivo e o nome do arquivo na lista lista_data.
                lista_data.append((data, arquivo))

            lista_data.sort(reverse=True)
            sleep(0.5)
            # seleciona a primeira tupla da lista ordenada, que contém a data de modificação e o nome do arquivo mais recente.
            ultimo_arquivo = lista_data[0]
            sleep(0.5)
            # extrai o nome do arquivo mais recente da tupla selecionada e armazena-o na variável ultimo_arquivo_final.
            ultimo_arquivo_final = ultimo_arquivo[1]
            sleep(0.5)
            # buscando o arquivo para manipulacao
            # carrega o arquivo mais recente em um objeto pandas.DataFrame utilizando a função pd.read_excel(),
            dataset = pd.read_excel(f"{caminho}\\{ultimo_arquivo_final}")
            #dataset.head()
            print(dataset)
            for arquivo in lista_arquivo:
                sleep(0.5)
                if arquivo != ultimo_arquivo_final:
                    os.remove(f"{caminho}\\{arquivo}")
                    print(arquivo)
        return dataset

    def criar_grafico(self):
        caminho = "C:\\relatorios"
        dataset = self.pegar_planilha(caminho)
        print(dataset)
        
        sleep(1)

        # excluindo colunas
        dataset.drop("Nº ordem rastreador", axis=1, inplace=True)
        dataset.drop("Requer tratamento", axis=1, inplace=True)
        dataset.drop("Situação do chamado", axis=1, inplace=True)
        dataset.drop("Unnamed: 6", axis=1, inplace=True)
        dataset.drop("Unnamed: 7", axis=1, inplace=True)
        dataset.drop("Unnamed: 8", axis=1, inplace=True)
        dataset.drop("Unnamed: 9", axis=1, inplace=True)
        dataset.drop("Unnamed: 11", axis=1, inplace=True)
        dataset.drop("Unnamed: 12", axis=1, inplace=True)
        dataset.drop("Unnamed: 15", axis=1, inplace=True)
        dataset.drop("Unnamed: 16", axis=1, inplace=True)
        dataset.drop("Unnamed: 17", axis=1, inplace=True)
        dataset.drop("Unnamed: 18", axis=1, inplace=True)
        dataset.drop("Chamado", axis=1, inplace=True)
        dataset.drop("Unnamed: 20", axis=1, inplace=True)
        dataset.drop("Unnamed: 21", axis=1, inplace=True)
        dataset.drop("Unnamed: 22", axis=1, inplace=True)
        dataset.drop("Unnamed: 23", axis=1, inplace=True)
        dataset.drop("Unnamed: 24", axis=1, inplace=True)
        dataset.drop("Unnamed: 26", axis=1, inplace=True)
        dataset.drop("Unnamed: 27", axis=1, inplace=True)
        dataset.drop("Unnamed: 28", axis=1, inplace=True)
        dataset.drop("Grupo de unidades rastreadas", axis=1, inplace=True)
        dataset.drop("Unidade organizacional", axis=1, inplace=True)
        dataset.drop("Local fim", axis=1, inplace=True)
        dataset.drop("Modo de violação", axis=1, inplace=True)
        dataset.drop("Unnamed: 25", axis=1, inplace=True)

        # trocar nome das colunas
        df = dataset.rename(columns={"Unnamed: 10": "Regra",
                            "Unnamed: 13": "Data", "Unnamed: 14": "Duracao"})
        # filtro por regra
        nod = df.loc[(df["Regra"] == "Excesso de Velocidade - 82km/h")]

        # salvando em  csv
        nod.to_csv("csv/Velocidade")
        nod.to_excel("csv/velocidade.xlsx")
        # abrindo o csv
        novo = pd.read_csv("csv/Velocidade")
        # excluindo coluna
        novo.drop("Unnamed: 0", axis=1, inplace=True)
        # ordenando e salvando
        novo = novo.sort_values('Unidade rastreada')
        # fazendo contagens dos alertas por placa
        ng = novo['Unidade rastreada'].value_counts()
        print(ng)

        try:
            relatorio_velocidade = pd.read_excel('csv/velocidade.xlsx')        
            data_relatorio = relatorio_velocidade.iloc[0, 5][0:9]
        except:
            print("ERRO ! ARQUIVO CSV NÃO LOCALIZADO !")    

        # gerando grafico
        try:
            plt.style.use("grayscale")
            novo["Unidade rastreada"].value_counts().plot.barh(
                figsize=(17, 5), color='green', title=f"Alertas de Velocidade {data_relatorio } {hora_atual}")
            tsize = 14
            fsize, lsize = 15, 6
            xlab = 'Quantidade de ocorencias'
            ylab = 'Placas'
            plt.xlabel(xlab,  fontsize=fsize)
            plt.ylabel(ylab,  fontsize=fsize)
            plt.tick_params(labelsize=tsize, width=2)
            # plt.legend()
            plt.savefig(f"graficos/{data_atual}-Picos.png", format="png")
            plt.close()
            logging.info("Gerando grafico de Velocidade")
        except:
            logging.info("Sem Alertas de Velocidade")

    # else:
    #     print("obrigado")

    def criar_grafico_ocioso(self):
        caminho = "C:\\relatorios"
        dataset = self.pegar_planilha(caminho)
        print(dataset)
        
        sleep(1)         

        # excluindo colunas
        dataset.drop("Nº ordem rastreador", axis=1, inplace=True)
        dataset.drop("Requer tratamento", axis=1, inplace=True)
        dataset.drop("Situação do chamado", axis=1, inplace=True)
        dataset.drop("Motorista", axis=1, inplace=True)
        dataset.drop("Unnamed: 6", axis=1, inplace=True)
        dataset.drop("Unnamed: 7", axis=1, inplace=True)
        dataset.drop("Unnamed: 8", axis=1, inplace=True)
        dataset.drop("Unnamed: 9", axis=1, inplace=True)
        # dataset.drop("Unnamed: 11", axis=1, inplace=True)
        dataset.drop("Unnamed: 12", axis=1, inplace=True)
        dataset.drop("Unnamed: 13", axis=1, inplace=True)
        dataset.drop("Alerta", axis=1, inplace=True)
        dataset.drop("Unnamed: 15", axis=1, inplace=True)
        dataset.drop("Unnamed: 16", axis=1, inplace=True)
        dataset.drop("Unnamed: 17", axis=1, inplace=True)
        dataset.drop("Unnamed: 18", axis=1, inplace=True)
        dataset.drop("Chamado", axis=1, inplace=True)
        dataset.drop("Unnamed: 20", axis=1, inplace=True)
        dataset.drop("Unnamed: 21", axis=1, inplace=True)
        dataset.drop("Unnamed: 22", axis=1, inplace=True)
        dataset.drop("Unnamed: 23", axis=1, inplace=True)
        dataset.drop("Unnamed: 24", axis=1, inplace=True)
        dataset.drop("Unnamed: 26", axis=1, inplace=True)
        dataset.drop("Unnamed: 27", axis=1, inplace=True)
        dataset.drop("Unnamed: 28", axis=1, inplace=True)
        dataset.drop("Grupo de unidades rastreadas", axis=1, inplace=True)
        dataset.drop("Unidade organizacional", axis=1, inplace=True)
        dataset.drop("Local fim", axis=1, inplace=True)
        dataset.drop("Modo de violação", axis=1, inplace=True)
        dataset.drop("Unnamed: 25", axis=1, inplace=True)

        # trocar nome das colunas
        df = dataset.rename(
            columns={"Unnamed: 10": "Regra", "Unnamed: 11": "Data", "Unnamed: 14": "Duracao" })
        # filtro por regra
        nod = df.loc[(df['Regra'] == 'Motor Ocioso 24V - Tempo Superior ao Permitido')]
        nod.to_excel('csv/dados_ocioso_data.xlsx')

        # alteradno o tipo da data
        nod["Duracao"] = nod["Duracao"].astype("datetime64[ns]")

        # separando por minuto
        nod['Minutos'] = nod['Duracao'].dt.minute
        nod.to_excel('csv/dados_ocioso.xlsx')
        # salvando em  csv
        nod.to_csv("csv/Motor_Ocioso")
        # abrindo o csv
        novo = pd.read_csv("csv/Motor_Ocioso")
        # excluindo coluna
        novo.drop("Unnamed: 0", axis=1, inplace=True)
        # ordenando e salvando
        # novo.sort_values('Unidade rastreada').to_csv("Velocidade")
        # fazendo contagens dos alertas por placa
        # ng = novo['Unidade rastreada'].value_counts()
        # print(ng)
        # pegando o arquivo

        somar = pd.read_excel('csv/dados_ocioso.xlsx')
        # gerando grafico

        df = pd.read_excel('csv/dados_ocioso_data.xlsx')
        data_relatorio = df.iloc[0, 3][0:10]

        try:
            plt.style.use("grayscale")
            somar.groupby('Unidade rastreada')['Minutos'].sum().plot.barh(
                figsize=(20, 8), color='green', title=f"MOTOR OCIOSO {data_relatorio } {hora_atual}")
            tsize = 14
            fsize, lsize = 20, 6
            xlab = 'Tempo (MINUTOS) de Ociosidade'
            ylab = 'Placa / Motorista'
            plt.xlabel(xlab,  fontsize=fsize)
            plt.ylabel(ylab,  fontsize=fsize)
            plt.tick_params(labelsize=tsize, width=2)
            # plt.legend();
            plt.savefig(f"graficos/{data_atual}-Ocioso.png", format="jpg")
            plt.close()
            logging.info("Gerando grafico de Ociosidade")
        except:
            logging.info("Sem Alertas de Ociosidade")

    

    def horas(self):
        caminho = "C:\\relatorios"
        dataset = self.pegar_planilha(caminho)
        print(dataset)
        
        sleep(1)   

        # excluindo colunas
        dataset.drop("Nº ordem rastreador", axis=1, inplace=True)
        dataset.drop("Requer tratamento", axis=1, inplace=True)
        dataset.drop("Situação do chamado", axis=1, inplace=True)
        dataset.drop("Motorista", axis=1, inplace=True)
        #dataset.drop("Unnamed: 6", axis=1, inplace=True)
        dataset.drop("Unnamed: 7", axis=1, inplace=True)
        dataset.drop("Unnamed: 8", axis=1, inplace=True)
        dataset.drop("Unnamed: 9", axis=1, inplace=True)
        # dataset.drop("Unnamed: 11", axis=1, inplace=True)
        dataset.drop("Unnamed: 12", axis=1, inplace=True)
        dataset.drop("Unnamed: 13", axis=1, inplace=True)
        dataset.drop("Alerta", axis=1, inplace=True)
        dataset.drop("Unnamed: 15", axis=1, inplace=True)
        dataset.drop("Unnamed: 16", axis=1, inplace=True)
        dataset.drop("Unnamed: 17", axis=1, inplace=True)
        dataset.drop("Unnamed: 18", axis=1, inplace=True)
        dataset.drop("Chamado", axis=1, inplace=True)
        dataset.drop("Unnamed: 20", axis=1, inplace=True)
        dataset.drop("Unnamed: 21", axis=1, inplace=True)
        dataset.drop("Unnamed: 22", axis=1, inplace=True)
        dataset.drop("Unnamed: 23", axis=1, inplace=True)
        dataset.drop("Unnamed: 24", axis=1, inplace=True)
        dataset.drop("Unnamed: 26", axis=1, inplace=True)
        dataset.drop("Unnamed: 27", axis=1, inplace=True)
        dataset.drop("Unnamed: 28", axis=1, inplace=True)
        dataset.drop("Grupo de unidades rastreadas", axis=1, inplace=True)
        dataset.drop("Unidade organizacional", axis=1, inplace=True)
        dataset.drop("Local fim", axis=1, inplace=True)
        dataset.drop("Modo de violação", axis=1, inplace=True)
        dataset.drop("Unnamed: 25", axis=1, inplace=True)
        dataset.drop("Local início", axis=1, inplace=True)
        
        df = dataset.rename(
            columns={"Unnamed: 6": "Unidade", "Unnamed: 10": "Regra", "Unnamed: 11": "Data", "Unnamed: 14": "Duracao"})

        df.to_excel('csv/horas_base.xlsx')
        df = pd.read_excel('csv/horas_base.xlsx')
        data_relatorio = df.iloc[1, 4][0:10]
        

        df = df.drop(index=0)

        df.to_csv("csv/tempoun")
        df = pd.read_csv("csv/tempoun")

        nod = df.loc[(df['Regra'] == 'Entrada em área - Coca Cola Macaíba/RN')]        
        nod["Duracao"] = nod["Duracao"].astype("datetime64[s]")



        df = nod[['Unidade rastreada', 'Duracao']]
        df['hora'] = df['Duracao'].dt.hour
        df['Minutos'] = df['Duracao'].dt.minute
        df.to_excel('csv/unidade.xlsx')

        df = df.dropna(subset=['Minutos'], how='any')

        df.to_csv("csv/saida")

        tratamento = pd.read_csv("csv/saida")

        soma_por_unidade = tratamento.groupby("Unidade rastreada")[["hora","Minutos"]].sum()
        soma_por_unidade.to_csv("csv/saida_hora")

        tratamento_hora = pd.read_csv("csv/saida_hora")
        

        tratamento_hora['hora'] = tratamento_hora.apply(lambda row: row['hora'] + 1 if row['Minutos'] > 60 else row['hora'], axis=1)
        tratamento_hora['Minutos'] = tratamento_hora.apply(lambda row: row['Minutos'] - 60 if row['Minutos'] > 60 else row['Minutos'], axis=1)

        df = tratamento_hora.sort_values(by='hora', ascending=True)  # Ordena o DataFrame
        fig, ax = plt.subplots(figsize=(15, 6))
        ax.barh(df['Unidade rastreada'], df['hora'] + df['Minutos']/60, color='green')
        ax.set_xlabel('Tempo (horas)')
        ax.set_ylabel('Unidade rastreada')
        ax.set_title(f'Tempo de rastreamento por unidade {data_relatorio } {hora_atual}')

        plt.savefig(f'graficos/{data_atual}-hora.png', format="png")
        

        df = tratamento_hora.sort_values(by='hora', ascending=True)  # Ordena o DataFrame
        # configurar tamanho das colunas
        col_widths = [0.5, 0.2, 0.2]

        # criar figura e adicionar tabela
        fig, ax = plt.subplots(figsize=(5.5, 5))
        ax.axis('off')
        ax.axis('tight')
        table = ax.table(cellText=df.values, colLabels=df.columns, colWidths=col_widths, cellLoc='center', loc='center')
        plt.savefig(f'graficos/{data_atual}-hora_minuto.png', format="png")

        # Abrindo as duas imagens
        img1 = Image.open(f'graficos/{data_atual}-hora_minuto.png')
        img2 = Image.open(f'graficos/{data_atual}-hora.png')

        # Obtendo as dimensões das imagens
        width1, height1 = img1.size
        width2, height2 = img2.size

        # Redimensionando as imagens para ter a mesma altura
        if height1 > height2:
            ratio = height2 / height1
            new_width = int(width1 * ratio)
            img1 = img1.resize((new_width, height2))
        elif height2 > height1:
            ratio = height1 / height2
            new_width = int(width2 * ratio)
            img2 = img2.resize((new_width, height1))

        # Obtendo as dimensões atualizadas das imagens
        width1, height1 = img1.size
        width2, height2 = img2.size

        # Calculando a largura e a altura da imagem combinada
        combined_width = max(width1, width2)
        combined_height = height1 + height2

        # Criando uma nova imagem com as dimensões combinadas
        combined_image = Image.new('RGB', (combined_width, combined_height), color=(255, 255, 255))

        # Colocando a primeira imagem na nova imagem
        x1 = (combined_width - width1) // 2
        combined_image.paste(im=img1, box=(x1, 0))

        # Colocando a segunda imagem na nova imagem
        x2 = (combined_width - width2) // 2
        y2 = height1
        combined_image.paste(im=img2, box=(x2, y2))

        # Salvando a imagem combinada
        combined_image.save(f'graficos/{data_atual}-combined.png', format="png")