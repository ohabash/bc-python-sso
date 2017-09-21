from __future__ import print_function
import bigcommerce.api
import bigcommerce.customer_login_token
import os

# Customer login tokens must be signed with an app secret loaded in the environment
os.environ['APP_CLIENT_SECRET'] = 'e3867hrzn2egvqqb15zmoyv2r9hibdd'

# Create API object using OAuth credentials
api = bigcommerce.api.BigcommerceApi(client_id='h90nu8gj6bapi1bv1uuhfkmqdqbbfno', store_hash='z4fw8vjyrj', access_token='aff7qt8z2ogyfmfonax0522f6ohpsi5')

# Create a new customer
# api.Customers.create(first_name='Bob', last_name='Johnson', email='bob.johnson@example.com')

# Or get the customer if they already exist
customer = api.Customers.all(email='contactomarnow@gmail.com')[0]

# Create the JWT login token
login_token = bigcommerce.customer_login_token.create(api, customer.id)

# print('Token: %s' % login_token)

# You can build the URL yourself
url = '%s/login/token/%s' % ('https://store-z4fw8vjyrj.mybigcommerce.com', login_token)
print(url)
# Or use the helper method to build the URL (uses 1 API request to get the secure domain for the store)
# login_token_url = bigcommerce.customer_login_token.create_url(api, customer.id)
# print('Token URL: %s' % login_token_url)




