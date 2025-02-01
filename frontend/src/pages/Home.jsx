import React, { useState } from "react";
import FAQList from "../components/FAQList";

function Home() {
  const [lang, setLang] = useState("en");

  return (
    <div>
      <div className="container mt-3">
        <select
          className="form-select mb-3"
          onChange={(e) => setLang(e.target.value)}
        >
          <option value="en">English</option>
          <option value="hi">Hindi</option>
          <option value="bn">Bengali</option>
        </select>
        <FAQList lang={lang} />
      </div>
    </div>
  );
}

export default Home;
