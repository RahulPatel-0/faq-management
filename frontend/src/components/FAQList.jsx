import React, { useEffect, useState } from "react";
import { fetchFAQs } from "../api";

function FAQList({ lang }) {
  const [faqs, setFaqs] = useState([]);

  useEffect(() => {
    fetchFAQs(lang).then(setFaqs);
  }, [lang]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Frequently Asked Questions</h2>
      {faqs.map((faq) => (
        <div key={faq.id} className="card mb-3">
          <div className="card-body">
            <h5 className="card-title">{faq.question}</h5>
            <p
              className="card-text"
              dangerouslySetInnerHTML={{ __html: faq.answer }}
            ></p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default FAQList;
