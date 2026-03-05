import { useState, useRef } from "react";
import { uploadPdf } from "../lib/api";

const MAX_SIZE_MB = 50;

export default function PdfUploader() {
  const [status, setStatus] = useState("idle"); // idle | dragging | uploading | success | error
  const [result, setResult] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");
  const inputRef = useRef(null);

  function validate(file) {
    if (!file) return "No file selected.";
    if (file.type !== "application/pdf") return "Only PDF files are accepted.";
    if (file.size > MAX_SIZE_MB * 1024 * 1024)
      return `File too large. Max size is ${MAX_SIZE_MB}MB.`;
    return null;
  }

  async function handleFile(file) {
    const err = validate(file);
    if (err) {
      setStatus("error");
      setErrorMsg(err);
      return;
    }

    setStatus("uploading");
    setResult(null);
    setErrorMsg("");

    try {
      const data = await uploadPdf(file);
      setResult(data);
      setStatus("success");
    } catch (e) {
      setStatus("error");
      setErrorMsg(e.message || "Something went wrong.");
    }
  }

  function onDrop(e) {
    e.preventDefault();
    setStatus("idle");
    const file = e.dataTransfer.files[0];
    handleFile(file);
  }

  function onDragOver(e) {
    e.preventDefault();
    setStatus("dragging");
  }

  function onDragLeave() {
    setStatus("idle");
  }

  function onFileChange(e) {
    const file = e.target.files[0];
    if (file) handleFile(file);
    e.target.value = "";
  }

  function reset() {
    setStatus("idle");
    setResult(null);
    setErrorMsg("");
  }

  if (status === "success" && result) {
    return (
      <div className="rounded-2xl border border-green-200 bg-green-50 p-10 text-center">
        <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-green-100">
          <svg className="h-7 w-7 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <p className="text-lg font-semibold text-green-800">Upload successful</p>
        <p className="mt-2 text-sm text-green-700">
          <span className="font-medium">{result.filename}</span> — {result.pages} page{result.pages !== 1 ? "s" : ""}, {(result.size / 1024).toFixed(0)} KB
        </p>
        <button
          onClick={reset}
          className="mt-6 rounded-lg bg-green-600 px-5 py-2 text-sm font-medium text-white hover:bg-green-700 transition-colors cursor-pointer"
        >
          Upload another
        </button>
      </div>
    );
  }

  return (
    <div
      onDrop={onDrop}
      onDragOver={onDragOver}
      onDragLeave={onDragLeave}
      onClick={() => inputRef.current?.click()}
      className={`
        cursor-pointer rounded-2xl border-2 border-dashed p-12 text-center transition-colors
        ${status === "dragging"
          ? "border-amber-500 bg-amber-50"
          : "border-amber-300 bg-white/60 hover:border-amber-400 hover:bg-amber-50/50"
        }
      `}
    >
      <input
        ref={inputRef}
        type="file"
        accept=".pdf,application/pdf"
        onChange={onFileChange}
        className="hidden"
      />

      {status === "uploading" ? (
        <>
          <div className="mx-auto mb-4 h-10 w-10 animate-spin rounded-full border-4 border-amber-200 border-t-amber-600" />
          <p className="text-amber-700 font-medium">Uploading...</p>
        </>
      ) : (
        <>
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-amber-100">
            <svg className="h-7 w-7 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 4v16m0-16l-4 4m4-4l4 4" />
            </svg>
          </div>
          <p className="text-amber-800 font-medium">
            Drag & drop a Sanskrit PDF here
          </p>
          <p className="mt-1 text-sm text-amber-600">
            or click to browse — max {MAX_SIZE_MB}MB
          </p>
        </>
      )}

      {status === "error" && (
        <p className="mt-4 text-sm font-medium text-red-600">{errorMsg}</p>
      )}
    </div>
  );
}
