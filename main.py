# This Python file uses the following encoding: utf-8

import os
import sys
import socket
import time
import requests
import subprocess


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Check when create button is clicked
        self.ui.createBtn.clicked.connect(self.on_create_clicked)

        # Check when browse button is clicked
        self.ui.browseBtn.clicked.connect(self.on_browse_clicked)

        self.ui.progressBar.setValue(0)

        # Get latest info on available servers
        response = requests.get("https://api.papermc.io/v2/projects/paper")
        data = response.json()
        versions = data["versions"]
        self.ui.mcVersionDrop.addItems(versions)



    def on_create_clicked(self):
        print("create clicked")
        if (self.ui.eulaBtn.isChecked() == True):
            print("EULA accepted")
            if (self.ui.browseTxt.toPlainText() != ''):
                self.create_server()
            else:
                print("Empty")


    def on_browse_clicked(self):
        print("browse clicked")
        dir = QFileDialog.getExistingDirectory()
        os.chdir(dir)
        print(dir)
        self.ui.browseTxt.setText(dir)

    def create_server(self):
        print("Create started")

        version = self.ui.mcVersionDrop.currentText()
        print(version)

        self.ui.progressBar.setValue(10)

        # Get latest info on available servers
        response = requests.get("https://api.papermc.io/v2/projects/paper")
        data = response.json()
        latestVersion = data["versions"][-1]
        self.ui.progressBar.setValue(20)
        response = requests.get("https://api.papermc.io/v2/projects/paper/versions/" + version)
        data = response.json()
        latestBuild = data["builds"][-1]
        self.ui.progressBar.setValue(30)
        response = requests.get("https://api.papermc.io/v2/projects/paper/versions/" + version + "/builds/" + str(
            latestBuild) + "/downloads/paper-" + version + "-" + str(latestBuild) + ".jar")
        self.ui.progressBar.setValue(40)
        # Download the server
        with open("server.jar", "wb") as f:
            f.write(response.content)
            print("Minecraft server files downloaded!")
        self.ui.progressBar.setValue(70)
        with open("eula.txt", "w") as f:
            f.write(
                "#EULA accepted by user with MinecraftServerMaker.py\n#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).\neula=true")
        self.ui.progressBar.setValue(80)
        # Create bash file
        with open("run.sh", "w") as f:
            f.write(
                "#!/bin/bash\njava -Xmx" + "8" + "G -Xms" + "8" + "G -jar server.jar\necho \"Server off. Press enter to close\" \nread")
        self.ui.progressBar.setValue(90)
        os.chmod("run.sh", 0o755)

        self.ui.progressBar.setValue(100)
        subprocess.Popen("./run.sh")

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("The server is now set up.\nYou can run it by going to " + os.getcwd() +" And running \"run.sh\"")
        msg_box.setWindowTitle("Congradulations")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


