# simple-app-using-kivy-across-platform


[kivy](https://kivy.org/doc/stable/)

Two ways to create an app are as below:
1. Write everythong in Python, GUI in Python
2. Or Write GUI in kivy and everything else in Python


<h2>How to make APK File</h2>

1. Install Ubuntu in [Virtual Box](https://www.virtualbox.org/)
2. Copy files from current OS to Virtual Box [Ubuntu](https://ubuntu.com/) Environment
3. Open ubuntu terminal and run command (bash kivy-buildozer-installer.sh). Enter the password created while installing Ubuntu.
4. To try out the app run command (python3 main.py)
5. Run (buildozer init) to create buildozer.spec file. You can edit this.
6. Run (buildozer andriod clean debug)


<h2>How to install apk file on Adriod</h2>
1. Transfer the apk file to your andriod mobile.
2. Click on install when prompted and use the app.

To install the app on IOS, we need a mac. Follow the [official guide](https://kivy.org/doc/stable/guide/packaging-ios.html)



 
