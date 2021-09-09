import pprint
from demisto_client.demisto_api import rest

UPDATE_AUTOMATION_EXAMPLE_PATH = './examples/update_automation_example.py'


class Response:
    def __init__(self, data):
        self.data = data


def test_run_update_automation_example(mocker):
    """
    Given: A demisto instance.
    When: Running the update_automation_example.py script.
    Then: Ensure no errors are raised.
    """
    mocker.patch.object(rest.RESTClientObject, 'POST', return_value=Response(data='{ok}'))
    mocked_pprint = mocker.patch.object(pprint, 'pprint')
    with open(UPDATE_AUTOMATION_EXAMPLE_PATH) as example_file:
        exec(example_file.read())

    mocked_pprint.assert_called_once()
