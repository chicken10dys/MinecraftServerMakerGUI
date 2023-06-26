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

ramOptions = ["500M", "1G", "2G", "4G", "6G", "8G", "12G", "16G"]

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
        versions.reverse()
        self.ui.mcVersionDrop.addItems(versions)

        # Populate ram selector
        self.ui.ramDrop.addItems(ramOptions)

        # Detect platform to choose from .sh or .bat files
        if sys.platform.startswith('win'):
            self.script = "windows"
        elif sys.platform.startswith('linux'):
            self.script = "bash"
        elif sys.platform.startswith('darwin'):
            self.script = "bash"

        # Make version and ram text backgrounds transparent
        self.ui.mcVersionTxt.setStyleSheet("background-color: transparent;")
        self.ui.ramTxt.setStyleSheet("background-color: transparent;")

    def on_create_clicked(self):
        print("create clicked")
        if (self.ui.crossplayBtn.isChecked() == True):
            print("Crossplay enabled")
        if (self.ui.eulaBtn.isChecked() == True):
            print("EULA accepted")
            if (self.ui.browseTxt.toPlainText() != ''):
                self.create_server()
            else:
                print("Empty")
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("You must choose a save directory by entering it in or clicking browse")
                msg_box.setWindowTitle("Save path empty")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()

        else:
            print("Eula unselected")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText(
                "You must accept the EULA by checking the radio button at the top")
            msg_box.setWindowTitle("EULA not accepted")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()


    def on_browse_clicked(self):
        print("browse clicked")
        dir = QFileDialog.getExistingDirectory()
        os.chdir(dir)
        print(dir)
        self.ui.browseTxt.setPlainText(dir)

    def create_server(self):
        print("Create started")

        # Get version and print it for debugging
        version = self.ui.mcVersionDrop.currentText()
        print(version)

        # Get ram size and print it for debugging
        ram = self.ui.ramDrop.currentText()
        print(ram)

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
        print("Server: file 1/1 downloaded")
        if (self.ui.crossplayBtn.isChecked() == True): # If the user wants crossplay then download the required plugins
            response = requests.get("https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot")
            os.mkdir("plugins") # Make plugins directory
            with open("plugins/Geyser-Spigot.jar", "wb") as f: # Open new file for writing
                f.write(response.content)
            print("Crossplay: file 1/2 downloaded")
            self.ui.progressBar.setValue(50)
            response = requests.get("https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot")
            with open("plugins/floodgate-Spigot.jar", "wb") as f:
                f.write(response.content)
            print("Crossplay: file 2/2 downloaded")
            self.ui.progressBar.setValue(60)

        self.ui.progressBar.setValue(70)
        with open("eula.txt", "w") as f:
            f.write(
                "#EULA accepted by user with MinecraftServerMaker.py\n#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).\neula=true")
        self.ui.progressBar.setValue(80)

        if(self.script == "bash"):
            # Create bash file
            with open("run.sh", "w") as f:
                f.write(
                    "#!/bin/bash\njava -Xmx" + ram + " -Xms" + ram + " -jar server.jar\necho \"Server off. Press enter to close\" \nread")
            self.ui.progressBar.setValue(90)
            os.chmod("run.sh", 0o755)

            self.ui.progressBar.setValue(100)
            subprocess.Popen("./run.sh")

        elif (self.script == "windows"):
            with open("run.bat", "w") as f:
                f.write("java -Xmx" + ram + " -Xms" + ram + " -jar server.jar\npause")
            self.ui.progressBar.setValue(100)
            subprocess.Popen(os.getcwd() + "/run.bat")

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if (self.script == "bash"):
            msg_box.setText("The server is now set up.\nYou can run it by going to " + os.getcwd() +" And running \"run.sh\"")
        elif (self.script == "windows"):
            msg_box.setText("The server is now set up.\nYou can run it by going to " + os.getcwd() +" And running \"run.bat\"")
        msg_box.setWindowTitle("Congradulations")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

        if (self.script == "windows"):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("When the server opens for the first time you might see a windows firewall popup.\nIf you do then allow it for both public and private networks.")
            msg_box.setWindowTitle("Firewall information")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


