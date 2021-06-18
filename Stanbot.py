# Stanbot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')
logoUrl="https://tanks-encyclopedia.com/wp-content/uploads/2020/01/logo-big-border.png"
rulesChannelID=766257726019600409
rulesMessage1ID=844300625071046696
rulesMessage2ID=844300626204950558

def rulesAf():
	rulesAt=[]
	rulesAt.append("No excessive swearing.")
	rulesAt.append("Do not post NSFW content. (Adult content or otherwise).")
	rulesAt.append("Do not insult or harass other people. This includes racist / sexist remarks.")
	rulesAt.append("Do not post any information about another user, without said user agreeing.")
	rulesAt.append("Do not post NSFL content. (Shock imagery, gore, etc).")
	rulesAt.append("No advertising without asking staff first.")
	rulesAt.append("Do not spam or post spam messages of any sort.")
	rulesAt.append("No shortened links (bit.ly, goo.gl, etc.) and please accompany links with a short description about the link's content.")
	rulesAt.append("If your name has excessive amounts of symbols, uppercase letters, or is suggestive you may be asked to change it or have one set by a staff member. Your name must be easily mentionable and not only consist of numbers or special characters.")
	rulesAt.append("Impersonating other people or staff will not be tolerated.")
	return rulesAt
	
def rulesBf():
	rulesBt=[]
	rulesBt.append("If your actions on the server enter a grey area or break the rules, admins or moderators reserve the right to take action. This means that moderators can moderate how they see fit.")
	rulesBt.append("If you feel any action against you has been abusive or not founded, you can file an appeal with the administrator who've banned you. You may contact other admins if the admin who performed the moderation action refuses to hear you out.")
	rulesBt.append("The moderators will be held accountable for any abuse or wrongdoing on their part.")
	rulesBt.append("`@everyone` and `@here` is reserved for official announcements. You are not allowed to use it for personal reasons.")
	rulesBt.append("Instigations for the sake of seeing people argue is not allowed. You will be punished for attempting to start flame wars.")
	rulesBt.append("If an admin or moderator tells you to refrain from doing an action and you keep continuing doing said action, the admin or moderator has the right to warn you, place you in timeout, kick, or ban you depending on the severity no matter the situation. Refer back to 2.2 if you feel the admin or moderator's actions were unjust.")
	rulesBt.append("Refrain from posting controversial imagery and text relating to race, sex, and tragic events.")
	rulesBt.append("Alternate accounts without admin's approval will not be tolerated.")
	rulesBt.append("Refrain from posting about a topic in a channel where it does not belong. Slight deviations from this will be tolerated to an extent. This includes memes in #general.")
	return rulesBt

@bot.command(name='say')
@commands.has_any_role('admin', 'TE Admin')
async def say(ctx, message, channel: discord.TextChannel=None):
	if channel is None:
		await ctx.send(f"{message}")
	elif channel is not None:
		await channel.send(f"{message}")

@bot.command(name='websiteLink')
@commands.has_any_role('admin', 'TE Admin')
async def websiteLink(ctx, channel: discord.TextChannel=None):
	title="Tank Encyclopedia"
	description="*All about the tactics, technologies, and evolution of the tank worldwide from world war one to the atomic and digital ages: The first online tank museum.*"
	color=0xd2bc54
	websiteLink=discord.Embed(title=title, description=description, color=color)
	websiteLink.set_thumbnail(url=logoUrl)
	websiteLink.add_field(name="Tank Encyclopedia Homepage", value="https://tanks-encyclopedia.com/", inline=False)
	websiteLink.add_field(name="Tank Encyclopedia Team", value="https://tanks-encyclopedia.com/meet-the-team/", inline=False)
	websiteLink.add_field(name="Tank Encyclopedia Merch store", value="https://gunjigraphics.com/product-category/tank-encyclopedia/", inline=False)
	websiteLink.add_field(name="Tank Encyclopedia Patreon", value="https://www.patreon.com/tankartfund", inline=False)
	if channel is None:
		await ctx.send(embed=websiteLink)
	elif channel is not None:
		await channel.send(embed=websiteLink)

@bot.command(name='rules')
@commands.has_any_role('admin', 'TE Admin')
async def rules(ctx, channel: discord.TextChannel=None, rulesA=rulesAf(), rulesB=rulesBf()):
	title1="Tank Encyclopedia Community Chat Rules"
	description1="*Feel free to contact the staff for any clarification*"
	color1=0xd2bc54
	rules1=discord.Embed(title=title1, description=description1, color=color1)
	#rules1.set_author(name="Tank Encyclopedia Community Chat Rules")
	rules1.set_thumbnail(url=logoUrl)
	for rn, rule in enumerate(rulesA, start=1):
		rules1.add_field(name="Rule 1."+str(rn), value=rule, inline=False)
	if channel is None:
		await ctx.send(embed=rules1)
	elif channel is not None:
		await channel.send(embed=rules1)
	
	title2="Tank Encyclopedia Community Chat Rules"
	description2="*Feel free to contact the staff for any clarification*"
	color2=0xd2bc54
	rules2=discord.Embed(title=title2, description=description2, color=color2)
	#rules2.set_author(name="Tank Encyclopedia Community Chat Rules")
	rules2.set_thumbnail(url=logoUrl)
	for rn, rule in enumerate(rulesB, start=1):
		rules2.add_field(name="Rule 2."+str(rn), value=rule, inline=False)
	if channel is None:
		await ctx.send(embed=rules2)
	elif channel is not None:
		await channel.send(embed=rules2)

@bot.command(name='addRule')
@commands.has_any_role('admin', 'TE Admin')
async def addRule(ctx, rule, channelID:int=rulesChannelID, rulesID:int=None):
	ruleCat, ruleNumber, ruleDescription = rule.split('|')
	
	if rulesID is None:
		if int(ruleCat)==1:
			rulesID = rulesMessage1ID
		elif int(ruleCat)==2:
			rulesID = rulesMessage2ID
	
	channel = bot.get_channel(channelID)
	mess = await channel.fetch_message(rulesID)
	
	rules = mess.embeds[0]
	i=int(ruleNumber)-1
	rules.insert_field_at(index=i, name="Rule "+ruleCat+"."+ruleNumber, value=ruleDescription, inline=False)
	await mess.edit(embed=rules)

@bot.command(name='editRule')
@commands.has_any_role('admin', 'TE Admin')
async def editRule(ctx, rule, channelID:int=rulesChannelID, rulesID:int=None):
	ruleCat, ruleNumber, ruleDescription = rule.split('|')
	
	if rulesID is None:
		if int(ruleCat)==1:
			rulesID = rulesMessage1ID
		elif int(ruleCat)==2:
			rulesID = rulesMessage2ID
	
	channel = bot.get_channel(channelID)
	mess = await channel.fetch_message(rulesID)
	
	rules = mess.embeds[0]
	i=int(ruleNumber)-1
	rules.set_field_at(index=i, name="Rule "+ruleCat+"."+ruleNumber, value=ruleDescription, inline=False)
	await mess.edit(embed=rules)

@bot.command(name='deleteRule')
@commands.has_any_role('admin', 'TE Admin')
async def deleteRule(ctx, rule, channelID:int=rulesChannelID, rulesID:int=None):
	ruleCat, ruleNumber = rule.split('|')
	
	if rulesID is None:
		if int(ruleCat)==1:
			rulesID = rulesMessage1ID
		elif int(ruleCat)==2:
			rulesID = rulesMessage2ID
	
	channel = bot.get_channel(channelID)
	mess = await channel.fetch_message(rulesID)
	
	rules = mess.embeds[0]
	i=int(ruleNumber)-1
	rules.remove_field(index=i)
	await mess.edit(embed=rules)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)