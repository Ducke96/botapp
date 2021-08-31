from flask import Flask, render_template, request, redirect, url_for, flash 
import pyautogui, webbrowser ,pandas
from datetime import datetime
import time



# initializations
app = Flask(__name__)

# Mysql Connection

# settings
app.secret_key = "mysecretkey"

def enviarMensaje(mensajeF , numbers):

     #numeroRandom =  random.randint(1000000 , 9999999)
     #umTelefono = random.choice([310,311,312, 313, 314,315,316,320,321])
        

        for x in numbers:
            print(x)
        for x in numbers:    
            print("numero entrante"+str(x))


            if(str(x)[0]=="+" and len(str(x))>5):

                print(x)
                webbrowser.open(f'https://web.whatsapp.com/send?phone={str(x)}')
                time.sleep(20)
                pyautogui.typewrite(mensajeF)
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(5)
                pyautogui.press("enter")
                time.sleep(5)
                pyautogui.press("enter")
                time.sleep(5)
                pyautogui.hotkey('ctrl','w')
                time.sleep(5)
                flash('message Added successfully')  

            elif(str(x)[0]!="+" and len(str(x))>5):
                numeroReal =  "+57"+str(x)
                print(numeroReal)
                webbrowser.open(f'https://web.whatsapp.com/send?phone={numeroReal}')
                time.sleep(20)
                pyautogui.typewrite(mensajeF)
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(10)
                pyautogui.press("enter")
                time.sleep(5)
                pyautogui.press("enter")
                time.sleep(5)
                pyautogui.hotkey('ctrl','w')
                time.sleep(5)
                flash('message Added successfully')

        
# routes
@app.route('/')
def Login():
    
         
    return render_template('login.html')

@app.route('/CrearMensaje', methods=['POST'])
def CrearMensaje():
    if request.method == 'POST':
        now = datetime.now()
        new_date = datetime(2021,10,3)
        login = request.form['login']
        password = request.form['password']

        if(str(login)=="Usuario1@gmail.com" and str(password)=="User1548." and now < new_date):
            return render_template('index.html')
        
    return render_template('login.html')        
            
         
    

@app.route('/add_contact', methods=['POST'])
def add_contact():    
    if request.method == 'POST':
        flash('Mensaje en cola espere porfavor')
        mensajeW = request.form['mensajeW']
        uploaded_file = request.files['file']
        uploaded_video = request.files['video']



        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)

    

        data = pandas.read_csv(uploaded_file.filename, header=0)
        numbers = data["Phone"]


 
        enviarMensaje(mensajeW ,numbers)
    else :
        return render_template('login.html')



    return redirect(url_for('Index'))
# starting the app
if __name__ == "__main__":
    app.run(debug=True , port=3000)




