import { useState } from "react";

function ImageUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [commonPrefix, setCommonPrefix] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      console.log(selectedFile);
      formData.append("image", selectedFile);
      console.log(formData);

      try {
        const response = await fetch("http://127.0.0.1:5000/img", {
          method: "POST",
          body: formData,
        });

        if (response.status === 200) {
          const data = await response.json();
          setCommonPrefix(data.common_prefix);

          console.error("Error uploading image");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else {
      console.warn("No file selected");
      alert("No File Selected");
    }
  };

  return (
    <div>
      <h2>Image Upload</h2>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!selectedFile}>
        Upload Image
      </button>
      {commonPrefix && (
        <div>
          <h3>Common Prefix:</h3>
          <p>{commonPrefix}</p>
        </div>
      )}
    </div>
  );
}

export default ImageUpload;
