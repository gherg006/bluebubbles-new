from enum import Enum

class RequestType(Enum):
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    SEND_MESSAGE = "SEND_MESSAGE"
    GET_MESSAGE = "GET_MESSAGE"
    GET_USER_LIST = "GET_USER_LIST"

class ResponseType(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    MESSAGE = "MESSAGE"
    USER_LIST = "USER_LIST"