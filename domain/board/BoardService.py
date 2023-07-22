from pydantic import BaseModel, Field

from domain.board.BoardRepository import BoardRepository


class Board(BaseModel):
    name: str
    description: str


class BoardService:
    boardRepository = BoardRepository()

    async def getAllBoard(self):
        print("logged by service layer")
        return await self.boardRepository.getAllBoard()

    async def getBoardById(self, board_id):
        return await self.boardRepository.getBoardById(board_id)

    async def createBoard(self, createBoardDto):
        return await self.boardRepository.createBoard(createBoardDto)

    async def deleteBoardById(self, board_id):
        return await self.boardRepository.deleteBoardById(board_id)

    async def updateBoardById(self, board_id, createBoardDto):
        return await self.boardRepository.updateBoardById(board_id, createBoardDto)
