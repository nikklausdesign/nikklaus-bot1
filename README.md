# 🤖 nikklaus's design — Discord Bot

A custom Discord bot with Moderation, Welcome messages, and a Ticket system.

---

## 📁 File Structure
```
nikklaus-bot/
├── bot.py               ← Main entry point
├── requirements.txt     ← Python dependencies
├── Procfile             ← For Railway hosting
├── .env.example         ← Token template
└── cogs/
    ├── moderation.py    ← Ban, Kick, Mute, Clear
    ├── welcome.py       ← Welcome & Farewell messages
    └── tickets.py       ← Ticket panel system
```

---

## 🚀 STEP-BY-STEP SETUP

### STEP 1 — Create Your Bot on Discord

1. Go to https://discord.com/developers/applications
2. Click **New Application** → name it (e.g. "nikklaus bot")
3. Go to **Bot** tab → click **Add Bot**
4. Under **Privileged Gateway Intents**, enable ALL THREE:
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent
5. Click **Reset Token** → copy the token (keep it secret!)
6. Go to **OAuth2 → URL Generator**:
   - Scopes: ✅ `bot` + ✅ `applications.commands`
   - Bot Permissions: ✅ Administrator
7. Copy the generated URL → open it → add bot to **nikklaus's design**

---

### STEP 2 — Deploy to Railway.app

1. Create a free account at https://railway.app
2. Click **New Project → Deploy from GitHub Repo**
   - Upload these files to a GitHub repo first (github.com → New Repo → upload files)
3. In Railway, go to your project → **Variables** tab
4. Add a new variable:
   - Key:   `DISCORD_TOKEN`
   - Value: (paste your bot token from Step 1)
5. Railway will automatically detect `Procfile` and start the bot ✅

---

### STEP 3 — Set Up Each Feature

#### 🛡️ Moderation Commands (slash commands)
These work automatically once the bot is in your server:
| Command | Description |
|---|---|
| `/ban @user reason` | Bans a member |
| `/kick @user reason` | Kicks a member |
| `/mute @user 10 reason` | Mutes for 10 minutes |
| `/unmute @user` | Removes timeout |
| `/clear 20` | Deletes 20 messages |

#### 👋 Welcome Messages
- Edit `cogs/welcome.py` lines 5-6 to change channel names if needed
- Default: posts to **#welcome-and-rules** when someone joins

#### 🎫 Ticket System
1. Go to your **#tickets** channel in Discord
2. Type `/ticketpanel` — this posts the ticket button
3. Members click **🎫 Open a Ticket** → private channel created
4. Staff close it with **🔒 Close Ticket**

> ⚠️ Make sure the `SUPPORT_ROLE_NAME` in `cogs/tickets.py` matches an actual role in your server (default: "Admin")

---

## 🛠️ Customisation Tips

- **Welcome message**: Edit the text in `cogs/welcome.py` inside `on_member_join`
- **Support role**: Change `SUPPORT_ROLE_NAME = "Admin"` in `cogs/tickets.py` to your staff role name
- **Bot prefix**: Change `command_prefix="!"` in `bot.py`

---

## ❓ Troubleshooting

| Problem | Fix |
|---|---|
| Bot is offline | Check Railway logs — likely wrong token |
| Slash commands not showing | Wait 1-2 mins after bot starts, or re-invite bot |
| Welcome not posting | Check channel name matches `WELCOME_CHANNEL_NAME` |
| Tickets not creating | Ensure "CLIENT AREA" category exists in server |
