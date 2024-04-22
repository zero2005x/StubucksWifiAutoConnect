# Starbucks Wi-Fi 自動連接

## 簡介 / Introduction

此 Python 腳本旨在自動連接到星巴克 Wi-Fi，幫助使用者省去手動選擇並連接 Wi-Fi 的麻煩。腳本透過 Selenium Webdriver 自動化網頁互動，自動完成登入頁面的同意條款操作，從而實現自動連接。

This Python script is designed to automate the process of connecting to Starbucks Wi-Fi, sparing users the hassle of manually selecting and connecting to Wi-Fi. The script uses Selenium Webdriver to automate web interactions, automatically agreeing to terms on the login page, thus achieving auto-connection.

## 環境需求 / Environment Requirements

- Python 3
- Selenium
- WebDriver (Geckodriver for Firefox)
- Firefox 瀏覽器 / Firefox browser

## 安裝 / Installation

1. 確保已安裝 Python 3。
   Ensure Python 3 is installed.

2. 安裝 Selenium 庫：
   Install the Selenium library:

   ```bash
   pip install selenium
   ```
   
2. 下載相應的 WebDriver（Geckodriver）並放置於可執行路徑中。下載連結：
   Download the corresponding WebDriver (Geckodriver) and place it in an executable path. Download link:
   Firefox (Geckodriver): https://github.com/mozilla/geckodriver/releases   

## 使用說明 / Usage
1. 修改腳本中的 geckodriver_path 和 firefox_binary_path 變量，以匹配您的 Geckodriver 路徑和 Firefox 安裝路徑。Modify the geckodriver_path and firefox_binary_path variables in the script to match your Geckodriver path and Firefox installation path.

2. 在終端機或命令提示字元中運行腳本：Run the script in a terminal or command prompt:
	```bash
	python autoconnect_starbucks.py
	```
	
## 注意事項 / Notes
- 腳本默認設定為無頭模式，不會顯示瀏覽器介面。您可以透過註解掉 options.add_argument('--headless') 行來禁用無頭模式。The script is set to headless mode by default, not displaying the browser interface. You can disable headless mode by commenting out the options.add_argument('--headless') line.

- 確保您的電腦連接到星巴克 Wi-Fi 的範圍內才能正常使用此腳本。Ensure your computer is within the range of Starbucks Wi-Fi for the script to work properly.

## 貢獻 / Contributing
- 歡迎提交 Pull Request 來改進此腳本。請確保您的程式碼清晰且有適當的註解。Contributions to improve this script are welcome. Please ensure your code is clean and well-commented.
