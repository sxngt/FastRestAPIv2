from fastapi import Response, Depends, APIRouter
from fastapi_restful.cbv import cbv
from domain.board.BoardService import BoardService
from domain.board.dto.createBoardDto import CreateBoardDto

router = APIRouter(
    prefix="/api/board"
)


@cbv(router)
class BoardController:
    boardService: BoardService = Depends(BoardService)

    @router.get("/all")
    async def getAllBoard(self):
        return await self.boardService.getAllBoard()

    @router.get("/{board_id}")
    async def getBoardById(self, board_id: int):
        return await self.boardService.getBoardById(board_id)

    @router.post("/create")
    async def createBoard(self, createBoardDto: CreateBoardDto):
        print(createBoardDto)
        return await self.boardService.createBoard(createBoardDto)

    @router.delete("/{board_id}")
    async def deleteBoardById(self, board_id: int):
        return await self.boardService.deleteBoardById(board_id)

    @router.put("/{board_id}")
    async def updateBoardById(self, board_id: int, createBoardDto: CreateBoardDto):
        return await self.boardService.updateBoardById(board_id, createBoardDto)
