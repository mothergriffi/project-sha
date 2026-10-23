// Halaman ini memanggil backend langsung dari browser (client component),
// sehingga CORS di langkah 3 benar-benar terpakai.
"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("backend tidak terhubung"));
  }, []);

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold">SHA</h1>
      <p>Backend status: {status}</p>
    </main>
  );
}