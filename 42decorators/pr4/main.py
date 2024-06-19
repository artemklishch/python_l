def is_user_authenitcated():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenitcated():
            print("User is authenticated")
            return fn(*args, **kwargs)
        else:
            print("User is not authenticated")
            raise Exception("User is not authenticated")

    return wrapper


@check_user_auth
def do_sensitive_job():
    print("Result of some sensitive tasks")


try:
    do_sensitive_job()
except Exception as e:
    print(e)
