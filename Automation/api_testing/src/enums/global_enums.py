from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recieved status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"