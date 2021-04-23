import sys
from PyQt5 import QtWidgets, uic

class Advice(QtWidgets.QWidget):
    def __init__(self, ui, adv, mViget):
        super(Advice, self).__init__()
        uic.loadUi(ui, self)
        self.mViget = mViget
        self.adv = adv
        self.num = 0
        self.nadv(0)
        self.pr.clicked.connect(lambda: self.nadv(1))
        self.pl.clicked.connect(lambda: self.nadv(-1))
        self.menu.clicked.connect(self.adExit)


    def nadv(self, step):
        self.num = (self.num + step) % len(self.adv)
        text = self.adv[self.num]
        self.l1.setText(text)

    def adExit(self):
        self.mViget.setSelf()
        self.hide()








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    prog = Advice("untitled1.ui")
    prog.show()
    sys.exit(app.exec())
