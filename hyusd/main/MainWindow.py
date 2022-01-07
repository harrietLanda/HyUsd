import os

import sys
sys.path.append(r"C:/Users/harriet/workspace/deploy")
sys.path.append(r"C:/Users/harriet/workspace/hyusd/hyusd/main")


import hyusd_note_editor as hyne

from Qt import *

from qtpy import QtWidgets

class HyUSD_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: seashell;")

        self.setWindowTitle("HyUSD by Harriet Landa")
        self.resize(1920, 1080)

        self.create_widgets()
        self.create_connections()
        self.create_layout()

    def create_widgets(self):
        self.scene, self.view = hyne.main(app)

        self.populate_top_widgets()

        self.pro_layout = QtWidgets.QFormLayout()
        self.populate_properties()


    def populate_top_widgets(self):
        self.load_file_btn = QtWidgets.QPushButton('Load File')

        self.filter_lbl = QtWidgets.QLabel('Search')
        self.filter_le = QtWidgets.QLineEdit()
        self.filter_le.setPlaceholderText('filter')

        self.clean_btn = QtWidgets.QPushButton('Clean')

        self.flush_view = QtWidgets.QPushButton('Flush')

    def populate_properties(self, input=0):

        self.prop_dict = {}

        if input:
            file_name, size = self.get_properties()

            self.prop_dict['File Name'] = QtWidgets.QLineEdit(file_name)

            self.prop_dict['Size'] = QtWidgets.QLineEdit("{} KB".format(size))

        else:
            fpath = 'No directory yet'
            self.prop_dict['File Name'] = QtWidgets.QLineEdit(fpath)

            self.prop_dict['Size'] = QtWidgets.QLineEdit("0 KB")

        for k in self.prop_dict:
            try:
                self.prop_dict.get(k).setReadOnly(True)
            except:
                pass

            self.pro_layout.addRow(QtWidgets.QLabel(k), self.prop_dict.get(k))


    def flush_properties(self):

        if self.pro_layout.count() > 1:
            #delete each widget in the layout one by one
            while self.pro_layout.count():
                item = self.pro_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    #two ways to delete widgets
                    #widget.setParent(None)
                    widget.deleteLater()
                else:
                    deleteItemsOfLayout(item.pro_layout())
        else:
            pass

        self.populate_properties(input=1)

    def get_properties(self):
        try:
            size = float(os.path.getsize(self.fpath) * 0.001)
            file_name = os.path.basename(self.fpath)
        except:
            size, file_name = None
        return file_name, size

    def create_connections(self):
        self.load_file_btn.clicked.connect(self.load_file)

    def load_file(self):
        self.fpath, filter = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Load Image"), filter='USD (*.usdc, *.usdnc, *.usdc, *.usda)')
        self.flush_properties()

    def create_layout(self):

        self.main_layout =  QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QVBoxLayout()

        self.top_layout = QtWidgets.QHBoxLayout()

        self.main_layout.setSpacing(2)
        self.top_layout.addWidget(self.load_file_btn)
        self.top_layout.addWidget(self.filter_lbl)
        self.top_layout.addWidget(self.filter_le)
        self.top_layout.addWidget(self.clean_btn)
        self.top_layout.addWidget(self.flush_view)


        self.layout.addLayout(self.top_layout)
        self.layout.addWidget(self.view)

        self.main_layout.addLayout(self.layout)
        self.main_layout.addLayout(self.pro_layout)
        self.setLayout(self.main_layout)


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    window = HyUSD_MainWindow()
    window.show()
    app.exec_()