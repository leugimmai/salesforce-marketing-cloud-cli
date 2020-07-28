import FuelSDK
import sys
from colorama import Fore, Back, Style
from sfmc.retrieve_auth_token import retrieve_auth_token

def get_object_path(account, content_type, content_name):

    stubObj = retrieve_auth_token(account)

    full_path = content_name

    props = ["Name", "CategoryID"]
    search_filter = {'Property': 'Name', 'SimpleOperator': 'equals', 'Value': content_name}

    print(f'{Fore.YELLOW}==== Looking For {content_type} ====')

    if content_type == "Data Extension":
        get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="DataExtension", props=props, search_filter=search_filter )
    if content_type == "Triggered Send":
        get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="TriggeredSendDefinition", props=props, search_filter=search_filter )
    if content_type == "Data Filter":
        get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="FilterDefinition", props=props, search_filter=search_filter)
    if content_type == "Email":
        get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="Email", props=props, search_filter=search_filter)

    try:
        folder_id = get.results[0].CategoryID
    except:
        print(f"{Fore.RED}ERROR:{Style.RESET_ALL} Could Not Find {content_name}")
        sys.exit()

    search_filter = get_search_filter(str(folder_id))

    props = ["Name", "ID", "ParentFolder.ID", "ParentFolder.Name"]

    get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="DataFolder", props=props, search_filter=search_filter)

    print(f'{Fore.YELLOW}==== Retrieving Folder Path For {content_type} ====')

    full_path = get.results[0].Name + "/" + full_path

    while get.results[0]['ParentFolder']['ID']:

        parent_folder_id = get.results[0].ParentFolder["ID"]
        search_filter = get_search_filter(str(parent_folder_id))

        get = FuelSDK.ET_Get(auth_stub=stubObj, obj_type="DataFolder", props=props, search_filter=search_filter)

        full_path = get.results[0].Name + "/" + full_path

    print(f"{Fore.GREEN}==== Location:{Style.RESET_ALL} {full_path} {Fore.GREEN}===={Style.RESET_ALL}")


def get_search_filter(folder_id):

    return {'Property': 'ID', 'SimpleOperator': 'equals', 'Value': folder_id}
