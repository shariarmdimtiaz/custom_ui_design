import sys
from PyQt5 import QtWidgets, QtCore
# from PySide6.QtWidgets import QApplication, QWidget
from colmap_ui import Ui_DialogGenMesh

class DialogGenMesh(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogGenMesh()
        self.ui.setupUi(self)
        # Set form title
        self.setWindowTitle("Settings")
        self.ui.txtPath.setReadOnly(True)

        # Hide minimize & maximize, keep only close
        self.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )

        # Configure dsbTrimDef
        self.ui.dsbTrimDef.setDecimals(1)
        self.ui.dsbTrimDef.setMinimum(0.0)
        self.ui.dsbTrimDef.setMaximum(20.0)
        self.ui.dsbTrimDef.setValue(9.0)

        # Configure dsbWeightDef
        self.ui.dsbWeightDef.setDecimals(1)
        self.ui.dsbWeightDef.setMinimum(0.0)
        self.ui.dsbWeightDef.setMaximum(20.0)
        self.ui.dsbWeightDef.setValue(2.0)


        # Configure dsbDepthDef
        self.ui.dsbDepthDef.setDecimals(0)
        self.ui.dsbDepthDef.setMinimum(5)
        self.ui.dsbDepthDef.setMaximum(13)
        self.ui.dsbDepthDef.setValue(13)


    # def on_btnImport_clicked(self):
    #     file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
    #         self,
    #         "Select PLY file",
    #         "",
    #         "PLY Files (*.ply);"
    #     )
    #     if file_path:
    #         self.ui.txtPath.setText(file_path)

    def on_btnGenMesh_clicked(self):
        poissionTrimDefault = str(self.ui.dsbTrimDef.value())
        poissionWeightDefault = str(self.ui.dsbWeightDef.value())
        poissionDepthDefault = str(self.ui.dsbDepthDef.value())


    def on_btnCancel_clicked(self):
        # Close the dialog
        # self.reject()  # same as pressing "Cancel"
        # or use self.close() if you prefer just closing without return code
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dlg = DialogGenMesh()
    dlg.show()
    sys.exit(app.exec_())
