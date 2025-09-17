import sys
from PyQt6 import QtWidgets
from colmap_ui import Ui_DialogGenMesh

class DialogGenMesh(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogGenMesh()
        self.ui.setupUi(self)

        # Disconnect first (safety) then connect
        try:
            self.ui.btnImport.clicked.disconnect()
        except TypeError:
            pass  # no previous connection
        self.ui.btnImport.clicked.connect(self.on_btnImport_clicked)

    def on_btnImport_clicked(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select PLY file",
            "",
            "PLY Files (*.ply);"
        )
        if file_path:
            self.ui.txtPath.setText(file_path)

    def on_btnGen_clicked(self):
        poissionTrimDefault = str(self.ui.dsbTrimDef.value())
        poissionTrimMin = str(self.ui.dsbTrimMin.value())

        # Always start with the imported path only (don’t duplicate old text)
        file_path = self.ui.txtPath.toPlainText().splitlines()[0]  # keep only first line (the file path)

        # Add values once
        new_text = file_path + "\n" + poissionTrimDefault + ", " + poissionTrimMin

        self.ui.txtPath.setText(new_text)

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
