import { useState, useCallback } from "react";
import PdfUploader from "../components/PdfUploader";
import DigitizerProgress from "../components/DigitizerProgress";
import DigitizedViewer from "../components/DigitizedViewer";

export default function HomePage() {
  // States: "upload" | "digitizing" | "viewing" | "error"
  const [phase, setPhase] = useState("upload");
  const [jobInfo, setJobInfo] = useState(null);
  const [html, setHtml] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");

  function handleJobStarted(data) {
    setJobInfo(data);
    setPhase("digitizing");
  }

  const handleComplete = useCallback((resultHtml) => {
    setHtml(resultHtml);
    setPhase("viewing");
  }, []);

  const handleError = useCallback((msg) => {
    setErrorMsg(msg);
    setPhase("error");
  }, []);

  function reset() {
    setPhase("upload");
    setJobInfo(null);
    setHtml(null);
    setErrorMsg("");
  }

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

      {phase === "viewing" && html ? (
        /* Full-width viewer */
        <div className="mx-auto max-w-5xl px-6 py-8">
          <DigitizedViewer html={html} filename={jobInfo?.filename} onReset={reset} />
        </div>
      ) : (
        <>
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

          {/* Main content area */}
          <div className="mx-auto max-w-2xl px-6 pb-24">
            {phase === "upload" && (
              <PdfUploader onJobStarted={handleJobStarted} />
            )}

            {phase === "digitizing" && jobInfo && (
              <DigitizerProgress
                jobId={jobInfo.job_id}
                filename={jobInfo.filename}
                pages={jobInfo.pages}
                onComplete={handleComplete}
                onError={handleError}
              />
            )}

            {phase === "error" && (
              <div className="rounded-2xl border border-red-200 bg-red-50 p-10 text-center">
                <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-red-100">
                  <svg className="h-7 w-7 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </div>
                <p className="text-lg font-semibold text-red-800">Digitization failed</p>
                <p className="mt-2 text-sm text-red-600">{errorMsg}</p>
                <button
                  onClick={reset}
                  className="mt-6 rounded-lg bg-red-600 px-5 py-2 text-sm font-medium text-white hover:bg-red-700 transition-colors cursor-pointer"
                >
                  Try again
                </button>
              </div>
            )}
          </div>

          {/* How it works — only show during upload phase */}
          {phase === "upload" && (
            <div className="border-t border-amber-200/60 bg-white/30">
              <div className="mx-auto grid max-w-4xl grid-cols-1 gap-8 px-6 py-16 sm:grid-cols-3">
                <Step number="1" title="Upload PDF" desc="Drop your Sanskrit book PDF — scanned or text-based." />
                <Step number="2" title="AI Digitizes" desc="Our AI reads and digitizes the Sanskrit text from your PDF." />
                <Step number="3" title="Read & Export" desc="Browse the digitized text online or download it as a PDF." />
              </div>
            </div>
          )}
        </>
      )}
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
