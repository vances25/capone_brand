# 🌿 Weed Brand – Backend & Frontend Setup

This project consists of a FastAPI backend and a Next.js frontend, plus a Telegram bot for managing social links and handling customer contact.

---

## 📦 Environment Setup

### 🔐 Backend `.env` file

You must create a `.env` file in your `backend/` directory with the following content:

```
BOT_TOKEN=7187752091:AAGR166yN0ou2Ia9T7LMB0FmV69vhV6QlGM
STREAM_KEY=tSK_93fjwP7gqVxJz2nLbmTKeY48vR1hu
```

- `BOT_TOKEN`: Used for connecting the Telegram bot  
- `STREAM_KEY`: Used to verify admin access to update links

Make sure to install `python-dotenv` and load it in `main.py` or wherever needed:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

### 🌐 Frontend `.env.local` file

Create a `.env.local` file in your `frontend/` (Next.js) root directory:

```
NEXT_PUBLIC_API_URL=http://localhost:5050
```

> Prefix frontend variables with `NEXT_PUBLIC_` to expose them to the browser.

---

## 🚀 Running the App

### 1. Start the FastAPI backend

```bash
cd backend
python3 main.py
```

This starts:
- The API server at `http://localhost:5050`
- The Telegram bot inside the same event loop

> Make sure the `.env` is correctly configured and all Python dependencies are installed.

---

### 2. Start the Next.js frontend

```bash
cd frontend
npm run dev
```

This starts your frontend on `http://localhost:3000`.

---

## 🤖 Telegram Bot Commands

Once running, the Telegram bot supports:

- `/set_telegram <url>` — Set your Telegram link  
- `/set_instagram <url>` — Set your Instagram link  

These links will update and reflect on the `/socials` endpoint.

---

## 🛡️ Security Notes

- Only users with the correct `STREAM_KEY` can access `/update` to change links.
- You can restrict Telegram bot access using specific chat IDs.

---

## ✅ To-Do
- [ ] Add admin panel to frontend
- [ ] Send DM to admin when user submits phone number
