

def detectUser(user):
    if user.role == 1:
        redirecturl = 'venDashboard'
        return redirecturl
        
    elif user.role == 2 :
        redirecturl = 'custDashboard'
        return redirecturl
    
    elif user.role == None and user.is_admin:
        redirecturl = '/admin/'
        return redirecturl
        