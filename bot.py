import discord
from discord.ext import commands
from contento import get_class

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""    
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
@bot.command(name='?')
async def _bot(ctx):
    await ctx.send('$adios: para despedirse')
    await ctx.send('$wiki + imagen para analizar una imagen de una tropa de ttd y saber a que faccion pertenece')
    await ctx.send('$hola : para una simple respuesta')
@bot.command(name='hola')
async def _bot(ctx):
    await ctx.send('hola como estas?')
@bot.command(name='adios')
async def _bot(ctx):
    await ctx.send('hasta la proxima')
@bot.command(name= "wiki")
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Imagen guardada en ./{file_url}")
            try: 
                clase = get_class(model_path = "keras_model.h5", labels_path = "labels.txt", image_path = f"./{file_name}"  )
                if clase[0] == "camera":
                    await ctx.send("Es posiblemente un cameraman la faccion mas comun")
                elif clase[0] == "tv":
                    await ctx.send("Es posiblemente un tv la faccion mas valiosa excepto por sus representantes")
                elif clase[0] == "speaker":
                    await ctx.send("speakerman la faccion mas comun aunque era buena")
                elif clase[0] == "clock":
                    await ctx.send("Es posiblemente un paya- digo un clockman la faccion mas paya- digo la mas poderosa")
                elif clase[0] == "drill":
                    await ctx.send("Es posiblemente un ######### digo un drill payasa unidad digo buens unidades")
                elif clase[0] == "otros":
                    await ctx.send("uy es otro probablemente es de las unidades mas fuertes")
                elif clase[0] == "fan":
                    await ctx.send("Es posiblemente un fan man pueden realentizar enemigos pero son muy buenos")
            
            except:
                await ctx.send("hA OcuRido Alg0 Mq1")   
    else:
        await ctx.send("No se subio la imagen asi q no puedo saber q faccion es")
bot.run('MTIwOTYxNzI3NDc2ODcyODEwNA.GcKAEm.ovOa4yDMZaF_PJl2mmYZO2vfst65SJc7UZpgRw')