import os
import bigcommerce
# Public apps (OAuth)
# Access_token is optional, if you don't have one you can use oauth_fetch_token (see below)
api = bigcommerce.api.BigcommerceApi(client_id='h90nu8gj6bapi1bv1uuhfkmqdqbbfno', store_hash='z4fw8vjyrj', access_token='aff7qt8z2ogyfmfonax0522f6ohpsi5')

# Private apps (Basic Auth)
# api = bigcommerce.api.BigcommerceApi(host='store.mybigcommerce.com', basic_auth=('username', 'api token'))


# get product
# p = api.Products.all()

# get user obj (id) through filter
omar = api.Customers.all(email='contactomarnow@gmail.com')[0].id
print omar