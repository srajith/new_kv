#!/usr/bin/env pytho3
# -*- coding: utf-8 -*-
# @Author: r4j
# @Date:   2020-04-19 19:27:15
# @Last Modified by:   r4j
# @Last Modified time: 2020-04-21 23:42:20

import requests
import json

# status = 0 ==> OK 
# status = 1 ==> Failed

def get_attendace(username, password):
	status = 0
	s = requests.Session()

	# Login 
	data = {
	  'username': username,
	  'password': password
	}

	response = s.post('https://mgc.ibossems.com/', data=data)
	# print(response.text)
	if "invalid" in response.text or "Account not found!!" in response.text or "Account Inactive" in response.text:
		return "Invalid username/password"
	cookies = s.cookies.get_dict()

	# Getting attendance 

	response = requests.post('https://mgc.ibossems.com/student/attendance/list', headers={'X-Requested-With': 'XMLHttpRequest'}, cookies=cookies, data={'task':'LISTING'} )
	context = response.text
	data = json.loads(context)

	total = 0
	present = 0

	for i in data['attends']:
		total += i['total']
		present += i['present']


	percentage = ( present * 100 ) / total
	return "Present: {}\nTotal: {}\nPercentage: {}".format(present, total, round(percentage))

print(get_attendace("", ""))