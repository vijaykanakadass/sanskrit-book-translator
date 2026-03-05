# Sanskrit Book Translator

Upload Sanskrit book PDFs and get beautifully formatted English translations as interactive web pages — with PDF export.

> **Built by AI, steered by humans.** This project is developed agentically, while a human developer guides the direction, reviews decisions, and steers the overall architecture.

## Features

> **Status: Early Development** — This project is actively being built. Features are being added incrementally.

- [x] Project scaffolding (client + server)
- [ ] PDF upload and text extraction
- [ ] AI-powered Sanskrit to English translation
- [ ] Rich web view with formatted translations
- [ ] PDF export of translated content
- [ ] Book library to browse past translations

## Tech Stack

| Layer      | Technology                        |
| ---------- | --------------------------------- |
| Frontend   | React 19, Vite, JavaScript        |
| Styling    | Tailwind CSS                      |
| Backend    | Express, JavaScript               |
| Database   | Supabase (PostgreSQL)             |
| Storage    | Supabase Storage (PDF files)      |
| PDF Parse  | pdf-parse                         |
| PDF Export | jspdf / @react-pdf/renderer       |

## Project Structure

```
├── client/          # React + Vite frontend
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── lib/     # Supabase client, API helpers
├── server/          # Express backend
│   └── src/
│       ├── routes/
│       ├── services/  # Translation service abstraction
│       └── lib/       # Supabase admin client
├── .env.example
└── .gitignore
```

## Getting Started

### Prerequisites

- Node.js 18+
- A [Supabase](https://supabase.com) project (free tier works)

### Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd sanskrit-book-translator
   ```

2. **Configure environment variables**

   ```bash
   cp .env.example .env
   ```

   Fill in your Supabase credentials in `.env`.

3. **Install dependencies**

   ```bash
   cd client && npm install
   cd ../server && npm install
   ```

4. **Start development servers**

   ```bash
   # Terminal 1 — backend
   cd server && npm run dev

   # Terminal 2 — frontend
   cd client && npm run dev
   ```

   The frontend runs on `http://localhost:5173` and proxies API requests to the Express server on port `3001`.

## License

MIT
