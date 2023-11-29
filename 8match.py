status=eval(input("Enter the status of the customer:"))
match status:
  case 400:
    print('bad request')
  case 404:
    print('not found')
  case 405:
    print('method not allowed')
  case 406:
    print('not acceptable')
  case 408:
    print('request timeout')
  case 409:
    print('conflict')
  case 410:
    print('gone')
  case 411:
    print('length required')
  case _:
    print('INPUT OUT')