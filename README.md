# Dejavu Bot

[![Build and Deploy to Google Compute Engine](https://github.com/SwirlingDust/dejavu-bot/actions/workflows/setup-gcloud.yml/badge.svg)](https://github.com/SwirlingDust/dejavu-bot/actions/workflows/setup-gcloud.yml)

Simple utility bot for the Windsong Bards Discord server.

## Environmental Variables (.env)

Reference: [Setting up a bot application](https://discordjs.guide/preparations/setting-up-a-bot-application.html)

- `DISCORD_TOKEN`: Used for bot client authentication. Available as TOKEN under Settings>>Bot
- `CLIENT_ID`: Used for commands registration. Available as APPLICATION ID under Settings>>General Information
- `TEST_GUILD_ID`: Used for registering guild commands for testing. Copy ID from Discord with developer mode enabled.

## Local Development

### 1 Run bot client with node

1. Install nvm, node, npm: [nodejs on wsl](https://docs.microsoft.com/en-gb/windows/dev-environment/javascript/nodejs-on-wsl)
2. `npm install` to install dependencies.
3. Configure environmental variables in `.env`.
4. `node index.js` to start up bot client.
5. `CTRL-C` to exit.

### 2 Run bot client with Docker

1. Configure environmental variables in `.env`.
2. `docker compose up -d` to start up bot client.
3. `docker compose down` to exit.

### 3 Commands registration with node

1. `node deploy-commands.js`
