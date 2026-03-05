export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 to-orange-50">
      <div className="mx-auto max-w-4xl px-6 py-20">
        <h1 className="text-5xl font-bold tracking-tight text-amber-900">
          Sanskrit Book Translator
        </h1>
        <p className="mt-4 text-lg text-amber-700">
          Upload a Sanskrit PDF and get a beautifully formatted English
          translation.
        </p>

        <div className="mt-12 rounded-2xl border-2 border-dashed border-amber-300 bg-white/60 p-12 text-center">
          <p className="text-amber-600">
            PDF upload coming soon — stay tuned.
          </p>
        </div>
      </div>
    </div>
  );
}
