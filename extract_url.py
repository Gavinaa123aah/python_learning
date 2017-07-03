import cases_web as web
import cases_async_csv as async

def __extract__():
    print web.cases_after_login.count()


if __name__ == '__main__':
    __extract__()