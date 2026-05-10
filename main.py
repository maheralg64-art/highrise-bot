from highrise import BaseBot, __main__
from highrise.models import SessionMetadata, User

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("البوت اشتغل")
        await self.highrise.chat("بوت شغال ✅")

    async def on_chat(self, user: User, message: str) -> None:
        if message.lower() == "هلا":
            await self.highrise.chat(f"هلا والله {user.username}")

if __name__ == "__main__":
    __main__.main(Bot)
