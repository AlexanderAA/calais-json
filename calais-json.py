import urllib, httplib
import demjson

class Calais:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.processing_directives = {"contentType":"TEXT/HTML", "outputFormat":"application/json", "reltagBaseURL":None, "calculateRelevanceScore":"true", "enableMetadataType":None, "discardMetadata":None, "omitOutputtingOriginalText":"true"}
        self.user_directives = {"allowDistribution":"false", "allowSearch":"false", "externalID":None}
        self.external_metadata = {}  
        self.PARAMS_XML = """
<c:params xmlns:c="http://s.opencalais.com/1/pred/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"> <c:processingDirectives %s> </c:processingDirectives> <c:userDirectives %s> </c:userDirectives> <c:externalMetadata %s> </c:externalMetadata> </c:params>
"""
    
    def analyze(self, text):
        try:
            return demjson.decode(self.rest_POST(text))
        except Exception:
            return {}
        
    def rest_POST(self, content):
        params = urllib.urlencode({'licenseID':self.api_key, 'content':content, 'paramsXML':self._get_params_XML()})
        headers = {"Content-type":"application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("api.opencalais.com:80")
        conn.request("POST", "/enlighten/rest/", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return (data)
    
    def _get_params_XML(self):
        return self.PARAMS_XML % (" ".join('c:%s="%s"' % (k,v) for (k,v) in self.processing_directives.items() if v), " ".join('c:%s="%s"' % (k,v) for (k,v) in self.user_directives.items() if v), " ".join('c:%s="%s"' % (k,v) for (k,v) in self.external_metadata.items() if v))

    