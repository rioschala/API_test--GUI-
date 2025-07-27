import requests

def findReason():
    global reason
    response = requests.get("https://naas.isalman.dev/no", timeout=10)
    element=response.json()
    reason = element['reason']
    return reason

def on_button_click(result_label):
    result = findReason()
    result_label.config(text=result)
