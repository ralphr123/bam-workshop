/**
 * Make an HTTP request to python server running on port 4200
 * @param {{ method: string; path: string; body?: Record<string, any> }} args
 * @returns {Promise<Record<string, any>>} - Response data
 */
export async function callBackend({ method = "GET", path, body = undefined }) {
  const res = await fetch(`http://localhost:4200${path}`, {
    headers: {
      "Content-Type": "application/json",
    },
    method,
    body: JSON.stringify(body),
  });

  const data = await res.json();

  return data;
}
