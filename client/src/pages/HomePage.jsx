import PdfUploader from "../components/PdfUploader";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 to-orange-50">
      {/* Nav */}
      <nav className="border-b border-amber-200/60 bg-white/40 backdrop-blur-sm">
        <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
          <span className="text-lg font-bold tracking-tight text-amber-900">
            Sanskrit Translator
          </span>
        </div>
      </nav>

      {/* Hero */}
      <div className="mx-auto max-w-3xl px-6 pt-20 pb-12 text-center">
        <h1 className="text-5xl font-bold tracking-tight text-amber-900 sm:text-6xl">
          Translate Sanskrit books
          <span className="block text-amber-600">into English</span>
        </h1>
        <p className="mx-auto mt-6 max-w-xl text-lg text-amber-700">
          Upload a Sanskrit PDF and get a beautifully formatted English
          translation you can read online or download.
        </p>
      </div>

      {/* Upload */}
      <div className="mx-auto max-w-2xl px-6 pb-24">
        <PdfUploader />
      </div>

      {/* How it works */}
      <div className="border-t border-amber-200/60 bg-white/30">
        <div className="mx-auto grid max-w-4xl grid-cols-1 gap-8 px-6 py-16 sm:grid-cols-3">
          <Step number="1" title="Upload PDF" desc="Drop your Sanskrit book PDF — scanned or text-based." />
          <Step number="2" title="AI Translates" desc="Our AI reads the Sanskrit text and translates it to English." />
          <Step number="3" title="Read & Export" desc="Browse the translation online or download it as a PDF." />
        </div>
      </div>
    </div>
  );
}

function Step({ number, title, desc }) {
  return (
    <div className="text-center">
      <div className="mx-auto flex h-10 w-10 items-center justify-center rounded-full bg-amber-100 text-sm font-bold text-amber-700">
        {number}
      </div>
      <h3 className="mt-3 font-semibold text-amber-900">{title}</h3>
      <p className="mt-1 text-sm text-amber-600">{desc}</p>
    </div>
  );
}
