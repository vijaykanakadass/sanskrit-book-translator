export default function DigitizedViewer({ html, filename, onReset }) {
  return (
    <div className="space-y-6">
      {/* Header bar */}
      <div className="flex items-center justify-between rounded-xl bg-white/80 border border-amber-200 px-6 py-4">
        <div>
          <h2 className="text-lg font-semibold text-amber-900">Digitized Output</h2>
          <p className="text-sm text-amber-600">{filename}</p>
        </div>
        <button
          onClick={onReset}
          className="rounded-lg bg-amber-600 px-4 py-2 text-sm font-medium text-white hover:bg-amber-700 transition-colors cursor-pointer"
        >
          Upload another
        </button>
      </div>

      {/* Digitized content */}
      <div
        className="digitized-content rounded-xl border border-amber-200 bg-white p-8 shadow-sm"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </div>
  );
}
