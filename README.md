



<h1 align="center" style="margin: 0 auto 0 auto;"> <img width="32" src="docs/docs_img/icon.png" alt="logo" > Program Trading Based on Webull</h1>
<h4 align="center" style="margin: 0 auto 0 auto;">Market data from Webull and Yahoo! Build your own strategy, and let the program trade for you with your Webull account.</h4>

<br>

## ⚠️ 0. Disclaimer and Security
- This App is not affiliated with [Webull Financial LLC](https://www.webull.com/).
- The Webull API used in this App is from: 
  - https://pypi.org/project/webull/ (Pypi.org)
  - https://github.com/tedchou12/webull (Github, by tedchou12)
  - Simply speaking, this API is like simulating you are using the Webull web platform. 
- The official [Webull API](https://github.com/webull-inc/openapi-python-sdk) is still under testing. This App will switch to the official API when it is ready.
- The App GUI is developed via [Tkinter-Designer](https://github.com/ParthJadhav/Tkinter-Designer), an easy and fast way to create a Python GUI.
- Feel free to **fork** and **edit** the code to customize the App for your own use.

<br>

- For security:
  - Do **NOT** save your password and PID locally. Type it when you log in.
  - Do **NOT** upload or share the credential JSON files generated by the App.
  - The `access_token` will expire **weekly** for your account security, you need to re-login to set up a new one.
  
<br>

- If you don't have Webull account, feel free to use my [referral link](https://www.webull.com/ko-yield/1686282581612-6819bd?__app_cfg__=%7B%22supportTheme%22%3Atrue%7D&inviteCode=vxXUIqoQXd1E&source=hdx) to sign up, you can get 12 free stocks after depositing $0.01 or more.

- Give repository a star if it helps~

<br>


## 🤖 1. Install

### 🐍 1.1 Install Python

Use the link below to download and install Python. (Make sure to add Python to your system PATH during the installation)

https://www.python.org/downloads/   

### 💾 1.2 Clone this repository
```
git clone https://github.com/LukeWang01/Program-Trading-Based-on-Webull.git
```

or,

Download the Zip file and unzip to a folder.

### 💽 1.3 Install the required packages:

```
pip install -r requirements.txt
```

or,

```
pip3 install -r requirements.txt
```

<a href="https://github.com/LukeWang01/Program-Trading-Based-on-Webull/blob/main/docs/fix_install_error.md" target="_blank">If got errors when installing (click here)</a>

<br>

## 🚀 2. Run

### 2.1 Launch the App

Go to the Program-Trading-Based-on-Webull folder, open the terminal,

```
python app.py
```

or,

Double-click the `app_launcher.bat` to run. (Windows only)

<br>

<img src="docs/docs_img/log_in_1.png" width="800" alt="log in">

<br>

<br>

### 2.2 First-time launch setup (Setup only once for the Authentication)

<a href="https://github.com/LukeWang01/Program-Trading-Based-on-Webull/blob/main/docs/first_run_setup.md" target="_blank">Instructions for the first run setup (click here) </a>

<br>

## 💲 3. Build your own strategy

You can create your strategy following the example strategy:

`Program-Trading-Based-on-Webull/strategy/My_Strategy.py` (<a href="https://github.com/LukeWang01/Program-Trading-Based-on-Webull/blob/main/strategy/My_Strategy.py" target="_blank">Click here to open</a>)

<br>

Just override the `strategy_decision()` function in the `My_Strategy` class, and add any attributes you need.


<br>

Run your strategy and make tradings after logging in:

<br>

<img src="docs/docs_img/strategy_1.png" width="800" alt="strategy_1">

<img src="docs/docs_img/strategy_2.png" width="800" alt="strategy_1">

<br>

## 🖥️ 4. App Features

#### 4.1 Log in
<img src="docs/docs_img/gui_0.png" width="800" alt="strategy_1">

#### 4.2 Account Dashboard
<img src="docs/docs_img/gui_1.png" width="800" alt="strategy_1">

#### 4.3 Select and run strategy, monitor the market and strategy
<img src="docs/docs_img/gui_2.png" width="800" alt="strategy_1">

#### 4.4 Edit your profile settings, add notification email account
<img src="docs/docs_img/gui_3.png" width="800" alt="strategy_1">

#### 4.5 View the trading orders and transaction history
<img src="docs/docs_img/gui_4.png" width="800" alt="strategy_1">

#### 4.6 View the performance of your strategy or account
<img src="docs/docs_img/gui_5.png" width="800" alt="strategy_1">

#### 4.7 View the App running log
<img src="docs/docs_img/gui_6.png" width="800" alt="strategy_1">

#### 4.8 Edit the notification email account settings
<img src="docs/docs_img/gui_7.png" width="800" alt="strategy_1">

#### 4.9 Download the stock intraday and history data, saving as csv file
<img src="docs/docs_img/gui_8.png" width="800" alt="strategy_1">

<img src="docs/docs_img/gui_8_download.png" width="800" alt="strategy_1">

#### 4.10 Safe exit the App
<img src="docs/docs_img/gui_9.png" width="800" alt="strategy_1">

<br>

<br>

<br>

#### Feel free to edit the code to customize the App for your own use.

<br>

**Good luck to all traders!**

Luke

<br>

## 🦋 Supporting Me

<br>

<a href="https://www.buymeacoffee.com/LukeWang" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
<a href="https://www.paypal.com/paypalme/ZiluWang?locale.x=en_US" target="_blank"><img src="https://github.com/LukeWang01/Program-Trading-Based-on-Webull/assets/25569658/975ac8a4-2f7d-4b11-9900-707abf8d275a" alt="Paypal" width="180" ></a>
<br>


