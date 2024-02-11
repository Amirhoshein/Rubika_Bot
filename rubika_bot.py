from rubpy import Client, Message, handlers
from rubpy import models, methods, exceptions
from rich.console import Console
from datetime import datetime
from asyncio import run

groups = [
    '' # your group guid
]


console = Console()

async def startBot(client: Client) -> None:
    for guid in groups:
        results = await client.get_group_info(group_guid=guid)
        group_name = results.group.group_title
        now = datetime.now()


async def main():
    async with Client(session='account') as client:

        with console.status(f'bot on!') as status:
            await startBot(client=client)
            @client.on(handlers.MessageUpdates(models.is_group))
            async def updates(update: Message):

                if update.raw_text == 'a' :
                    await client.send_message(
                        object_guid=update.object_guid,
                        message='aa',
                        reply_to_message_id=update.message_id
                    )

            await client.run_until_disconnected()


if __name__ == '__main__':
    run(main())