
import discord
from discord.ext import commands
import mysql.connector

# MySQL database setup
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pranav@28",
        database="workik_db",  # Use the name of your database
        auth_plugin='mysql_native_password'
    )
    cursor = db.cursor()
    print("Database connection successful")

except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
    # Exit the script or handle the error appropriately
    exit()

# Discord bot setup
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='authenticate')
async def authenticate(ctx):
    # Assuming ctx.guild.id as the unique identifier for Discord servers
    server_id = ctx.guild.id
    server_name = ctx.guild.name  # Assuming you want to store the server name
   

    # Store the server ID, server name, and token in the database
    try:
        cursor.execute("INSERT INTO auth_tokens (server_id, server_name) VALUES (%s, %s)", (server_id, server_name))
        db.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error inserting data into auth_tokens: {err}")

@bot.command(name='hello')
async def hello(ctx):
    # Check if the server is authenticated
    cursor.execute("SELECT * FROM auth_tokens WHERE server_id = %s", (ctx.guild.id,))
    result = cursor.fetchone()

    if result:
        # If authenticated, print "Hello World" along with the server name
        server_name = ctx.guild.name
        await ctx.send(f'Hello World {server_name}')
    else:
        await ctx.send('Bot not authenticated for this server')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTE4NDM3ODc5MjY5MzczMTM3OA.GIih20.huqq8w4wzCuS3CBrqpqyLFOX4JNGr8IEtde8uo')