# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader

from functools import partial
import random

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()


        self.game=[[None for i in range(3)]for j in range(3)]
        self.game[0][0] = self.ui.btn_00
        self.game[0][1] = self.ui.btn_01
        self.game[0][2] = self.ui.btn_02
        self.game[1][0] = self.ui.btn_10
        self.game[1][1] = self.ui.btn_11
        self.game[1][2] = self.ui.btn_12
        self.game[2][0] = self.ui.btn_20
        self.game[2][1] = self.ui.btn_21
        self.game[2][2] = self.ui.btn_22

        self.player = 1
        self.player1_wins=0
        self.player2_wins=0
        self.draw=0
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play,i,j))
        self.ui.btn_new.clicked.connect(self.NewGame)
    def play(self,i,j):
        if self.game[i][j].text()=="":
            if self.player==1:
                self.game[i][j].setText('x')
                self.game[i][j].setStyleSheet('color: blue; background-color:#CCffff')
                self.player=2
                if self.ui.rb_cpu.isChecked():
                    while True:
                        row = random.randint(0, 2)
                        col = random.randint(0, 2)
                        if self.game[row][col].text() == "":
                            self.game[row][col].setText('o')
                            self.game[row][col].setStyleSheet('color: red; background-color:#ffCCCC')
                            self.player = 1
                            break

            elif self.player == 2:
                if self.ui.rb_player.isChecked()==True:
                    self.game[i][j].setText('o')
                    self.game[i][j].setStyleSheet('color: red; background-color:#ffCCCC')
                    self.player = 1

        self.check()
    def check(self):
        if all([self.game[0][i].text()=='x' for i in range(3)]) or all([self.game[1][i].text()=='x' for i in range(3)]) or all([self.game[2][i].text()=='x' for i in range(3)]):
            self.player1_wins+=1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg_box=QMessageBox()
            msg_box.setText('???????????? ??????????1 ?????????? ????.')
            msg_box.exec_()

        elif all([self.game[i][0].text()=='x' for i in range(3)]) or all([self.game[i][1].text()=='x' for i in range(3)]) or all([self.game[i][2].text()=='x' for i in range(3)]):
            self.player1_wins+=1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg_box=QMessageBox()
            msg_box.setText('???????????? ??????????1 ?????????? ????.')
            msg_box.exec_()

        elif self.game[0][2].text()=="x" and self.game[1][1].text()=="x" and self.game[2][0].text()=="x":
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg_box = QMessageBox()
            msg_box.setText('???????????? ??????????1 ?????????? ????.')
            msg_box.exec_()

        elif self.game[0][0].text()=="x" and self.game[1][1].text()=="x" and self.game[2][2].text()=="x":
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg_box = QMessageBox()
            msg_box.setText('???????????? ??????????1 ?????????? ????.')
            msg_box.exec_()

        elif all([self.game[0][i].text()=='o' for i in range(3)]) or all([self.game[1][i].text()=='o' for i in range(3)]) or all([self.game[2][i].text()=='o' for i in range(3)]):
            self.player2_wins+=1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg_box=QMessageBox()
            msg_box.setText('???????????? ??????????2 ?????????? ????.')
            msg_box.exec_()

        elif all([self.game[i][0].text()=='o' for i in range(3)]) or all([self.game[i][1].text()=='o' for i in range(3)]) or all([self.game[i][2].text()=='o' for i in range(3)]):
            self.player2_wins+=1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg_box=QMessageBox()
            msg_box.setText('???????????? ??????????2 ?????????? ????.')
            msg_box.exec_()

        elif self.game[0][2].text()=="o" and self.game[1][1].text()=="o" and self.game[2][0].text()=="o":
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg_box = QMessageBox()
            msg_box.setText('???????????? ??????????2 ?????????? ????.')
            msg_box.exec_()
        elif self.game[0][0].text()=="o" and self.game[1][1].text()=="o" and self.game[2][2].text()=="o":
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg_box = QMessageBox()
            msg_box.setText('???????????? ??????????2 ?????????? ????.')
            msg_box.exec_()

        elif all([self.game[0][i].text()!='' for i in range(3)]) and all([self.game[1][i].text()!='' for i in range(3)]) and all([self.game[2][i].text()!='' for i in range(3)]):
            print([[self.game[i][j].text() for i in range(3)] for j in range(3)])
            self.draw += 1
            self.ui.lbl_draw.setText(str(self.draw))
            msg_box = QMessageBox()
            msg_box.setText('draw')
            msg_box.exec_()
    def NewGame(self):
        self.player=1
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet('color: white; background-color:#e2e2e2')
                self.player1_wins = 0
                self.player2_wins = 0
                self.draw = 0
                self.ui.lbl_player1.setText(str(self.player1_wins))
                self.ui.lbl_player2.setText(str(self.player2_wins))
                self.ui.lbl_draw.setText(str(self.draw))
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
