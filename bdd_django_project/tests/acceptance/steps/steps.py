from behave import given, when, then
import requests

api_url = None
response_code = {}
response_text = {}
api_endpoints = {}
request_headers = {}


# Background
@given(u'I set sample API url')
def step_impl(context):
    global api_url
    api_url = 'http://127.0.0.1:8000'


# Scenario - Base url validation
@when(u'Send GET HTTP request to api url')
def step_impl(context):
    response = requests.get(url=api_url)
    response_code['base_url'] = response.status_code


@then(u'I received valid HTTP response code 200')
def step_impl(context):
    rc = response_code.get('base_url', 0)
    assert rc == 200


# Scenario - Users API validation
@given(u'I set GET api endpoint as "{users_endpoint}"')
def step_impl(context, users_endpoint):
    api_endpoints['users_url'] = f'{api_url}/{users_endpoint}'
    print(f'{api_endpoints.get("users_url", "null")}')


@when(u'I send GET HTTP request')
def step_impl(context):
    response = requests.post(url=api_endpoints['users_url'],
                             headers=request_headers)
    response_text['users_url'] = response.text
    response_code['users_url'] = response.status_code
    print(f'GET response - {response.text}')


@then(u'I receive valid HTTP response code 200')
def step_impl(context):
    rc = response_code.get('users_url', 0)
    assert rc == 200


@then(u'Response BODY is not-empty')
def step_impl(context):
    text = response_text.get('users_url', None)
    assert text is not None
