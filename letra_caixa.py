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

##################################################################################

## Função Botão Calcular ####

def calcular():   

    try:     
        # Valida sem um dos radio button foi selecionado.
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

            ###############################

        else:
            mensagem_tipo_material()

    # Trata erro de valor informado errado.
    except:
        mensagem_error()

##################################################################################


app = QtWidgets.QApplication([])
tela = uic.loadUi("letra_caixa.ui")
tela.setFixedSize(470, 180)
tela.bt_calcular.clicked.connect(calcular)

tela.show()
app.exec()