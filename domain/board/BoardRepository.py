from starlette import status
from starlette.responses import JSONResponse

from domain.board.dto.createBoardDto import CreateBoardDto
from prismaClient import prisma


class BoardRepository:
    @staticmethod
    async def getAllBoard():
        board = await prisma.board.find_many()
        return board

    @staticmethod
    async def getBoardById(board_id):
        board = await prisma.board.find_unique(
            where={
                'id': board_id
            }
        )
        if board:
            return board
        else:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"{board_id}는없는 id값 입니다.")

    @staticmethod
    async def createBoard(createBoardDto: CreateBoardDto):
        await prisma.board.create(
            data={
                'name': createBoardDto.name,
                'description': createBoardDto.description
            }
        )

    @staticmethod
    async def deleteBoardById(board_id):
        res = await prisma.board.delete(
            where={
                'id': board_id
            }
        )
        if not res:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="이미 삭제된 게시물입니다.")

    @staticmethod
    async def updateBoardById(board_id, createBoardDto):
        res = await prisma.board.update(
            where={
                'id': board_id
            },
            data={
                'name': createBoardDto.name,
                'description': createBoardDto.description
            }
        )
        if not res:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="없는 게시물 입니다.")
