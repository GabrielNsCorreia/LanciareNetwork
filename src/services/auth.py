import repositories.user_repository as user

def auth(name, username, email):    
    if(user.get_user_by_name(name) or user.get_user_by_username(username) or user.get_user_by_email(email)):
        return False

    return True
