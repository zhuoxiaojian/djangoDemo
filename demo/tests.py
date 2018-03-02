from django.test import TestCase

# Create your tests here.
from demo.tasks import test_add,http_get_request
if __name__ == '__main__':
    # result = test_add.delay(5,5)
    # print(result.backend)
    a_result = http_get_request.delay()
    print(a_result)
