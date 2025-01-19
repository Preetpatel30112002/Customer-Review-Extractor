import React, { useState } from "react";
import axios from "axios";

const Review_Extractor = () => {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const fetchReviews = async () => {
    if (!url.trim()) {
      setResult("Please enter a valid URL.");
      return;
    }

    setIsLoading(true);
    setResult("Fetching reviews, please wait...");

    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/api/reviews?page=${encodeURIComponent(url)}`
      );
      setResult(JSON.stringify(response.data, null, 4)); // Pretty-print JSON
    } catch (error) {
      setResult(`Error: ${error.response?.data?.error || error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Review Extractor</h2>
      <div style={styles.formGroup}>
        <label htmlFor="url" style={styles.label}>
          Enter Product URL:
        </label>
        <input
          type="text"
          id="url"
          style={styles.input}
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com/product"
        />
      </div>
      <button
        style={styles.button}
        onClick={fetchReviews}
        disabled={isLoading}
      >
        {isLoading ? "Fetching..." : "Fetch Reviews"}
      </button>
      <textarea
        style={styles.textarea}
        value={result}
        readOnly
        placeholder="JSON result will appear here..."
      ></textarea>
    </div>
  );
};

const styles = {
    container: {
      fontFamily: "Arial, sans-serif",
      margin: "20px auto",
      maxWidth: "600px",
      padding: "20px",
      backgroundColor: "white",
      borderRadius: "8px",
      boxShadow: "0 2px 8px rgba(0, 0, 0, 0.2)",
      display: "flex",
      flexDirection: "column",
      alignItems: "center", // Center align all child elements horizontally
    },
    header: {
      textAlign: "center",
      marginBottom: "20px", // Add spacing below the header
    },
    formGroup: {
      marginBottom: "15px",
      width: "100%", // Ensure the input spans the container width
    },
    label: {
      fontSize: "1rem",
      marginBottom: "5px",
      display: "block",
      textAlign: "left", // Align the label text to the left
    },
    input: {
      width: "100%",
      padding: "10px",
      fontSize: "1rem",
      border: "1px solid #ccc",
      borderRadius: "5px",
      boxSizing: "border-box", // Include padding and border in element's total width/height
    },
    button: {
      padding: "10px 20px",
      backgroundColor: "#007bff",
      color: "white",
      border: "none",
      borderRadius: "5px",
      fontSize: "1rem",
      cursor: "pointer",
      marginTop: "10px",
      alignSelf: "flex-start", // Align the button to the left
    },
    textarea: {
      width: "100%",
      height: "200px",
      padding: "10px",
      fontSize: "1rem",
      border: "1px solid #ccc",
      borderRadius: "5px",
      marginTop: "15px",
      resize: "none",
      boxSizing: "border-box", // Ensure padding and border are included in total width/height
    },  
};

export default Review_Extractor;
