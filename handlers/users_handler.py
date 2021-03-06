import sys
import server

sys.path.append('controllers')
import users_controller

def get_users(req):
  page_size = int(req.args['page_size'])
  page_index = int(req.args['page_index'])
  name = req.args['name']

  if page_size < 0 or page_index < 0:
    return server.bad_req('invalid params')

  return users_controller.get_users(page_size, page_index, name)

def create_user(req):
  try:
    req = req.get_json()
  except:
    return server.bad_req()

  first_name = req['first_name']
  last_name = req['last_name']
  email = req['email']
  password = req['password']
  created_by = req['created_by']

  return users_controller.create_user(first_name, last_name, email, password, created_by)

def delete_user(user_id):
  if user_id < 1:
    return server.bad_req('invalid user id')

  return users_controller.delete_user(user_id)
