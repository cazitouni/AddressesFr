import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'simple_ban_dialog_base.ui'))
class SimbleBanDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(SimbleBanDialog, self).__init__(parent)
        self.setupUi(self)