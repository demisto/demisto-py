import ast
import os
import time
import demisto_client
from demisto_client.demisto_api.rest import ApiException


def main():
    client = demisto_client.configure(
        base_url=os.getenv('DEMISTO_BASE_URL'), api_key=os.getenv('DEMISTO_API_KEY'), verify_ssl=False
    )

    while True:

        try:
            investigation_playbook_raw = demisto_client.generic_request_func(
                self=client, method="GET", path=f"/inv-playbook/74"
            )
            investigation_playbook = ast.literal_eval(investigation_playbook_raw[0])
            print(investigation_playbook['state'])
            time.sleep(300)
        except ApiException as err:
            print(err)



if __name__ in ["__builtin__", "builtins", '__main__']:
    main()