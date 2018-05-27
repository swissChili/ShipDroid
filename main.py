import discord
import asyncio

from pymongo import MongoClient
import json

client = discord.Client()

database = MongoClient()

db = database.shipdroid

recipes = db.recipes


recipe0 = {
	"product": "health1",
	"content": "flutterfly, creature eyeball, tasty herb"
}
recipe1 = {
	"product": "mana1",
	"content": "tasty herb, flutterfly, creature eyeball"
}
recipe2 = {
	"product": "health2",
	"content": "some berry, turd, glowfly"
}

result = recipes.insert_many([recipe0, recipe1, recipe2])

print(result)


def say_hello(name):
	print("Hola " + name)


def get_recipe(product):
	content = recipes.find_one({"product": product})
	try:
		return content.get("content")
	except AttributeError:
		return False 

@client.event
async def on_ready():
	say_hello(client.user.name)


@client.event
async def on_message(message):
	if "/r" in message.content.lower():
		string = message.content.lower()

		command = string.split(" ", 1)[1]

		if get_recipe(command) != False:
			intro = await client.send_message(message.channel, "The crafting recipe for {command} is:".format(command = command))
			message = await client.send_message(message.channel, get_recipe(command))
			print(message)
		else:
			norecipe = await client.send_message(message.channel, "There is no recipe available for {command}, for help, type /help.".format(command = command))

	elif "/w" in message.content.lower():
		message = await client.send_message(message.channel, "weapons")


client.run("NDUwMDQ3MDQ0MjgzOTI0NDkw.Detifw.BThf1xz8X7IHnotVqqX_KJ2q8Kw")