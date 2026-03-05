export async function uploadPdf(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("/api/upload", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Upload failed");
  }

  return response.json();
}

export async function getJobStatus(jobId) {
  const response = await fetch(`/api/jobs/${jobId}`);

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Failed to fetch job status");
  }

  return response.json();
}
