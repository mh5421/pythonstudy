from sqlalchemy import Column, VARCHAR, text, exc, and_, or_, func, String, DateTime
from dataSource import *
from dto import *

__all__ = ["insertBoard", "selectBoard"]

def insertBoard(data):
    """

    """
def selectBoard():
    query ="""
    select * from board

    """
    stmt = text(query)
    result = session.execute(stmt)


    # result 값을 [key: value]의 list 형태로 변경
    resultVal = [{column: value for column, value in rowproxy.items() }for rowproxy in result]
    print("*************")
    print(resultVal)
    print("*************")

    return resultVal