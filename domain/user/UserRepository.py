from prismaClient import prisma


class UserRepository:
    @staticmethod
    async def createUser(name, username, hashedPassword):
        await prisma.user.create(
            {
                "name": name,
                "username": username,
                "password": hashedPassword
            }
        )

    @staticmethod
    async def findUser(username):
        print(username)
        return await prisma.user.find_unique(
            where={
                'username': username
            }
        )
