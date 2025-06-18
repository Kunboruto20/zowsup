from ..common.http.warequest import WARequest
import random

class WADobConsentRequest(WARequest):

    def __init__(self, config=None,env=None):

        super(WADobConsentRequest,self).__init__(config,env)
        if config.id is None:
            raise ValueError("Config does not contain id")
        
        self.addParam("context","dob")

        years = ["1997","1998","1999","2000","2001","2002","2003","2004","2005"]
        self.addParam("dob",random.choice(years))

        self.url = "v.whatsapp.net/v2/consent"
