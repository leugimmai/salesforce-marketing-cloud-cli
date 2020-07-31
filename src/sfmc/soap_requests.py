import requests
import json
from helpers.xml import to_dict

def retrieve_automation_name_for_query(auth_token, query_name):
    automation_id = get_automation_id(auth_token, query_name)

    if automation_id != None:
        return get_automation_name(auth_token, automation_id)

    return ""

def get_automation_name(auth, id):
    soap_request = '''
        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
        <s:Header>
            <fueloauth xmlns="http://exacttarget.com">''' + auth.authToken +'''</fueloauth>
        </s:Header>
        <s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <RetrieveRequestMsg xmlns="http://exacttarget.com/wsdl/partnerAPI">
                <RetrieveRequest>
                    <ObjectType>Program</ObjectType>
                    <Properties>Name</Properties>
                    <Properties>ObjectID</Properties>
                    <Filter xsi:type="SimpleFilterPart">
                        <Property>ObjectID</Property>
                        <SimpleOperator>equals</SimpleOperator>
                        <Value>'''+ id +'''</Value>
                    </Filter>
                </RetrieveRequest>
            </RetrieveRequestMsg>
        </s:Body>
    </s:Envelope>
                '''

    headers = {'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': 'Retrieve'}

    response = requests.post(url=auth.soap_endpoint, headers=headers, data=soap_request)

    response = to_dict(response.text)

    return response['soap:Envelope']['soap:Body']['RetrieveResponseMsg']['Results']['Name']

def get_automation_id(auth, name):
    soap_request = '''
        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
        <s:Header>
            <fueloauth xmlns="http://exacttarget.com">''' + auth.authToken +'''</fueloauth>
        </s:Header>
        <s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <RetrieveRequestMsg xmlns="http://exacttarget.com/wsdl/partnerAPI">
                <RetrieveRequest>
                    <ObjectType>Activity</ObjectType>
                    <Properties>Name</Properties>
                    <Properties>Program.ObjectID</Properties>
                    <Filter xsi:type="SimpleFilterPart">
                        <Property>Name</Property>
                        <SimpleOperator>equals</SimpleOperator>
                        <Value>'''+ name +'''</Value>
                    </Filter>
                </RetrieveRequest>
            </RetrieveRequestMsg>
        </s:Body>
    </s:Envelope>
                '''

    headers = {'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': 'Retrieve'}

    response = requests.post(url=auth.soap_endpoint, headers=headers, data=soap_request)

    response = to_dict(response.text)

    if response == "Bad Request":
        return None

    if 'Program' not in json.dumps(response['soap:Envelope']['soap:Body']):
        return None
    else:
        response = response['soap:Envelope']['soap:Body']['RetrieveResponseMsg']['Results']

        if type(response) is dict:
            return response['Program']['ObjectID']
        else:
            return response[0]['Program']['ObjectID']
