import discord
import os

bot = discord.Bot()
token = os.environ['token']


class VerifyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label='Your table number / "VISITOR"', placeholder="C10 / VISITOR"))
        self.add_item(discord.ui.InputText(label="Your seat number", placeholder="18"))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

@bot.command(description="replipepli") 
async def ping(ctx): 
    await ctx.respond(f"Pong! Viive on {bot.latency} sekuntti(a)")

@bot.command(description="replipepli") 
async def ctxtesterthing(ctx): 
    await ctx.respond(ctx)

@bot.command(description="Lähettää jotain nappia (ei toimi kunnolla") 
async def lähetä(ctx): 
    modal = VerifyModal(title="Verifioi itsesi!")
    await ctx.send_modal(modal)

@bot.command(description="Lähettää jotain nappia (oikea versio)") 
async def lähetä2(ctx):
  embed = discord.Embed(
        title="My Amazing Embed",
        description="Embeds are super easy, barely an inconvenience.",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
  embed.add_field(name='Reagoi tähän viesiin emojilla "✅" verifioidaksesi itsesi', value="")

  embed.set_footer(text="Made by Hassy Tema") # footers can have icons too
  message = await ctx.respond(embed=embed)
  msg = await message.original_response()
  await msg.add_reaction("✅")

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message # our embed
    channel = discord.utils.get(message.guild.channels, name="admin-cmd") #our channel
    if message.channel.id == channel.id: # checking if it's the same channel
        if message.author == bot.user: #checking if it's sent by the bot
            if reaction.emoji.name == "✅": #checking the emoji
                await ctx.respond("ookoo")
  


bot.run(token)