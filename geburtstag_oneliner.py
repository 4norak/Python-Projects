type('MyClient', (__import__("discord").Client,), {'on_message': __import__("asyncio").coroutine(lambda self,message: self.loop.create_task(message.channel.send("Danke")) if "glückwunsch" in message.content.lower() or "alles gute" in message.content.lower() else None)})().run(TOKEN)