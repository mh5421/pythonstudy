from sqlalchemy import String, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

__all__ = ['login']

class login(Base):
    __tableName__ = 'member'
    __table_args__ = {
        'comment':'로그인 기능'
    }

    m_id = Column(Integer, primary_key=True, comment="회원번호")
    m_userid = Column(VARCHAR(30), comment="회원아이디")
    m_pass = Column(VARCHAR(20), comment="비밀번호")
    m_email = Column(VARCHAR(50), comment="이메일")
    mg_id = Column(Integer, comment="회원그룹")

    def __init__(self, memberid, **kwargs):
        self.m_id = memberid

        self.m_userid = kwargs.get('m_userid', None)
        self.m_pass = kwargs.get('m_pass', None)
        self.m_email = kwargs.get('m_email', None)
        self.mg_id = kwargs.get('mg_id', None)

    def __repr__(self):
        return "{''}