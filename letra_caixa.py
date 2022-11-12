from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

## Funções de Mensagens #####

def mensagem_tipo_material():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar um material!')
        x = msg1.exec()

def mensagem_altura():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a altura da letra caixa em cm! - Ex: 10')
        x = msg1.exec()

def mensagem_quantidade():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a quantidade!')
        x = msg1.exec()

def mensagem_error():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Favor informar a altura e a quantidade com número inteiro!')
        x = msg1.exec()

def calculo_layout():
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Calculo do Layout realizado!')
        x = msg1.exec()

##################################################################################

## Funções para limpar campos #####
def limpa_campos():
    tela.ln_altura.setText("")
    tela.ln_quantidade.setText("")
    tela.ln_valor.setText("")

def limpa_campos_layout():
    tela.ln_altura.setText("")
    tela.ln_quantidade.setText("")
    tela.ln_valor.setText("")
    tela.ln_layout_1.setText("0")
    tela.ln_layout_2.setText("0")
    tela.ln_layout_3.setText("0")
    tela.ln_layout_4.setText("0")
    tela.ln_layout_5.setText("0")
    tela.ln_layout_6.setText("0")
    tela.ln_valor_total.setText("")

##################################################################################

## Função valida se os campos dos layots estão preenchidos
def mensagem_campo_layout():
    if tela.ln_layout_1.text() and tela.ln_layout_2.text() and tela.ln_layout_3.text() and tela.ln_layout_4.text() \
        and tela.ln_layout_5.text() and tela.ln_layout_6.text() != "0":
        msg1 = QMessageBox()
        msg1.setIcon(QMessageBox.Information)
        msg1.setWindowTitle('Atenção!')
        msg1.setText('Os 6 campos de layout já foram calculados. Favor limpar a aplicação!')
        x = msg1.exec()

##################################################################################

## Função Botão Calcular ####

def calcular():
    
    mensagem_campo_layout()    

    try:     
        # Valida sem um dos radio buttons foi selecionado.
        if tela.rd_1.isChecked() or tela.rd_2.isChecked() or tela.rd_3.isChecked() or tela.rd_4.isChecked():

            # Valida qual radio button foi selecionado e atribui um valor a variavel (valor_material).
            if tela.rd_1.isChecked():
                valor_material = 3.5

            elif tela.rd_2.isChecked():
                valor_material = 4.5  

            elif tela.rd_3.isChecked():
                valor_material = 5.5 

            elif tela.rd_4.isChecked():
                valor_material = 6.5 
            
             ###############################

            # Valida se os campos receberam algum valor.
            if tela.ln_altura.text() == "":
                mensagem_altura()           

            elif tela.ln_quantidade.text() == "":
                mensagem_quantidade()
            
            ###############################

            # Executa o calculo
            else:
                altura = int(tela.ln_altura.text())
                quantidade = int(tela.ln_quantidade.text())
                valor_total = altura * quantidade * valor_material
                tela.ln_valor.setText(f'R$ {valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".") )

                # Regra de validação dos campos e atribuição de valores
                if tela.ln_layout_1.text() == "0":
                    tela.ln_layout_1.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    limpa_campos()
                    calculo_layout()

                elif tela.ln_layout_2.text() == "0":  
                    tela.ln_layout_2.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    calculo_layout()
                    limpa_campos()                    

                elif tela.ln_layout_3.text() == "0":  
                    tela.ln_layout_3.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    calculo_layout()
                    limpa_campos()                    

                elif tela.ln_layout_4.text() == "0":  
                    tela.ln_layout_4.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    calculo_layout()
                    limpa_campos()                    

                elif tela.ln_layout_5.text() == "0":  
                    tela.ln_layout_5.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    calculo_layout()
                    limpa_campos()
                                
                elif tela.ln_layout_6.text() == "0":  
                    tela.ln_layout_6.setText(f'{valor_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
                    calculo_layout()
                    limpa_campos()
            
            ###############################

        else:
            mensagem_tipo_material()

    # Trata erro de valor informado errado.
    except:
        mensagem_error()

    # Calcula o valor total dos layouts calculados
    valor_total_geral = float(tela.ln_layout_1.text().replace(",", "X").replace(".", "").replace("X", ".")) \
    + float(tela.ln_layout_2.text().replace(",", "X").replace(".", "").replace("X", ".")) \
    + float(tela.ln_layout_3.text().replace(",", "X").replace(".", "").replace("X", ".")) \
    + float(tela.ln_layout_4.text().replace(",", "X").replace(".", "").replace("X", ".")) \
    + float(tela.ln_layout_5.text().replace(",", "X").replace(".", "").replace("X", ".")) \
    + float(tela.ln_layout_6.text().replace(",", "X").replace(".", "").replace("X", ".")) 

    tela.ln_valor_total.setText(f'R$ {valor_total_geral:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))      

##################################################################################

app = QtWidgets.QApplication([])
tela = uic.loadUi("letra_caixa.ui")
tela.setFixedSize(470, 357)
tela.bt_calcular.clicked.connect(calcular)
tela.bt_limpar.clicked.connect(limpa_campos and limpa_campos_layout)

tela.show()
app.exec()
