from behave import *
from jsonschema import validate
import requests
import jsonschemas

use_step_matcher("re")


@given("we have behave installed")
def step_impl(context):
    pass


@when('we send "([^"]*)" request to "([^"]*)"')
def step_impl(context, request_type, request_uri):
    context.execute_steps(
        'when we send "{}" request to "{}" with parameter "empty" and value "empty"'.format(request_type, request_uri))


@then("should be received correct status code")
def step_impl(context):
    print(context.response.json())
    assert context.response.status_code == requests.codes.ok, 'Incorrect status code {}'.format(
        context.response.status_code)


@step("should be received response with correct structure")
def step_impl(context):
    if context.host in jsonschemas.jsonschemas.keys():
        validate(context.response.json(), jsonschemas.jsonschemas[context.host])
    else:
        assert False, "Json-schema for {} doesn't presented in schemas.".format(context.host)


@when('we send "([^"]*)" request to "([^"]*)" with parameter "(?P<parameter>.+)" and value "(?P<value>.+)"')
def step_impl(context, request_type, request_uri, parameter, value):
    context.host = request_uri
    if request_type.lower() == "get":
        context.response = requests.get(context.host, params={parameter: value})


@step('"([^"]*)" block should contain parameter "(?P<parameter>.+)" and value "(?P<value>.+)"')
def step_impl(context, response_block, parameter, value):
    response = context.response.json()
    if response_block == 'args':
        try:
            assert response['args'][parameter] == value, "Parameter {} has incorrect value {} instead of {}".format(
                parameter, response['args'][parameter], value)
        except KeyError:
            assert False, "Parameter {} doesn't presented in response".format(parameter)
