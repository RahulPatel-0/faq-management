import { expect } from "chai";
import { render, screen } from "@testing-library/react";
import FAQComponent from "../components/FAQComponent";  // Adjust path

describe("FAQ Component", () => {
  it("renders FAQ question", () => {
    render(<FAQComponent question="What is React?" answer="A JS library" />);
    expect(screen.getByText("What is React?")).to.exist;
  });
});
