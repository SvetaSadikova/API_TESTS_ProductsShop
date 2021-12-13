from fixture.Registration.registration import Registration


class Application:
    def __init__(self, url):
        self.MyUrl = url
        self.RegisterNewUser = Registration(self)
        #self.AuthUser = Authentication(self)
