import os

import discord
from discord import app_commands


TOKEN = os.environ.get("DISCORD_TOKEN", "YOUR_BOT_TOKEN_HERE")


class EchoBot(discord.Client):
    def __init__(self) -> None:
        # Default intents are enough for a simple echo command.
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        # Sync global slash commands on startup so /say is available.
        await self.tree.sync()


bot = EchoBot()


@bot.tree.command(name="say", description="Echo your text and mention you.")
@app_commands.describe(message="What should I repeat?")
async def say(interaction: discord.Interaction, message: str) -> None:
    content = f"{message}\n\n{interaction.user.mention}"
    await interaction.response.send_message(
        content,
        allowed_mentions=discord.AllowedMentions(users=True),
    )


def main() -> None:
    token = TOKEN
    if not token or token == "YOUR_BOT_TOKEN_HERE":
        raise RuntimeError(
            "Set your bot token in the DISCORD_TOKEN env var or replace TOKEN."
        )
    bot.run(token)


if __name__ == "__main__":
    main()

