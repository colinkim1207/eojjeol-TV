import discord
import time
import random


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("저쩔티비")

        await client.change_presence(status=discord.Status.online, activity=game)

        print("어쩔준비")
        


    async def on_message(self, message):
        if message.author.bot:
            return None
        
        if message.content == "어쩔티비":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
        
        if message.content == "어쩔냉장고":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔공기청정기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔에어컨":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔복합기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔청소기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔컴퓨터":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔세탁기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔건조기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔드라이기":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
            
        if message.content == "어쩔다리미":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
        
        if message.content == "어쩔노트북":
            munza = '저쩔티비', '저쩔티비', '저쩔냉장고', '저쩔공기청정기', '저쩔에에컨', '저쩔복합기', '저쩔청소기', '저쩔컴퓨터', '저쩔세탁기', '저쩔건조기', '저쩔드라이기', '저쩔다리미', '저쩔노트북', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비', '저쩔티비'
            channel = message.channel
            msg = random.choice(munza)
            await channel.send(msg)
            return None
        
if __name__ == "__main__":
    client = chatbot()
    client.run("토큰")