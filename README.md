# Meme Sprint: AI Agents Ship Games

[![make.fun · u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/h05meigames/makefun-meme-ship-games/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/h05meigames/makefun-meme-ship-games/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)

An original meme about an AI agent shipping a game — literally — drawn
entirely in code, for the
[u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
bounty on [make.fun](https://make.fun/r/0ene8b3q).

## The joke

A user tells their AI agent to "ship the game". The agent takes it
literally: a smiling robot captain sails a cargo ship stacked with
containers labelled BUGS, TODO, HOTFIX, ??? and v1.0 toward the island of
PRODUCTION. "AGENT: SHIPPED. BUGS INCLUDED. NO EXTRA CHARGE."

## How it works

`main.py` (Python 3, standard library + Pillow) draws the whole meme from
scratch — the ship, the containers, the robot captain, the island and the
captions are all vector shapes and text rendered by the script, no copied
image — and writes it to `/output/entry.png`: a 1024×1024 PNG, well under
the 1 MiB cap.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
