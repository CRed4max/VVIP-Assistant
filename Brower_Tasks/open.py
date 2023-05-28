import webbrowser
def OpenBrowser(url):
    webbrowser.open(url,new=2, autoraise=True)
def OpenUrlInNewTab(url):
    webbrowser.open(url)
def OpenNewUrl(url):
    webbrowser.open(url)
def OpenNewTabInNewWindow():
    pth = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth))
    chrome = webbrowser.get('chrome')
    chrome.open_new_tab('chrome://www.facebook.com')