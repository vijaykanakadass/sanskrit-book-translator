import { useState, useEffect, useRef } from "react";
import { getJobStatus } from "../lib/api";

const POLL_INTERVAL = 3000;

export default function DigitizerProgress({ jobId, filename, pages, onComplete, onError }) {
  const [detail, setDetail] = useState("Submitting to Sarvam...");
  const [elapsed, setElapsed] = useState(0);
  const startTime = useRef(Date.now());

  useEffect(() => {
    const timer = setInterval(() => {
      setElapsed(Math.floor((Date.now() - startTime.current) / 1000));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    let cancelled = false;

    async function poll() {
      try {
        const job = await getJobStatus(jobId);
        if (cancelled) return;

        setDetail(job.detail || "Processing...");

        if (job.status === "completed") {
          onComplete(job.html);
          return;
        }
        if (job.status === "failed") {
          onError(job.error || "Digitization failed");
          return;
        }

        setTimeout(poll, POLL_INTERVAL);
      } catch (e) {
        if (!cancelled) {
          onError(e.message || "Lost connection to server");
        }
      }
    }

    poll();
    return () => { cancelled = true; };
  }, [jobId, onComplete, onError]);

  function formatTime(s) {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return m > 0 ? `${m}m ${sec}s` : `${sec}s`;
  }

  return (
    <div className="rounded-2xl border border-amber-200 bg-white/80 p-10 text-center">
      <div className="mx-auto mb-6 h-12 w-12 animate-spin rounded-full border-4 border-amber-200 border-t-amber-600" />

      <p className="text-lg font-semibold text-amber-900">Digitizing your PDF</p>
      <p className="mt-1 text-sm text-amber-700">
        <span className="font-medium">{filename}</span> — {pages} page{pages !== 1 ? "s" : ""}
      </p>

      <div className="mt-6 rounded-lg bg-amber-50 px-4 py-3">
        <p className="text-sm text-amber-800">{detail}</p>
        <p className="mt-1 text-xs text-amber-500">Elapsed: {formatTime(elapsed)}</p>
      </div>

      <p className="mt-4 text-xs text-amber-400">
        This may take a minute or two for large documents.
      </p>
    </div>
  );
}
