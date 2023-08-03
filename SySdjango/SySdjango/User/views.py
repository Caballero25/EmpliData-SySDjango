from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
import re
import random
import smtplib

# Create your views here.

def index(request):
    return render(request, 'index.html')


def registro(request): 
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        if 'datosPrincipales' in request.POST:
            global email, username, password1, password2
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if email == "" or email == None or username == "" or username == None or password1 == "" or password1 == None or password2 == "" or password2 == None:
                return render(request, 'registro.html', {'error': "Los datos del formulario no pueden estar vacíos"})
            else:
                if password1 != password2:
                    return render(request, 'inderegistro.html', {'error': "Las contraseñas ingresadas no coinciden"})
                else:
                    if not email.endswith("@gmail.com") or any(digit.isspace() for digit in email):
                        return render(request, 'inderegistro.html', {'error': "El email debe ser dominio '@gmail.com' y no debe contener espacios"})
                    elif len(username) < 4 or not username[0].isupper(): 
                        return render(request, 'inderegistro.html', {'error': "El nombre de usuario debe contener al menos 4 carácteres y la primer letra en mayúscula"})
                    elif len(password1) < 7 or not any(char.isdigit() for char in password1) or not any(index.isupper() for index in password1) or not re.search(r"[~@#_^*%/.+:;=/<>]", password1):
                        return render(request, 'inderegistro.html', {'error': "Su contraseña debe tener al menos: 7 carácteres y un número, una mayúscula, un carácter especial '~@#_^*%/.+:;=/<>'"})
                    else:
                        # Generar el código random del correo electrónico
                        def generar_codigo_random():
                            codigo = ''.join(random.choices('0123456789', k=5))
                            return codigo
                        global codigo_random
                        codigo_random = str(generar_codigo_random())

                        def enviar_email():
                            nombre_sistema = "SySDjango"
                            correo_sistema = 'sabrositoRte@gmail.com'
                            # Mensaje del correo
                            mensaje = f"""Hola. \n
                            Te damos la bienvenida al sistema de administracion SySDjango. \n
                            Para confirmar tu registro por favor escriba el codigo que esta escrito a continuacion 
                            en su formulario de validacion dentro de la pagina web \n\n
                            {codigo_random} \n\n
                            Si usted no ha solicitado el registro en SySDjango, por favor ignore este correo electronico \n\n\n\n
                            SySDjango - David Caballero
                            """
                            # Asunto del correo
                            subject = 'Confirme su registro - ' + nombre_sistema
                            # Construir el mensaje completo
                            msgEmail = f'Subject: {subject}\n\n{mensaje}'

                            # Configurar el servidor SMTP
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(correo_sistema, 'ylzempbethtbnkyv')

                            # Enviar el correo electrónico
                            server.sendmail(correo_sistema, email, msgEmail)

                        enviar_email()

                        return render(request, 'confirmacionRegistro.html', {'email': email,
                                                                'username': username,
                                                                'password1': password1,
                                                                'password2': password2})
        else:
            codigoIngresado = request.POST['codigo']
            if codigoIngresado != codigo_random:
                return render(request, 'confirmacionRegistro.html', {'email': email,
                                                                'username': username,
                                                                'password1': password1,
                                                                'password2': password2,
                                                                'error': 'El código no coincide, intente de nuevo'}) 
            else:
                createUser = User.objects.create(username = username, email = email)
                createUser.set_password(password1)
                createUser.save()
                login(request, createUser)
                return redirect('app')       
            
def app(request):
    return render(request, 'app.html')
   

