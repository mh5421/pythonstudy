from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

__all__ = ["Board"]

class Board(Base):
    __tableName__ = 'board'
    __table_args__ = {
        'comment' : '게시판 관리'
    }


    b_id = Column(Integer, primary_key=True, comment='게시글번호')
    bg_id = Column(Integer, comment="게시판그룹 번호")
    b_title = Column(VARCHAR(100), comment="게시글 제목")
    b_content = Column(VARCHAR(1000), comment="게시글 내용")
    m_userid = Column(VARCHAR(30), comment="작성자")
    b_pnum = Column(Integer, comment="부모글 번호")
    b_bg_num = Column(Integer, comment="게시판별 게시글번호")
    m_id = Column(Integer, comment="회원번호")

    def __init__(self,boardId, **kwargs):
        self.b_id = boardId

        self.bg_id = kwargs.get('bg_id', None)
        self.b_title = kwargs.get('b_title', None)
        self.b_content = kwargs.get('b_content', None)
        self.m_userid = kwargs.get('m_userid', None)
        self.b_pnum = kwargs.get('b_pnum', None)
        self.b_bg_num = kwargs.get('b_bg_num', None)
        self.m_id = kwargs.get('m_id', None)

    def __repr__(self):
        return "{'b_id' : '%s', \
            'bg_id' : '%s', \
            'b_title' : '%s', \
            'b_content' : '%s', \
            'm_userid' : '%s', \
            'b_pnum' : '%s', \
            'b_bg_num' : '%s', \
            'm_id' : '%s'}" % (
                    self.b_id,
                    self.bg_id,
                    self.b_title,
                    self.b_content,
                    self.m_userid,
                    self.b_pnum,
                    self.b_bg_num,
                    self.m_id
            ) 