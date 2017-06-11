from flask import request

with app.test_request_context('/render', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/render'
    assert request.method == 'GET'
