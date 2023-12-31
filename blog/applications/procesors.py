from applications.home.models import Home

#Siempre una procesors es una funcion
#Procesor para recuperar telefono y correo del registro home
def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }
