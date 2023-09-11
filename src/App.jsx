import "./App.css";
import ImageUpload from "./components/Img/ImageUpload";

function App() {
  return (
    <>
      <h1>Relic.ai</h1>
      <ImageUpload />
      <iframe
        src="https://1e2d0be74f1311ee2b.gradio.live"
        height="800px"
        width="1000px"
      ></iframe>
    </>
  );
}

export default App;
