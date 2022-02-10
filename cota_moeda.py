import requests
import tkinter as tk


def pegar_cota():
    request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    request_dic = request.json()

    cota_dollar = request_dic['USDBRL']['bid']
    cota_euro = request_dic['EURBRL']['bid']
    cota_btc = request_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cota_dollar}
    Euro: {cota_euro}
    BTC: {cota_btc}'''

    cotaprint['text'] = texto


window = tk.Tk()

window.title('Cotação Moeda')
window.minsize(290, 100)
text_window = tk.Label(window, text='Olá, saiba as cotações do dia', foreground="blue")
text_window.pack()

botao = tk.Button(window, text='Clique aquí', command=pegar_cota, foreground="green")
botao.pack()

cotaprint = tk.Label(window, text='', foreground="red")
cotaprint.pack()


window.mainloop()
