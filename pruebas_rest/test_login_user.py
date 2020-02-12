import pytest
import requests
import json

def test_login_no_password(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'test@test.com'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing password", resp.text


def test_login_no_email(supply_url):
	url = supply_url + "/login/" 
	data = {}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing email or username", resp.text


@pytest.mark.parametrize("userid, firstname",[(1,"George"),(2,"Janet")])
def test_list_valid_user(supply_url,userid,firstname):
	url = supply_url + "/users/" + str(userid)
	resp = requests.get(url)
	j = json.loads(resp.text)
	print(j)
	assert resp.status_code == 200, resp.text
	assert j['data']['id'] == userid, resp.text
	assert j['data']['first_name'] == firstname, resp.text

#Iterando sobre varios Nodos
def test_petstore(supply_url_petstore):
	url = supply_url_petstore
	data = {'status':'pending'}
	resp = requests.get(url,data)
	j = json.loads(resp.text)
	for x in j:
		assert x['status'] == 'pending'
	assert resp.status_code == 200 , resp.text
	